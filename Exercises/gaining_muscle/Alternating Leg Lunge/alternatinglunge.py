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

pTime = 0
start_time = time.time()
repetition_time = 999
display_info = True

per_left_leg = 0
bar_left_leg = 0

per_right_leg = 0
bar_right_leg = 0

leftleg= 0
rightleg = 0

right = 0
left = 0

done = 0

perform_interpolation = True

cooldown_duration = 5
cooldown_timer = 0

color_right_leg = (0, 0, 255)
color_left_leg = (0, 0, 255)

while True:
    success, img = cap.read()
    img = cv2.resize(img, (1280, 720))

    elapsed_time = time.time() - start_time
    remaining_time = max(0, repetition_time - elapsed_time)

    if display_info:  # Check if to display counter, bar, and percentage
        img = detector_alternatingleftlunge.findPose(img, False)
        lmList_jumping_jacks = detector_alternatingleftlunge.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_jumping_jacks) != 0:

            # Right and Left keypoints
            rightleg, orientation = detector_alternatingleftlunge.AlternatingLunge(img, 24, 26, 28, True)
            leftleg, orientation2 = detector_alternatingleftlunge.AlternatingLunge(img, 23, 25, 27, True)

            if cooldown_timer > 0:
                cooldown_timer -= 1

            #print(orientation, orientation2)
            if orientation == 'right' and orientation2 == 'right':
                    per_right_leg = np.interp(rightleg, (90, 170), (100, 0))
                    bar_right_leg = np.interp(rightleg, (90, 170), (480, 680))
                    per_left_leg = np.interp(leftleg, (90, 170), (100, 0))
                    bar_left_leg = np.interp(leftleg, (90, 170), (480, 680))

                    if int(per_left_leg) == 100:
                        color_left_leg = (0, 255, 0)  # Change color of left leg bar to green
                    elif int(per_right_leg) == 100:
                        color_right_leg = (0, 255, 0)
                    else:
                        color_left_leg = (0, 0, 255)  # Keep color of left leg bar as red
                        color_right_leg = (0, 0, 255)

                    if rightleg <= 80:
                        if dir_alternating_right_lunge == 0:
                            count_alternating_right_lunge += 0.5
                            dir_alternating_right_lunge = 1
                            cooldown_timer = cooldown_duration
                            print("count right: ",count_alternating_right_lunge)
                    elif rightleg >= 150:
                        if dir_alternating_right_lunge == 1:
                            count_alternating_right_lunge += 0.5
                            dir_alternating_right_lunge = 0
                            cooldown_timer = cooldown_duration
                            print("count right: ",count_alternating_right_lunge)
                    
                    if leftleg <= 80:
                        if dir_alternating_left_lunge == 0:
                            count_alternating_left_lunge += 0.5
                            dir_alternating_left_lunge = 1
                            cooldown_timer = cooldown_duration
                            print("count left: ", count_alternating_left_lunge)
                    elif leftleg >= 150:
                        if dir_alternating_left_lunge == 1:
                            count_alternating_left_lunge += 0.5
                            dir_alternating_left_lunge = 0
                            cooldown_timer = cooldown_duration
                            print("count left: ", count_alternating_left_lunge)

            elif orientation =='left' and orientation2 == 'left':
                if leftleg is not None and rightleg is not None:
                    per_right_leg = np.interp(rightleg, (190, 280), (0, 100))
                    bar_right_leg = np.interp(rightleg, (190, 280), (680, 480))
                    per_left_leg = np.interp(leftleg, (190, 280), (0, 100))
                    bar_left_leg = np.interp(leftleg, (190, 280), (680, 480))

                    if int(per_left_leg) == 100:
                        color_left_leg = (0, 255, 0)  # Change color of left leg bar to green
                    elif int(per_right_leg) == 100:
                        color_right_leg = (0, 255, 0)
                    else:
                        color_left_leg = (0, 0, 255)  # Keep color of left leg bar as red
                        color_right_leg = (0, 0, 255)

                    if rightleg > 280:
                        if dir_alternating_right_lunge == 0:
                            count_alternating_right_lunge += 0.5
                            dir_alternating_right_lunge = 1
                            cooldown_timer = cooldown_duration
                    elif rightleg < 179:
                        if dir_alternating_right_lunge == 1:
                            count_alternating_right_lunge += 0.5
                            dir_alternating_right_lunge = 0
                            cooldown_timer = cooldown_duration
                    if leftleg > 280:
                        if dir_alternating_left_lunge == 0:
                            count_alternating_left_lunge += 0.5
                            dir_alternating_left_lunge = 1
                            cooldown_timer = cooldown_duration
                    elif leftleg < 179:
                        if dir_alternating_left_lunge == 1:
                            count_alternating_left_lunge += 0.5
                            dir_alternating_left_lunge = 0
                            cooldown_timer = cooldown_duration

            elif orientation == 'front facing' and orientation2 == 'front facing':
                    
                    per_right_leg = np.interp(rightleg, (100, 200), (100, 0))
                    bar_right_leg = np.interp(rightleg, (100, 200), (480, 680))
                    per_left_leg = np.interp(leftleg, (100, 200), (100, 0))
                    bar_left_leg = np.interp(leftleg, (100, 200), (480, 680))


                    if int(per_left_leg) == 100:
                        color_left_leg = (0, 255, 0)  # Change color of left leg bar to green
                    elif int(per_right_leg) == 100:
                        color_right_leg = (0, 255, 0)
                    else:
                        color_left_leg = (0, 0, 255)  # Keep color of left leg bar as red
                        color_right_leg = (0, 0, 255)

                    if rightleg <= 150 and leftleg <= 100:
                        if dir_alternating_right_lunge == 0:
                            count_alternating_right_lunge += 0.5
                            dir_alternating_right_lunge = 1
                            cooldown_timer = cooldown_duration
                    else: 
                        if dir_alternating_right_lunge == 1:
                            count_alternating_right_lunge += 0.5
                            dir_alternating_right_lunge = 0
                            cooldown_timer = cooldown_duration

                    if rightleg <= 100 and leftleg <= 150:
                        if dir_alternating_left_lunge == 0:
                            count_alternating_left_lunge += 0.5
                            dir_alternating_left_lunge = 1
                            cooldown_timer = cooldown_duration
                    else:
                        if dir_alternating_left_lunge == 1:
                            count_alternating_left_lunge += 0.5
                            dir_alternating_left_lunge = 0
                            cooldown_timer = cooldown_duration

        #Delay Timer for Pose Estimation
        fps = cap.get(cv2.CAP_PROP_FPS)
        if cooldown_timer > 0:
            cooldown_timer -= 1 / fps

        cvzone.putTextRect(img, 'Leg Lunge (alternate)', [345, 30], thickness=2, border=2, scale=2.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # RIGHT LEG
        cv2.putText(img, f"R {int(per_right_leg)}%", (24, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 480), (50, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_leg)), (50, 680), color_right_leg, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_left_leg)}%", (962, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 480), (995, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_leg)), (995, 680), color_left_leg, -1)

    # Counter 
    cv2.rectangle(img, (20, 20), (140, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(count_alternating_right_lunge)}/5", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 0, 0), 7)

    cv2.rectangle(img, (150, 20), (270, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(count_alternating_left_lunge)}/5", (160, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (0, 0, 255), 7)

    # Timer
    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [345, 30], thickness=2, border=2, scale=2.5)
        display_info = False

    # Repetition
    if count_alternating_left_lunge >= 5:  # Assuming 10 jumping jacks for demonstration
        cvzone.putTextRect(img, 'Exercise Complete', [345, 30], thickness=2, border=2, scale=2.5)
        display_info = False

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()



