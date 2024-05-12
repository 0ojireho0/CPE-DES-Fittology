# UNFINISHED LEFT AND RIGHT

import math
import cv2
import numpy as np
import time
import alternating_leg_lunge_front_PoseModule as pm
import cvzone

cap = cv2.VideoCapture(r'D:\CPEDES\Flask\Exercises\gaining_muscle\Alternating Leg Lunge\alternatinglungecomplete.mp4')

detector_leglunge = pm.poseDetectoralternatinglunge()

dir_left_leglunge = 0
dir_right_leglunge = 0

repetition_time_leglunge = 60  # Repetition time

# Display info
display_info_leglunge = True

orientation_leglunge = ""
orientation2_leglunge = ""

per_right_leglunge = 0
per_left_leglunge = 0
bar_left_leglunge = 0
bar_right_leglunge = 0 

leftangle_leglunge = 0
rightangle_leglunge = 0

color_right_leglunge = (0, 0, 255)
color_left_leglunge = (0, 0, 255)

feedback_left_leglunge = ""
feedback_right_leglunge = ""

success_threshold_leglunge = 100

peak_value_leglunge = 0
atrest_value_leglunge = 0

unsuccessful_reps_count_left_leglunge = 0
successful_reps_count_left_leglunge = 0

unsuccessful_reps_count_right_leglunge = 0
successful_reps_count_right_leglunge = 0

dir_left_unsuccessful_leglunge = 0
dir_right_unsuccessful_leglunge = 0

total_reps_count_leglunge = 0

total_reps_count_left_leglunge = 0
total_reps_count_right_leglunge = 0

start_time1_leglunge = time.time()
start_time2_leglunge = time.time()
start_time3_leglunge = time.time()
time_threshold_leglunge = 10 # Specify the time threshold in seconds # can be changed for testing but default should be 1, 0.2 is for testing
within_range_time1_leglunge = 0
within_range_time2_leglunge = 0

# gen feedback success
general_feedback_left_leglunge = ""
general_feedback_right_leglunge = ""

# gen feedback unsuccess
dir_gen_feedback_leglunge = 0
dir_gen_feedback_unsuccessful_leglunge = 0

cooldown_timer_leglunge = 0
cooldown_duration_leglunge = 5

while True:
    success, img = cap.read()
    img = cv2.resize(img, (1280, 720))

    elapsed_time_leglunge = time.time() - start_time1_leglunge
    remaining_time_leglunge = max(0, repetition_time_leglunge - elapsed_time_leglunge)

    if display_info_leglunge:  # Check if to display counter, bar, and percentage
        img = detector_leglunge.findPose(img, False)
        lmList_leglunge = detector_leglunge.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_leglunge) != 0:

            # Right and Left keypoints
            rightleg_leglunge = detector_leglunge.AlternatingLunge(img, 24, 26, 28, True)
            leftleg_leglunge = detector_leglunge.AlternatingLunge(img, 23, 25, 27, True)

            if cooldown_timer_leglunge > 0:
                cooldown_timer_leglunge -= 1

            per_right_leglunge = np.interp(rightleg_leglunge, (150, 200), (100, 0))
            bar_right_leglunge = np.interp(rightleg_leglunge, (150, 200), (480, 680))

            per_left_leglunge = np.interp(leftleg_leglunge, (150, 200), (100, 0))
            bar_left_leglunge = np.interp(leftleg_leglunge, (150, 200), (480, 680))

            if int(per_left_leglunge) == 100:
                color_left_leglunge = (0, 255, 0)  # Change color of left leg bar to green
            else:
                color_left_leglunge = (0, 0, 255)
            
            if int(per_right_leglunge) == 100:
                color_right_leglunge = (0, 255, 0)
            else:
                color_right_leglunge = (0, 0, 255)

            #left
            if 40 <= per_left_leglunge <= 90:
                # Increment the time within range
                within_range_time1_leglunge += time.time() - start_time2_leglunge

                # Check if peak value has been within range for the specified time
                if within_range_time1_leglunge >= time_threshold_leglunge:
                    if dir_left_unsuccessful_leglunge == 0:
                        unsuccessful_reps_count_left_leglunge += 0.5
                        dir_left_unsuccessful_leglunge = 1
                        print("UP LEFT: ", unsuccessful_reps_count_left_leglunge)


            else:
                within_range_time1_leglunge = 0
                # Update the start time to the current time
                start_time2_leglunge = time.time()

            if 1 <= per_left_leglunge <= 10:
                if dir_left_unsuccessful_leglunge == 1:
                    unsuccessful_reps_count_left_leglunge += 0.5
                    dir_left_unsuccessful_leglunge = 0
                    print("UP DOWN: ", unsuccessful_reps_count_left_leglunge)


            if rightleg_leglunge <= 100 and leftleg_leglunge <= 150:
                if dir_left_leglunge == 0:
                    successful_reps_count_left_leglunge += 0.5
                    dir_left_leglunge = 1
                    cooldown_timer_leglunge = cooldown_duration_leglunge
            else:
                if dir_left_leglunge == 1:
                    successful_reps_count_left_leglunge += 0.5
                    dir_left_leglunge = 0
                    cooldown_timer_leglunge = cooldown_duration_leglunge
    
            # right
            if 40 <= per_right_leglunge <= 90:
                # Increment the time within range
                within_range_time2_leglunge += time.time() - start_time3_leglunge

                # Check if peak value has been within range for the specified time
                if within_range_time2_leglunge >= time_threshold_leglunge:
                    if dir_right_unsuccessful_leglunge == 0:
                        unsuccessful_reps_count_right_leglunge += 0.5
                        dir_right_unsuccessful_leglunge = 1
                        print("right UP", unsuccessful_reps_count_right_leglunge)
            else:
                within_range_time2_leglunge = 0
                # Update the start time to the current time
                start_time3_leglunge = time.time()

            if 1 <= per_right_leglunge <= 10:
                #print("left down val: ", per_left)
                if dir_right_unsuccessful_leglunge == 1:
                    unsuccessful_reps_count_right_leglunge += 0.5
                    dir_right_unsuccessful_leglunge = 0
                    print("right DOWN", unsuccessful_reps_count_right_leglunge)

            if rightleg_leglunge <= 150 and leftleg_leglunge <= 100:
                if dir_right_leglunge == 0:
                    successful_reps_count_right_leglunge += 0.5
                    dir_right_leglunge = 1
                    cooldown_timer_leglunge = cooldown_duration_leglunge
            else: 
                if dir_right_leglunge == 1:
                    successful_reps_count_right_leglunge += 0.5
                    dir_right_leglunge = 0
                    cooldown_timer_leglunge = cooldown_duration_leglunge

            # feedback for left hand  # TO BE FETCHED 
            feedback_left_leglunge = detector_leglunge.feedback_leglunge(per_left_leglunge)

            detector_leglunge.update_next_per_left(per_left_leglunge)

            # feedback for right hand  # TO BE FETCHED 
            feedback_right_leglunge = detector_leglunge.feedback_leglunge(per_right_leglunge)

            detector_leglunge.update_next_per_left(per_right_leglunge)

        cvzone.putTextRect(img, 'Leg Lunge Front', [345, 30], thickness=2, border=2, scale=2.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time_leglunge)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # RIGHT LEG
        cv2.putText(img, f"R {int(per_right_leglunge)}%", (24, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 480), (50, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_leglunge)), (50, 680), color_right_leglunge, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_left_leglunge)}%", (962, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 480), (995, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_leglunge)), (995, 680), color_left_leglunge, -1)

    # Counter 
    cv2.rectangle(img, (20, 20), (140, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(successful_reps_count_right_leglunge)}/5", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (150, 20), (270, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(successful_reps_count_left_leglunge)}/5", (160, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    # Timer
    if remaining_time_leglunge <= 0:
        cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
        display_info_leglunge = False

    total_reps_count_left_leglunge = successful_reps_count_left_leglunge + unsuccessful_reps_count_left_leglunge
    total_reps_count_right_leglunge = successful_reps_count_right_leglunge + unsuccessful_reps_count_right_leglunge  


    if successful_reps_count_right_leglunge >= 6 and successful_reps_count_left_leglunge >= 6:
        cvzone.putTextRect(img, 'All Repetitions Completed', [420, 30], thickness=2, border=2, scale=2.5)
        display_info_leglunge = False
        # General feedback after finishing the exercise # TO BE FETCHED
        if dir_gen_feedback_leglunge == 0:
            general_feedback_left_leglunge = detector_leglunge.left_leg_feedback(total_reps_count_left_leglunge)
            general_feedback_right_leglunge = detector_leglunge.right_leg_feedback(total_reps_count_right_leglunge)
            dir_gen_feedback_leglunge = 1
        

    if unsuccessful_reps_count_left_leglunge >= 2:
        cvzone.putTextRect(img, 'You have made 2 unsuccessful tries for left leg. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_leglunge = False

        if dir_gen_feedback_unsuccessful_leglunge == 0:
            general_feedback_left_leglunge = detector_leglunge.left_leg_unsuccessful_feedback(total_reps_count_left_leglunge)
            dir_gen_feedback_unsuccessful_leglunge = 1

    if unsuccessful_reps_count_right_leglunge >= 2:
        cvzone.putTextRect(img, 'You have made 2 unsuccessful tries for right leg. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_leglunge = False

        if dir_gen_feedback_unsuccessful_leglunge == 0:
            general_feedback_right_leglunge = detector_leglunge.right_leg_unsuccessful_feedback(total_reps_count_right_leglunge)
            dir_gen_feedback_unsuccessful_leglunge == 1



    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()



