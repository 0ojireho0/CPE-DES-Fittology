# import libraries
import math
import cv2
import numpy as np
import time
import dumbbellfrontraise_front_PoseModule as pm  # Assuming you have a pose module named 'dumbbellfrontraise_PoseModule.py'
import cvzone

# Camera
cap = cv2.VideoCapture(r'D:\CPEDES\Flask\Exercises\gaining_muscle\Dumbbell Front Raise\dumbbell front raise.mp4')

detector_dumbbellfrontraise = pm.poseDetector()

dir_left_dumbbellfrontraise = 0
dir_right_dumbbellfrontraise = 0

repetition_time_dumbbellfrontraise = 60  # Repetition time

# Display info
display_info_dumbbellfrontraise = True

orientation_dumbbellfrontraise = ""
orientation2_dumbbellfrontraise = ""

per_right_dumbbellfrontraise = 0
per_left_dumbbellfrontraise = 0
bar_left_dumbbellfrontraise = 0
bar_right_dumbbellfrontraise = 0 


color_right_dumbbellfrontraise = (0, 0, 255)
color_left_dumbbellfrontraise = (0, 0, 255)

feedback_left_dumbbellfrontraise = ""
feedback_right_dumbbellfrontraise = ""

success_threshold_dumbbellfrontraise = 100

atrest_value_dumbbellfrontraise = 0

unsuccessful_reps_count_left_dumbbellfrontraise = 0
successful_reps_count_left_dumbbellfrontraise = 0

unsuccessful_reps_count_right_dumbbellfrontraise = 0
successful_reps_count_right_dumbbellfrontraise = 0

dir_left_unsuccessful_dumbbellfrontraise = 0
dir_right_unsuccessful_dumbbellfrontraise = 0

total_reps_count_dumbbellfrontraise = 0

total_reps_count_left_dumbbellfrontraise = 0
total_reps_count_right_dumbbellfrontraise = 0

start_time1_dumbbellfrontraise = time.time()
start_time2_dumbbellfrontraise = time.time()
start_time3_dumbbellfrontraise = time.time()
time_threshold_dumbbellfrontraise = 10 # Specify the time threshold in seconds # can be changed for testing but default should be 1, 0.2 is for testing
within_range_time1_dumbbellfrontraise = 0
within_range_time2_dumbbellfrontraise = 0

# gen feedback success
general_feedback_left_dumbbellfrontraise = ""
general_feedback_right_dumbbellfrontraise = ""

# gen feedback unsuccess
dir_gen_feedback_dumbbellfrontraise = 0
dir_gen_feedback_unsuccessful_dumbbellfrontraise = 0

cooldown_timer_dumbbellfrontraise = 0
cooldown_duration_dumbbellfrontraise = 5

angle_left_dumbbellfrontraise = 0
angle_right_dumbbellfrontraise = 0

# main loop
while True:
    # reads camera
    success, img = cap.read()
    # resizes video feed (can be changed depending on requirements of our Raspberry PI and Display Monitor Resolution)
    img = cv2.resize(img, (1280, 720))

    # Timer - starts timer based on set duration
    elapsed_time_dumbbellfrontraise = time.time() - start_time1_dumbbellfrontraise
    remaining_time_dumbbellfrontraise = max(0, repetition_time_dumbbellfrontraise - elapsed_time_dumbbellfrontraise)

    if display_info_dumbbellfrontraise:  # Check if to display counter, bar, and percentage
        img = detector_dumbbellfrontraise.findPose(img, False)  # initializes img as variable for findpose function
        lmList_dumbbellfrontraise = detector_dumbbellfrontraise.findPosition(img, False)  # initializes lmList as variable for findPosition function

        # Define hand angles outside the if statement
        if len(lmList_dumbbellfrontraise) != 0:

            angle_left_dumbbellfrontraise = detector_dumbbellfrontraise.findAngle(img, 15, 11, 23, 13)
            angle_right_dumbbellfrontraise = detector_dumbbellfrontraise.findAngle2(img, 24, 12, 16, 14) 

            # # Interpolate angle to percentage and position on screen
            per_left_dumbbellfrontraise = np.interp(angle_left_dumbbellfrontraise, (20, 150), (0, 100))
            bar_left_dumbbellfrontraise = np.interp(angle_left_dumbbellfrontraise, (20, 150), (400, 200))

            per_right_dumbbellfrontraise = np.interp(angle_right_dumbbellfrontraise, (20, 150), (0, 100))
            bar_right_dumbbellfrontraise = np.interp(angle_right_dumbbellfrontraise, (20, 150), (400, 200))

            if int(per_left_dumbbellfrontraise) == 100:
                color_left_dumbbellfrontraise = (0, 255, 0)  # Change color of left leg bar to green
            else:
                color_left_dumbbellfrontraise = (0, 0, 255)
            
            if int(per_right_dumbbellfrontraise) == 100:
                color_right_dumbbellfrontraise = (0, 255, 0)
            else:
                color_right_dumbbellfrontraise = (0, 0, 255)

            #left
            if 40 <= per_left_dumbbellfrontraise <= 90:
                # Increment the time within range
                within_range_time1_dumbbellfrontraise += time.time() - start_time2_dumbbellfrontraise

                # Check if peak value has been within range for the specified time
                if within_range_time1_dumbbellfrontraise >= time_threshold_dumbbellfrontraise:
                    if dir_left_unsuccessful_dumbbellfrontraise == 0:
                        unsuccessful_reps_count_left_dumbbellfrontraise += 0.5
                        dir_left_unsuccessful_dumbbellfrontraise = 1
            else:
                within_range_time1_dumbbellfrontraise = 0
                # Update the start time to the current time
                start_time2_dumbbellfrontraise = time.time()

            if 1 <= per_left_dumbbellfrontraise <= 10:
                if dir_left_unsuccessful_dumbbellfrontraise == 1:
                    unsuccessful_reps_count_left_dumbbellfrontraise += 0.5
                    dir_left_unsuccessful_dumbbellfrontraise = 0

            if per_left_dumbbellfrontraise == success_threshold_dumbbellfrontraise:
                if dir_left_dumbbellfrontraise == 0:
                    successful_reps_count_left_dumbbellfrontraise += 0.5
                    dir_left_dumbbellfrontraise = 1

            elif per_left_dumbbellfrontraise == atrest_value_dumbbellfrontraise:
                if dir_left_dumbbellfrontraise == 1:
                    successful_reps_count_left_dumbbellfrontraise += 0.5
                    dir_left_dumbbellfrontraise = 0

            # right
            if 40 <= per_right_dumbbellfrontraise <= 90:
                # Increment the time within range
                within_range_time2_dumbbellfrontraise += time.time() - start_time3_dumbbellfrontraise

                # Check if peak value has been within range for the specified time
                if within_range_time2_dumbbellfrontraise >= time_threshold_dumbbellfrontraise:
                    if dir_right_unsuccessful_dumbbellfrontraise == 0:
                        unsuccessful_reps_count_right_dumbbellfrontraise += 0.5
                        dir_right_unsuccessful_dumbbellfrontraise = 1
            else:
                within_range_time2_dumbbellfrontraise = 0
                # Update the start time to the current time
                start_time3_dumbbellfrontraise = time.time()

            if 1 <= per_right_dumbbellfrontraise <= 10:
                #print("left down val: ", per_left)
                if dir_right_unsuccessful_dumbbellfrontraise == 1:
                    unsuccessful_reps_count_right_dumbbellfrontraise += 0.5
                    dir_right_unsuccessful_dumbbellfrontraise = 0

            if per_right_dumbbellfrontraise == success_threshold_dumbbellfrontraise:
                if dir_right_dumbbellfrontraise == 0:
                    successful_reps_count_right_dumbbellfrontraise += 0.5
                    dir_right_dumbbellfrontraise = 1
                    cooldown_timer_dumbbellfrontraise = cooldown_duration_dumbbellfrontraise
            elif per_right_dumbbellfrontraise == atrest_value_dumbbellfrontraise: 
                if dir_right_dumbbellfrontraise == 1:
                    successful_reps_count_right_dumbbellfrontraise += 0.5
                    dir_right_dumbbellfrontraise = 0
                    cooldown_timer_dumbbellfrontraise = cooldown_duration_dumbbellfrontraise

            # feedback for left hand  # TO BE FETCHED 
            feedback_left_dumbbellfrontraise = detector_dumbbellfrontraise.feedback_dumbbellfrontraise(per_left_dumbbellfrontraise)

            detector_dumbbellfrontraise.update_next_per_left(per_left_dumbbellfrontraise)

            # feedback for right hand  # TO BE FETCHED 
            feedback_right_dumbbellfrontraise = detector_dumbbellfrontraise.feedback_dumbbellfrontraise(per_right_dumbbellfrontraise)

            detector_dumbbellfrontraise.update_next_per_left(per_right_dumbbellfrontraise)

        # label
        cvzone.putTextRect(img, 'Dumbbell Raise Front', [345, 30], thickness=2, border=2, scale=2.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time_dumbbellfrontraise)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # bar
        cv2.putText(img, f"R {int(per_right_dumbbellfrontraise)}%", (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_dumbbellfrontraise)), (50, 400), color_right_dumbbellfrontraise, -1)

        cv2.putText(img, f"L {int(per_left_dumbbellfrontraise)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_dumbbellfrontraise)), (995, 400), color_left_dumbbellfrontraise, -1)

    # count
    cv2.rectangle(img, (20, 20), (140, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(successful_reps_count_right_dumbbellfrontraise)}/5", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (150, 20), (270, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(successful_reps_count_left_dumbbellfrontraise)}/5", (160, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    if remaining_time_dumbbellfrontraise <= 0:
        cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
        display_info_dumbbellfrontraise = False

    if successful_reps_count_right_dumbbellfrontraise >= 10 and successful_reps_count_left_dumbbellfrontraise >= 10:
        cvzone.putTextRect(img, 'All Repetitions Completed', [420, 30], thickness=2, border=2, scale=2.5)
        display_info_dumbbellfrontraise = False
        # General feedback after finishing the exercise # TO BE FETCHED
        if dir_gen_feedback_dumbbellfrontraise == 0:
            general_feedback_left_dumbbellfrontraise = detector_dumbbellfrontraise.left_arm_feedback(total_reps_count_left_dumbbellfrontraise)
            general_feedback_right_dumbbellfrontraise = detector_dumbbellfrontraise.right_arm_feedback(total_reps_count_right_dumbbellfrontraise)
            dir_gen_feedback_dumbbellfrontraise = 1

    if unsuccessful_reps_count_left_dumbbellfrontraise >= 2 and unsuccessful_reps_count_right_dumbbellfrontraise >= 2:
        cvzone.putTextRect(img, 'You have made 2 unsuccessful tries for both arms. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_dumbbellfrontraise = False

        if dir_gen_feedback_unsuccessful_dumbbellfrontraise == 0:
            general_feedback_left_dumbbellfrontraise = detector_dumbbellfrontraise.left_arm_unsuccessful_feedback(total_reps_count_left_dumbbellfrontraise)
            general_feedback_right_dumbbellfrontraise = detector_dumbbellfrontraise.right_arm_unsuccessful_feedback(total_reps_count_right_dumbbellfrontraise)
            dir_gen_feedback_unsuccessful_dumbbellfrontraise = 1
    
    if unsuccessful_reps_count_left_dumbbellfrontraise >= 2:
        cvzone.putTextRect(img, 'You have made 2 unsuccessful tries for left arm. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_dumbbellfrontraise = False

        if dir_gen_feedback_unsuccessful_dumbbellfrontraise == 0:
            general_feedback_left_dumbbellfrontraise = detector_dumbbellfrontraise.left_arm_unsuccessful_feedback(total_reps_count_left_dumbbellfrontraise)
            dir_gen_feedback_unsuccessful_dumbbellfrontraise = 1

    if unsuccessful_reps_count_right_dumbbellfrontraise >= 2:
        cvzone.putTextRect(img, 'You have made 2 unsuccessful tries for right arm. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_dumbbellfrontraise = False

        if dir_gen_feedback_unsuccessful_dumbbellfrontraise == 0:
            general_feedback_right_dumbbellfrontraise = detector_dumbbellfrontraise.right_arm_unsuccessful_feedback(total_reps_count_right_dumbbellfrontraise)
            dir_gen_feedback_unsuccessful_dumbbellfrontraise == 1

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
