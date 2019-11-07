import cv2, sys
import numpy as np
import os
import glob

def encode():


    video=cv2.VideoCapture("Sample1280.mp4")#Sample video
    msg = input("Enter the Message to be inputted here")
    a=1
    while video.isOpened():# while true:

        succes,image = video.read()#True if video is read properly
        if succes == True:# runs till the Video is running
            print ("read %d image" %a ,succes)
            print("image Dimensions:",image.shape[0],image.shape[1],image.shape[2])
            h=image.shape[0]
            w=image.shape[1]
            channel=image.shape[2]
            arr = []
            for i in (1,h-1):#accessing diagonal element
               if image[i,i][0] !=0 | image[i,i][1 ] !=0 | image[i,i][2] !=0 :# not taking [0,0,0] black pixels
                    arr.append(image[i,i])
            print(len(arr))

            i=0
            j=0
            k=0
            while j<len(msg):
                n=ord(msg[i])
                b= '0' + "{0:b}".format(n)#Converting to binary
                if len(b)== 7:
                    b= '00' + b# converting into 9 element string
                    print(b)

                x=0
                while x<(len(b)):
                    if b[x]=='0':
                            if (arr[j][k]%2)!=0:
                                arr[j][k]-=1
                    elif b[x]=='1':
                            if arr[j][k] % 2 == 0:
                                arr[j][k ]= arr[j][k]-1
                    print(arr[j][k])
                    if k==2:#arr[[0,1,2][][][].....]
                            k=0
                            j+=1
                    else:
                            k+=1
                    x+=1
                j+=1
                k=0
                i+=1


            print("Encrypted ,\n image is saved with name 'enc_img.png' at the location of the program")



            j=0
            for m in range(1,h):
                if (image[m,m][0]!=0) & (image[m,m]!=0) & (image[m,m]!=0):#image with pixel [0,0,0]
                            image[m,m] = arr[j]#Encrypting image
                j+=1

            #in above for loop we have created the encrypted image
            cv2.imwrite('enc_img {: d}.png'.format(a) , image)#Saves the encrypted imagw
            cv2.imshow('enc_image {: d}' .format(a), image)
            cv2.waitKey(0)
            a+=1
        else:
                            break
    video.release()


    img_array = []
    for filename in glob.glob('C:/Users/HOME/.PyCharmCE2019.2/config/scratches/*.png'):#S Extracting the image from the python file directory
        img=cv2.imread(filename)
        h,w,layers = img.shape
        size=(h,w)
        img_array.append(img)

    out=cv2.VideoWriter('project.avi' , cv2.VideoWriter_fourcc(*'DIVX'), 15, size)# Initialising VideoWriter
    for i in range(len(img_array)):
        out.write(img_array[i])# Creating Video Image from Individual frames
    out.release()





#starting decoding technique
def decode():
    video = cv2.VideoCapture('project.avi')#
    stb=""
    a=0# counter variable
    arr = []
    msg=""
    while video.isOpened():
        ret,image=video.read()
        if ret==True:# while video Reading On
            print('Read %d frame:'%a , ret)
            h = image.shape[0]
            w = image.shape[1]
            layers = image.shape[2]
            print('image %d dimensions : '%a,h,w)
            for i in range(1,h-1):
                if image[i,i][0]!=0 | image[i,i][1]!=0  | image[i,i][2]!=0:# Except the [0, 0, 0] pixels
                    arr.append(image[i,i])#extracting the used pixels
            j=0
            k=0
            for j in range(1,h-1):
                for k in range(0,3):
                    if arr[j][k]%2==0: #checks wether 0 or 1
                        stb = stb +"0"
                    if  arr[j][k]%2==1:
                            stb =stb +"1"

            c=0
            n=len(stb)%9
            for i in range(1,n):
                asci = int(stb[c:c+9])# Substring the total String Binary Message
                c=c+9
                ch = chr(asci)# Converting to individual charachters and Adding it to msg string
                msg=msg+ch
        print(msg)
    video.release()
while True:
    n = input('Enter the value 1: to en code  a message \n2:To de code a message \n 3. To exit')
    if n=='1':
        encode()
    elif n=='2':
        decode()
    elif n=='3':
        sys.exit()
    else:
        print("Enter correct input \nor Enter '0' to exit")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
































