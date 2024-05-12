# import libraries
import math
import cv2
import numpy as np
import time
import chestpress_front_PoseModule as pm
import cvzone


#Camera
cap = cv2.VideoCapture(r'D:\CPEDES\Flask\Exercises\gaining_muscle\Chest Press\chestpressvid.mp4')

detector_chestpress = pm.poseDetector()

dir_left_chestpress = 0
dir_right_chestpress = 0

repetition_time_chestpress = 60  # Repetition time

# Display info
display_info_chestpress = True

orientation_chestpress = ""
orientation2_chestpress = ""

per_right_chestpress = 0
per_left_chestpress = 0
bar_left_chestpress = 0
bar_right_chestpress = 0 


color_right_chestpress = (0, 0, 255)
color_left_chestpress = (0, 0, 255)

feedback_left_chestpress = ""
feedback_right_chestpress = ""

success_threshold_chestpress = 100

atrest_value_chestpress = 0

unsuccessful_reps_count_left_chestpress = 0
successful_reps_count_left_chestpress = 0

unsuccessful_reps_count_right_chestpress = 0
successful_reps_count_right_chestpress = 0

dir_left_unsuccessful_chestpress = 0
dir_right_unsuccessful_chestpress = 0

total_reps_count_chestpress = 0

total_reps_count_left_chestpress = 0
total_reps_count_right_chestpress = 0

start_time1_chestpress = time.time()
start_time2_chestpress = time.time()
start_time3_chestpress = time.time()
time_threshold_chestpress = 10 # Specify the time threshold in seconds # can be changed for testing but default should be 1, 0.2 is for testing
within_range_time1_chestpress = 0
within_range_time2_chestpress = 0

# gen feedback success
general_feedback_left_chestpress = ""
general_feedback_right_chestpress = ""

# gen feedback unsuccess
dir_gen_feedback_chestpress = 0
dir_gen_feedback_unsuccessful_chestpress = 0

cooldown_timer_chestpress = 0
cooldown_duration_chestpress = 5

angle_left_chestpress = 0
angle_right_chestpress = 0


# main loop
while True:
    # reads camera 
    success, img = cap.read()
    # resizes video feed (can be changed depending on requirements of our Raspberry PI and Display Monitor Resolution)
    img = cv2.resize(img, (1280, 720))

    # Timer - starts timer based on set duration
    elapsed_time_chestpress = time.time() - start_time1_chestpress
    remaining_time_chestpress = max(0, repetition_time_chestpress - elapsed_time_chestpress)


    if display_info_chestpress:  # Check if to display counter, bar, and percentage
        img = detector_chestpress.findPose(img, False) # initializes img as variable for findpose function
        lmList_chestpress = detector_chestpress.findPosition(img, False) # initializes lmList_bicep as variable for findPosition function

        # Define hand angles outside the if statement
        if len(lmList_chestpress) != 0:
            angle_left_chestpress = detector_chestpress.findAngle(img, 11, 13, 15)
            angle_right_chestpress = detector_chestpress.findAngle(img, 12, 14, 16) # defines right arm landmark keypoints
            # (refer to mediapipe landmark mapping for number equivalent)

            per_left_chestpress = np.interp(angle_left_chestpress, (60, 200), (0, 100)) # first parenthesis, the value threshold of the angle. Second, represents the interp value
            bar_left_chestpress = np.interp(angle_left_chestpress, (60, 200), (400, 200)) # 

            per_right_chestpress = np.interp(angle_right_chestpress, (150, 300), (100, 0)) # 
            bar_right_chestpress = np.interp(angle_right_chestpress, (150, 300), (200, 400)) # 


            if int(per_left_chestpress) == 100:
                color_left_chestpress = (0, 255, 0)  # Change color of left leg bar to green
            else:
                color_left_chestpress = (0, 0, 255)
            
            if int(per_right_chestpress) == 100:
                color_right_chestpress = (0, 255, 0)
            else:
                color_right_chestpress = (0, 0, 255)

            #left
            if 40 <= per_left_chestpress <= 90:
                # Increment the time within range
                within_range_time1_chestpress += time.time() - start_time2_chestpress

                # Check if peak value has been within range for the specified time
                if within_range_time1_chestpress >= time_threshold_chestpress:
                    if dir_left_unsuccessful_chestpress == 0:
                        unsuccessful_reps_count_left_chestpress += 0.5
                        dir_left_unsuccessful_chestpress = 1
                        print("UP WRONG LEFT: ", unsuccessful_reps_count_left_chestpress)

            else:
                within_range_time1_chestpress = 0
                # Update the start time to the current time
                start_time2_chestpress = time.time()

            if 1 <= per_left_chestpress <= 10:
                if dir_left_unsuccessful_chestpress == 1:
                    unsuccessful_reps_count_left_chestpress += 0.5
                    dir_left_unsuccessful_chestpress = 0
                    print("DOWN WRONG LEFT: ", unsuccessful_reps_count_left_chestpress)

            if per_left_chestpress == success_threshold_chestpress:
                if dir_left_chestpress == 0:
                    successful_reps_count_left_chestpress += 0.5
                    dir_left_chestpress = 1

            elif per_left_chestpress == atrest_value_chestpress:
                if dir_left_chestpress == 1:
                    successful_reps_count_left_chestpress += 0.5
                    dir_left_chestpress = 0

            # right
            if 40 <= per_right_chestpress <= 90:
                # Increment the time within range
                within_range_time2_chestpress += time.time() - start_time3_chestpress

                # Check if peak value has been within range for the specified time
                if within_range_time2_chestpress >= time_threshold_chestpress:
                    if dir_right_unsuccessful_chestpress == 0:
                        unsuccessful_reps_count_right_chestpress += 0.5
                        dir_right_unsuccessful_chestpress = 1
                        print("UP RIGHT WRONG", unsuccessful_reps_count_right_chestpress)
            else:
                within_range_time2_chestpress = 0
                # Update the start time to the current time
                start_time3_chestpress = time.time()

            if 1 <= per_right_chestpress <= 10:
                #print("left down val: ", per_left)
                if dir_right_unsuccessful_chestpress == 1:
                    unsuccessful_reps_count_right_chestpress += 0.5
                    dir_right_unsuccessful_chestpress = 0
                    print("DOWN RIGHT WRONG", unsuccessful_reps_count_right_chestpress)

            if per_right_chestpress == success_threshold_chestpress:
                if dir_right_chestpress == 0:
                    successful_reps_count_right_chestpress += 0.5
                    dir_right_chestpress = 1
                    cooldown_timer_chestpress = cooldown_duration_chestpress
            elif per_right_chestpress == atrest_value_chestpress: 
                if dir_right_chestpress == 1:
                    successful_reps_count_right_chestpress += 0.5
                    dir_right_chestpress = 0
                    cooldown_timer_chestpress = cooldown_duration_chestpress

            # feedback for left hand  # TO BE FETCHED 
            feedback_left_chestpress = detector_chestpress.feedback_chestpress(per_left_chestpress)

            detector_chestpress.update_next_per_left(per_left_chestpress)

            # feedback for right hand  # TO BE FETCHED 
            feedback_right_chestpress = detector_chestpress.feedback_chestpress(per_right_chestpress)

            detector_chestpress.update_next_per_left(per_right_chestpress)

        # label
        cvzone.putTextRect(img, 'Chest Press Tracker', [345, 30], thickness=2, border=2, scale=2.5) 

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time_chestpress)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # bar
        cv2.putText(img, f"R {int(per_right_chestpress)}%" , (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_chestpress)), (50, 400), color_right_chestpress, -1)

        cv2.putText(img, f"L {int(per_left_chestpress)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_chestpress)), (995, 400), color_left_chestpress, -1)

    #count
    cv2.rectangle(img, (20, 20), (140, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(successful_reps_count_right_chestpress)}/5", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (150, 20), (270, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(successful_reps_count_left_chestpress)}/5", (160, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255 ,255), 7)

    if remaining_time_chestpress <= 0:
        cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
        display_info_chestpress = False

    if successful_reps_count_right_chestpress >= 5 and successful_reps_count_left_chestpress >= 5:
        cvzone.putTextRect(img, 'All Repetitions Completed', [420, 30], thickness=2, border=2, scale=2.5)
        display_info_chestpress = False
        # General feedback after finishing the exercise # TO BE FETCHED
        if dir_gen_feedback_chestpress == 0:
            general_feedback_left_chestpress = detector_chestpress.left_arm_feedback(total_reps_count_left_chestpress)
            general_feedback_right_chestpress = detector_chestpress.right_arm_feedback(total_reps_count_right_chestpress)
            dir_gen_feedback_chestpress = 1
            print(f"{general_feedback_left_chestpress} {general_feedback_right_chestpress}")


    if unsuccessful_reps_count_left_chestpress >= 2 and unsuccessful_reps_count_right_chestpress >= 2:
        cvzone.putTextRect(img, 'You have made 2 unsuccessful tries for both arms. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_chestpress = False

        if dir_gen_feedback_unsuccessful_chestpress == 0:
            general_feedback_left_chestpress = detector_chestpress.left_arm_unsuccessful_feedback(total_reps_count_left_chestpress)
            general_feedback_right_chestpress = detector_chestpress.right_arm_unsuccessful_feedback(total_reps_count_right_chestpress)
            dir_gen_feedback_unsuccessful_chestpress = 1
    
    
    if unsuccessful_reps_count_left_chestpress >= 2:
        cvzone.putTextRect(img, 'You have made 2 unsuccessful tries for left arm. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_chestpress = False

        if dir_gen_feedback_unsuccessful_chestpress == 0:
            general_feedback_left_chestpress = detector_chestpress.left_arm_unsuccessful_feedback(total_reps_count_left_chestpress)
            dir_gen_feedback_unsuccessful_chestpress = 1

    if unsuccessful_reps_count_right_chestpress >= 2:
        cvzone.putTextRect(img, 'You have made 2 unsuccessful tries for right arm. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_chestpress = False

        if dir_gen_feedback_unsuccessful_chestpress == 0:
            general_feedback_right_chestpress = detector_chestpress.right_arm_unsuccessful_feedback(total_reps_count_right_chestpress)
            dir_gen_feedback_unsuccessful_chestpress == 1


    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
