import socket
import uuid
from struct import pack

class Arp:
    def __init__(self):
        pass

    def getMacAddress(self):
        data = uuid.getnode()
        return data

    def scan(self, iprange, ifname):
        macaddress = self.getMacAddress()
        print(macaddress)
