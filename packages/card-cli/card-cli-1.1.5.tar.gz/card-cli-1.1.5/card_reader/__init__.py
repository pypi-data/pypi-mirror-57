#!/usr/bin/env python3
from argparse import ArgumentParser
from platform import system
from time import sleep

import usb.core
import usb.util

import logging
import json
import sys


logger = logging.getLogger(__name__)
__VERSION__ = 'v1.1.5'

class Reader():
    def __init__(self, device_vendor_id = 0, device_product_id = 0):
        """Constructor."""
        self.device_vendor_id = device_vendor_id
        self.device_product_id = device_product_id
        self.delay = 1000
    
    def load_device_endpoint(self):
        """Initialize the device and load the correct endpoint."""
        self.device = usb.core.find(idVendor=self.device_vendor_id, idProduct=self.device_product_id)

        if not self.device:
            return False

        if self.device.is_kernel_driver_active(0):
            try:
                self.device.detach_kernel_driver(0)
            except usb.core.USBError as e:
                raise e
                # sys.exit("Could not detatch kernel driver: %s" % str(e))

        try:
            self.device.set_configuration()
            self.device.reset()
        except usb.core.USBError as e:
            raise e
            # sys.exit("Could not set configuration: %s" % str(e))

        self.device_endpoint = self.device[0][(0, 0)][0]
        return self.device_endpoint

    def read_card(self, msr, msr_active, pcProx, pcProx_active):
        """Read msr or rfid card."""
        swiped = False
        data = []

        while True:
            try:
                if msr_active == False and pcProx_active == True: sleep(0.5)
                if msr_active == True:
                    try:
                        if swiped: return msr.process_msr_data(data)

                        data += msr.device.read(msr.device_endpoint.bEndpointAddress, msr.device_endpoint.wMaxPacketSize, msr.delay)
                        if len(data) >= 537:
                            swiped = True
                    except usb.core.USBError as e:
                        if e.args == (110, 'Operation timed out'):
                            # print('Invalid swipe, discarding %s bytes of data', len(data))
                            data = []
                        else:
                            logger.error(e)
                            sys.exit()
                if pcProx_active == True:
                    dev = usb.core.find(idVendor=pcProx.device_vendor_id, idProduct=pcProx.device_product_id)
                    for interface in dev.get_active_configuration():
                        if dev.is_kernel_driver_active(interface.bInterfaceNumber):
                            # Detach kernel drivers and claim through libusb
                            dev.detach_kernel_driver(interface.bInterfaceNumber)
                            usb.util.claim_interface(dev, interface.bInterfaceNumber)           
                    dev.set_configuration()
                    dev.ctrl_transfer(0x21, 9, 0x0300, 0, [0x008d])
                    response = dev.ctrl_transfer(0xA1, 1, 0x0300, 0, 4)
                    proxHex = ''
                    for h in (response):
                        # JRK - added if stmt to handle 1-digit numbers without leading 0
                        if (h < 16 and h > 0):
                            proxHex += '0' + hex(h)[2:]
                        else:
                            proxHex += hex(h)[2:]
                    if proxHex != "0000":
                        proxHex = [char for char in proxHex] 
                        k = 0
                        for char in proxHex:
                            proxHex[k] = char.capitalize()
                            k += 1
                        proxHex = ''.join(map(str, proxHex))
                        return pcProx.process_pcProx_data(proxHex)
            except Exception as e:
                logger.error(e)
                sys.exit()


    def process_msr_data(self, data):
        """Process magnetic card strip data."""
        encoding_formats = ['ISO/ABA', 'AAMVA', 'CADL', 'Blank', 'Other', 'Undetermined', 'None']

        parsed = {}
        parsed['encoding_type'] = encoding_formats[data[6]]
        parsed['tracks'] = [{}, {}, {}]

        data_offset = 9

        # Process all 3 tracks
        for i in range(0, 3):
            track = {}
            parsed['tracks'][i] = track

            track['length'] = data[i + 3]

            if not track['length']:
                continue

            track['raw'] = ''.join(map(chr, data[data_offset:data_offset + track['length'] + 1]))
            track['data'] = track['raw'].strip('\x10\t\n\r\0')

            data_offset += track['length'] + 1

            # Remove raw data
            track.pop('raw', None)

            # Skip empty tracks
            if not len(track['data']):
                continue

            if parsed['encoding_type'] == 'ISO/ABA':
                if i == 0:
                    format_code_offset = track['data'].find('%', 0)
                    primary_account_number_offset = format_code_offset + 1
                    name_offset = track['data'].find('^', format_code_offset + 1)
                    additional_data_offset = track['data'].find('^', name_offset + 1)

                    track['format_code'] = track['data'][format_code_offset + 1]
                    track['primary_account_number'] = track['data'][primary_account_number_offset + 1:name_offset]

                    track['name'] = track['data'][name_offset + 1:additional_data_offset]
                    track['last_name'], track['first_name'] = track['name'].split('/')

                    track['expiration_year'] = track['data'][additional_data_offset + 1:additional_data_offset + 3]
                    track['expiration_month'] = track['data'][additional_data_offset + 3:additional_data_offset + 5]
                elif i == 1:
                    primary_account_number_offset = track['data'].find(';', 0)
                    additional_data_offset = track['data'].find('=', primary_account_number_offset + 1)

                    track['primary_account_number'] = track['data'][primary_account_number_offset + 1:
                                                                    additional_data_offset]

                    track['expiration_year'] = track['data'][additional_data_offset + 1:additional_data_offset + 3]
                    track['expiration_month'] = track['data'][additional_data_offset + 3:additional_data_offset + 5]

        return parsed

    def process_pcProx_data(self, data):
        """Process RFID strip data."""
        if data:
            data = ';' + data  + '?'
            return ({
                'encoding_type': 'Other',
                'tracks': [
                    {'length': 0},
                    {'length': len(data), 'data': data},
                    {'length': 0}
                ]
            })


def auto_int(x):
    """Convert a string to int with auto base detection."""
    return int(x, 0)

def main():   
    parser = ArgumentParser(prog='card-cli', description='%(prog)s is a command line utility for reading smartcards and magnetic stripe cards.')
    parser.add_argument('-dvid', '--device-vendor-id', type=auto_int)
    parser.add_argument('-dpid', '--device-product-id', type=auto_int)
    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + __VERSION__)
    args = parser.parse_args()

    logging.basicConfig()

    reader = Reader()

    pcProx_active = False
    msr_active = False

    pcProx = Reader(0x0c27, 0x3bfa)
    if (pcProx.load_device_endpoint() != False): pcProx_active = True

    msr = Reader(**vars(args))
    if (msr.load_device_endpoint() != False): msr_active = True
    

    while True:
        try:
            if pcProx_active == False and msr_active == False:
                logger.warn('No devices connected!')
                sleep(5)
                if (pcProx.load_device_endpoint() != False): 
                    pcProx_active = True
                if (msr.load_device_endpoint() != False): 
                    msr_active = True
                sys.exit()
            logger.warn(f'MSR active: {msr_active} || PCPROX active: {pcProx_active}')
            data = reader.read_card(msr, msr_active, pcProx, pcProx_active)
            if data and type(data) != bool: 
                print(json.dumps(data), flush=True)
                sleep(1)
        except KeyboardInterrupt:
            break

if __name__ == '__main__':
	main()
