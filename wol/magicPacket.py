import socket
import re

class MagicPacket:
    def __init__(self, macAddress):
        self.mac = macAddress

    def __createPacket(self):
        hexTable = {
             "0": 0, "1": 1, "2": 2, "3": 3,
             "4": 4, "5": 5, "6": 6, "7": 7,
             "8": 8, "9": 9, "a": 10, "b": 11,
             "c": 12, "d": 13, "e": 14, "f": 15,
        }
        macAddress = self.mac.replace(":", "").replace("-", "").lower()
        data = bytearray()
        for i in range(0, len(macAddress), 2):
            data.append(hexTable[macAddress[i]] * 16 + hexTable[macAddress[i + 1]])
        data = b"\xff\xff\xff\xff\xff\xff" + b"".join(bytes(data) for i in range(16))
        print(data)
        return data
   
    def sendPacket(self):
        ip = "255.255.255.255"
        port = 9999

        data = self.__createPacket()
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.sendto(data,(ip, port))
