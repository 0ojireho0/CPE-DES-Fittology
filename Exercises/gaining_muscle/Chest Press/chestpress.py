# import libraries
import math
import cv2
import numpy as np
import time
import chestpress_PoseModule as pm
import cvzone


#Camera
cap = cv2.VideoCapture(r'D:\CPEDES\Flask\Exercises\gaining_muscle\Chest Press\chestpressvid.mp4')

#import class
detector_chestpress = pm.poseDetector()

#Initialize Variables
count_chestpress_left = 0
count_chestpress_right = 0

dir_chestpress_left = 0
dir_chestpress_right = 0

start_time_chestpress = time.time() # starts time
repetition_time_chestpress = 60 # duration time
display_info_chestpress = True # display features

bar_left_chestpress = 0
bar_right_chestpress = 0
per_left_chestpress = 0
per_right_chestpress = 0
angle_left_chestpress = 0
angle_right_chestpress = 0


# main loop
while True:
    # reads camera 
    success, img = cap.read()
    # resizes video feed (can be changed depending on requirements of our Raspberry PI and Display Monitor Resolution)
    img = cv2.resize(img, (1280, 720))

    # Timer - starts timer based on set duration
    elapsed_time = time.time() - start_time_chestpress
    remaining_time = max(0, repetition_time_chestpress - elapsed_time)


    if display_info_chestpress:  # Check if to display counter, bar, and percentage
        img = detector_chestpress.findPose(img, False) # initializes img as variable for findpose function
        lmList_bicep = detector_chestpress.findPosition(img, False) # initializes lmList_bicep as variable for findPosition function

        # Define hand angles outside the if statement
        if len(lmList_bicep) != 0:
            angle_left_chestpress = detector_chestpress.findAngle(img, 11, 13, 15)
            angle_right_chestpress = detector_chestpress.findAngle(img, 12, 14, 16) # defines right arm landmark keypoints
            # (refer to mediapipe landmark mapping for number equivalent)

            # Interpolate angle to percentage and position on screen
            per_left_chestpress = np.interp(angle_left_chestpress, (50, 155), (0, 100)) # first parenthesis, the value threshold of the angle. Second, represents the interp value
            bar_left_chestpress = np.interp(angle_left_chestpress, (50, 165), (400, 200)) # 

            per_right_chestpress = np.interp(angle_right_chestpress, (190, 300), (100, 0)) # 
            bar_right_chestpress = np.interp(angle_right_chestpress, (190, 300), (200, 400)) # 

            if angle_left_chestpress >= 155:
                if dir_chestpress_left == 0 and count_chestpress_left < 5:
                    count_chestpress_left += 0.5
                    if count_chestpress_left == 5:
                        dir_chestpress_left = -1
                    else:
                        dir_chestpress_left = 1 
            elif angle_left_chestpress <= 50:
                if dir_chestpress_left == 1 and count_chestpress_left < 5:
                    count_chestpress_left += 0.5
                    if count_chestpress_left == 5:
                        dir_chestpress_left = -1
                    else:
                        dir_chestpress_left = 0  

            if angle_right_chestpress <= 190: 
                if dir_chestpress_right == 0 and count_chestpress_right < 5:
                    count_chestpress_right += 0.5
                    if count_chestpress_right == 5:
                        dir_chestpress_right = -1
                    else:
                        dir_chestpress_right = 1 

            if angle_right_chestpress >= 270:
                if dir_chestpress_right == 1 and count_chestpress_right < 5:
                    count_chestpress_right += 0.5
                    if count_chestpress_right == 5:
                        dir_chestpress_right = -1
                    else:
                        dir_chestpress_right = 0

        # label
        cvzone.putTextRect(img, 'Chest Press Tracker', [345, 30], thickness=2, border=2, scale=2.5) 

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # bar
        cv2.putText(img, f"R {int(per_right_chestpress)}%" , (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_chestpress)), (50, 400), (0, 0, 255), -1)

        cv2.putText(img, f"L {int(per_left_chestpress)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_chestpress)), (995, 400), (0, 0, 255), -1)
        
        if angle_left_chestpress >= 155:
            cv2.rectangle(img, (952, int(bar_left_chestpress)), (995, 400), (0, 255, 0), -1)

        if angle_right_chestpress <= 190:
            cv2.rectangle(img, (8, int(bar_right_chestpress)), (50, 400), (0, 255, 0), -1)

    #count
    cv2.rectangle(img, (20, 20), (140, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(count_chestpress_right)}/5", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (150, 20), (270, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(count_chestpress_right)}/5", (160, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255 ,255), 7)

    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
        display_info_chestpress = False

    if count_chestpress_right == 5 and count_chestpress_left == 5:
        cvzone.putTextRect(img, 'All Repetitions Completed', [390, 30], thickness=2, border=2, scale=2.5)
        display_info_chestpress = False

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
