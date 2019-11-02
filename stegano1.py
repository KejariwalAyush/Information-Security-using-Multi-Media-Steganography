import cv2
import numpy as np
import glob


video=cv2.VideoCapture("Sample1280.mp4")

a=1
while video.isOpened():
    check,frame=video.read()

    if check:
        cv2.imwrite('C:/Users/HOME/Desktop/demo/{:d}.jpg'.format(a),frame)
        print('read %d frame:'%a,check)
        text=input("the text to be hidden")
        image=cv2.imread('C:/Users/HOME/Desktop/demo/{:d}.jpg'.format(a))
        rows,cols=image.shape
        count=0

        for i in range(len(text)):
            asci=ord(text[i])
            st="{0:b}".format(asci)
            st='0'+ st+'0'
            for row in range(0,rows):
                col=0
                for j in range(0,9,3):

                    for col in range(count,count+3):

                        r,g,b=image[row][col]

                        if (st[j]==0)&(r%2==0)|(st[j]==1)&(r%2!=0):
                            pass
                        else:
                            r=-1
                        if (st[j+1]==0)&(g%2==0)|(st[j+1]==1)&(g%2!=0):
                            pass
                        else:
                            g=-1
                        if (st[j+2]==0)&(b%2==0)|(st[j+2]==1)&(b%2!=0):
                            pass
                        else:
                            b=-1
                        image[row][col]=r,g,b

                col+=3
        # frame=cv2.flip(frame,1)

        cv2.imwrite('C:/Users/HOME/Desktop/demo/{:d}.jpg'.format(a),image)

        a+=1
    else:
        break




video.release()
cv2.destroyAllWindows()



img_array =[]
for filename in glob.glob('C:/Users/HOME/Desktop/demo/*.jpg'):
    img=cv2.imread(filename)
    height, width ,layers= img.shape
    size=(width,height)
    img_array.append(img)#adss on to complete the image array
    #read.write.append.read+write

out=cv2.VideoWriter('vidproject.avi', cv2.VideoWriter_fourcc(*'DIVX'), 15 , size)

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()


