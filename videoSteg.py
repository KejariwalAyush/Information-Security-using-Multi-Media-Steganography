import cv2,sys,glob
import numpy as np
from imgstg import encode
from imgstg import decode

def enc_vid():
    # to open video file
    print("create a new txt file and enter your text there ",end="\n")
    loc = input("enter the file location : ")
    loc = loc.replace('\\','/')
    myfile = open(loc, "rt")# open lorem.txt for reading text
    msg = myfile.read()         # read the entire file into a string
    myfile.close()                   # close the file
    message = msg
    mm = message
    message = message.replace("\n","||||||||||||")
    # message = input("Enter a message \n")
    # message = 'This project is made by Ayush Kejariwal , Subhanjan Dash , Sourav bera. The project to be presented in ICCIC international conference'
    # imgloc = 'D:/sample.mkv'
    imgloc = input('enter location of video in which you want to encode msg : ')
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
        # print ('message %d encoded'%i)
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

    out = cv2.VideoWriter('project.mkv',cv2.VideoWriter_fourcc(*'HFYU'), fps, size)

    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()

    print ('output video is project.mkv at the location of this prg')

def dec_vid():
    imgloc = input('enter location of video which you want to decode : ')
    # imgloc = 'project1.mkv'
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
        mr = m[::-1]    # to reverse the string if only spaces are present in frame its reverse is also same
        if(mr==m):
            break
        msg = msg + m
        # print (msg)
        # print ('message %d decoded'%i)

        i+=1
    msg = msg.rstrip()
    msg = msg.replace("||||||||||||","\n")
    print ('msg decoded')
    print (msg)
    cap.release()
    cv2.destroyAllWindows() 

# here starts main function of the program
while (True):
    n = input ("enter 1: to encode a message in video \n      2: to decode a message from video \n      0: to EXIT : ")
    if n=='1' :
        enc_vid()
    elif n=='2' :
        dec_vid()
    elif n=='0' :
        sys.exit()
    else : 
        print ("please enter correct input OR enter 0 to EXIT")