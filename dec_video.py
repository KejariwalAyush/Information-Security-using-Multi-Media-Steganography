import cv2, sys, glob
import numpy as np


def decode(imgloc):
	img = cv2.imread(imgloc)      # importing image from which msg will be extracted
	# print('Image  :', img.shape)
	# cv2.imshow('image',img)
	h = img.shape[0]
	w = img.shape[1]
	pixel = []
	for n in range(0,h):
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
		if  (no>127) | (no<0) :              # ascii values range is from 0 to 127
			break
		else :
			pass
		data+=str(chr(no))
		print (data)
		b=''
		x=0

	return data

# to open video file
# message = input("Enter a message")
# message = 'this is a test message for video encoding with text message'
cap = cv2.VideoCapture('vidstegano.mkv')
count = 0
# extracting frames and saving it new folder
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        print('Read %d frame :'%count,ret)
        # frame = cv2.flip(frame,1)
        # this line flips the image horizontally ; for vertical,both replace 1 by 0,2 respectively
        cv2.imwrite('C:/Users/HOME/Desktop/demo/frame{:d}.png'.format(count),frame)
        # this above one saves it in the location
        count += 1
        print(count)
    else:
        break

msg=''
i = 0
while (i < count):
	imgloc = 'C:/Users/HOME/Desktop/demo/frame%d.png' % i
	if msg[-7:-1]=='111111':
		break
	msg = msg + decode(imgloc)
    # print (msg)
    # print ('message %d encoded'%i)
	i += 1
print('msg decoded')
print(msg)
cap.release()
cv2.destroyAllWindows()
