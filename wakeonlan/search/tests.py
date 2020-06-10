#!/usr/bin/env python3

#from django.test import TestCase

import socket
import uuid
from struct import pack

if __name__ == "__main__":
    local_mac = [int(("%x" % uuid.getnode())[i:i+2], 16) for i in range(0, 12, 2)]
    local_mac = pack("!6B", *local_mac)
    print(local_mac)
    macaddress =  ""
    for byte in local_mac:
        macaddress += chr(byte & 0xf)
        macaddress += chr(byte >> 8)
    print(macaddress)
