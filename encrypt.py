import cv2
import numpy as np

# msg = input("enter message to be hidden : ")
msg = "Hii"
img = cv2.imread('D:/data/frame0.jpg')
print('Image Dimensions :', img.shape)
h = img.shape[0]
w = img.shape[1]
channels = img.shape[2]
# Number of Channels represents the number of components used to represent each pixel.
# cv2.imshow('image',img)
pixel = []
for n in range(1,h):
    if (img[n,n][0]!=0) & (img[n,n][1]!=0) & (img[n,n][2] != 0) :
        pixel.append(img[n, n])
for i in pixel:
    print (i,end=' ')   
print (len(pixel)) 
i,j,k=0,0,0
# i here is for msg counter of character which will be updated when the funct change is called
# def change(): 
while (i<len(msg)):
    no = ord(msg[i])
    b = '0'+"{0:b}".format(no)
    print (b)
    x=0
    while(x<len(b)):
        if ((pixel[j][k]%2==0) & (b[x]=='0')) | ((pixel[j][k]%2!=0) & (b[x]!='0')) :
            pass
        else :
            pixel[j][k]-1
        k+=1
        x+=1
        if k==2 :
            k=0
            j+=1         
    i+=1
print ('Encrypted')
j=0
for n in range(1,h):
    if (img[n,n][0]!=0) & (img[n,n][1]!=0) & (img[n,n][2] != 0) & (j<len(pixel)) :
        img[n][n]=pixel[j]
    j+=1
for i in pixel:
    print (i,end=' ')
print (len(pixel))

