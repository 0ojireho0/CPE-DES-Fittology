import math
import cv2
import numpy as np
import time
import shouldertap_PoseModule as pm
import cvzone
# C:\Users\RID\Desktop\pose_estimation\aipose2\Exercise\weightloss\jumpingjack.mp4

cap = cv2.VideoCapture(0)
detector_ShoulderTap = pm.poseDetectorShoulderTap()

count_shoulder_tap_right = 0
count_shoulder_tap_left = 0
dir_shoulder_tap_right = 0
dir_shoulder_tap_left = 0

start_time_shouldertap = time.time()
repetition_time_shouldertap = 60
display_info_shouldertap = True

per_left_arm_shouldertap = 0
bar_left_arm_shouldertap = 0

per_right_arm_shouldertap = 0
bar_right_arm_shouldertap = 0

color_left_arm_shouldertap = 0
color_right_arm_shouldertap = 0


while True:
    success, img = cap.read()
    img = cv2.resize(img, (1280, 720))

    elapsed_time = time.time() - start_time_shouldertap
    remaining_time = max(0, repetition_time_shouldertap - elapsed_time)

    if display_info_shouldertap:  # Check if to display counter, bar, and percentage
        img = detector_ShoulderTap.findPose(img, False)
        lmList_jumping_jacks = detector_ShoulderTap.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_jumping_jacks) != 0:

            distance1, distance2 = detector_ShoulderTap.ShoulderTap(img, 12, 14, 16, 11, 13, 15, drawpoints=True) 

            #Interpolate angle to percentage and position on screen
            per_right_arm_shouldertap = np.interp(distance1, (180, 350), (100, 0))
            bar_right_arm_shouldertap = np.interp(distance1, (180, 350), (200, 400))

            per_left_arm_shouldertap = np.interp(distance2, (180, 350), (100, 0))
            bar_left_arm_shouldertap = np.interp(distance2, (180, 350), (200, 400))


            if int(per_left_arm_shouldertap) == 100 :
                color_left_arm_shouldertap = (0, 255, 0) 
            elif int(per_right_arm_shouldertap) == 100:
                color_right_arm_shouldertap = (0, 255, 0)
            else:
                color_left_arm_shouldertap = (0, 0, 255)  
                color_right_arm_shouldertap = (0, 0, 255)

            if distance1 <= 180:
                if dir_shoulder_tap_right == 0 and count_shoulder_tap_right < 5:
                    count_shoulder_tap_right += 0.5
                    if count_shoulder_tap_right == 5:
                        dir_shoulder_tap_right = -1
                    else:
                        dir_shoulder_tap_right = 1
            elif distance1 >= 350:
                if dir_shoulder_tap_right == 1 and count_shoulder_tap_right < 5:
                    count_shoulder_tap_right += 0.5
                    if count_shoulder_tap_right == 5:
                        dir_shoulder_tap_right = -1
                    else:
                        dir_shoulder_tap_right = 0

            if distance2 <= 180:
                if dir_shoulder_tap_left == 0 and count_shoulder_tap_left < 5:
                    count_shoulder_tap_left += 0.5
                    if count_shoulder_tap_left == 5:
                        dir_shoulder_tap_left = -1
                    else:
                        dir_shoulder_tap_left = 1
            elif distance2 >= 350:
                if dir_shoulder_tap_left == 1 and count_shoulder_tap_left < 5:
                    count_shoulder_tap_left += 0.5
                    if count_shoulder_tap_left == 5:
                        dir_shoulder_tap_left = -1
                    else:
                        dir_shoulder_tap_left = 0

        cvzone.putTextRect(img, 'Shoulder Tap Tracker', [370, 30], thickness=2, border=2, scale=2.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color


        #Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # ARM RIGHT
        cv2.putText(img, f"R {int(per_right_arm_shouldertap)}%", (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_arm_shouldertap)), (50, 400), color_right_arm_shouldertap, -1)

        # ARM LEFT
        cv2.putText(img, f"L {int(per_left_arm_shouldertap)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_arm_shouldertap)), (995, 400), color_left_arm_shouldertap, -1)

    # Counter 
    cv2.rectangle(img, (20, 20), (150, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(count_shoulder_tap_right)}/5", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (170, 20), (300, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(count_shoulder_tap_left)}/5", (180, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [370, 30], thickness=2, border=2, scale=2.5)
        display_info = False

    if count_shoulder_tap_right >= 5 and count_shoulder_tap_left >= 5:  # Assuming 10 jumping jacks for demonstration
        cvzone.putTextRect(img, 'Exercise Complete', [370, 30], thickness=2, border=2, scale=2.5)
        display_info = False

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()






