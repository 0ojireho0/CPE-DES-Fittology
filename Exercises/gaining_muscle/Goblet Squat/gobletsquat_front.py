import math
import cv2
import numpy as np
import time
import gobletsquat_front_PoseModule as pm
import cvzone

cap = cv2.VideoCapture(r'D:\CPEDES\Flask\Exercises\gaining_muscle\Goblet Squat\Goblet Squat-Front and Side View.mp4')
detector_gobletsquat = pm.poseDetectorGobletSquat()


dir_left_gobletsquat = 0
dir_right_gobletsquat = 0

repetition_time_gobletsquat = 60  # Repetition time

# Display info
display_info_gobletsquat = True

per_right_gobletsquat = 0
per_left_gobletsquat = 0
bar_left_gobletsquat = 0
bar_right_gobletsquat = 0 


color_right_gobletsquat = (0, 0, 255)
color_left_gobletsquat = (0, 0, 255)

feedback_left_gobletsquat = ""
feedback_right_gobletsquat = ""

success_threshold_gobletsquat = 100

atrest_value_gobletsquat = 0

unsuccessful_reps_count_left_gobletsquat = 0
successful_reps_count_left_gobletsquat = 0

unsuccessful_reps_count_right_gobletsquat = 0
successful_reps_count_right_gobletsquat = 0

dir_left_unsuccessful_gobletsquat = 0
dir_right_unsuccessful_gobletsquat = 0

total_reps_count_gobletsquat = 0

total_reps_count_left_gobletsquat = 0
total_reps_count_right_gobletsquat = 0

start_time1_gobletsquat = time.time()
start_time2_gobletsquat = time.time()
start_time3_gobletsquat = time.time()
time_threshold_gobletsquat = 10 
within_range_time1_gobletsquat = 0
within_range_time2_gobletsquat = 0

# gen feedback success
general_feedback_left_gobletsquat = ""
general_feedback_right_gobletsquat = ""

# gen feedback unsuccess
dir_gen_feedback_gobletsquat = 0
dir_gen_feedback_unsuccessful_gobletsquat = 0

cooldown_timer_gobletsquat = 0
cooldown_duration_gobletsquat = 5


while True:
    success, img = cap.read()
    img = cv2.resize(img, (1280, 720))

    elapsed_time_gobletsquat = time.time() - start_time1_gobletsquat
    remaining_time_gobletsquat = max(0, repetition_time_gobletsquat - elapsed_time_gobletsquat)

    if display_info_gobletsquat:  # Check if to display counter, bar, and percentage
        img = detector_gobletsquat.findPose(img, False)
        lmList_gobletsquat = detector_gobletsquat.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_gobletsquat) != 0:

            # Right and Left keypoints
            rightleg_gobletsquat = detector_gobletsquat.GobletSquat(img, 24, 26, 28, True)
            leftleg_gobletsquat = detector_gobletsquat.GobletSquat(img, 23, 25, 27, True)

            if cooldown_timer_gobletsquat > 0:
                cooldown_timer_gobletsquat -= 1

            per_right_gobletsquat = np.interp(rightleg_gobletsquat, (160, 240), (100, 0))
            bar_right_gobletsquat = np.interp(rightleg_gobletsquat, (160, 240), (480, 680))
            per_left_gobletsquat = np.interp(leftleg_gobletsquat, (160, 240), (100, 0))
            bar_left_gobletsquat = np.interp(leftleg_gobletsquat, (160, 240), (480, 680))

            if int(per_left_gobletsquat) == 100:
                color_left_gobletsquat = (0, 255, 0)  # Change color of left leg bar to green
            else:
                color_left_gobletsquat = (0, 0, 255)
            
            if int(per_right_gobletsquat) == 100:
                color_right_gobletsquat = (0, 255, 0)
            else:
                color_right_gobletsquat = (0, 0, 255)

            #left
            if 40 <= per_left_gobletsquat <= 90:
                # Increment the time within range
                within_range_time1_gobletsquat += time.time() - start_time2_gobletsquat

                # Check if peak value has been within range for the specified time
                if within_range_time1_gobletsquat >= time_threshold_gobletsquat:
                    if dir_left_unsuccessful_gobletsquat == 0:
                        unsuccessful_reps_count_left_gobletsquat += 0.5
                        dir_left_unsuccessful_gobletsquat = 1
            else:
                within_range_time1_gobletsquat = 0
                # Update the start time to the current time
                start_time2_gobletsquat = time.time()

            if 1 <= per_left_gobletsquat <= 10:
                if dir_left_unsuccessful_gobletsquat == 1:
                    unsuccessful_reps_count_left_gobletsquat += 0.5
                    dir_left_unsuccessful_gobletsquat = 0

            if per_left_gobletsquat == success_threshold_gobletsquat:
                if dir_left_gobletsquat == 0:
                    successful_reps_count_left_gobletsquat += 0.5
                    dir_left_gobletsquat = 1

            elif per_left_gobletsquat == atrest_value_gobletsquat:
                if dir_left_gobletsquat == 1:
                    successful_reps_count_left_gobletsquat += 0.5
                    dir_left_gobletsquat = 0

            # right
            if 40 <= per_right_gobletsquat <= 90:
                # Increment the time within range
                within_range_time2_gobletsquat += time.time() - start_time3_gobletsquat

                # Check if peak value has been within range for the specified time
                if within_range_time2_gobletsquat >= time_threshold_gobletsquat:
                    if dir_right_unsuccessful_gobletsquat == 0:
                        unsuccessful_reps_count_right_gobletsquat += 0.5
                        dir_right_unsuccessful_gobletsquat = 1
            else:
                within_range_time2_gobletsquat = 0
                # Update the start time to the current time
                start_time3_gobletsquat = time.time()

            if 1 <= per_right_gobletsquat <= 10:
                if dir_right_unsuccessful_gobletsquat == 1:
                    unsuccessful_reps_count_right_gobletsquat += 0.5
                    dir_right_unsuccessful_gobletsquat = 0

            if per_right_gobletsquat == success_threshold_gobletsquat:
                if dir_right_gobletsquat == 0:
                    successful_reps_count_right_gobletsquat += 0.5
                    dir_right_gobletsquat = 1
                    cooldown_timer_gobletsquat = cooldown_duration_gobletsquat
            elif per_right_gobletsquat == atrest_value_gobletsquat: 
                if dir_right_gobletsquat == 1:
                    successful_reps_count_right_gobletsquat += 0.5
                    dir_right_gobletsquat = 0
                    cooldown_timer_gobletsquat = cooldown_duration_gobletsquat

            # feedback for left hand  # TO BE FETCHED 
            feedback_left_gobletsquat = detector_gobletsquat.feedback_gobletsquat(per_left_gobletsquat)

            detector_gobletsquat.update_next_per_left(per_left_gobletsquat)

            # feedback for right hand  # TO BE FETCHED 
            feedback_right_gobletsquat = detector_gobletsquat.feedback_gobletsquat(per_right_gobletsquat)

            detector_gobletsquat.update_next_per_left(per_right_gobletsquat)


        cvzone.putTextRect(img, 'Front Goblet Squat', [450, 30], thickness=2, border=2, scale=1.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time_gobletsquat)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)
        # RIGHT LEG
        cv2.putText(img, f"R {int(per_right_gobletsquat)}%", (24, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 480), (50, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_gobletsquat)), (50, 680), color_right_gobletsquat, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_left_gobletsquat)}%", (962, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 480), (995, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_gobletsquat)), (995, 680), color_left_gobletsquat, -1)

    # Counter 
    cv2.rectangle(img, (20, 20), (200, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(successful_reps_count_right_gobletsquat)}/10", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (210, 20), (390, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(successful_reps_count_left_gobletsquat)}/10", (220, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)


    #Timer
    if remaining_time_gobletsquat <= 0:
        cvzone.putTextRect(img, "Time's Up", [420, 30], thickness=2, border=2, scale=2.5)
        display_info_gobletsquat = False

    if successful_reps_count_right_gobletsquat >= 10 and successful_reps_count_left_gobletsquat >= 10:
            cvzone.putTextRect(img, 'All Repetitions Completed', [420, 30], thickness=2, border=2, scale=2.5)
            display_info_gobletsquat = False
            # General feedback after finishing the exercise # TO BE FETCHED
            if dir_gen_feedback_gobletsquat == 0:
                general_feedback_left_gobletsquat = detector_gobletsquat.left_leg_feedback(total_reps_count_left_gobletsquat)
                general_feedback_right_gobletsquat = detector_gobletsquat.right_leg_feedback(total_reps_count_right_gobletsquat)
                dir_gen_feedback_gobletsquat = 1

    if unsuccessful_reps_count_left_gobletsquat >= 3 and unsuccessful_reps_count_right_gobletsquat >= 3:
        cvzone.putTextRect(img, 'You have made 2 unsuccessful tries for both arms. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_gobletsquat = False

        if dir_gen_feedback_unsuccessful_gobletsquat == 0:
            general_feedback_left_gobletsquat = detector_gobletsquat.left_leg_unsuccessful_feedback(total_reps_count_left_gobletsquat)
            general_feedback_right_gobletsquat = detector_gobletsquat.right_leg_unsuccessful_feedback(total_reps_count_right_gobletsquat)
            dir_gen_feedback_unsuccessful_gobletsquat = 1

    if unsuccessful_reps_count_left_gobletsquat >= 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for left arm. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_gobletsquat = False

        if dir_gen_feedback_unsuccessful_gobletsquat == 0:
            general_feedback_left_gobletsquat = detector_gobletsquat.left_leg_unsuccessful_feedback(total_reps_count_left_gobletsquat)
            dir_gen_feedback_unsuccessful_gobletsquat = 1

    if unsuccessful_reps_count_right_gobletsquat >= 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for right arm. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_gobletsquat = False

        if dir_gen_feedback_unsuccessful_gobletsquat == 0:
            general_feedback_right_gobletsquat = detector_gobletsquat.right_leg_unsuccessful_feedback(total_reps_count_right_gobletsquat)
            dir_gen_feedback_unsuccessful_gobletsquat == 1


    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()



