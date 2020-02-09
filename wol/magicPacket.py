import socket
import re

class MagicPacket:
    def __init__(self, mac):
        self.mac = mac

    def __createPacket(self):


    def sendPacket(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
