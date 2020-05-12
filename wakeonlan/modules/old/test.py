#!/usr/bin/env python3

import socket
import struct

def checksum(packet) -> int:
    try:
        if len(packet) & 1 == 1: packet += bytes([0]) 
        sumBytes = 0
        for i in range(0, len(packet), 2):
            sumBytes += ((packet[i + 1] << 8) + packet[i])
        print(sumBytes)
        while sumBytes > 65535:
            sumBytes = (sumBytes & 0xffff) + (sumBytes >> 16)
        return sumBytes ^ 0xffff
    except Exception as e:
        raise e

def createPacket():
    cs = 0
    header = struct.pack("bbHHh", 8, 0, cs, 1, 1)
    body = b"\xff" * 64
    message = header + body
    print(message)
    cs = checksum(message)
    print(cs)
    header = struct.pack("bbHHh", 8, 0, cs, 1, 1)
    message = header + body
    return message

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    message = createPacket()
    sock.sendto(message, ("10.0.222.19", 1))
    data = sock.recvfrom(512)
    print(data)
    data = b"\xff\xff\xff"
    print(data[:1])
