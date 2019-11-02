import cv2
import numpy as np

# msg = input("enter message to be hidden : ")
msg = "Hii"
img = cv2.imread('D:/data/frame0.jpg')      # importing image which will be modified 
print('Image Dimensions :', img.shape)
h = img.shape[0]
w = img.shape[1]
channels = img.shape[2]
# Number of Channels represents the number of components used to represent each pixel.
cv2.imshow('image',img)                   # to show the unstegno image
pixel = []
for n in range(1,h):
	if (img[n,n][0]!=0) & (img[n,n][1]!=0) & (img[n,n][2] != 0) :       # to extract pixels leaving [0 0 0] type of pixels
		pixel.append(img[n, n])
# for i in pixel:
# 	print (i,end=' ')               # to print unedited image pixels
print (len(pixel)) 
i,j,k=0,0,0
# i here is for msg counter of character which will be updated when the funct change is called
# below under 1st while (whole) encryption code has been written
while (i<len(msg)):
	no = ord(msg[i])
	b = '0'+"{0:b}".format(no)
	print (b)
	x=0
	while (x<len(b)):
		if (b[x]=='0'):
			if (pixel[j][k]%2!=0):
				pixel[j][k]-=1
		elif (b[x]=='1'):
			if (pixel[j][k]%2==0):
				pixel[j][k]-=1
		print (pixel[j][k],end = ' ')
		if k==2:
			k=0
			j+=1
		else :
			k+=1
		x+=1
	j+=1
	k=0
	i+=1
print ('Encrypted')
j=0
for n in range(1,h):
	if (img[n,n][0]!=0) & (img[n,n][1]!=0) & (img[n,n][2] != 0) & (j<len(pixel)) :
		img[n][n]=pixel[j]
	j+=1
# in above for loop we have created the encrypted image 
cv2.imshow('enc-image',img)
cv2.imwrite('enc_img.jpg',img)
# for i in pixel:
# 	print (i,end=' ')
print (len(pixel))

cv2.destroyAllWindows()