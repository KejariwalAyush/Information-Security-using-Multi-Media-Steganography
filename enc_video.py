import cv2,sys,glob
import numpy as np
from imgstg import encode


# to open video file
myfile = open("test.txt", "rt") # open lorem.txt for reading text
msg = myfile.read()         # read the entire file into a string
myfile.close()                   # close the file
message = msg
mm = message

message = message.replace("\n","||||||||||||")
# message = input("Enter a message \n")
# message = 'This project is made by Ayush Kejariwal , Subhanjan Dash , Sourav bera. The project to be presented in ICCIC international conference'
imgloc = 'D:/sample.mkv'
# imgloc = input('enter location of video which you want to decode : ')
cap = cv2.VideoCapture(imgloc)
fps = cap.get(cv2.CAP_PROP_FPS)
count = 100000
for i in range (0,600):
    message+=' '
# print (i)
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
# r = int(5*len(message)/(count%100000))+1
# print(r)
i=100000
l1 = 0
l2 = 250
while(True):
    msg = message[l1:l2]
    # print (msg)
    imgoc = 'D:/data/frame%d.png'%i
    encode(msg,imgoc)
    print ('message %d encoded'%i)
    if l2==len(message):
        break
    l1=l2
    l2=l2+250
    if l2>=len(message):
        l2=len(message)
    i+=1

print ('message has been encoded and msg is')
print(mm)

i+=1
# while(i<=count):
#     imgoc = 'D:/data/frame%d.png'%i
#     img = cv2.imread(imgloc)
#     cv2.imwrite(imgloc, img,  [cv2.IMWRITE_PNG_COMPRESSION, 9])
#     i+=1
cap.release()
cv2.destroyAllWindows()

img_array = []
for filename in glob.glob('D:/data/*.png'):
    # print (filename)
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)

out = cv2.VideoWriter('project1.mkv',cv2.VideoWriter_fourcc(*'HFYU'), fps, size)

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()

print ('output video is project.mkv at the location of this prg')