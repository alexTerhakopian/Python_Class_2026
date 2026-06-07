import cv2 
import matplotlib.pyplot as plt
import numpy as np 

cap = cv2.VideoCapture(0) # alternative way to take a continuas video using my camera 

def is_candy_bar_shape(contour, min_area=3000, max_area=80000): #depending on the distance from the camera, these areas may need to be changed to be representative 

    area = cv2.contourArea(contour)
    if area < min_area or area > max_area: #double check that area that i mentioned earleir 
        return False, None

    epsilon = 0.04 * cv2.arcLength(contour, True) #I am not really sure what a contour is/how it works, but we use it here 
    approx = cv2.approxPolyDP(contour, epsilon, True)

    if not (4 <= len(approx) <= 6): #check if its rectangular enough 
        return False, None

    x, y, w, h = cv2.boundingRect(contour) #aspect ratio (rectangular?)
    aspect_ratio = max(w, h) / min(w, h)  # always >= 1

    if not (1.0 <= aspect_ratio <= 10.0): #again, these numvers may need to be adjusted based on the type of candy bar or what specific rectangular ratios you are expecting. 
        return False, None

#one limitation here is that the rectangle is only detected if more wide than tall, so any candy bar stanading vertically will not be detected
    bounding_box_area = w * h
    rectangularity = area / bounding_box_area
    if rectangularity < 0.6:
        return False, None

    return True, (x, y, w, h)


while True:
    ret, frame = cap.read()  
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (5, 5), 0) #apply gaussian blur as done earlier to smooth things out 

    edges = cv2.Canny(blur, 80, 180) #now we apply an hpf to increase sharpness to be able to detect edges 

    kernel = np.ones((3, 3), np.uint8) #I do not entirely undertand what this does, but through reserach it was a nessecary thing to include 
    dilated = cv2.dilate(edges, kernel, iterations=2)

    contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


    output = frame.copy() #this is making a frame to put around the detected candy bar 
    detected = False

    for contour in contours:
        found, bbox = is_candy_bar_shape(contour)
        if found:
            x, y, w, h = bbox
            # actuall command to draw box is herer 
            cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(output, "Candy Bar?", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2) #phont only for aesthetic purposes. Only nessecary thing is where we want the message to show
            detected = True

    # Show a red alert banner if the cady bar is detected
    if detected: 
        cv2.putText(output, "CANDY BAR DETECTED", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 3)

    # Show all windows (this shows the normal camera, not grayscale, along with any rectagle and text if a candy bar is detected)
    cv2.imshow('Edges (HPF)', edges)
    cv2.imshow('Dilated Edges', dilated)
    cv2.imshow('Detection Output', output)

    if cv2.waitKey(1) & 0xFF == ord('q'): #we use the same q command as earlier to break 
        break

cap.release()
cv2.destroyAllWindows()


#a couple notes: 
#this is very sensetive to lighting, sometimes detecting letters on my shirt as "candy bars" then being unable to detect a rectangular shaped object right in front of it
#this code is also very dependent on the distance from the camera and other factors like that 
#finally, it needst to be fined tuned accounting for distance and size of the candy bar it is supposed to detect 
#one last issue is it can only detect bars if they are horizontal, not verticle 