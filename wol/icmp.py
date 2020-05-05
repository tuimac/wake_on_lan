import socket
import struct
import random
import threading
import traceback
from endpoint import Endpoint

class IcmpClient:
    def __init__(self):
        self.bindIp = socket.gethostbyname(socket.getfqdn())
        self.bindPort = 4000
        self.protocol = "icmp"

    def __checksum(self, packet) -> int:
        try:
            sumBytes = 0
            for i in range(0, len(packet), 2):
                a = packet[i]
                if len(packet) == i + 2: b = 0
                else: b = packet[i]
                sumBytes += ((a << 8) + b)
            if sumBytes > 65535:
                return 65535 ^ (sumBytes - ((sumBytes >> 16) << 16))
            else:
                return 65535 ^ sumBytes
        except Exception as e:
            raise e

    def sendEchoRequest(self, destIp, times, size=64) -> bool:
        '''
        Create packe, send echo request, count success reply
        then if all request is fine, return True.

        Parameters
        ----------
        destIp : string
            IP address to send packet.
        times : int
            times of sending packets.
        size : int
            size of messages within a packet.
        '''
        try:
            # Create endpoints.
            if destIp == "localhost" or destIp.split(".")[0] == "127":
                self.bindIp = destIp
            endpoint = Endpoint(self.bindIp, self.bindPort, self.protocol)
            inboundQueue = endpoint.getInboundQueue()
            outboundQueue = endpoint.getOutboundQueue()

            # RFC 792: https://tools.ietf.org/html/rfc792
            type = 8
            code = 0
            checksum = 0

            # Use for checking wheather receive packet is correct or not.
            ipTable = dict()

            # Define source and destination IP address to pass to Endpoint Class.
            destIp = socket.gethostbyname(destIp)
            sourceIp = destIp
            #sourceIp = socket.gethostbyname(socket.getfqdn())

            for sequence in range(times):
                identifier = random.randint(0, 65355)
                ipTable[str(identifier)] = sequence
                # Create each packet.
                header = struct.pack("bbHHh", type, code, checksum, identifier, sequence)
                body = b"\xff" * size
                message = header + body
                checksum = self.__checksum(message)
                print(checksum)
                header = struct.pack("bbHHh", type, code, checksum, identifier, sequence)
                message = header + body
                sendPacket = (message, (destIp, self.bindPort))

                # Ask to send packet to destination.
                print(sendPacket)
                outboundQueue.put(sendPacket)

                # Ask to get packet from destination.
                recvPacket = inboundQueue.get()
                print(recvPacket)
                print("-----------------------------------------")
            endpoint.closeAllEndpoints()
            return False
        except Exception as e:
            raise e
