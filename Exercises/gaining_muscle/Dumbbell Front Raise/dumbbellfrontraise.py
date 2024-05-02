# import libraries
import math
import cv2
import numpy as np
import time
import dumbbellfrontraise_PoseModule as pm  # Assuming you have a pose module named 'dumbbellfrontraise_PoseModule.py'
import cvzone

# Camera
cap = cv2.VideoCapture(r'D:\CPEDES\Flask\Exercises\gaining_muscle\Dumbbell Front Raise\dumbbell front raise.mp4')

# import class
detector_dumbbell = pm.poseDetector()

# Initialize Variables
count_left_dumbbellfrontraise = 0
count_right_dumbbellfrontraise = 0

dir_left_dumbbellfrontraise = 0
dir_right_dumbbellfrontraise = 0

start_time_dumbbellfrontraise = time.time()  # starts time
repetition_time_dumbbellfrontraise = 60  # duration time
display_info_dumbbellfrontraise = True  # display features

bar_left_dumbbellfrontraise = 0
bar_right_dumbbellfrontraise = 0
per_left_dumbbellfrontraise = 0
per_right_dumbbellfrontraise = 0
angle_left_dumbbellfrontraise = 0
angle_right_dumbbellfrontraise = 0

# main loop
while True:
    # reads camera
    success, img = cap.read()
    # resizes video feed (can be changed depending on requirements of our Raspberry PI and Display Monitor Resolution)
    img = cv2.resize(img, (1280, 720))

    # Timer - starts timer based on set duration
    elapsed_time = time.time() - start_time_dumbbellfrontraise
    remaining_time = max(0, repetition_time_dumbbellfrontraise - elapsed_time)

    if display_info_dumbbellfrontraise:  # Check if to display counter, bar, and percentage
        img = detector_dumbbell.findPose(img, False)  # initializes img as variable for findpose function
        lmList = detector_dumbbell.findPosition(img, False)  # initializes lmList as variable for findPosition function

        # Define hand angles outside the if statement
        if len(lmList) != 0:

            angle_left_dumbbellfrontraise = detector_dumbbell.findAngle(img, 15, 11, 23, 13)
            angle_right_dumbbellfrontraise = detector_dumbbell.findAngle2(img, 24, 12, 16, 14) 


            # # Interpolate angle to percentage and position on screen
            per_left_dumbbellfrontraise = np.interp(angle_left_dumbbellfrontraise, (20, 150), (0, 100))
            bar_left_dumbbellfrontraise = np.interp(angle_left_dumbbellfrontraise, (20, 160), (400, 200))

            per_right_dumbbellfrontraise = np.interp(angle_right_dumbbellfrontraise, (20, 150), (0, 100))
            bar_right_dumbbellfrontraise = np.interp(angle_right_dumbbellfrontraise, (20, 160), (400, 200))

            #Check for the left dumbbell front raises
            if angle_left_dumbbellfrontraise >= 150:
                if dir_left_dumbbellfrontraise == 0 and count_left_dumbbellfrontraise < 5:
                    count_left_dumbbellfrontraise += 0.5
                    if count_left_dumbbellfrontraise == 5:
                        dir_left_dumbbellfrontraise = -1
                    else:
                        dir_left_dumbbellfrontraise = 1
            elif angle_left_dumbbellfrontraise <= 20:
                if dir_left_dumbbellfrontraise == 1 and count_left_dumbbellfrontraise < 5:
                    count_left_dumbbellfrontraise += 0.5
                    if count_left_dumbbellfrontraise == 5:
                        dir_left_dumbbellfrontraise = -1
                    else:
                        dir_left_dumbbellfrontraise = 0

            # Check for the right dumbbell front raises
            if angle_right_dumbbellfrontraise >= 150:
                if dir_right_dumbbellfrontraise == 0 and count_right_dumbbellfrontraise < 5:
                    count_right_dumbbellfrontraise += 0.5
                    if count_right_dumbbellfrontraise == 5:
                        dir_right_dumbbellfrontraise = -1
                    else:
                        dir_right_dumbbellfrontraise = 1
            if angle_right_dumbbellfrontraise <= 20:
                if dir_right_dumbbellfrontraise == 1 and count_right_dumbbellfrontraise < 5:
                    count_right_dumbbellfrontraise += 0.5
                    if count_right_dumbbellfrontraise == 5:
                        dir_right_dumbbellfrontraise = -1
                    else:
                        dir_right_dumbbellfrontraise = 0

        # label
        cvzone.putTextRect(img, 'Dumbbell Raise Tracker', [345, 30], thickness=2, border=2, scale=2.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # bar
        cv2.putText(img, f"R {int(per_right_dumbbellfrontraise)}%", (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_dumbbellfrontraise)), (50, 400), (0, 0, 255), -1)

        cv2.putText(img, f"L {int(per_left_dumbbellfrontraise)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_dumbbellfrontraise)), (995, 400), (0, 0, 255), -1)

        if angle_left_dumbbellfrontraise >= 150:
            cv2.rectangle(img, (952, int(bar_left_dumbbellfrontraise)), (995, 400), (0, 255, 0), -1)

        if angle_right_dumbbellfrontraise >= 150:
            cv2.rectangle(img, (8, int(bar_right_dumbbellfrontraise)), (50, 400), (0, 255, 0), -1)

    # count
    cv2.rectangle(img, (20, 20), (140, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(count_right_dumbbellfrontraise)}/5", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (150, 20), (270, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(count_left_dumbbellfrontraise)}/5", (160, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
        display_info_dumbbellfrontraise = False

    if count_right_dumbbellfrontraise == 5 and count_left_dumbbellfrontraise == 5:
        cvzone.putTextRect(img, 'All Repetitions Completed', [390, 30], thickness=2, border=2, scale=2.5)
        display_info_dumbbellfrontraise = False

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
