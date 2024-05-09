# import libraries
import math
import cv2
import numpy as np
import time
import BicepCurl_PoseModule as pm
import cvzone


#Camera
cap = cv2.VideoCapture(r'D:\CPEDES\Flask\Exercises\gaining_muscle\bicep curl\bicepcurl.mp4')

#import class
detector_bicep = pm.poseDetector()

#Initialize Variables
count_bicep_left = 0
count_bicep_right = 0
dir_bicep_left = 0
dir_bicep_right = 0

start_time = time.time() # starts time
repetition_time = 60 # duration time
display_info = True # display features

bar_left = 0
bar_right = 0
per_left = 0
per_right = 0
angle_left = 0
angle_right = 0

color_right_bicepcurl = (0, 0, 255)
color_left_bicepcurl = (0, 0, 255)

orientation = ''
orientation2 = ''


# main loop
while True:
    # reads camera 
    success, img = cap.read()
    # resizes video feed (can be changed depending on requirements of our Raspberry PI and Display Monitor Resolution)
    img = cv2.resize(img, (1280, 720))

    # Timer - starts timer based on set duration
    elapsed_time = time.time() - start_time
    remaining_time = max(0, repetition_time - elapsed_time)


    if display_info:  # Check if to display counter, bar, and percentage
        img = detector_bicep.findPose(img, False) # initializes img as variable for findpose function
        lmList_bicep = detector_bicep.findPosition(img, False) # initializes lmList_bicep as variable for findPosition function

        # Define hand angles outside the if statement
        if len(lmList_bicep) != 0:

            angle_left, orientation = detector_bicep.BicepCurl(img, 11 ,13, 15, True)
            angle_right, orientation2 = detector_bicep.BicepCurl(img, 12, 14 ,16, True)

            if orientation == 'right' and orientation2 == "right":
                per_left = np.interp(angle_left, (180, 300), (0, 100))
                bar_left = np.interp(angle_left, (180, 300), (400, 200))

                per_right = np.interp(angle_right, (180, 300), (0, 100)) 
                bar_right = np.interp(angle_right, (180, 300), (400, 200)) 

                if int(per_left) == 100:
                    color_left_bicepcurl = (0, 255, 0)  # Change color of left leg bar to green
                elif int(per_right) == 100:
                    color_right_bicepcurl = (0, 255, 0)
                else:
                    color_left_bicepcurl = (0, 0, 255)  # Keep color of left leg bar as red
                    color_right_bicepcurl = (0, 0, 255)

                if angle_right >= 300:
                    if dir_bicep_right == 0:
                        count_bicep_right += 0.5
                        dir_bicep_right = 1
                elif angle_right <= 190:
                    if dir_bicep_right == 1:
                        count_bicep_left += 0.5
                        dir_bicep_right = 0

                if angle_left >= 300:
                    if dir_bicep_left == 0:
                        count_bicep_left += 0.5
                        dir_bicep_left = 1

                elif angle_left <= 190:
                    if dir_bicep_left == 1:
                        count_bicep_left += 0.5
                        dir_bicep_left = 0

            elif orientation == 'left' and orientation2 == 'left' :
                per_left = np.interp(angle_left, (40, 180), (100, 0))
                bar_left = np.interp(angle_left, (40, 180), (200, 400))

                per_right = np.interp(angle_right, (40, 180), (100, 0)) 
                bar_right = np.interp(angle_right, (40, 180), (200, 400)) 

                if int(per_left) == 100:
                    color_left_bicepcurl = (0, 255, 0)  # Change color of left leg bar to green
                elif int(per_right) == 100:
                    color_right_bicepcurl = (0, 255, 0)
                else:
                    color_left_bicepcurl = (0, 0, 255)  # Keep color of left leg bar as red
                    color_right_bicepcurl = (0, 0, 255)

                if angle_right <= 40:
                    if dir_bicep_right == 0:
                        count_bicep_right += 0.5
                        dir_bicep_right = 1

                elif angle_right >= 180:
                    if dir_bicep_right == 1:
                        count_bicep_right += 0.5
                        dir_bicep_right = 0
                
                if angle_left <= 40:
                    if dir_bicep_left == 0:
                        count_bicep_left += 0.5
                        dir_bicep_left = 1

                elif angle_left >= 180:
                    if dir_bicep_left == 1:
                        count_bicep_left += 0.5
                        dir_bicep_left = 0

            elif orientation == 'front' and orientation2 == 'front':
                per_left = np.interp(angle_left, (30, 130), (100, 0)) # first parenthesis, the value threshold of the angle. Second, represents the interp value
                bar_left = np.interp(angle_left, (30, 140), (200, 400)) # *

                per_right = np.interp(angle_right, (200, 340), (0, 100)) # *
                bar_right = np.interp(angle_right, (200, 350), (400, 200)) # *

                if int(per_left) == 100:
                    color_left_bicepcurl = (0, 255, 0)  # Change color of left leg bar to green
                elif int(per_right) == 100:
                    color_right = (0, 255, 0)
                else:
                    color_left_bicepcurl = (0, 0, 255)  # Keep color of left leg bar as red
                    color_right_bicepcurl = (0, 0, 255)

                # Check for the left dumbbell curls
                if per_left == 100: 
                    if dir_bicep_left == 0:
                        count_bicep_left += 0.5
                        dir_bicep_left = 1 

                if per_left == 0:
                    if dir_bicep_left == 1:
                        count_bicep_left += 0.5
                        dir_bicep_left = 0  

                # Check for the right dumbbell curls
                if per_right == 100: 
                    if dir_bicep_right == 0:
                        count_bicep_right += 0.5
                        dir_bicep_right = 1 
                if per_right == 0:
                    if dir_bicep_right == 1:
                        count_bicep_right += 0.5
                        dir_bicep_right = 0  

        # label
        cvzone.putTextRect(img, 'Bicep Curl Tracker', [345, 30], thickness=2, border=2, scale=2.5) 

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # Orientation
        cv2.rectangle(img, (890, 100), (1180, 160), (0, 0, 255), -2)
        cv2.putText(img, f"Orientation: {orientation}", (900, 140), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)

        # bar
        cv2.putText(img, f"R {int(per_right)}%" , (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (255, 255, 255), 5)
        cv2.rectangle(img, (8, int(bar_right)), (50, 400), color_right_bicepcurl, -1)

        cv2.putText(img, f"L {int(per_left)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (255, 255, 255), 5)
        cv2.rectangle(img, (952, int(bar_left)), (995, 400), color_left_bicepcurl, -1)

    #count
    cv2.rectangle(img, (20, 20), (140, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(count_bicep_right)}/5", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (150, 20), (270, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(count_bicep_left)}/5", (160, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [345, 30], thickness=2, border=2, scale=2.5)
        display_info = False

    if count_bicep_right >= 5 and count_bicep_left >= 5:
        cvzone.putTextRect(img, 'All Repetitions Completed', [345, 30], thickness=2, border=2, scale=2.5)
        display_info = False

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
