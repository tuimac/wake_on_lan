import socket
import time
from threading import Thread
from queue import Queue

class Endpoint(Thread):
    def __init__(self, inIp, inPort, outIp, outPort, protocol):
        Thread.__init__(self)
        self.__inIp = inIp
        self.__inPort = inPort
        self.__outIp = outIp
        self.__outPort = outPort
        self.__protocol = protocol
        self.__inboundQueue = Queue()
        self.__outboundQueue = Queue()

    def run(self):
        try:
            sock = {
                "icmp": lambda: socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP),
                "udp": lambda: socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            }[self.__protocol]()
            if self.__protocol == "icmp":
                self.__inbound = IcmpInboundEndpoint(self.__inboundQueue, self.__inIp, self.__inPort, sock)
                self.__inbound.daemon = True
                self.__inbound.start()
                self.__outbound = IcmpOutboundEndpoint(self.__outboundQueue, self.__outIp, self.__outPort, sock)
                self.__outbound.daemon = True
                self.__outbound.start()
                self.__inbound.join()
                self.__outbound.join()
            else:
                pass
            sock.close()
        except KeyboardInterrupt:
            self.closeAllEndpoints()
        except socket.error as e:
            raise e
        except Exception as e:
            raise e

    def getInboundQueue(self):
        return self.__inboundQueue

    def getOutboundQueue(self):
        return self.__outboundQueue

    def closeAllEndpoints(self):
        try:
            self.__inbound.closeEndpoint()
            self.__outbound.closeEndpoint()
        except Exception as e:
            raise e

class IcmpInboundEndpoint(Thread):
    def __init__(self, queue, ip, port, socket):
        Thread.__init__(self)
        self.__queue = queue
        self.__ip = ip
        self.__port = port
        self.__socket = socket
        self.__delete = False
        self.__buffer = 0xffff

    def run(self):
        try:
            while not self.__delete:
                data = self.__socket.recvfrom(self.__buffer)
                self.__queue.put(data)
        except KeyboardInterrupt:
            self.closeEndpoint()
        except Exception as e:
            raise e

    def closeEndpoint(self):
        try:
            self.__delete = True
            self.__queue.put((b"", ("0.0.0.0", 0)))
        except Exception as e:
            raise e

class IcmpOutboundEndpoint(Thread):
    def __init__(self, queue, ip, port, socket):
        Thread.__init__(self)
        self.__queue = queue
        self.__ip = ip
        self.__port = port
        self.__socket = socket
        self.__delete = False

    def run(self):
        try:
            while not self.__delete:
                message = self.__queue.get()
                self.__socket.sendto(message, (self.__ip, self.__port))
        except KeyboardInterrupt:
            self.closeEndpoint()
        except Exception as e:
            raise e

    def closeEndpoint(self):
        try:
            self.__delete = True
            self.__queue.put((b"", ("0.0.0.0", 0)))
        except Exception as e:
            raise e
