import math
import cv2
import numpy as np
import time
import highkneetap_PoseModule as pm
import cvzone

cap = cv2.VideoCapture(r'D:\CPEDES\Flask\Exercises\gaining_muscle\High Knee Tap\highkneetap.mp4')
detector_HighKneeTap = pm.poseDetectorHighKneeTap()

count_high_knee_tap_right = 0
count_high_knee_tap_left = 0

dir_high_knee_tap_right = 0

dir_high_knee_tap_left = 0


start_time_hkt = time.time()
repetition_time_hkt = 60
display_info_hkt = True

leftbody_hkt = 0
rightbody_hkt = 0

per_left_body_hkt = 0
bar_left_body_hkt = 0

per_right_body_hkt = 0
bar_right_body_hkt = 0

cooldown_duration_hkt = 5
cooldown_timer_hkt = 0

color_left_leg_hkt = (0, 0, 255)
color_right_leg_hkt = (0, 0, 255)


while True:
    success, img = cap.read()
    img = cv2.resize(img, (1280, 720))

    elapsed_time = time.time() - start_time_hkt
    remaining_time = max(0, repetition_time_hkt - elapsed_time)

    if display_info_hkt:  # Check if to display counter, bar, and percentage
        img = detector_HighKneeTap.findPose(img, False)
        lmList_jumping_jacks = detector_HighKneeTap.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_jumping_jacks) != 0:

            # Right and Left keypoints
            rightleg_hkt, orientation = detector_HighKneeTap.HighKneeTap(img, 24, 26, 28, True)
            leftleg_hkt, orientation2 = detector_HighKneeTap.HighKneeTap(img, 23, 25, 27, True)

            if cooldown_timer_hkt > 0:
                cooldown_timer_hkt -= 1

            if orientation == 'right' and orientation2 == 'right':
                    per_right_leg_hkt = np.interp(rightleg_hkt, (70, 170), (100, 0))
                    bar_right_leg_hkt = np.interp(rightleg_hkt, (70, 170), (480, 680))
                    per_left_leg_hkt = np.interp(leftleg_hkt, (70, 170), (100, 0))
                    bar_left_leg_hkt = np.interp(leftleg_hkt, (70, 170), (480, 680))

                    if int(per_left_leg_hkt) == 100 :
                        color_left_leg_hkt = (0, 255, 0) 
                    elif int(per_right_leg_hkt) == 100:
                        color_right_leg_hkt = (0, 255, 0)
                    else:
                        color_left_leg_hkt = (0, 0, 255)  
                        color_right_leg_hkt = (0, 0, 255)
                    
                    if 50 <= rightleg_hkt <= 60:
                        if dir_high_knee_tap_right == 0:
                            count_high_knee_tap_right += 1
                            dir_high_knee_tap_right = 1
                            cooldown_timer_hkt = cooldown_duration_hkt
                            print("Up Right: ",count_high_knee_tap_right)
                    elif rightleg_hkt >= 155: 
                        if dir_high_knee_tap_right == 1:
                            dir_high_knee_tap_right = 0

                    if 50 <= leftleg_hkt <= 60:
                        if dir_high_knee_tap_left == 0:
                            count_high_knee_tap_left += 1
                            dir_high_knee_tap_left = 1
                            cooldown_timer_hkt = cooldown_duration_hkt
                            print("Up Left: ",count_high_knee_tap_left)

                    elif leftleg_hkt >= 155:
                        if dir_high_knee_tap_left == 1:
                            dir_high_knee_tap_left = 0

            elif orientation =='left' and orientation2 == 'left':
                    per_right_leg_hkt = np.interp(rightleg_hkt, (210, 300), (0, 100))
                    bar_right_leg_hkt = np.interp(rightleg_hkt, (210, 300), (680, 480))
                    per_left_leg_hkt = np.interp(leftleg_hkt, (210, 300), (0, 100))
                    bar_left_leg_hkt = np.interp(leftleg_hkt, (210, 300), (680, 480))

                    if int(per_left_leg_hkt) == 100 :
                        color_left_leg_hkt = (0, 255, 0) 
                    elif int(per_right_leg_hkt) == 100:
                        color_right_leg_hkt = (0, 255, 0)
                    else:
                        color_left_leg_hkt = (0, 0, 255)  
                        color_right_leg_hkt = (0, 0, 255)

                    if rightleg_hkt >= 295:
                        if dir_high_knee_tap_right == 0:
                            count_high_knee_tap_right += 1
                            dir_high_knee_tap_right = 1
                            cooldown_timer_hkt = cooldown_duration_hkt
                    elif rightleg_hkt <= 210: 
                        if dir_high_knee_tap_right == 1:
                            dir_high_knee_tap_right = 0

                    if leftleg_hkt >= 300:
                        if dir_high_knee_tap_left == 0:
                            count_high_knee_tap_left += 1
                            dir_high_knee_tap_left = 1
                            cooldown_timer_hkt = cooldown_duration_hkt
                    elif leftleg_hkt <= 210:
                        if dir_high_knee_tap_left == 1:
                            dir_high_knee_tap_left = 0

            elif orientation == 'front' and orientation2 == 'front':
                    per_right_leg_hkt = np.interp(rightleg_hkt, (150, 240), (100, 0))
                    bar_right_leg_hkt = np.interp(rightleg_hkt, (150, 240), (480, 680))
                    per_left_leg_hkt = np.interp(leftleg_hkt, (150, 240), (100, 0))
                    bar_left_leg_hkt = np.interp(leftleg_hkt, (150, 240), (480, 680))
                    
                    if int(per_left_leg_hkt) == 100 :
                        color_left_leg_hkt = (0, 255, 0) 
                    elif int(per_right_leg_hkt) == 100:
                        color_right_leg_hkt = (0, 255, 0)
                    else:
                        color_left_leg_hkt = (0, 0, 255)  
                        color_right_leg_hkt = (0, 0, 255)

                    if rightleg_hkt <= 150:
                        if dir_high_knee_tap_right == 0:
                            count_high_knee_tap_right += 1
                            dir_high_knee_tap_right = 1
                            cooldown_timer_hkt = cooldown_duration_hkt
                    elif rightleg_hkt >= 240: 
                        if dir_high_knee_tap_right == 1:
                            dir_high_knee_tap_right = 0

                    if leftleg_hkt <= 150:
                        if dir_high_knee_tap_left == 0:
                            count_high_knee_tap_left += 1
                            dir_high_knee_tap_left = 1
                            cooldown_timer_hkt = cooldown_duration_hkt
                    elif leftleg_hkt >= 240:
                        if dir_high_knee_tap_left == 1:
                            dir_high_knee_tap_left = 0


        

        cvzone.putTextRect(img, 'High Knee Tap Tracker', [450, 30], thickness=2, border=2, scale=2)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # Orientation
        cv2.rectangle(img, (890, 100), (1180, 160), (0, 0, 255), -2)
        cv2.putText(img, f"Orientation: {orientation}", (900, 140), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)

        # RIGHT LEG
        cv2.putText(img, f"R {int(per_right_leg_hkt)}%", (24, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 480), (50, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_leg_hkt)), (50, 680), color_right_leg_hkt, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_left_leg_hkt)}%", (962, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 480), (995, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_leg_hkt)), (995, 680), color_left_leg_hkt, -1)
    
    # Counter 
    cv2.rectangle(img, (20, 20), (200, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(count_high_knee_tap_right)}/5", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (210, 20), (390, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(count_high_knee_tap_left)}/5", (220, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    #Timer
    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
        display_info_hkt = False

    # Repetition
    if count_high_knee_tap_right >= 5 and count_high_knee_tap_left >= 5:  # Changeable
        cvzone.putTextRect(img, 'Exercise Complete', [390, 30], thickness=2, border=2, scale=2.5)
        display_info_hkt = False

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()



