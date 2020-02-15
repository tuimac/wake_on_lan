import socket
import struct
import random

class Icmp:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)

    def __checksum(self, data):
        return 0

    def echoRequest(self, ip, times, size=64):
        ip = socket.gethostbyname(ip)

        def createPacket(sequence):
            type = 8
            code = 0
            checksum = 0
            identifier = random.randint(0, 65355)

            header = struct.pack("bbHHh", type, code, checksum, identifier, sequence)
            data = b"\xff" * size
            packet = header + data
            print(packet)
            checksum = self.__checksum(header + packet)
            header = struct.pack("bbHHh", type, code, checksum, identifier, sequence)
            packet = header + data
            return packet

        for i in range(1, times + 1):
            packet = createPacket(i)
            sendto = self.sock.sendto(packet, (ip, type))
