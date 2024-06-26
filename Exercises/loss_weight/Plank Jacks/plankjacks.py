import math
import cv2
import numpy as np
import time
import plankjacks_PoseModule as pm
import cvzone


cap = cv2.VideoCapture(r'D:\CPEDES\Flask\Exercises\loss_weight\Plank Jacks\plankjacks.mp4')
detector_PlankJacks = pm.poseDetectorPlankJacks()

count_Plank_Jacks = 0
dir_Plank_Jacks = 0

start_time_plankjacks = time.time()
repetition_time_plankjacks = 60
display_info_plankjacks = True

per_right_leg_plankjacks = 0
bar_left_leg_plankjacks = 0


cooldown_duration_plankjacks = 5
cooldown_timer_plankjacks = 0

color_left_leg_plankjacks = (0, 0, 255)
color_right_leg_plankjacks = (0, 0, 255)

while True:
    success, img = cap.read()
    img = cv2.resize(img, (1280, 720))

    elapsed_time = time.time() - start_time_plankjacks
    remaining_time = max(0, repetition_time_plankjacks - elapsed_time)

    if display_info_plankjacks:  # Check if to display counter, bar, and percentage
        img = detector_PlankJacks.findPose(img, False)
        lmList_jumping_jacks = detector_PlankJacks.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_jumping_jacks) != 0:

            measure = detector_PlankJacks.Plankjack(img, 28, 26, 24, 23, 25, 27, True)

            if cooldown_timer_plankjacks > 0:
                cooldown_timer_plankjacks -= 1

            per_left_leg_plankjacks = np.interp(measure, (40, 170), (0, 100))
            bar_left_leg_plankjacks = np.interp(measure, (40, 170), (680, 480))

            per_right_leg_plankjacks = np.interp(measure, (40, 170), (0, 100))
            bar_right_leg_plankjacks = np.interp(measure, (40, 170), (680, 480))

            if per_left_leg_plankjacks == 100 and per_right_leg_plankjacks == 100:
                color_left_leg_plankjacks = (0, 255, 0)
                color_right_leg_plankjacks = (0, 255, 0) 
            else:
                color_left_leg_plankjacks = (0, 0, 255)  
                color_right_leg_plankjacks = (0, 0, 255)

            if measure >= 170:
                if dir_Plank_Jacks == 0:
                    count_Plank_Jacks += 0.5
                    dir_Plank_Jacks = 1
            elif measure <= 80:
                if dir_Plank_Jacks == 1:
                    count_Plank_Jacks += 0.5
                    dir_Plank_Jacks = 0

        #Delay Timer for Pose Estimation

        cvzone.putTextRect(img, 'Plank Jacks', [345, 30], thickness=2, border=2, scale=2.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # RIGHT LEG
        cv2.putText(img, f"R {int(per_right_leg_plankjacks)}%", (24, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 480), (50, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_leg_plankjacks)), (50, 680), color_right_leg_plankjacks, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_left_leg_plankjacks)}%", (962, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 480), (995, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_leg_plankjacks)), (995, 680), color_left_leg_plankjacks, -1)

    # Counter 
    cv2.rectangle(img, (20, 20), (170, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(count_Plank_Jacks)}/5", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    # Timer
    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [345, 30], thickness=2, border=2, scale=2.5)
        display_info_plankjacks = False

    # Repetition
    if count_Plank_Jacks >= 5:  # Assuming 10 jumping jacks for demonstration
        cvzone.putTextRect(img, 'Exercise Complete', [345, 30], thickness=2, border=2, scale=2.5)
        display_info_plankjacks = False

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break


cap.release()

cv2.destroyAllWindows()



