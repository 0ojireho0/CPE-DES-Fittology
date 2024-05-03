import math
import cv2
import numpy as np
import time
import alternatinglunge_PoseModule as pm
import cvzone


cap = cv2.VideoCapture(r'D:\CPEDES\Flask\Exercises\gaining_muscle\Alternating Leg Lunge\alternatinglungecomplete.mp4')
detector_alternatingleftlunge = pm.poseDetectoralternatinglunge()

count_alternating_right_lunge = 0
count_alternating_left_lunge = 0

dir_alternating_left_lunge = 0
dir_alternating_right_lunge = 0


start_time_alternatinglunge = time.time()
repetition_time_alternatinglunge = 60
display_info_alternatinglunge = True

per_left_leg_alternatinglunge = 0
bar_left_leg_alternatinglunge = 0

per_right_leg_alternatinglunge = 0
bar_right_leg_alternatinglunge = 0

leftleg_alternatinglunge  = 0
rightleg_alternatinglunge = 0


cooldown_duration_alternatinglunge = 5
cooldown_timer_alternatinglunge = 0

color_right_leg_alternatinglunge = (0, 0, 255)
color_left_leg_alternatinglunge = (0, 0, 255)

while True:
    success, img = cap.read()

    img = cv2.resize(img, (1280, 720))

    elapsed_time = time.time() - start_time_alternatinglunge
    remaining_time = max(0, repetition_time_alternatinglunge - elapsed_time)

    if display_info_alternatinglunge:  # Check if to display counter, bar, and percentage
        img = detector_alternatingleftlunge.findPose(img, False)
        lmList_jumping_jacks = detector_alternatingleftlunge.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_jumping_jacks) != 0:

            # Right and Left keypoints
            rightleg_alternatinglunge, orientation = detector_alternatingleftlunge.AlternatingLunge(img, 24, 26, 28, True)
            leftleg_alternatinglunge, orientation2 = detector_alternatingleftlunge.AlternatingLunge(img, 23, 25, 27, True)

            if cooldown_timer_alternatinglunge > 0:
                cooldown_timer_alternatinglunge -= 1

            #print(orientation, orientation2)
            if orientation == 'right' and orientation2 == 'right':
                    per_right_leg_alternatinglunge = np.interp(rightleg_alternatinglunge, (90, 170), (100, 0))
                    bar_right_leg_alternatinglunge = np.interp(rightleg_alternatinglunge, (90, 170), (480, 680))
                    per_left_leg_alternatinglunge = np.interp(leftleg_alternatinglunge, (90, 170), (100, 0))
                    bar_left_leg_alternatinglunge = np.interp(leftleg_alternatinglunge, (90, 170), (480, 680))

                    if int(per_left_leg_alternatinglunge) == 100:
                        color_left_leg_alternatinglunge = (0, 255, 0)  # Change color of left leg bar to green
                    elif int(per_right_leg_alternatinglunge) == 100:
                        color_right_leg_alternatinglunge = (0, 255, 0)
                    else:
                        color_left_leg_alternatinglunge = (0, 0, 255)  # Keep color of left leg bar as red
                        color_right_leg_alternatinglunge = (0, 0, 255)

                    if rightleg_alternatinglunge <= 80:
                        if dir_alternating_right_lunge == 0:
                            count_alternating_right_lunge += 0.5
                            dir_alternating_right_lunge = 1
                            cooldown_timer_alternatinglunge = cooldown_duration_alternatinglunge
                    elif rightleg_alternatinglunge >= 150:
                        if dir_alternating_right_lunge == 1:
                            count_alternating_right_lunge += 0.5
                            dir_alternating_right_lunge = 0
                            cooldown_timer_alternatinglunge = cooldown_duration_alternatinglunge
                    
                    if leftleg_alternatinglunge <= 80:
                        if dir_alternating_left_lunge == 0:
                            count_alternating_left_lunge += 0.5
                            dir_alternating_left_lunge = 1
                            cooldown_timer_alternatinglunge = cooldown_duration_alternatinglunge
                    elif leftleg_alternatinglunge >= 150:
                        if dir_alternating_left_lunge == 1:
                            count_alternating_left_lunge += 0.5
                            dir_alternating_left_lunge = 0
                            cooldown_timer_alternatinglunge = cooldown_duration_alternatinglunge

            elif orientation =='left' and orientation2 == 'left':
                if leftleg_alternatinglunge is not None and rightleg_alternatinglunge is not None:
                    per_right_leg_alternatinglunge = np.interp(rightleg_alternatinglunge, (190, 280), (0, 100))
                    bar_right_leg_alternatinglunge = np.interp(rightleg_alternatinglunge, (190, 280), (680, 480))
                    per_left_leg_alternatinglunge = np.interp(leftleg_alternatinglunge, (190, 280), (0, 100))
                    bar_left_leg_alternatinglunge = np.interp(leftleg_alternatinglunge, (190, 280), (680, 480))

                    if int(per_left_leg_alternatinglunge) == 100:
                        color_left_leg_alternatinglunge = (0, 255, 0)  # Change color of left leg bar to green
                    elif int(per_right_leg_alternatinglunge) == 100:
                        color_right_leg_alternatinglunge = (0, 255, 0)
                    else:
                        color_left_leg_alternatinglunge = (0, 0, 255)  # Keep color of left leg bar as red
                        color_right_leg_alternatinglunge = (0, 0, 255)

                    if rightleg_alternatinglunge > 280:
                        if dir_alternating_right_lunge == 0:
                            count_alternating_right_lunge += 0.5
                            dir_alternating_right_lunge = 1
                            cooldown_timer_alternatinglunge = cooldown_duration_alternatinglunge
                    elif rightleg_alternatinglunge < 179:
                        if dir_alternating_right_lunge == 1:
                            count_alternating_right_lunge += 0.5
                            dir_alternating_right_lunge = 0
                            cooldown_timer_alternatinglunge = cooldown_duration_alternatinglunge
                    if leftleg_alternatinglunge > 280:
                        if dir_alternating_left_lunge == 0:
                            count_alternating_left_lunge += 0.5
                            dir_alternating_left_lunge = 1
                            cooldown_timer_alternatinglunge = cooldown_duration_alternatinglunge
                    elif leftleg_alternatinglunge < 179:
                        if dir_alternating_left_lunge == 1:
                            count_alternating_left_lunge += 0.5
                            dir_alternating_left_lunge = 0
                            cooldown_timer_alternatinglunge = cooldown_duration_alternatinglunge

            elif orientation == 'front' and orientation2 == 'front':
                    
                    per_right_leg_alternatinglunge = np.interp(rightleg_alternatinglunge, (100, 200), (100, 0))
                    bar_right_leg_alternatinglunge = np.interp(rightleg_alternatinglunge, (100, 200), (480, 680))
                    per_left_leg_alternatinglunge = np.interp(leftleg_alternatinglunge, (100, 200), (100, 0))
                    bar_left_leg_alternatinglunge = np.interp(leftleg_alternatinglunge, (100, 200), (480, 680))


                    if int(per_left_leg_alternatinglunge) == 100:
                        color_left_leg_alternatinglunge = (0, 255, 0)  # Change color of left leg bar to green
                    elif int(per_right_leg_alternatinglunge) == 100:
                        color_right_leg_alternatinglunge = (0, 255, 0)
                    else:
                        color_left_leg_alternatinglunge = (0, 0, 255)  # Keep color of left leg bar as red
                        color_right_leg_alternatinglunge = (0, 0, 255)

                    if rightleg_alternatinglunge <= 150 and leftleg_alternatinglunge <= 100:
                        if dir_alternating_right_lunge == 0:
                            count_alternating_right_lunge += 0.5
                            dir_alternating_right_lunge = 1
                            cooldown_timer_alternatinglunge = cooldown_duration_alternatinglunge
                    else: 
                        if dir_alternating_right_lunge == 1:
                            count_alternating_right_lunge += 0.5
                            dir_alternating_right_lunge = 0
                            cooldown_timer_alternatinglunge = cooldown_duration_alternatinglunge

                    if rightleg_alternatinglunge <= 100 and leftleg_alternatinglunge <= 150:
                        if dir_alternating_left_lunge == 0:
                            count_alternating_left_lunge += 0.5
                            dir_alternating_left_lunge = 1
                            cooldown_timer_alternatinglunge = cooldown_duration_alternatinglunge
                    else:
                        if dir_alternating_left_lunge == 1:
                            count_alternating_left_lunge += 0.5
                            dir_alternating_left_lunge = 0
                            cooldown_timer_alternatinglunge = cooldown_duration_alternatinglunge

  
        cvzone.putTextRect(img, 'Leg Lunge (alternate)', [345, 30], thickness=2, border=2, scale=2.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # Orientation
        cv2.rectangle(img, (890, 100), (1180, 160), (0, 0, 255), -2)
        cv2.putText(img, f"Orientation: {orientation}", (900, 140), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)

        # RIGHT LEG
        cv2.putText(img, f"R {int(per_right_leg_alternatinglunge)}%", (24, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 480), (50, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_leg_alternatinglunge)), (50, 680), color_right_leg_alternatinglunge, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_left_leg_alternatinglunge)}%", (962, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 480), (995, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_leg_alternatinglunge)), (995, 680), color_left_leg_alternatinglunge, -1)

    # Counter 
    cv2.rectangle(img, (20, 20), (140, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(count_alternating_right_lunge)}/5", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (150, 20), (270, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(count_alternating_left_lunge)}/5", (160, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    # Timer
    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
        display_info_alternatinglunge = False

    # Repetition
    if count_alternating_left_lunge >= 5:  # Assuming 10 jumping jacks for demonstration
        cvzone.putTextRect(img, 'Exercise Complete', [390, 30], thickness=2, border=2, scale=2.5)
        display_info_alternatinglunge = False

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()



