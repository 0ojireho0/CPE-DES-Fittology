import math
import cv2
import numpy as np
import time
import PlankToeTaps_PoseModule as pm
import cvzone

cap = cv2.VideoCapture(r'D:\CPEDES\Flask\Exercises\loss_weight\Plank Toe Taps\PlankToeTaps.mp4')
detector_PlankToeTaps = pm.poseDetectorPlankToeTaps()

count_plank_toe_taps_right = 0
count_plank_toe_taps_left = 0


dir_plank_toe_taps_right = 0
dir_plank_toe_taps_left = 0


start_time = time.time()
repetition_time = 60
display_info = True

per_left_leg = 0
bar_left_leg = 0

per_right_leg = 0
bar_right_leg = 0

cooldown_duration = 5
cooldown_timer = 0

color_left_leg = (0, 0, 255)
color_right_leg = (0, 0, 255)


orientation = ''
orientation2 = ''

while True:
    success, img = cap.read()
    img = cv2.resize(img, (1280, 720))

    elapsed_time = time.time() - start_time
    remaining_time = max(0, repetition_time - elapsed_time)

    if display_info:  # Check if to display counter, bar, and percentage
        img = detector_PlankToeTaps.findPose(img, False)
        lmList_jumping_jacks = detector_PlankToeTaps.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_jumping_jacks) != 0:

            # Right and Left keypoints
            distance1, distance2 = detector_PlankToeTaps.PlankToeTaps(img, 16, 14, 12, 24, 26, 28, 32, 15, 13, 11, 23, 25, 27, 31, True)
           
            print("right: ", distance1, "left: ", distance2)

            if cooldown_timer > 0:
                cooldown_timer -= 1

            per_right_leg = np.interp(distance1, (40, 350), (100, 0))
            bar_right_leg = np.interp(distance1, (40, 350), (480, 680))
            per_left_leg = np.interp(distance2, (40, 350), (100, 0))
            bar_left_leg = np.interp(distance2, (40, 350), (480, 680))

            if int(per_left_leg) == 100:
                color_left_leg = (0, 255, 0)  # Change color of left leg bar to green
            elif int(per_right_leg) == 100:
                color_right_leg = (0, 255, 0)
            else:
                color_left_leg = (0, 0, 255)  # Keep color of left leg bar as red
                color_right_leg = (0, 0, 255)

            if distance1 <= 40:
                if dir_plank_toe_taps_right == 0:
                    count_plank_toe_taps_right += 0.5
                    dir_plank_toe_taps_right = 1
                    print("right up: ",count_plank_toe_taps_right)
            elif distance1 >= 300:
                if dir_plank_toe_taps_right == 1:
                    count_plank_toe_taps_right += 0.5
                    dir_plank_toe_taps_right = 0
                    print("right down: ",count_plank_toe_taps_right)
            
            if distance2 <= 40:
                if dir_plank_toe_taps_left == 0:
                    count_plank_toe_taps_left += 0.5
                    dir_plank_toe_taps_left = 1
                    print("left up: ",count_plank_toe_taps_left)
            elif distance2 >= 300:
                if dir_plank_toe_taps_left == 1:
                    count_plank_toe_taps_left += 0.5
                    dir_plank_toe_taps_left = 0
                    print("left down: ",count_plank_toe_taps_left)

        cvzone.putTextRect(img, 'Plank Toe Taps Counter', [390, 30], thickness=2, border=2, scale=2.5)

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
    cv2.rectangle(img, (20, 20), (140, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(count_plank_toe_taps_right)}/6", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (150, 20), (270, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(count_plank_toe_taps_left)}/6", (160, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    # Timer
    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [345, 30], thickness=2, border=2, scale=2.5)
        display_info = False

    # Repetition
    if count_plank_toe_taps_right == 5 and count_plank_toe_taps_left == 5:  # Assuming 10 jumping jacks for demonstration
        cvzone.putTextRect(img, 'Exercise Complete', [345, 30], thickness=2, border=2, scale=2.5)
        display_info = False

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break


cap.release()


cv2.destroyAllWindows()



