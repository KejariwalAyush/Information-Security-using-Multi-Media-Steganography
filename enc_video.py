import cv2,sys,glob
import numpy as np


# to open video file
message = input("Enter a message")
# message = 'this is a test message for video encoding with text message'
imgloc = input('enter location of video which you want to decode : ')
cap = cv2.VideoCapture(imgloc)
count = 0
# extracting frames and saving it new folder
while(cap.isOpened()):
    ret, frame = cap.read()
    if(ret):
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
l2 = 30
while(True):
    msg = message[l1:l2]
    print (msg)
    imgoc = 'C:/Users/HOME/Desktop/demo/frame%d.png'%i
    encode(msg,imgoc)
    print ('message %d encoded'%i)
    if l2==len(message):
        break
    l1=l2
    l2=l2+30
    if l2>=len(message):
        l2=len(message)
    i+=1

cap.release()
cv2.destroyAllWindows()

img_array = []
for filename in glob.glob('C:/Users/HOME/Desktop/demo*.png'):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)


out = cv2.VideoWriter('project1.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, size)

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()

print ('output video is project.avi at the location of this prg')