import socket
import uuid
from struct import pack

class Arp:
    def __init__(self):
        pass

    def getMacAddress(self):
        rawData = uuid.getnode()
        data = bytes()
        for i in range(6):
            data += bytes([rawData & 0xff])
            rawData = rawData >> 8
        return data

    def scan(self, iprange):
        macaddress = self.getMacAddress()
        print(macaddress)
