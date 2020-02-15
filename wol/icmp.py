import socket
import struct
import random

class ControlMessages:
    def __init__(self):
        pass

    def echoRequest(self, type, size=32):
        code = 0
        checksum = 0
        identifier = random.randint(0, 65356)
        

class Icmp:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)

    def createPacket(self, type):
        #Code this function is based on this rfc article.
        #http://www.networksorcery.com/enp/rfc/rfc792.txt

        cm = ControlMessages()
        typeswitcher = {
            8: "echoRequest"
        }
        method = getattr(cm, typeswitcher[type])(type)
        return method

    def checksum(self, data):
        pass

    def ping(self):
        packet = self.createPacket(8)

