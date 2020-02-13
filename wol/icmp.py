import socket
import struct

class ControlMessages:
    def __init__(self):
        pass

    def echoRequest(self):
        print("hello")

class Icmp:
    def __init__(self):
        #self.sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
        pass

    def createPacket(self, type):
        #Code this function is based on this rfc article.
        #http://www.networksorcery.com/enp/rfc/rfc792.txt

        cm = ControlMessages()
        
        typeswitcher = {
            8: "echoRequest"
        }
        method = getattr(cm, typeswitcher[type])
        return method()

    def checksum(self, data):
        pass

    def ping(self):
        pass
