================================
Card reader command-line utility
================================
Configured Readers
------------------
- ACS ACR122U (rfid)
- pcProx RDR-7582AKU (rfid)

Usage
-----  
**via command line:**
::  
card-cli --device-vendor-id 0x03f0 --device-product-id 0x2724

card-cli is a command line utility for reading smartcards and magnetic stripe cards. 

--device-vendor-id (-dvid) and --device-product-id (-dpid) is only required to connect msr device.
