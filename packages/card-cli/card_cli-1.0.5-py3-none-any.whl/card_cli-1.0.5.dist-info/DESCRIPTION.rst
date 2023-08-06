================================
Card reader command-line utility
================================
Configured Readers
------------------
- ACS ACR122U (rfid)
- HP IDRA-334133 (msr)
- pcProx (rfid)

=============
Local Install
=============
Requirements
------------
- pcscd - ``smartcard.pcsc.PCSCExceptions.EstablishContextException: Failure to establish context: Service not available.``

-- see https://manpages.ubuntu.com/manpages/bionic/man8/pcscd.8.html  

- udev rules (for msr) - ``usb.core.USBError: [Errno 13] Access denied (insufficient permissions)``  

-- cd /etc/udev/rules.d  
-- open 70-snap.core.rules or other file where usb rules are defined  
-- add in file: ``ATTRS{idVendor}=="03f0", ATTRS{idProduct}=="2724", ENV{ID_MM_ERICSSON_MBM}="1" MODE="0666", GROUP="plugdev"``  

- modprobe PN533 (for rfid) - Script won't recognize smartcard reader. 

-- see https://stackoverflow.com/questions/31131569/unable-to-claim-usb-interface-device-or-resource-busy  

Usage
-----  
**via command line:**
::  
card-cli --device-vendor-id 0x03f0 --device-product-id 0x2724

card-cli is a command line utility for reading smartcards and magnetic stripe cards. 

--device-vendor-id (-dvid) and --device-product-id (-dpid) is only required to connect msr device.


