import cv2,sys,glob
import numpy as np
from imgstg import decode

# imgloc = input('enter location of video which you want to decode : ')
imgloc = 'project1.mkv'
cap = cv2.VideoCapture(imgloc)
count = 100000
ms = ''
for i in range (0,250):
    ms+=' '
# extracting frames and saving it new folder
while(cap.isOpened()):
    ret, frame = cap.read()
    if(ret):
        # print('Read %d frame :'%count,ret)
        # frame = cv2.flip(frame,1)
        # this line flips the image horizontally ; for vertical,both replace 1 by 0,2 respectively
        cv2.imwrite('D:/data/frame{:d}.png'.format(count),frame) 
        # this above one saves it in the location
        count += 1
    else:
        break

i=100000
msg,m = '',''
while(i<count):
    imgoc = 'D:/data/frame%d.png'%i
    m = decode(imgoc)
    mr = m[::-1]
    if(mr==m):
        break
    msg = msg + m
    # print (msg)
    print ('message %d decoded'%i)
    
    i+=1
msg = msg.rstrip()
msg = msg.replace("||||||||||||","\n")
print ('msg decoded')
print (msg)
cap.release()
cv2.destroyAllWindows()
