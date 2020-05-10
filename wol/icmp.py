import time
import datetime
import socket
import struct
import random
import threading
import traceback
from endpoint import Endpoint

class IcmpClient:
    def __init__(self):
        self.sourceIp = socket.gethostbyname(socket.getfqdn())
        self.sourcePort = 0
        self.protocol = "icmp"

    def __checksum(self, packet) -> int:
        try:
            sumBytes = 0
            if len(packet) & 1 == 1: packet += bytes([0])
            for i in range(0, len(packet), 2):
                sumBytes += ((packet[i + 1] << 8) + packet[i])
            while sumBytes > 65535:
                sumBytes = (sumBytes & 0xffff) + (sumBytes >> 16)
            return sumBytes ^ 0xffff
        except Exception as e:
            raise e

    def sendEchoRequest(self, destIp, destPort=7, times=0, size=64) -> bool:
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
        endpoint = ""
        try:
            # Create endpoints.
            if destIp == "localhost" or destIp.split(".")[0] == "127":
                self.sourceIp = destIp
            endpoint = Endpoint(self.sourceIp, \
                                self.sourcePort, \
                                destIp, \
                                destPort, \
                                self.protocol)
            endpoint.daemon = True
            endpoint.start()
            inboundQueue = endpoint.getInboundQueue()
            outboundQueue = endpoint.getOutboundQueue()

            # RFC 792: https://tools.ietf.org/html/rfc792
            type = 8
            code = 0
            checksum = 0

            # Use for checking wheather receive packet is correct or not.
            idTable = dict()

            # Define source and destination IP address to pass to Endpoint Class.
            destIp = socket.gethostbyname(destIp)
            sourceIp = destIp
            
            for sequence in range(times):
                startTime = datetime.datetime.now()
                identifier = random.randint(0, 65355)
                idTable[str(identifier)] = sequence
                # Create each packet.
                header = struct.pack("bbHHh", type, code, 0, identifier, sequence)
                body = b"\xff" * size
                message = header + body
                checksum = self.__checksum(message)
                header = struct.pack("bbHHh", type, code, checksum, identifier, sequence)
                message = header + body
                # Ask to send packet to destination.
                outboundQueue.put(message)
                # Ask to get packet from destination.
                recvPacket = inboundQueue.get()
                # Check
                header = recvPacket[0][20:28]
                recvType, recvCode, recvChecksum, recvId, recvSequence = struct.unpack("bbHHh", header)
                if recvType != 0: return False
                if idTable[str(recvId)] != recvSequence: return False
                time.sleep(1 - startTime - datetime.datetime.now())
            endpoint.closeAllEndpoints()
            return True
        except KeyboardInterrupt:
            endpoint.closeAllEndpoints()
        except KeyError as e:
            return False
        except Exception as e:
            raise e
