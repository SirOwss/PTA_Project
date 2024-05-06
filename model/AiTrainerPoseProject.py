
import math
import time
import cv2
import numpy as np
import User_UI.PoseModule as pm
from PIL import Image, ImageTk
import tkinter as tk
class POOOS():
    cap = cv2.VideoCapture(0)
    detector = pm.poseDetector()
    count = 0
    dir = 0
    pTime = 0

    def update_image():
        global count, dir, pTime
        success, img = cap.read()
        img = cv2.resize(img , (800,600))
        img = detector.findPose(img, False)
        lmlist = detector.findPosition(img,False)

        if len(lmlist) != 0:
            angle = detector.findAngle(img, 26, 30, 32)
            per = np.interp(angle,(87,109),(0,100))
            color_Per = (255,0,255)
            if per == 100:
                color_Per = (0,255,0)
                if dir == 1:
                    count +=0.5
                    dir = 0
            if per == 0:
                color_Per = (0,255,0)
                if dir == 0:
                    count += 0.5
                    dir = 1

            cv2.rectangle(img, (15,645), (300,680) , (0,0,255),cv2.FILLED)
            cv2.putText(img, f'Count= {int(count)}', (45,670), cv2.FONT_HERSHEY_PLAIN,2,
                        (0,255,255),2)
            cv2.putText(img, f'{int(math.fabs(per))} %', (45,705), cv2.FONT_HERSHEY_PLAIN,2,
                        color_Per,2)

        cTime = time.time()
        fps = 1/(cTime - pTime)
        pTime = cTime
        cv2.putText(img, f'fps: {int(fps)}', (50,100), cv2.FONT_HERSHEY_PLAIN,2,
                    (0,0,255),2)

        # Convert the image from BGR to RGB
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # Convert the Image object into a TkPhoto object
        im = Image.fromarray(img)
        imgtk = ImageTk.PhotoImage(image=im) 
        # Put the image into the label
        image_label.config(image=imgtk)
        image_label.image = imgtk
        # Call this function again after 10 milliseconds
        window.after(10, update_image)

# Call the function to start
