<<<<<<< HEAD
#!/usr/bin/env python3

import re
=======
mport re
>>>>>>> 94aadea11bd0767410bd69ef8c5318ece8a4984c
import binascii

if __name__ =="__main__":
    mac1 = "AB:12:CD:34:eF-56"
    mac = mac1.replace(":", "").replace("-", "").lower()
    #mac = re.split(":|-", mac1)
    print(mac)
    byte_order = bytes()

    hexMap = {
         "0": b"\x00", "1": b"\x01",
         "2": b"\x02", "3": b"\x03",
         "4": b"\x04", "5": b"\x05",
         "6": b"\x06", "7": b"\x07",
         "8": b"\x08", "9": b"\x09",
         "a": b"\x0a", "b": b"\x0b",
         "c": b"\x0c", "d": b"\x0d",
         "e": b"\x0e", "f": b"\x0f",
    }
<<<<<<< HEAD
    
=======

>>>>>>> 94aadea11bd0767410bd69ef8c5318ece8a4984c
    for byte in mac:
        byte_order += hexMap[byte]

    print(byte_order)
    #print(type(byte_order))
