#تمرين2 الجزء الثاني
#تم
import cv2
import numpy as np
import time
import PoseModule as pm
import math

cap = cv2.VideoCapture(0)

detector = pm.poseDetector()
count = 0
dir = 0
pTime = 0


while True:
    success, img = cap.read()
    img = cv2.resize(img , (1280,720))
    # img = cv2.imread("assets/test.png")
    img = detector.findPose(img, False)
    lmlist = detector.findPosition(img,False)
    

    if len(lmlist) != 0:
        #Right Leg
        angle = detector.findAngle(img, 24, 26, 28)
        # #Left Leg
        # detector.findAngle(img, 23, 25 , 27)
        per = np.interp(angle,(204,257),(-100,0))
        #print(angle,per)
        #bar = np.interp(angle, (204,257), (650,100))

        #check for the leg 
        color_Per = (255,0,255)
        if per == 0:
            #100%
            color_Per = (0,255,0)
            if dir == 0:
                count +=0.5
                dir = 1
        if per == -100:
            #0%
            color_Per = (0,255,0)
            if dir == 1:
                count += 0.5
                dir = 0
        

        # Draw Bar
        # cv2.rectangle(img, (1200,650), (300,650) , (0,0,255),cv2.FILLED)
        # cv2.rectangle(img, (1200,int(bar)), (300,650) , (0,0,255),cv2.FILLED)
        
        


        #Draw Counter
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

    cv2.imshow("Image", img)
    cv2.waitKey(1)
