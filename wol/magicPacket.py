import socket
import re

class MagicPacket:
    def __init__(self, macAddress):
        self.mac = macAddress

    def __createPacket(self):
        macAddress = self.mac.replace(":", "").replace("-", "").lower()

        secondDigit = {
             "0": 0, "1": 16,
             "2": 32, "3": 48,
             "4": 64, "5": 80,
             "6": 96, "7": 112,
             "8": 128, "9": 144,
             "a": 160, "b": 176,
             "c": 192, "d": 208,
             "e": 224, "f": 240,
        }
        firstDigit = {
             "0": 0, "1": 1,
             "2": 2, "3": 3,
             "4": 4, "5": 5,
             "6": 6, "7": 7,
             "8": 8, "9": 9,
             "a": 10, "b": 11,
             "c": 12, "d": 13,
             "e": 14, "f": 15,
        }
        data = bytearray()
        for i in range(0, len(macAddress), 2):
            data = 


        #data = "ffffffffffff" + "".join(macAddress for i in range(16))
        #data = bytes(bytearray(data, 'utf-8'))
        print(data)
        return data

    def sendPacket(self):
        ip = socket.gethostbyname("node7")
        port = 9999

        data = self.__createPacket()
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(data, (ip, port))
