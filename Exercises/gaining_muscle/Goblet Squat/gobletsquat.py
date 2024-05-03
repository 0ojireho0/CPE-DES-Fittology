import math
import cv2
import numpy as np
import time
import gobletsquat_PoseModule as pm
import cvzone

cap = cv2.VideoCapture(r'C:\Users\RID\Desktop\pose_estimation\aipose2\Exercise\gainingmuscle\gobletsquat2.mp4')
detector_gobletsquat = pm.poseDetectorGobletSquat()

count_goblet_squat = 0
dir_goblet_squat = 0

pTime = 0
start_time = time.time()
repetition_time = 60
display_info = True

leftbody = 0
rightbody = 0

per_left_body = 0
bar_left_body = 0

per_right_body = 0
bar_right_body = 0

cooldown_duration = 5
cooldown_timer = 0

color_left_leg = (0, 0, 255)
color_right_leg = (0, 0, 255)

done = 0

while True:
    success, img = cap.read()
    img = cv2.resize(img, (1280, 720))

    elapsed_time = time.time() - start_time
    remaining_time = max(0, repetition_time - elapsed_time)

    if display_info:  # Check if to display counter, bar, and percentage
        img = detector_gobletsquat.findPose(img, False)
        lmList_jumping_jacks = detector_gobletsquat.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_jumping_jacks) != 0:

            # Right and Left keypoints
            rightleg, orientation = detector_gobletsquat.GobletSquat(img, 24, 26, 28, True)
            leftleg, orientation2 = detector_gobletsquat.GobletSquat(img, 23, 25, 27, True)

            if cooldown_timer > 0:
                cooldown_timer -= 1

            if orientation == 'right' and orientation2 == 'right':
                    
                    per_right_leg = np.interp(rightleg, (90, 170), (100, 0))
                    bar_right_leg = np.interp(rightleg, (90, 170), (480, 680))
                    per_left_leg = np.interp(leftleg, (90, 170), (100, 0))
                    bar_left_leg = np.interp(leftleg, (90, 170), (480, 680))

                    if int(per_left_leg) == 100 and int(per_right_leg) == 100:
                        color_left_leg = (0, 255, 0) 
                        color_right_leg = (0, 255, 0) 
                    else:
                        color_left_leg = (0, 0, 255)  
                        color_right_leg = (0, 0, 255)

                    if rightleg <= 90 and leftleg <= 90:
                        if dir_goblet_squat == 0:
                            count_goblet_squat += 0.5
                            dir_goblet_squat = 1
                            cooldown_timer = cooldown_duration
                    elif rightleg >= 170 and leftleg >= 170:
                        if dir_goblet_squat == 1:
                            count_goblet_squat += 0.5
                            dir_goblet_squat = 0
                            cooldown_timer = cooldown_duration

            elif orientation =='left' and orientation2 == 'left':
                if leftleg is not None and rightleg is not None:
                    per_right_leg = np.interp(rightleg, (190, 270), (0, 100))
                    bar_right_leg = np.interp(rightleg, (190, 270), (680, 480))
                    per_left_leg = np.interp(leftleg, (190, 270), (0, 100))
                    bar_left_leg = np.interp(leftleg, (190, 270), (680, 480))

                    if int(per_left_leg) == 100 and int(per_right_leg) == 100:
                        color_left_leg = (0, 255, 0) 
                        color_right_leg = (0, 255, 0) 
                    else:
                        color_left_leg = (0, 0, 255)  
                        color_right_leg = (0, 0, 255)
              
                    if rightleg >= 270 and leftleg >= 270:
                        if dir_goblet_squat == 0:
                            count_goblet_squat += 0.5
                            dir_goblet_squat = 1
                            cooldown_timer = cooldown_duration
                    elif rightleg <= 190 and leftleg <= 190:
                        if dir_goblet_squat == 1:
                            count_goblet_squat += 0.5
                            dir_goblet_squat = 0
                            cooldown_timer = cooldown_duration



            elif orientation == 'front' and orientation2 == 'front':

                    per_right_leg = np.interp(rightleg, (150, 240), (100, 0))
                    bar_right_leg = np.interp(rightleg, (150, 240), (480, 680))
                    per_left_leg = np.interp(leftleg, (150, 240), (100, 0))
                    bar_left_leg = np.interp(leftleg, (150, 240), (480, 680))
                    
                    
                    if int(per_left_leg) == 100 and int(per_right_leg) == 100:
                        color_left_leg = (0, 255, 0) 
                        color_right_leg = (0, 255, 0) 
                    else:
                        color_left_leg = (0, 0, 255)  
                        color_right_leg = (0, 0, 255)  # Keep color of right leg bar as red

                    if rightleg <= 160 and leftleg <= 160:
                        if dir_goblet_squat == 0:
                            count_goblet_squat += 0.5
                            dir_goblet_squat = 1
                            cooldown_timer = cooldown_duration
                    elif rightleg >= 240 and leftleg >= 240: 
                        if dir_goblet_squat == 1:
                            count_goblet_squat += 0.5
                            dir_goblet_squat = 0
                            cooldown_timer = cooldown_duration

        #Delay Timer for Pose Estimation
        fps = cap.get(cv2.CAP_PROP_FPS)
        if cooldown_timer > 0:
            cooldown_timer -= 1 / fps

        cvzone.putTextRect(img, 'Goblet Squat Tracker', [450, 30], thickness=2, border=2, scale=2)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # Orientation
        cv2.rectangle(img, (890, 100), (1180, 160), (0, 0, 255), -2)
        cv2.putText(img, f"Orientation: {orientation}", (900, 140), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)

        # RIGHT LEG
        cv2.putText(img, f"R {int(per_right_leg)}%", (24, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 480), (50, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_leg)), (50, 680), color_right_leg, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_left_leg)}%", (962, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 480), (995, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_leg)), (995, 680), color_left_leg, -1)

    # Counter 
    cv2.rectangle(img, (20, 20), (200, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(count_goblet_squat)}/5", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (210, 20), (390, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(count_goblet_squat)}/5", (220, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)



    #Timer
    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
        display_info = False

    # Repetition
    if count_goblet_squat >= 6:  # Assuming 10 jumping jacks for demonstration
        cvzone.putTextRect(img, 'Exercise Complete', [390, 30], thickness=2, border=2, scale=2.5)
        display_info = False

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()



