import socket
import struct
import random
import threading 
import traceback
from endpoint import Endpoint 

class Icmp:
    def __init__(self):
        endpoint = Endpoint()
        self.inboundQueue = endpoint.getIn

    def __checksum(self, packet):
        checksum = 0
        for i in range(0, len(packet), 2):
            oneComplement = 65535 ^ ((packet[i] << 8) + packet[i + 1])
            checksum += oneComplement
        return checksum

    def createPacket(self, sequence, size):
        type = 8
        code = 0
        checksum = 0
        identifier = random.randint(0, 65355)

        header = struct.pack("bbHHh", type, code, checksum, identifier, sequence)
        data = b"\xff" * size
        packet = header + data
        checksum = self.__checksum(header + packet)
        header = struct.pack("bbHHh", type, code, checksum, identifier, sequence)
        packet = header + data
        return packet

    def sendEchoRequest(self, destIp, times, size=64):
        destIp = socket.gethostbyname(destIp)
        sourceIp = socket.gethostbyname(socket.getfqdn())
        try:
            recv.start()
            for i in range(1, times + 1):
                dataSize = self.sock.sendto(self.createPacket(i, size), (destIp, 0))
                packet = queue.get()
                print(packet)
            self.stop = True
            recv.join()
        except:
            traceback.print_exc()
            self.stop = True
