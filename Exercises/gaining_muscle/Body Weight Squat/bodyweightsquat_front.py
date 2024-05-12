import math
import cv2
import numpy as np
import time
import bodyweightsquat_front_PoseModule as pm
import cvzone

cap = cv2.VideoCapture(r'D:\CPEDES\Flask\Exercises\gaining_muscle\Body Weight Squat\bwscomplete.mp4')
detector_bodyweightsquat = pm.poseDetectorBodyWeightSquat()

dir_left_bodyweightsquat = 0
dir_right_bodyweightsquat = 0

repetition_time_bodyweightsquat = 60  # Repetition time

# Display info
display_info_bodyweightsquat = True

orientation_bodyweightsquat = ""
orientation2_bodyweightsquat = ""

per_right_bodyweightsquat = 0
per_left_bodyweightsquat = 0
bar_left_bodyweightsquat = 0
bar_right_bodyweightsquat = 0 

leftbody_bodyweightsquat = 0
rightbody_bodyweightsquat = 0

color_right_bodyweightsquat = (0, 0, 255)
color_left_bodyweightsquat = (0, 0, 255)

feedback_body_bodyweightsquat = ""

success_threshold_bodyweightsquat = 100

peak_value_bodyweightsquat = 0
atrest_value_bodyweightsquat = 0

unsuccessful_reps_count_body_bodyweightsquat = 0
successful_reps_count_body_bodyweightsquat = 0

dir_left_unsuccessful_bodyweightsquat = 0

total_reps_count_body_bodyweightsquat = 0

start_time1_bodyweightsquat = time.time()
start_time2_bodyweightsquat = time.time()
start_time3_bodyweightsquat = time.time()
time_threshold_bodyweightsquat = 3 # Specify the time threshold in seconds # can be changed for testing but default should be 1, 0.2 is for testing
within_range_time1_bodyweightsquat = 0
within_range_time2_bodyweightsquat = 0

# gen feedback success
general_feedback_body_bodyweightsquat = ""

# gen feedback unsuccess
dir_gen_feedback_bodyweightsquat = 0
dir_gen_feedback_unsuccessful_bodyweightsquat = 0

cooldown_timer_bodyweightsquat = 0
cooldown_duration_bodyweightsquat = 5

while True:
    success, img = cap.read()
    img = cv2.resize(img, (1280, 720))

    elapsed_time_bodyweightsquat = time.time() - start_time1_bodyweightsquat
    remaining_time_bodyweightsquat = max(0, repetition_time_bodyweightsquat - elapsed_time_bodyweightsquat)

    if display_info_bodyweightsquat:  # Check if to display counter, bar, and percentage
        img = detector_bodyweightsquat.findPose(img, False)
        lmList_bodyweightsquat = detector_bodyweightsquat.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_bodyweightsquat) != 0:
            
            leftbody_bodyweightsquat = detector_bodyweightsquat.WeightSquat(img, 12, 24, 26, True)
            rightbody_bodyweightsquat = detector_bodyweightsquat.WeightSquat(img, 11, 23, 25, True)
                     
            per_right_body_bodyweightsquat = np.interp(rightbody_bodyweightsquat, (180, 270), (100, 0))
            bar_right_body_bodyweightsquat = np.interp(rightbody_bodyweightsquat, (180, 270), (200, 400))

            per_left_body_bodyweightsquat = np.interp(leftbody_bodyweightsquat, (180, 270), (100, 0))
            bar_left_body_bodyweightsquat = np.interp(leftbody_bodyweightsquat, (180, 270), (200, 400))

            if int(per_left_body_bodyweightsquat) == 100 and int(per_right_body_bodyweightsquat) == 100:
                color_left_bodyweightsquat = (0, 255, 0)
                color_right_bodyweightsquat = (0, 255, 0)  # Change color of left leg bar to green
            else:
                color_left_bodyweightsquat = (0, 0, 255)
                color_right_bodyweightsquat = (0, 0, 255)

            #body checker for successful and unsuccessful
            if 50 <= per_left_bodyweightsquat <= 90 or 50 <= per_right_body_bodyweightsquat <= 90:
                # Increment the time within range
                within_range_time1_bodyweightsquat += time.time() - start_time2_bodyweightsquat
                #print(within_range_time1_bodyweightsquat)

                # Check if peak value has been within range for the specified time
                if within_range_time1_bodyweightsquat >= time_threshold_bodyweightsquat:
                    if dir_left_unsuccessful_bodyweightsquat == 0:
                        unsuccessful_reps_count_body_bodyweightsquat += 0.5
                        dir_left_unsuccessful_bodyweightsquat = 1
                        #print("UP LEFT: ", unsuccessful_reps_count_body_bodyweightsquat)
            else:
                within_range_time1_bodyweightsquat = 0
                # Update the start time to the current time
                start_time2_bodyweightsquat = time.time()

            if 1 <= per_left_bodyweightsquat <= 10 or 1 <= per_right_body_bodyweightsquat <= 10:
                if dir_left_unsuccessful_bodyweightsquat == 1:
                    unsuccessful_reps_count_body_bodyweightsquat += 0.5
                    dir_left_unsuccessful_bodyweightsquat = 0
                    #print("UP DOWN: ", unsuccessful_reps_count_body_bodyweightsquat)

            if rightbody_bodyweightsquat <= 180 and leftbody_bodyweightsquat <= 180: 
                if dir_left_bodyweightsquat == 0:
                    successful_reps_count_body_bodyweightsquat += 0.5
                    dir_left_bodyweightsquat = 1
            elif rightbody_bodyweightsquat >= 270 and leftbody_bodyweightsquat >= 270:
                if dir_left_bodyweightsquat == 1:
                    successful_reps_count_body_bodyweightsquat += 0.5
                    dir_left_bodyweightsquat = 0

            # feedback for right hand  # TO BE FETCHED 
            feedback_body_bodyweightsquat = detector_bodyweightsquat.feedback_bodyweightsquat(per_right_bodyweightsquat)

            detector_bodyweightsquat.update_next_per_left(per_right_bodyweightsquat)

    
        cvzone.putTextRect(img, 'Front Body Weight Squat Tracker', [420, 30], thickness=2, border=2, scale=1.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time_bodyweightsquat)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # RIGHT LEG
        cv2.putText(img, f"R {int(per_right_body_bodyweightsquat)}%", (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_body_bodyweightsquat)), (50, 400), color_right_bodyweightsquat, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_left_body_bodyweightsquat)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_body_bodyweightsquat)), (995, 400), color_left_bodyweightsquat, -1)

    cv2.rectangle(img, (20, 10), (140, 120), (255, 0, 0), -1)
    cv2.putText(img, f"{int(successful_reps_count_body_bodyweightsquat)}/5", (30, 80), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    if remaining_time_bodyweightsquat <= 0:
        cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
        display_info_bodyweightsquat = False

    total_reps_count_body_bodyweightsquat = successful_reps_count_body_bodyweightsquat + unsuccessful_reps_count_body_bodyweightsquat

    if successful_reps_count_body_bodyweightsquat >= 10:
        cvzone.putTextRect(img, 'All Repetitions Completed', [420, 30], thickness=2, border=2, scale=2.5)
        display_info_bodyweightsquat = False
        # General feedback after finishing the exercise # TO BE FETCHED
        if dir_gen_feedback_bodyweightsquat == 0:
            general_feedback_left_bodyweightsquat = detector_bodyweightsquat.body_feedback(total_reps_count_body_bodyweightsquat)
            print(general_feedback_left_bodyweightsquat)
            dir_gen_feedback_bodyweightsquat = 1
        
    if unsuccessful_reps_count_body_bodyweightsquat >= 2:
        cvzone.putTextRect(img, 'You have made 2 unsuccessful tries. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_bodyweightsquat = False

        if dir_gen_feedback_unsuccessful_bodyweightsquat == 0:
            general_feedback_left_bodyweightsquat = detector_bodyweightsquat.body_unsuccessful_feedback(total_reps_count_body_bodyweightsquat)
            dir_gen_feedback_unsuccessful_bodyweightsquat = 1


    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



