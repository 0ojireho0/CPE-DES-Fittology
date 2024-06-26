# import libraries
import math
import cv2
import numpy as np
import time
import bicepcurl_front_PoseModule as pm
import cvzone

cap = cv2.VideoCapture(r'C:\Users\jerem\Downloads\Video\VID_20240511_145612.mp4')

#import class
detector_bicep = pm.poseDetector()

#Initialize Variables
count_bicep_left = 0
count_bicep_right = 0

dir_bicep_left = 0
dir_bicep_right = 0

 # starts time
repetition_time_bicep = 60 # duration time
display_info_bicep = True # display features

bar_left_bicep = 0
bar_right_bicep = 0
per_left_bicep = 0
per_right_bicep = 0
angle_left_bicep = 0
angle_right_bicep = 0

color_right_bicep = (0, 0, 255)
color_left_bicep = (0, 0, 255)

feedback_left_bicep = ""
feedback_right_bicep = ""

min_threshold_bicep = 10
max_threshold_bicep = 90
success_threshold_bicep = 100

peak_value_bicep = 0
atrest_value_bicep = 0
reps_count_bicep = 0

unsuccessful_reps_count_left_bicep = 0
successful_reps_count_left_bicep = 0

unsuccessful_reps_count_right_bicep = 0
successful_reps_count_right_bicep = 0

dir_bicep_left_unsuccessful_bicep = 0
dir_bicep_right_unsuccessful_bicep = 0

total_reps_count_bicep = 0

total_reps_count_left_bicep = 0
total_reps_count_right_bicep = 0

#timer
start_time1_bicep = time.time()
start_time2_bicep = time.time()
start_time3_bicep = time.time()
time_threshold_bicep = 1 # Specify the time threshold in seconds # can be changed for testing but default should be 1, 0.2 is for testing
within_range_time1_bicep = 0
within_range_time2_bicep = 0

# gen feedback success
general_feedback_left_bicep = ""
general_feedback_right_bicep = ""

# gen feedback unsuccess
dir_gen_feedback_bicep = 0
dir_gen_feedback_unsuccessful_bicep = 0

# main loop
while True:
    # reads camera 
    success, img = cap.read()
    # resizes video feed (can be changed depending on requirements of our Raspberry PI and Display Monitor Resolution)
    img = cv2.resize(img, (1280, 720))

    # Timer - starts timer based on set duration
    elapsed_time_bicep = time.time() - start_time1_bicep
    remaining_time_bicep = max(0, repetition_time_bicep - elapsed_time_bicep)


    if display_info_bicep:  # Check if to display counter, bar, and percentage
        img = detector_bicep.findPose(img, False) # initializes img as variable for findpose function
        lmList_bicep = detector_bicep.findPosition(img, False) # initializes lmList_bicep as variable for findPosition function

        # Define hand angles outside the if statement
        if len(lmList_bicep) != 0:

            angle_left_bicep = detector_bicep.BicepCurl(img, 11 ,13, 15, True)
            angle_right_bicep = detector_bicep.BicepCurl(img, 12, 14 ,16, True)

            per_left_bicep = np.interp(angle_left_bicep, (30, 130), (100, 0)) 
            bar_left_bicep = np.interp(angle_left_bicep, (30, 140), (200, 400)) 

            per_right_bicep = np.interp(angle_right_bicep, (200, 340), (0, 100)) 
            bar_right_bicep = np.interp(angle_right_bicep, (200, 340), (400, 200)) 

            # color changer for the bar
            if int(per_left_bicep) == 100:
                color_left_bicep = (0, 255, 0)  # Change color of left leg bar to green
            elif int(per_right_bicep) == 100:
                color_right_bicep = (0, 255, 0)
            else:
                color_left_bicep = (0, 0, 255)  # Keep color of left leg bar as red
                color_right_bicep = (0, 0, 255)

            #left
            if 40 <= per_left_bicep <= 90:
                # Increment the time within range
                within_range_time1 += time.time() - start_time2_bicep

                # Check if peak value has been within range for the specified time
                if within_range_time1 >= time_threshold_bicep:
                    if dir_bicep_left_unsuccessful_bicep == 0:
                        unsuccessful_reps_count_left_bicep += 0.5
                        dir_bicep_left_unsuccessful_bicep = 1

            else:
                within_range_time1 = 0
                # Update the start time to the current time
                start_time2_bicep = time.time()

            if 1 <= per_left_bicep <= 10:
                if dir_bicep_left_unsuccessful_bicep == 1:
                    unsuccessful_reps_count_left_bicep += 0.5
                    dir_bicep_left_unsuccessful_bicep = 0

            if per_left_bicep == success_threshold_bicep:
                if dir_bicep_left == 0:
                    successful_reps_count_left_bicep += 0.5
                    dir_bicep_left = 1
                
            elif per_left_bicep == atrest_value_bicep:
                if dir_bicep_left == 1:
                    successful_reps_count_left_bicep += 0.5
                    dir_bicep_left = 0

            # right
            if 40 <= per_right_bicep <= 90:
                # Increment the time within range
                within_range_time2 += time.time() - start_time3_bicep

                # Check if peak value has been within range for the specified time
                if within_range_time2 >= time_threshold_bicep:
                    if dir_bicep_right_unsuccessful_bicep == 0:
                        unsuccessful_reps_count_right_bicep += 0.5
                        dir_bicep_right_unsuccessful_bicep = 1
                        print("right", unsuccessful_reps_count_right_bicep)

            else:
                within_range_time2 = 0
                # Update the start time to the current time
                start_time3_bicep = time.time()

            if 1 <= per_right_bicep <= 10:
                #print("left down val: ", per_left)
                if dir_bicep_right_unsuccessful_bicep == 1:
                    unsuccessful_reps_count_right_bicep += 0.5
                    dir_bicep_right_unsuccessful_bicep = 0
                    print("right", unsuccessful_reps_count_right_bicep)

            if per_right_bicep == success_threshold_bicep:
                if dir_bicep_right == 0:
                    successful_reps_count_right_bicep += 0.5
                    dir_bicep_right = 1
                
            elif per_right_bicep == atrest_value_bicep:
                if dir_bicep_right == 1:
                    successful_reps_count_right_bicep += 0.5
                    dir_bicep_right = 0

            # feedback for left hand  # TO BE FETCHED 
            feedback_left_bicep = detector_bicep.feedback_bicep(per_left_bicep)

            detector_bicep.update_next_per_left(per_left_bicep)

            # feedback for right hand  # TO BE FETCHED 
            feedback_right_bicep = detector_bicep.feedback_bicep(per_right_bicep)

            detector_bicep.update_next_per_left(per_right_bicep)

        # label
        cvzone.putTextRect(img, 'Front Facing Bicep Curl Tracker', [440, 30], thickness=2, border=2, scale=1.5) 

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time_bicep)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # bar
        cv2.putText(img, f"R {int(per_right_bicep)}%" , (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (255, 255, 255), 5)
        cv2.rectangle(img, (8, int(bar_right_bicep)), (50, 400), color_right_bicep, -1)

        cv2.putText(img, f"L {int(per_left_bicep)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (255, 255, 255), 5)
        cv2.rectangle(img, (952, int(bar_left_bicep)), (995, 400), color_left_bicep, -1)

    #counter in display
    cv2.rectangle(img, (20, 20), (200, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(successful_reps_count_right_bicep)}/10", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (210, 20), (390, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(successful_reps_count_left_bicep)}/10", (220, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    # To check if time is still running
    if remaining_time_bicep <= 0:
        cvzone.putTextRect(img, "Time's Up", [420, 30], thickness=2, border=2, scale=2.5)
        display_info_bicep = False

    #total counts
    total_reps_count_left = successful_reps_count_left_bicep + unsuccessful_reps_count_left_bicep
    total_reps_count_right = successful_reps_count_right_bicep + unsuccessful_reps_count_right_bicep  


    if successful_reps_count_right_bicep >= 10 and successful_reps_count_left_bicep >= 10:
        cvzone.putTextRect(img, 'All Repetitions Completed', [420, 30], thickness=2, border=2, scale=2.5)
        display_info_bicep = False
        # General feedback after finishing the exercise # TO BE FETCHED
        if dir_gen_feedback_bicep == 0:
            general_feedback_left_bicep = detector_bicep.left_arm_feedback(total_reps_count_left)
            general_feedback_right_bicep = detector_bicep.right_arm_feedback(total_reps_count_right)
            dir_gen_feedback_bicep = 1
        
    # To check for unsuccessful arm rep counter # CHANGED
    if unsuccessful_reps_count_left_bicep == 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for left arm. Please retry again', [420, 30], thickness=2, border=2, scale=1)
        display_info_bicep = False

        if dir_gen_feedback_unsuccessful_bicep == 0:
            general_feedback_left_bicep = detector_bicep.left_arm_unsuccessful_feedback(total_reps_count_left)
            dir_gen_feedback_unsuccessful_bicep = 1

    if unsuccessful_reps_count_right_bicep == 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for right arm. Please retry again', [420, 30], thickness=2, border=2, scale=1)
        display_info_bicep = False

        if dir_gen_feedback_unsuccessful_bicep == 0:
            general_feedback_right_bicep = detector_bicep.right_arm_unsuccessful_feedback(total_reps_count_right)
            dir_gen_feedback_unsuccessful_bicep == 1

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
