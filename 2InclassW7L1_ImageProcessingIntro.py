import cv2 
import matplotlib.pyplot as plt
import numpy as np 

#press q to escape, not x since it will restart 

cap = cv2.VideoCapture(0) #open defualt camera 

while True: 
    ret, frame = cap.read() #read a fram from the camera 

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #convert frame to grayscale 
    edges = cv2.Canny(gray, 100, 200) #apply hpf
    blur = cv2.GaussianBlur(gray, (5,5), 0) #now applying gaussian cblur to frame 
    #for teh blur, if you apply something like 99, 5 you can see streaks resulting in blurring of the horizontal. so it is (horizontal, verticle)


    #cv2.imshow('Live video', gray)
    cv2.imshow('edges', edges ) #as you can see, this actually does detect edges (ie even mustasche, not beard though, but also creases in hand/shirt)
    #this is how robots can detect objects, or atleast their edges 
    #cv2.imshow('Blurred', blur) #now this applies a blur, it is adjsted throuhg the 5 5 (may need to be square matrix and/or odd number)

    #check if the q key is pressed to exit the loop 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 

cap.release() 
cv2.destroyAllWindows() #destory all openCV windows 

# !OVERALL LESSON!: when an hpf is applied, the result will boost the sharpness of the image
#if an lpf is applied, the image is instead blurred 
#there is a third option, 

#this is also the method that 