import cv2,sys,glob
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
	for n in range(1,h):
		if (img[n,n][0]!=0) & (img[n,n][1]!=0) & (img[n,n][2] != 0) :       # to extract pixels leaving [0 0 0] type of pixels
			pixel.append(img[n, n])
	# for i in pixel:
	# 	print (i,end=' ')               # to print unedited image pixels
	# print (len(pixel))
	i,j,k=0,0,0
	# i here is for msg counter of character which will be updated when the funct change is called
	# below under 1st while (whole) encryption code has been written
	while (i<=len(msg)):

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
	print ('Encrypted ,\nimage is saved with name "enc_img.png" at the location of this program')
	j=0
	for n in range(1,h):
		if (img[n,n][0]!=0) & (img[n,n][1]!=0) & (img[n,n][2] != 0) & (j<len(pixel)) :
			img[n][n]=pixel[j]
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
# to open video file
message = 'Morning this is the Steganography express at your call we wish you happy journey '
# message = 'this is a test message for video encoding with text message'
message+='1111111'
imgloc = "SampleVideo_1280x720_10mb.mkv"
cap = cv2.VideoCapture(imgloc)
fps=cap.get(cv2.CAP_PROP_FPS)
print(fps)
count = 0
# extracting frames and saving it new folder
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        # print('Read %d frame :'%count,ret)
        # frame = cv2.flip(frame,1)
        # this line flips the image horizontally ; for vertical,both replace 1 by 0,2 respectively
        cv2.imwrite('C:/Users/HOME/Desktop/demo/frame{:d}.png'.format(count),frame)
        # this above one saves it in the location
        count += 1
    else:
        break


i=0
l1 = 0
l2 = 7
while(True):
    msg = message[l1:l2]
    print (msg)
    imgloc = 'C:/Users/HOME/Desktop/demo/frame%d.png'%i
    encode(msg,imgloc)
    print ('message %d encoded'%i)
    if l2==len(message):
        break
    l1=l2
    l2=l2+7
    if l2>=len(message):
        l2=len(message)
    i+=1

cap.release()
cv2.destroyAllWindows()





img_array = []
for filename in glob.glob('C:/Users/HOME/Desktop/demo/*.png'):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)




out = cv2.VideoWriter('vidstegano.mkv',cv2.VideoWriter_fourcc(*'DIVX'), fps, size)

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()

print ('output video is vidstegano.mkv at the location of this program')