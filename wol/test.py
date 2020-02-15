#!/usr/bin/env python3

import struct
import socket

if __name__ == '__main__':
    ip = "10.0.222.7"
    ip = socket.inet_aton(ip)
    print(ip)
    ip = ip * 1.5
    print(ip)
