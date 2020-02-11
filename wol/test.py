#!/usr/bin/env python3

import re
import binascii
import socket
import struct
import fcntl

if __name__ =="__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, ICMP_CODE)
    data = bytearray()
    
