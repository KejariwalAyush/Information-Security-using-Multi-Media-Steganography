import cv2
import numpy as np

imgloc = input("enter image which needs to be decoded \nimage location with image name (with png extention) : ")
imgloc=imgloc.replace('\\','/')
img = cv2.imread(imgloc)      # importing image from which msg will be extracted
# print('Image Dimensions :', img.shape)
cv2.imshow('image',img)
h = img.shape[0]
w = img.shape[1]
pixel = []
for n in range(1,h):
	if (img[n,n][0]!=0) & (img[n,n][1]!=0) & (img[n,n][2] != 0) :       # to extract pixels leaving [0 0 0] type of pixels
		pixel.append(img[n, n])
# for i in pixel:
# 	print (i,end=' ')      
j,x=0,0
data,b='',''
while (j<=len(pixel)):
	k=0
	while(x!=8):                                # under this while binary code is extracted from image
		if(pixel[j][k]%2==0):
			b=b+'0'
		else:
			b=b+'1'
		x+=1
		if(k==2):
			k=0
			j+=1
		else:
			k+=1
		
	j+=1
	# print (b)
	no = int(b,2)                       # converts to a no. from its binary
	if (no>127) | (no<0) :              # ascii values range is from 0 to 127
		break
	else :
		pass
	data+=str(chr(no))
	# print (data)
	b=''
	x=0

print (data)
