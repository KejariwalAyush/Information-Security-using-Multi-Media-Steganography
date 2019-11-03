import cv2, sys
import numpy as np
from encrypt import encode
from decode import decode
while (True):
    n = input ("enter 1: to encode a message in image \n      2: to decode a message from image \n      0: to EXIT : ")
    if n=='1' :
        encode()
    elif n=='2' :
        decode()
    elif n=='0' :
        sys.exit()
    else : 
        print ("please enter correct input OR enter 0 to EXIT")
