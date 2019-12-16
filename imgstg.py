import cv2, sys
import numpy as np

def encode(msg,imgloc): 
	img = cv2.imread(imgloc)      # importing image which will be modified 
	# print('Image Dimensions :', img.shape)
	h = img.shape[0]
	w = img.shape[1]
	channels = img.shape[2]
	# Number of Channels represents the number of components used to represent each pixel.
	# cv2.imshow('image',img)                   # to show the unstegno image
	pixel = []
	
	for m in range(1,h):
	    for n in range(1,w):
	        if (img[m,n][0]!=0) & (img[m,n][1]!=0) & (img[m,n][2] != 0) :       # to extract pixels leaving [0 0 0] type of pixels
	            pixel.append(img[m,n])
	# for i in pixel:
	# 	print (i,end=' ')               # to print unedited image pixels
	# print (len(pixel)) 
	i,j,k=0,0,0
	# i here is for msg counter of character which will be updated when the funct change is called
	# below under 1st while (whole) encryption code has been written
	while (i<=len(msg)):
		if i==len(msg):
			b='11111111'
		else :
			no = ord(msg[i])
			b = '0'+"{0:b}".format(no)
		if (len(b)==7):								# this is for smaller binary values like for space its 32
			b='0'+b									# and its binary is 0100000 after tranformation 00100000
		elif (len(b)==6):
			b='00'+b
		# print (b)
		x=0
		while (x<len(b)):
			if (b[x]=='0'):
				if (pixel[j][k]%2!=0):
					pixel[j][k]-=1
			elif (b[x]=='1'):
				if (pixel[j][k]%2==0):
					pixel[j][k]-=1
			# print (pixel[j][k],end = ' ')
			if k==2:
				k=0
				j+=1
			else :
				k+=1
			x+=1
		j+=1
		k=0
		i+=1
	# print ('Encrypted ,\nimage is saved with name "enc_img.png" at the location of this program')
	j=0
	for m in range(1,h):
		for n in range(1,w):
		    if (img[m,n][0]!=0) & (img[m,n][1]!=0) & (img[m,n][2] != 0) & (j<len(pixel)) :
		        img[m][n]=pixel[j]
		        j+=1
	# in above for loop we have created the encrypted image 
	enc_img = img
	cv2.imwrite(imgloc,img)
	# cv2.imshow('enc_image',enc_img)
	# for i in pixel:
	# 	print (i,end=' ')
	# print (len(pixel))

	# cv2.waitKey(0)
	# cv2.destroyAllWindows()

def decode(imgloc):
	img = cv2.imread(imgloc)      # importing image from which msg will be extracted
	# print('Image Dimensions :', img.shape)
	# cv2.imshow('image',img)
	h = img.shape[0]
	w = img.shape[1]
	pixel = []
	# if w>h :
	# 	g=h
	# else :
	# 	g=w
	for m in range(1,h):
	    for n in range(1,w):
	        if (img[m,n][0]!=0) & (img[m,n][1]!=0) & (img[m,n][2] != 0) :       # to extract pixels leaving [0 0 0] type of pixels
	            pixel.append(img[m,n])
	# for i in pixel:
	# 	print (i,end=' ')      
	j,x=0,0
	data,b='',''
	while (j<len(pixel)):
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
		if (b=='11111111') | (no>127) | (no<0) :              # ascii values range is from 0 to 127
			break
		else :
			pass
		data+=str(chr(no))
		# print (data)
		b=''
		x=0
	# data = data.replace("||||||||||||","\n")

	return data
