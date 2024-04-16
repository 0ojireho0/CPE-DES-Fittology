 # import libraries
import math
import cv2
import numpy as np
import time
import PushUp_PoseModule as pm
import cvzone

#Camera
cap = cv2.VideoCapture(r'D:\CPEDES\Flask\Exercises\push-up\PushUp.mp4')

# Import class
detector_pushup = pm.poseDetectorPushUp()

# Initialize variables
count_pushup = 0  # count_pushup of reps
pushup_dir = 0  # pushup_direction
pTime = 0  # Time
start_time_pushup = time.time()  # Start time
repetition_time_pushup = 60  # Repetition time

# Display info
display_pushup = True

per_right_pushup = 0
per_left_pushup = 0
bar_left_pushup = 0
bar_right_pushup = 0 

leftangle_pushup = 0
rightangle_pushup = 0

#main loop
while True:
    success, img = cap.read()
    img = cv2.resize(img, (1280, 720))

    elapsed_time = time.time() - start_time_pushup
    remaining_time = max(0, repetition_time_pushup - elapsed_time)

    if display_pushup:  # Check if to display count_pushup, bar, and percentage

        img = detector_pushup.findPose(img, False) # initializes img as variable for findpose function
        lmList = detector_pushup.findPosition(img, False) # initializes lmList_bicep as variable for findPosition function

        # Define hand angles outside the if statement
        if len(lmList) != 0:
            # Check if the person is in a proper push-up posture
            leftangle_pushup, rightangle_pushup = detector_pushup.findPushupAngle(img, 11, 13, 15, 12, 14, 16, drawpoints=True)  # defines left  and right arm landmark keypoints 

            # Interpolate angles to percentage and position on screen
            per_left_pushup = np.interp(leftangle_pushup, (-30, 170), (0, 100)) # first parenthesis, the value threshold of the angle. Second, represents the interp value
            bar_left_pushup = np.interp(leftangle_pushup, (-30, 180), (200, 400))

            per_right_pushup = np.interp(rightangle_pushup, (34, 163), (0, 100))
            bar_right_pushup = np.interp(rightangle_pushup, (34, 173), (400, 200))

            # Check for NaN values
            if not math.isnan(leftangle_pushup) and not math.isnan(rightangle_pushup):
                leftHandAngle = int(np.interp(leftangle_pushup, [-30, 180], [100, 0]))
                rightHandAngle = int(np.interp(rightangle_pushup, [34, 173], [100, 0]))
            else:
                leftHandAngle = 0
                rightHandAngle = 0
            
            #Check if the person is in a proper push-up posture
            if detector_pushup.isPushUpPosture(lmList):
                if leftHandAngle >= 70 and rightHandAngle >= 70:
                    if pushup_dir == 0:
                        count_pushup += 0.5
                        pushup_dir = 1
                        print(count_pushup)
                if leftHandAngle <= 70 and rightHandAngle <= 70:
                    if pushup_dir == 1:
                        count_pushup += 0.5
                        pushup_dir = 0
                        print(count_pushup)

        cvzone.putTextRect(img, 'Ai Push-Up count_pushuper', [345, 30], thickness=2, border=2, scale=2.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # Draw bars for left and right angles
        cv2.putText(img, f"R {int(per_right_pushup)}%", (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (255, 255, 255), 5)
        cv2.rectangle(img, (8, int(bar_right_pushup)), (50, 400), (0, 0, 255), -1)

        cv2.putText(img, f"L {int(per_right_pushup)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (255, 255, 255), 5)
        cv2.rectangle(img, (952, int(bar_right_pushup)), (995, 400), (0, 0, 255), -1)

        if leftangle_pushup > 70:
            cv2.rectangle(img, (952, int(bar_right_pushup)), (995, 400), (0, 255, 0), -1)

        if rightangle_pushup > 70:
            cv2.rectangle(img, (8, int(bar_right_pushup)), (50, 400), (0, 255, 0), -1)

    cv2.rectangle(img, (0, 0), (130, 120), (255, 0, 0), -1)
    cv2.putText(img, f"{int(count_pushup)}/9", (20, 70), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (0, 0, 255), 7)

    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [345, 30], thickness=2, border=2, scale=2.5)
        display_info = False

    if int(count_pushup) >= 9:
        cvzone.putTextRect(img, 'Repetition completed', [345, 30], thickness=2, border=2, scale=2.5)
        display_info = False

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


