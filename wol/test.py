#!/usr/bin/env python3

import struct
import socket

if __name__ == '__main__':
    name = socket.getfqdn()
    print(name)
    print(socket.gethostbyname(socket.getfqdn()))
