import math
import cv2
import numpy as np
import time
import shouldertaps_front_PoseModule as pm
import cvzone
# C:\Users\RID\Desktop\pose_estimation\aipose2\Exercise\weightloss\jumpingjack.mp4

cap = cv2.VideoCapture(r'D:\CPEDES\Flask\Exercises\gaining_muscle\Shoulder Tap\Shoulder Taps.mp4')
detector_shouldertaps = pm.poseDetectorShoulderTap()

dir_left_shouldertaps = 0
dir_right_shouldertaps = 0

repetition_time_shouldertaps = 60  # Repetition time

# Display info
display_info_shouldertaps = True

orientation_shouldertaps = ""
orientation2_shouldertaps = ""

per_right_shouldertaps = 0
per_left_shouldertaps = 0
bar_left_shouldertaps = 0
bar_right_shouldertaps = 0 


color_right_shouldertaps = (0, 0, 255)
color_left_shouldertaps = (0, 0, 255)

feedback_left_shouldertaps = ""
feedback_right_shouldertaps = ""

success_threshold_shouldertaps = 100

atrest_value_shouldertaps = 0

unsuccessful_reps_count_left_shouldertaps = 0
successful_reps_count_left_shouldertaps = 0

unsuccessful_reps_count_right_shouldertaps = 0
successful_reps_count_right_shouldertaps = 0

dir_left_unsuccessful_shouldertaps = 0
dir_right_unsuccessful_shouldertaps = 0

total_reps_count_shouldertaps = 0

total_reps_count_left_shouldertaps = 0
total_reps_count_right_shouldertaps = 0

start_time1_shouldertaps = time.time()
start_time2_shouldertaps = time.time()
start_time3_shouldertaps = time.time()
time_threshold_shouldertaps = 1 # Specify the time threshold in seconds # can be changed for testing but default should be 1, 0.2 is for testing
within_range_time1_shouldertaps = 0
within_range_time2_shouldertaps = 0

# gen feedback success
general_feedback_left_shouldertaps = ""
general_feedback_right_shouldertaps = ""

# gen feedback unsuccess
dir_gen_feedback_shouldertaps = 0
dir_gen_feedback_unsuccessful_shouldertaps = 0

cooldown_timer_shouldertaps = 0
cooldown_duration_shouldertaps = 5


while True:
    success, img = cap.read()
    img = cv2.resize(img, (1280, 720))

    elapsed_time_shouldertaps = time.time() - start_time1_shouldertaps
    remaining_time_shouldertaps = max(0, repetition_time_shouldertaps - elapsed_time_shouldertaps)

    if display_info_shouldertaps:  # Check if to display counter, bar, and percentage
        img = detector_shouldertaps.findPose(img, False)
        lmList_shouldertaps = detector_shouldertaps.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_shouldertaps) != 0:

            distance1_shouldertaps, distance2_shouldertaps = detector_shouldertaps.ShoulderTap(img, 12, 14, 16, 11, 13, 15, drawpoints=True) 

            #Interpolate angle to percentage and position on screen
            per_right_shouldertaps = np.interp(distance1_shouldertaps, (180, 350), (100, 0))
            bar_right_shouldertaps = np.interp(distance1_shouldertaps, (180, 350), (200, 400))

            per_left_shouldertaps = np.interp(distance2_shouldertaps, (180, 350), (100, 0))
            bar_left_shouldertaps = np.interp(distance2_shouldertaps, (180, 350), (200, 400))


            if int(per_left_shouldertaps) == 100:
                color_left_shouldertaps = (0, 255, 0)  # Change color of left leg bar to green
            else:
                color_left_shouldertaps = (0, 0, 255)
            
            if int(per_right_shouldertaps) == 100:
                color_right_shouldertaps = (0, 255, 0)
            else:
                color_right_shouldertaps = (0, 0, 255)

            #left
            if 40 <= per_left_shouldertaps <= 90:
                # Increment the time within range
                within_range_time1_shouldertaps += time.time() - start_time2_shouldertaps

                # Check if peak value has been within range for the specified time
                if within_range_time1_shouldertaps >= time_threshold_shouldertaps:
                    if dir_left_unsuccessful_shouldertaps == 0:
                        unsuccessful_reps_count_left_shouldertaps += 0.5
                        dir_left_unsuccessful_shouldertaps = 1
            else:
                within_range_time1_shouldertaps = 0
                # Update the start time to the current time
                start_time2_shouldertaps = time.time()

            if 1 <= per_left_shouldertaps <= 10:
                if dir_left_unsuccessful_shouldertaps == 1:
                    unsuccessful_reps_count_left_shouldertaps += 0.5
                    dir_left_unsuccessful_shouldertaps = 0

            if per_left_shouldertaps == success_threshold_shouldertaps:
                if dir_left_shouldertaps == 0:
                    successful_reps_count_left_shouldertaps += 0.5
                    dir_left_shouldertaps = 1

            elif per_left_shouldertaps == atrest_value_shouldertaps:
                if dir_left_shouldertaps == 1:
                    successful_reps_count_left_shouldertaps += 0.5
                    dir_left_shouldertaps = 0

            # right
            if 40 <= per_right_shouldertaps <= 90:
                # Increment the time within range
                within_range_time2_shouldertaps += time.time() - start_time3_shouldertaps

                # Check if peak value has been within range for the specified time
                if within_range_time2_shouldertaps >= time_threshold_shouldertaps:
                    if dir_right_unsuccessful_shouldertaps == 0:
                        unsuccessful_reps_count_right_shouldertaps += 0.5
                        dir_right_unsuccessful_shouldertaps = 1
            else:
                within_range_time2_shouldertaps = 0
                # Update the start time to the current time
                start_time3_shouldertaps = time.time()

            if 1 <= per_right_shouldertaps <= 10:
                if dir_right_unsuccessful_shouldertaps == 1:
                    unsuccessful_reps_count_right_shouldertaps += 0.5
                    dir_right_unsuccessful_shouldertaps = 0

            if per_right_shouldertaps == success_threshold_shouldertaps:
                if dir_right_shouldertaps == 0:
                    successful_reps_count_right_shouldertaps += 0.5
                    dir_right_shouldertaps = 1
                    cooldown_timer_shouldertaps = cooldown_duration_shouldertaps
            elif per_right_shouldertaps == atrest_value_shouldertaps: 
                if dir_right_shouldertaps == 1:
                    successful_reps_count_right_shouldertaps += 0.5
                    dir_right_shouldertaps = 0
                    cooldown_timer_shouldertaps = cooldown_duration_shouldertaps

            # feedback for left hand  # TO BE FETCHED 
            feedback_left_shouldertaps = detector_shouldertaps.feedback_shouldertaps(per_left_shouldertaps)

            detector_shouldertaps.update_next_per_left(per_left_shouldertaps)

            # feedback for right hand  # TO BE FETCHED 
            feedback_right_shouldertaps = detector_shouldertaps.feedback_shouldertaps(per_right_shouldertaps)

            detector_shouldertaps.update_next_per_left(per_right_shouldertaps)


        cvzone.putTextRect(img, 'Front Shoulder Tap', [370, 30], thickness=2, border=2, scale=2.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color


        #Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time_shouldertaps)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # ARM RIGHT
        cv2.putText(img, f"R {int(per_right_shouldertaps)}%", (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_shouldertaps)), (50, 400), color_right_shouldertaps, -1)

        # ARM LEFT
        cv2.putText(img, f"L {int(per_left_shouldertaps)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_shouldertaps)), (995, 400), color_left_shouldertaps, -1)

    # Counter 
    cv2.rectangle(img, (20, 20), (150, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(successful_reps_count_right_shouldertaps)}/10", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (170, 20), (300, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(successful_reps_count_left_shouldertaps)}/10", (180, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    if remaining_time_shouldertaps <= 0:
        cvzone.putTextRect(img, "Time's Up", [370, 30], thickness=2, border=2, scale=2.5)
        display_info = False

    if successful_reps_count_right_shouldertaps >= 10 and successful_reps_count_left_shouldertaps >= 10:
            cvzone.putTextRect(img, 'All Repetitions Completed', [420, 30], thickness=2, border=2, scale=2.5)
            display_info_shouldertaps = False
            # General feedback after finishing the exercise # TO BE FETCHED
            if dir_gen_feedback_shouldertaps == 0:
                general_feedback_left_shouldertaps = detector_shouldertaps.left_leg_feedback(total_reps_count_left_shouldertaps)
                general_feedback_right_shouldertaps = detector_shouldertaps.right_leg_feedback(total_reps_count_right_shouldertaps)
                dir_gen_feedback_shouldertaps = 1
                print(f"{general_feedback_left_shouldertaps} {general_feedback_right_shouldertaps}")

    if unsuccessful_reps_count_left_shouldertaps >= 3 and unsuccessful_reps_count_right_shouldertaps >= 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for both arms. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_shouldertaps = False

        if dir_gen_feedback_unsuccessful_shouldertaps == 0:
            general_feedback_left_shouldertaps = detector_shouldertaps.left_leg_unsuccessful_feedback(total_reps_count_left_shouldertaps)
            general_feedback_right_shouldertaps = detector_shouldertaps.right_leg_unsuccessful_feedback(total_reps_count_right_shouldertaps)
            dir_gen_feedback_unsuccessful_shouldertaps = 1

    if unsuccessful_reps_count_left_shouldertaps >= 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for left arm. Please retry again', [420, 30], thickness=2, border=2, scale=1)
        display_info_shouldertaps = False

        if dir_gen_feedback_unsuccessful_shouldertaps == 0:
            general_feedback_left_shouldertaps = detector_shouldertaps.left_leg_unsuccessful_feedback(total_reps_count_left_shouldertaps)
            dir_gen_feedback_unsuccessful_shouldertaps = 1

    if unsuccessful_reps_count_right_shouldertaps >= 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for right arm. Please retry again', [420, 30], thickness=2, border=2, scale=1)
        display_info_shouldertaps = False

        if dir_gen_feedback_unsuccessful_shouldertaps == 0:
            general_feedback_right_shouldertaps = detector_shouldertaps.right_leg_unsuccessful_feedback(total_reps_count_right_shouldertaps)
            dir_gen_feedback_unsuccessful_shouldertaps == 1

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()






