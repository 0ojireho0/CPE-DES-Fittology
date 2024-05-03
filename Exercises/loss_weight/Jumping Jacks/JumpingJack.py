import math
import cv2
import numpy as np
import time
import JumpingJack_PoseModule as pm
import cvzone
# C:\Users\RID\Desktop\pose_estimation\aipose2\Exercise\weightloss\jumpingjack.mp4

cap = cv2.VideoCapture(r'C:\Users\RID\Desktop\pose_estimation\aipose2\Exercise\weightloss\jumpingjacksvid.mp4')
detector_JumpingJack = pm.poseDetectorJumpingJack()

count_jumping_jacks = 0
dir_jumping_jacks = 0

pTime = 0
start_time = time.time()
repetition_time = 60
display_info = True

per_left_arm = 0
bar_left_arm = 0

per_right_arm = 0
bar_right_arm = 0

per_down_left = 0
per_down_right = 0

bar_down_left = 0
bar_down_right = 0

leftwholearm = 0
rightwholearm = 0
distance = 0


done = 0

while True:
    success, img = cap.read()
    img = cv2.resize(img, (1280, 720))

    elapsed_time = time.time() - start_time
    remaining_time = max(0, repetition_time - elapsed_time)

    if display_info:  # Check if to display counter, bar, and percentage
        img = detector_JumpingJack.findPose(img, False)
        lmList_jumping_jacks = detector_JumpingJack.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_jumping_jacks) != 0:

            leftwholearm, rightwholearm, = detector_JumpingJack.UpperBodySwing(
                img, 23, 11, 13, 14, 12, 24, 15, 16, drawpoints= True)
            distance = detector_JumpingJack.findJumpingJack(img, 24, 26, 28, 23, 25, 27, drawpoints=True)  # Define landmark keypoints

            #Interpolate angle to percentage and position on screen
            per_left_arm = np.interp(leftwholearm, (200, 270), (100, 0))
            bar_left_arm = np.interp(leftwholearm, (210, 280), (200, 400))

            per_right_arm = np.interp(rightwholearm, (200, 270), (100, 0))
            bar_right_arm = np.interp(rightwholearm, (210, 280), (200, 400))


            per_down_left = np.interp(distance, (35, 180), (0, 100))
            bar_down_left = np.interp(distance, (35, 190), (680, 480))

            per_down_right= np.interp(distance, (35, 180), (0, 100))
            bar_down_right= np.interp(distance, (35, 190), (680, 480))


            if leftwholearm <= 220 and rightwholearm  <= 220 and distance >= 180:
                if dir_jumping_jacks == 0:
                    count_jumping_jacks += 0.5
                    dir_jumping_jacks = 1 
                    
            elif leftwholearm >= 270 and rightwholearm >= 270 and distance <= 35:
                if dir_jumping_jacks == 1:
                    count_jumping_jacks += 0.5
                    dir_jumping_jacks = 0  



        cvzone.putTextRect(img, 'Ai Jumping Jack Tracker', [345, 30], thickness=2, border=2, scale=2.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color


        #Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # ARM RIGHT
        cv2.putText(img, f"R {int(per_right_arm)}%", (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_arm)), (50, 400), (0, 0, 255), -1)

        # ARM LEFT
        cv2.putText(img, f"L {int(per_left_arm)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_arm)), (995, 400), (0, 0, 255), -1)

        # RIGHT LEG
        cv2.putText(img, f"R {int(per_down_right)}%", (24, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 480), (50, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_down_right)), (50, 680), (0, 0, 255), -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_down_left)}%", (962, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 480), (995, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_down_left)), (995, 680), (0, 0, 255), -1)

        if leftwholearm <= 210:
            cv2.rectangle(img, (952, int(bar_left_arm)), (995, 400), (0, 255, 0), -1)

        if rightwholearm <= 210:
            cv2.rectangle(img, (8, int(bar_right_arm)), (50, 400), (0, 255, 0), -1)

        if distance >= 180:
            cv2.rectangle(img, (952, int(bar_down_left)), (995, 680), (0, 255, 0), -1)
        
        if distance >= 180:
            cv2.rectangle(img, (8, int(bar_down_right)), (50, 680), (0, 255, 0), -1)

    cv2.rectangle(img, (20, 10), (140, 120), (255, 0, 0), -1)
    cv2.putText(img, f"{int(count_jumping_jacks)}/5", (30, 80), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [370, 30], thickness=2, border=2, scale=2.5)
        display_info = False

    if count_jumping_jacks >= 5:  # Assuming 10 jumping jacks for demonstration
        cvzone.putTextRect(img, 'Exercise Complete', [370, 30], thickness=2, border=2, scale=2.5)
        display_info = False

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()






