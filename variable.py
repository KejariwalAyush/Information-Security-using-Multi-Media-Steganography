import cv2
import numpy as np

msg = 'Hii'
# b = "{0:b}".format(ord(msg[1])) 
# b = '0' + b
# print (b)

pixel = [(27, 64, 164), (248, 244, 194), (174, 246, 250), (149, 95, 232),
(188, 156, 169), (71, 167, 127), (132, 173, 97), (113, 69, 206),
(255, 29, 213), (53, 153, 220), (246, 225, 229), (142, 82, 175)]
for i in pixel:
    print (i,end=' ')
i,j,k,p = 0,0,0,0

while (i<len(msg)):
    no = ord(msg[i])
    b = '0'+"{0:b}".format(no)
    print (b)
    x=0
    while(x<len(b)):
        if ((pixel[j][k]%2==0) & (b[x]=='0')) | ((pixel[j][k]%2!=0) & (b[x]!='0')) :
            pass
        else :
            pixel[j][k] -= 1
		
        k+=1
        x+=1
        if k==2 :
            k=0
            j+=1         
    i+=1
print ('Encrypted')
for i in pixel:
    print (i,end=' ')