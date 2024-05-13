import math
import cv2
import numpy as np
import time
import highkneetap_front_PoseModule as pm
import cvzone

cap = cv2.VideoCapture(r'D:\CPEDES\Flask\Exercises\gaining_muscle\High Knee Tap\highkneetap.mp4')
detector_highkneetap = pm.poseDetectorHighKneeTap()

dir_left_highkneetap = 0
dir_right_highkneetap = 0

repetition_time_highkneetap = 60  # Repetition time

# Display info
display_info_highkneetap = True

per_right_highkneetap = 0
per_left_highkneetap = 0
bar_left_highkneetap = 0
bar_right_highkneetap = 0 


color_right_highkneetap = (0, 0, 255)
color_left_highkneetap = (0, 0, 255)

feedback_left_highkneetap = ""
feedback_right_highkneetap = ""

success_threshold_highkneetap = 100

atrest_value_highkneetap = 0

unsuccessful_reps_count_left_highkneetap = 0
successful_reps_count_left_highkneetap = 0

unsuccessful_reps_count_right_highkneetap = 0
successful_reps_count_right_highkneetap = 0

dir_left_unsuccessful_highkneetap = 0
dir_right_unsuccessful_highkneetap = 0

total_reps_count_highkneetap = 0

total_reps_count_left_highkneetap = 0
total_reps_count_right_highkneetap = 0

start_time1_highkneetap = time.time()
start_time2_highkneetap = time.time()
start_time3_highkneetap = time.time()
time_threshold_highkneetap = 1 # Specify the time threshold in seconds # can be changed for testing but default should be 1, 0.2 is for testing
within_range_time1_highkneetap = 0
within_range_time2_highkneetap = 0

# gen feedback success
general_feedback_left_highkneetap = ""
general_feedback_right_highkneetap = ""

# gen feedback unsuccess
dir_gen_feedback_highkneetap = 0
dir_gen_feedback_unsuccessful_highkneetap = 0

cooldown_timer_highkneetap = 0
cooldown_duration_highkneetap = 5

leftleg_highkneetap = 0
rightleg_highkneetap = 0

while True:
    success, img = cap.read()
    img = cv2.resize(img, (1280, 720))

    elapsed_time_highkneetap = time.time() - start_time1_highkneetap
    remaining_time_highkneetap = max(0, repetition_time_highkneetap - elapsed_time_highkneetap)

    if display_info_highkneetap:  # Check if to display counter, bar, and percentage
        img = detector_highkneetap.findPose(img, False)
        lmList_highkneetap = detector_highkneetap.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_highkneetap) != 0:

            # Right and Left keypoints
            rightleg_highkneetap = detector_highkneetap.HighKneeTap(img, 24, 26, 28, True)
            leftleg_highkneetap = detector_highkneetap.HighKneeTap(img, 23, 25, 27, True)

            if cooldown_timer_highkneetap > 0:
                cooldown_timer_highkneetap -= 1

            per_right_highkneetap = np.interp(rightleg_highkneetap, (150, 240), (100, 0))
            bar_right_highkneetap = np.interp(rightleg_highkneetap, (150, 240), (480, 680))

            per_left_highkneetap = np.interp(leftleg_highkneetap, (150, 240), (100, 0))
            bar_left_highkneetap = np.interp(leftleg_highkneetap, (150, 240), (480, 680))

            if int(per_left_highkneetap) == 100:
                color_left_highkneetap = (0, 255, 0)  # Change color of left leg bar to green
            else:
                color_left_highkneetap = (0, 0, 255)
            
            if int(per_right_highkneetap) == 100:
                color_right_highkneetap = (0, 255, 0)
            else:
                color_right_highkneetap = (0, 0, 255)

            #left
            if 40 <= per_left_highkneetap <= 90:
                # Increment the time within range
                within_range_time1_highkneetap += time.time() - start_time2_highkneetap

                # Check if peak value has been within range for the specified time
                if within_range_time1_highkneetap >= time_threshold_highkneetap:
                    if dir_left_unsuccessful_highkneetap == 0:
                        unsuccessful_reps_count_left_highkneetap += 0.5
                        dir_left_unsuccessful_highkneetap = 1
            else:
                within_range_time1_highkneetap = 0
                # Update the start time to the current time
                start_time2_highkneetap = time.time()

            if 1 <= per_left_highkneetap <= 10:
                if dir_left_unsuccessful_highkneetap == 1:
                    unsuccessful_reps_count_left_highkneetap += 0.5
                    dir_left_unsuccessful_highkneetap = 0

            if per_left_highkneetap == success_threshold_highkneetap:
                if dir_left_highkneetap == 0:
                    successful_reps_count_left_highkneetap += 0.5
                    dir_left_highkneetap = 1

            elif per_left_highkneetap == atrest_value_highkneetap:
                if dir_left_highkneetap == 1:
                    successful_reps_count_left_highkneetap += 0.5
                    dir_left_highkneetap = 0

            # right
            if 40 <= per_right_highkneetap <= 90:
                # Increment the time within range
                within_range_time2_highkneetap += time.time() - start_time3_highkneetap

                # Check if peak value has been within range for the specified time
                if within_range_time2_highkneetap >= time_threshold_highkneetap:
                    if dir_right_unsuccessful_highkneetap == 0:
                        unsuccessful_reps_count_right_highkneetap += 0.5
                        dir_right_unsuccessful_highkneetap = 1
            else:
                within_range_time2_highkneetap = 0
                # Update the start time to the current time
                start_time3_highkneetap = time.time()

            if 1 <= per_right_highkneetap <= 10:
                if dir_right_unsuccessful_highkneetap == 1:
                    unsuccessful_reps_count_right_highkneetap += 0.5
                    dir_right_unsuccessful_highkneetap = 0

            if per_right_highkneetap == success_threshold_highkneetap:
                if dir_right_highkneetap == 0:
                    successful_reps_count_right_highkneetap += 0.5
                    dir_right_highkneetap = 1
                    cooldown_timer_highkneetap = cooldown_duration_highkneetap
            elif per_right_highkneetap == atrest_value_highkneetap: 
                if dir_right_highkneetap == 1:
                    successful_reps_count_right_highkneetap += 0.5
                    dir_right_highkneetap = 0
                    cooldown_timer_highkneetap = cooldown_duration_highkneetap

            # feedback for left hand  # TO BE FETCHED 
            feedback_left_highkneetap = detector_highkneetap.feedback_highkneetap(per_left_highkneetap)

            detector_highkneetap.update_next_per_left(per_left_highkneetap)

            # feedback for right hand  # TO BE FETCHED 
            feedback_right_highkneetap = detector_highkneetap.feedback_highkneetap(per_right_highkneetap)

            detector_highkneetap.update_next_per_left(per_right_highkneetap)


        cvzone.putTextRect(img, 'Front High Knee Tap', [450, 30], thickness=2, border=2, scale=1.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time_highkneetap)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # RIGHT LEG
        cv2.putText(img, f"R {int(per_right_highkneetap)}%", (24, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 480), (50, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_highkneetap)), (50, 680), color_right_highkneetap, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_left_highkneetap)}%", (962, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 480), (995, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_highkneetap)), (995, 680), color_left_highkneetap, -1)
    
    # Counter 
    cv2.rectangle(img, (20, 20), (200, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(successful_reps_count_right_highkneetap)}/10", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (210, 20), (390, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(successful_reps_count_left_highkneetap)}/10", (220, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    #Timer
    if remaining_time_highkneetap <= 0:
        cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
        display_info = False

    if successful_reps_count_right_highkneetap >= 10 and successful_reps_count_left_highkneetap >= 10:
            cvzone.putTextRect(img, 'All Repetitions Completed', [420, 30], thickness=2, border=2, scale=2.5)
            display_info_highkneetap = False
            # General feedback after finishing the exercise # TO BE FETCHED
            if dir_gen_feedback_highkneetap == 0:
                general_feedback_left_highkneetap = detector_highkneetap.left_leg_feedback(total_reps_count_left_highkneetap)
                general_feedback_right_highkneetap = detector_highkneetap.right_leg_feedback(total_reps_count_right_highkneetap)
                dir_gen_feedback_highkneetap = 1

    if unsuccessful_reps_count_left_highkneetap >= 3 and unsuccessful_reps_count_right_highkneetap >= 3:
        cvzone.putTextRect(img, 'You have made 2 unsuccessful tries for both arms. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_highkneetap = False

        if dir_gen_feedback_unsuccessful_highkneetap == 0:
            general_feedback_left_highkneetap = detector_highkneetap.left_leg_unsuccessful_feedback(total_reps_count_left_highkneetap)
            general_feedback_right_highkneetap = detector_highkneetap.right_leg_unsuccessful_feedback(total_reps_count_right_highkneetap)
            dir_gen_feedback_unsuccessful_highkneetap = 1

    if unsuccessful_reps_count_left_highkneetap >= 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for left arm. Please retry again', [420, 30], thickness=2, border=2, scale=1)
        display_info_highkneetap = False

        if dir_gen_feedback_unsuccessful_highkneetap == 0:
            general_feedback_left_highkneetap = detector_highkneetap.left_leg_unsuccessful_feedback(total_reps_count_left_highkneetap)
            dir_gen_feedback_unsuccessful_highkneetap = 1

    if unsuccessful_reps_count_right_highkneetap >= 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for right arm. Please retry again', [420, 30], thickness=2, border=2, scale=1)
        display_info_highkneetap = False

        if dir_gen_feedback_unsuccessful_highkneetap == 0:
            general_feedback_right_highkneetap = detector_highkneetap.right_leg_unsuccessful_feedback(total_reps_count_right_highkneetap)
            dir_gen_feedback_unsuccessful_highkneetap == 1


    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()



