import socket
import uuid
from struct import pack

class Arp:
    def __init__(self):
        pass

    def getMacAddress():
        data = uuid.getnode()
        while data > 0:
            tmp = data & 0xff
            macaddress += hex(tmp)[2:].zfill(2) + ":"
            data = data >> 8
            

    def scan(iprange, ifname):

