#!/usr/bin/env python3

import re
import binascii
import socket
import struct

if __name__ =="__main__":
    #sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    nic = "wlp1s0"
    print(struct.pack("256", nic))
