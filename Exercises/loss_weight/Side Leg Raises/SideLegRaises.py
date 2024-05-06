# import libraries
import math
import cv2
import numpy as np
import time
import SideLegRaises_PoseModule as pm
import cvzone


#Camera
cap = cv2.VideoCapture(r'D:\CPEDES\Flask\Exercises\loss_weight\Side Leg Raises\sidelegraises.mp4')

#import class
detector_SideLegRaises = pm.poseDetectorSideLegRaises()

#Initialize Variables
count_sidelegraise_left = 0
count_sidelegraise_right = 0

dir_sidelegraises_left = 0
dir_sidelegraises_right = 0

start_time_slr = time.time() # starts time
repetition_time_slr = 60 # duration time
display_info_slr = True # display features

bar_left_slr = 0
bar_right_slr = 0
per_left_slr = 0
per_right_slr = 0
angle_left_slr = 0

color_left_leg_slr = (0, 0, 255)
color_right_leg_slr = (0, 0, 255)

left_leg_slr = 0
right_leg_slr = 0


# main loop
while True:
    # reads camera 
    success, img = cap.read()
    # resizes video feed (can be changed depending on requirements of our Raspberry PI and Display Monitor Resolution)
    img = cv2.resize(img, (1280, 720))

    # Timer - starts timer based on set duration
    elapsed_time = time.time() - start_time_slr
    remaining_time = max(0, repetition_time_slr - elapsed_time)


    if display_info_slr:  # Check if to display counter, bar, and percentage
        img = detector_SideLegRaises.findPose(img, False) # initializes img as variable for findpose function
        lmList_bicep = detector_SideLegRaises.findPosition(img, False) # initializes lmList_bicep as variable for findPosition function

        # Define hand angles outside the if statement
        if len(lmList_bicep) != 0:
            right_leg_slr = detector_SideLegRaises.SideLegRight(img, 12, 24, 26, 28, True)
            left_leg_slr = detector_SideLegRaises.SideLegLeft(img, 11, 23, 25, 27, True) # defines right arm landmark keypoints

            per_right_slr = np.interp(right_leg_slr, (180, 260), (0, 100)) 
            bar_right_slr = np.interp(right_leg_slr, (180, 260), (400, 200)) 

            per_left_slr = np.interp(left_leg_slr, (100, 170), (100, 0)) 
            bar_left_slr = np.interp(left_leg_slr, (100, 170), (200, 400)) 

            if int(per_left_slr) == 100 :
                color_left_leg_slr = (0, 255, 0) 
            elif int(per_right_slr) == 100:
                color_right_leg_slr = (0, 255, 0)
            else:
                color_left_leg_slr = (0, 0, 255)  
                color_right_leg_slr = (0, 0, 255)

            if right_leg_slr >= 260:
                if dir_sidelegraises_right == 0 and count_sidelegraise_right <= 5:
                    count_sidelegraise_right += 0.5
                    if count_sidelegraise_right == 5:
                        dir_sidelegraises_right = 0
                    else:
                        dir_sidelegraises_right = 1
            if right_leg_slr <= 180:
                if dir_sidelegraises_right == 1 and count_sidelegraise_right <= 5:
                    count_sidelegraise_right += 0.5
                    if count_sidelegraise_right == 5:
                        dir_sidelegraises_right = 1
                    else:
                        dir_sidelegraises_right = 0
            
            if left_leg_slr <= 100:
                if dir_sidelegraises_left == 0 and count_sidelegraise_left <= 5:
                    count_sidelegraise_left += 0.5
                    if count_sidelegraise_left == 5:
                        dir_sidelegraises_left = 0
                    else:
                        dir_sidelegraises_left = 1
            elif left_leg_slr >= 170:
                if dir_sidelegraises_left == 1 and count_sidelegraise_left <= 5:
                    count_sidelegraise_left += 0.5
                    if count_sidelegraise_left == 5:
                        dir_sidelegraises_left = 1
                    else:
                        dir_sidelegraises_left = 0

        # label
        cvzone.putTextRect(img, 'Side Leg Raise', [345, 30], thickness=2, border=2, scale=2.5) 

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # bar
        cv2.putText(img, f"R {int(per_right_slr)}%" , (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_slr)), (50, 400), color_right_leg_slr, -1)

        cv2.putText(img, f"L {int(per_left_slr)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_slr)), (995, 400), color_left_leg_slr, -1)
        

    #count
    cv2.rectangle(img, (20, 20), (140, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(count_sidelegraise_right)}/5", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (150, 20), (270, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(count_sidelegraise_left)}/5", (160, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [345, 30], thickness=2, border=2, scale=2.5)
        display_info_slr = False

    if count_sidelegraise_right == 5 and count_sidelegraise_left == 5:
        cvzone.putTextRect(img, 'All Repetitions Completed', [345, 30], thickness=2, border=2, scale=2.5)
        display_info_slr = False

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
