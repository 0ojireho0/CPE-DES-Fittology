import math
import cv2
import numpy as np
import time
import jogginginplace_PoseModule as pm
import cvzone


cap = cv2.VideoCapture(r'C:\Users\RID\Desktop\pose_estimation\aipose2\Exercise\weightloss\Workout Guide - Jog in Place.mp4')
detector = pm.PoseDetector()

left_foot_lift_off_count = 0
right_foot_lift_off_count = 0
counter_left = 0
counter_right = 0

per_down_right = 0
bar_down_right = 0

per_down_left = 0
bar_down_left = 0


dir_left = 0
dir_right = 0

start_time = time.time()
repetition_time = 60
display_info = True

color_leg = (0, 0, 255)

while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.resize(img, (1280, 720))
    elapsed_time = time.time() - start_time
    remaining_time = max(0, repetition_time - elapsed_time)

    if display_info:
        img = detector.find_Pose(img, False)
        pose_landmarks = detector.get_pose_landmarks()
        drawings = detector.pose_landmarks_drawings(img, pose_landmarks,  32, 28, 30, 26, 24, True)
        drawings2 = detector.pose_landmarks_drawings(img, pose_landmarks, 31, 27, 29, 25, 23, True)

        if pose_landmarks:
            left_foot_lift_off_count, right_foot_lift_off_count = detector.detect_feet_lift_off(pose_landmarks, threshold=0.80)

            per_down_left = np.interp(left_foot_lift_off_count, (0, 1), (100, 0))
            bar_down_left = np.interp(left_foot_lift_off_count, (0, 1), (480, 680))

            per_down_right= np.interp(right_foot_lift_off_count, (0, 1), (100, 0))
            bar_down_right= np.interp(right_foot_lift_off_count, (0, 1), (480, 680))


            if per_down_left == 100 or per_down_right == 100:
                color_leg = (0, 255, 0)
     
            if left_foot_lift_off_count == 1:
                if dir_left == 0:
                    counter_left += 1
                    dir_left = 1
            else: 
                if dir_left == 1:
                    dir_left = 0

            if right_foot_lift_off_count == 1:
                if dir_right == 0:
                    counter_right += 1
                    dir_right = 1
            else: 
                if dir_right == 1:
                    dir_right = 0

        # label
        cvzone.putTextRect(img, 'Jogging in Place Tracker', [450, 30], thickness=2, border=2, scale=2) 

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # RIGHT LEG
        cv2.putText(img, f"R {int(per_down_right)}%", (24, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 480), (50, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_down_right)), (50, 680), color_leg, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_down_left)}%", (962, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 480), (995, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_down_left)), (995, 680), color_leg, -1)

    # Counter for the right foot
    cv2.rectangle(img, (20, 20), (200, 130), (0, 0, 255), -1)  # Adjusted rectangle shape
    cv2.putText(img, f"{int(counter_right)}/60", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    # Counter for the left foot
    cv2.rectangle(img, (210, 20), (390, 130), (255, 0, 0), -1)  # Adjusted rectangle shape and coordinates
    cv2.putText(img, f"{int(counter_left)}/60", (220, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [345, 30], thickness=2, border=2, scale=2.5)
        display_info = False

    if counter_right == 60 and counter_left == 60:
        cvzone.putTextRect(img, 'All Repetitions Completed', [345, 30], thickness=2, border=2, scale=2.5)
        display_info = False

    cv2.imshow("Image", img)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


