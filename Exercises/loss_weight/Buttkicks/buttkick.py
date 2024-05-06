import math
import cv2
import numpy as np
import time
import buttkick_PoseModule as pm
import cvzone


cap = cv2.VideoCapture(r'D:\CPEDES\Flask\Exercises\loss_weight\Buttkicks\buttkicks.mp4')
detector_alternatingleftlunge = pm.poseDetectorButtKick()

count_alternating_right_lunge_buttkick = 0
count_alternating_left_lunge_buttkick = 0

dir_alternating_left_lunge_buttkick = 0
dir_alternating_right_lunge_buttkick = 0


start_time_buttkick = time.time()
repetition_time_buttkick = 60
display_info_buttkick = True

per_left_leg_buttkick = 0
bar_left_leg_buttkick = 0

per_right_leg_buttkick = 0
bar_right_leg_buttkick = 0

leftleg_buttkick= 0
rightleg_buttkick = 0

right_buttkick = 0
left_buttkick = 0


cooldown_duration_buttkick = 5
cooldown_timer_buttkick = 0

color_left_leg_buttkick = (0, 0, 255)
color_right_leg_buttkick = (0, 0, 255)

while True:
    success, img = cap.read()
    img = cv2.resize(img, (1280, 720))

    elapsed_time = time.time() - start_time_buttkick
    remaining_time = max(0, repetition_time_buttkick - elapsed_time)

    if display_info_buttkick:  # Check if to display counter, bar, and percentage
        img = detector_alternatingleftlunge.findPose(img, False)
        lmList_jumping_jacks = detector_alternatingleftlunge.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_jumping_jacks) != 0:

            # Right and Left keypoints
            rightleg_buttkick, orientation = detector_alternatingleftlunge.ButtKick(img, 24, 26, 28, True)
            leftleg_buttkick, orientation2 = detector_alternatingleftlunge.ButtKick(img, 23, 25, 27, True)

            if cooldown_timer_buttkick > 0:
                cooldown_timer_buttkick -= 1

            
           

            #print(orientation, orientation2)
            if orientation == 'right' and orientation2 == 'right':
                    
                    per_right_leg_buttkick = np.interp(rightleg_buttkick, (90, 170), (100, 0))
                    bar_right_leg_buttkick = np.interp(rightleg_buttkick, (90, 170), (480, 680))
                    per_left_leg_buttkick = np.interp(leftleg_buttkick, (90, 170), (100, 0))
                    bar_left_leg_buttkick = np.interp(leftleg_buttkick, (90, 170), (480, 680))

                    if int(per_left_leg_buttkick) == 100:
                        color_left_leg_buttkick = (0, 255, 0)  # Change color of left leg bar to green
                    elif int(per_right_leg_buttkick) == 100:
                        color_right_leg_buttkick = (0, 255, 0)
                    else:
                        color_left_leg_buttkick = (0, 0, 255)  # Keep color of left leg bar as red
                        color_right_leg_buttkick = (0, 0, 255)

                    if rightleg_buttkick <= 90:
                        if dir_alternating_right_lunge_buttkick == 0 and count_alternating_right_lunge_buttkick <= 25:
                            count_alternating_right_lunge_buttkick += 0.5
                            if count_alternating_right_lunge_buttkick == 25:
                                dir_alternating_right_lunge_buttkick = 0
                            else:
                                dir_alternating_right_lunge_buttkick = 1
                                cooldown_timer_buttkick = cooldown_duration_buttkick
                    elif rightleg_buttkick >= 150:
                        if dir_alternating_right_lunge_buttkick == 1 and count_alternating_right_lunge_buttkick <= 25:
                            count_alternating_right_lunge_buttkick += 0.5
                            if count_alternating_right_lunge_buttkick == 25:
                                dir_alternating_right_lunge_buttkick = 1
                            else:
                                dir_alternating_right_lunge_buttkick = 0
                                cooldown_timer_buttkick = cooldown_duration_buttkick
                    
                    if leftleg_buttkick <= 90:
                        if dir_alternating_left_lunge_buttkick == 0 and count_alternating_left_lunge_buttkick <= 25:
                            count_alternating_left_lunge_buttkick += 0.5
                            if count_alternating_left_lunge_buttkick == 25:
                                dir_alternating_left_lunge_buttkick = 0
                            else:
                                dir_alternating_left_lunge_buttkick = 1
                                cooldown_timer_buttkick = cooldown_duration_buttkick
                    elif leftleg_buttkick >= 150:
                        if dir_alternating_left_lunge_buttkick == 1 and count_alternating_left_lunge_buttkick <= 25:
                            count_alternating_left_lunge_buttkick += 0.5
                            if count_alternating_left_lunge_buttkick == 25:
                                dir_alternating_left_lunge_buttkick = 1
                            else:
                                dir_alternating_left_lunge_buttkick = 0
                                cooldown_timer_buttkick = cooldown_duration_buttkick


            elif orientation =='left' and orientation2 == 'left':
                if leftleg_buttkick is not None and rightleg_buttkick is not None:
                    per_right_leg_buttkick = np.interp(rightleg_buttkick, (190, 270), (0, 100))
                    bar_right_leg_buttkick = np.interp(rightleg_buttkick, (190, 270), (680, 480))
                    per_left_leg_buttkick = np.interp(leftleg_buttkick, (190, 270), (0, 100))
                    bar_left_leg_buttkick = np.interp(leftleg_buttkick, (190, 270), (680, 480))

                    #print("R: ", rightleg) #"L: ", leftleg
                    if int(per_left_leg_buttkick) == 100:
                        color_left_leg_buttkick = (0, 255, 0)  # Change color of left leg bar to green
                    elif int(per_right_leg_buttkick) == 100:
                        color_right_leg_buttkick = (0, 255, 0)
                    else:
                        color_left_leg_buttkick = (0, 0, 255)  # Keep color of left leg bar as red
                        color_right_leg_buttkick = (0, 0, 255)
              
                    if rightleg_buttkick >= 270:
                        if dir_alternating_right_lunge_buttkick == 0 and count_alternating_right_lunge_buttkick <= 25:
                            count_alternating_right_lunge_buttkick += 0.5
                            if count_alternating_right_lunge_buttkick == 25:
                                dir_alternating_right_lunge_buttkick = 0
                            else:
                                dir_alternating_right_lunge_buttkick = 1
                                cooldown_timer_buttkick = cooldown_duration_buttkick
                    elif rightleg_buttkick <= 200:
                        if dir_alternating_right_lunge_buttkick == 1 and count_alternating_right_lunge_buttkick <= 25:
                            count_alternating_right_lunge_buttkick += 0.5
                            if count_alternating_right_lunge_buttkick == 25:
                                dir_alternating_right_lunge_buttkick = 1
                            else:
                                dir_alternating_right_lunge_buttkick = 0
                                cooldown_timer_buttkick = cooldown_duration_buttkick

                    if leftleg_buttkick >= 270:
                        
                        if dir_alternating_left_lunge_buttkick == 0 and count_alternating_left_lunge_buttkick <= 25:
                            count_alternating_left_lunge_buttkick += 0.5
                            if count_alternating_left_lunge_buttkick == 25:
                                dir_alternating_left_lunge_buttkick = 0
                            else:
                                dir_alternating_left_lunge_buttkick = 1
                                cooldown_timer_buttkick = cooldown_duration_buttkick
                    elif leftleg_buttkick <= 200:
                        if dir_alternating_left_lunge_buttkick == 1 and count_alternating_left_lunge_buttkick <= 25:
                            count_alternating_left_lunge_buttkick += 0.5
                            if count_alternating_left_lunge_buttkick == 25:
                                dir_alternating_left_lunge_buttkick = 1
                            else:
                                dir_alternating_left_lunge_buttkick = 0
                                cooldown_timer_buttkick = cooldown_duration_buttkick

            elif orientation == 'front' and orientation2 == 'front':
                    
                    per_right_leg_buttkick = np.interp(rightleg_buttkick, (100, 200), (100, 0))
                    bar_right_leg_buttkick = np.interp(rightleg_buttkick, (100, 200), (480, 680))
                    per_left_leg_buttkick = np.interp(leftleg_buttkick, (100, 200), (100, 0))
                    bar_left_leg_buttkick = np.interp(leftleg_buttkick, (100, 200), (480, 680))

                    if int(per_left_leg_buttkick) == 100:
                        color_left_leg_buttkick = (0, 255, 0)  # Change color of left leg bar to green
                    elif int(per_right_leg_buttkick) == 100:
                        color_right_leg_buttkick = (0, 255, 0)
                    else:
                        color_left_leg_buttkick = (0, 0, 255)  # Keep color of left leg bar as red
                        color_right_leg_buttkick = (0, 0, 255)  # Keep color of right leg bar as red

                    if rightleg_buttkick <= 90:
                        if dir_alternating_right_lunge_buttkick == 0 and count_alternating_right_lunge_buttkick <= 25:
                            count_alternating_right_lunge_buttkick += 0.5
                            if count_alternating_right_lunge_buttkick == 25:
                                dir_alternating_right_lunge_buttkick = 0
                            else:
                                dir_alternating_right_lunge_buttkick = 1
                                cooldown_timer_buttkick = cooldown_duration_buttkick
                    else: 
                        if dir_alternating_right_lunge_buttkick == 1 and count_alternating_right_lunge_buttkick <= 25:
                            count_alternating_right_lunge_buttkick += 0.5
                            if count_alternating_right_lunge_buttkick == 25:
                                dir_alternating_right_lunge_buttkick = 1
                            else:
                                dir_alternating_right_lunge_buttkick = 0
                                cooldown_timer_buttkick = cooldown_duration_buttkick

                    if leftleg_buttkick <= 90:
                        if dir_alternating_left_lunge_buttkick == 0 and count_alternating_left_lunge_buttkick <= 25:
                            count_alternating_left_lunge_buttkick += 0.5
                            if count_alternating_left_lunge_buttkick == 25:
                                dir_alternating_left_lunge_buttkick = 0
                            else:
                                dir_alternating_left_lunge_buttkick = 1
                                cooldown_timer_buttkick = cooldown_duration_buttkick
                    else:
                        if dir_alternating_left_lunge_buttkick == 1 and count_alternating_left_lunge_buttkick <= 25:
                            count_alternating_left_lunge_buttkick += 0.5
                            if count_alternating_left_lunge_buttkick == 25:
                                dir_alternating_left_lunge_buttkick = 1
                            else:
                                dir_alternating_left_lunge_buttkick = 0
                                cooldown_timer_buttkick = cooldown_duration_buttkick


        cvzone.putTextRect(img, 'Buttkick Tracker', [470, 30], thickness=2, border=2, scale=2.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)
       
        # Orientation
        cv2.rectangle(img, (890, 100), (1180, 160), (0, 0, 255), -2)
        cv2.putText(img, f"Orientation: {orientation}", (900, 140), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)

        # RIGHT LEG
        cv2.putText(img, f"R {int(per_right_leg_buttkick)}%", (24, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 480), (50, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_leg_buttkick)), (50, 680), color_right_leg_buttkick, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_left_leg_buttkick)}%", (962, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 480), (995, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_leg_buttkick)), (995, 680), color_left_leg_buttkick, -1)

    # Counter 
    cv2.rectangle(img, (20, 20), (200, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(count_alternating_right_lunge_buttkick)}/25", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (210, 20), (390, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(count_alternating_left_lunge_buttkick)}/25", (220, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    # Timer
    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [345, 30], thickness=2, border=2, scale=2.5)
        display_info_buttkick = False

    # Repetition
    if count_alternating_left_lunge_buttkick >= 25:  # Assuming 10 jumping jacks for demonstration
        cvzone.putTextRect(img, 'Exercise Complete', [345, 30], thickness=2, border=2, scale=2.5)
        display_info_buttkick = False

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break


cap.release()

cv2.destroyAllWindows()



