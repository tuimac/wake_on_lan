#!/usr/bin/env python3

import re
import binascii
import socket
<<<<<<< HEAD
import struct
import fcntl
import os
from ctypes import *

if __name__ =="__main__":
    CDLL("libc.so.6"))
=======


def createPacket():
    pass

if __name__ =="__main__":
    iface = "eth0@if25"
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    '''
    ip = socket.gethostbyname(socket.gethostname())
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    sock.bind(())
    '''
>>>>>>> 32bd14c2dcb4ef728644a2dc1bc662b6ba5e2eb2
