 # import libraries
import math
import cv2
import numpy as np
import time
import pushup_front_PoseModule as pm
import cvzone

#Camera
cap = cv2.VideoCapture(r'D:\CPEDES\Flask\Exercises\gaining_muscle\push-up\pushup2.mp4')

# Import class
detector_pushup = pm.poseDetectorPushUp()

# Initialize variables
count_left_pushup = 0  # Count of reps # changed
count_right_pushup = 0

dir_left_pushup = 0
dir_left_pushup = 0

dir_right_pushup = 0
dir_right_pushup = 0


repetition_time_pushup = 60  # Repetition time

# Display info
display_info_pushup = True

per_right_pushup = 0
per_left_pushup = 0
bar_left_pushup = 0
bar_right_pushup = 0 

leftangle_pushup = 0
rightangle_pushup = 0

color_right_pushup = (0, 0, 255)
color_left_pushup = (0, 0, 255)

feedback_left_pushup = ""
feedback_right_pushup = ""

success_threshold_pushup = 100

peak_value_pushup = 0
atrest_value_pushup = 0

unsuccessful_reps_count_left_pushup = 0
successful_reps_count_left_pushup = 0

unsuccessful_reps_count_right_pushup = 0
successful_reps_count_right_pushup = 0

dir_left_unsuccessful_pushup = 0
dir_right_unsuccessful_pushup = 0

total_reps_count_pushup = 0

total_reps_count_left_pushup = 0
total_reps_count_right_pushup = 0
start_time1_pushup = time.time()
start_time2_pushup = time.time()
start_time3_pushup = time.time()
time_threshold_pushup = 3 
within_range_time1_pushup = 0
within_range_time2_pushup = 0

# gen feedback success
general_feedback_left_pushup = ""
general_feedback_right_pushup = ""

# gen feedback unsuccess
dir_gen_feedback_pushup = 0
dir_gen_feedback_unsuccessful_pushup = 0

#main loop
while True:
    success, img = cap.read()
    img = cv2.resize(img, (1280, 720))

    elapsed_time_pushup = time.time() - start_time1_pushup
    remaining_time_pushup = max(0, repetition_time_pushup - elapsed_time_pushup)

    if display_info_pushup:  # Check if to display counter, bar, and percentage

        img = detector_pushup.findPose(img, False) # initializes img as variable for findpose function
        lmList = detector_pushup.findPosition(img, False) # initializes lmList_pushup as variable for findPosition function

        # Define hand angles outside the if statement
        if len(lmList) != 0:
            # Check if the person is in a proper push-up posture
            leftangle_pushup, rightangle_pushup = detector_pushup.findPushupAngle(img, 11, 13, 15, 12, 14, 16, drawpoints=True)  # defines left  and right arm landmark keypoints 

            #Interpolate angles to percentage and position on screen
            per_left_pushup = np.interp(leftangle_pushup, (190, 300), (100, 0)) # first parenthesis, the value threshold of the angle. Second, represents the interp value
            bar_left_pushup = np.interp(leftangle_pushup, (190, 300), (200, 400))

            per_right_pushup = np.interp(rightangle_pushup, (45, 160), (0, 100))
            bar_right_pushup = np.interp(rightangle_pushup, (45, 160), (400, 200))

            if detector_pushup.isPushUpPosture(lmList):
                if int(per_left_pushup) == 100:
                    color_left_pushup = (0, 255, 0)  # Change color of left leg bar to green
                else:
                    color_left_pushup = (0, 0, 255)
                
                if int(per_right_pushup) == 100:
                    color_right_pushup = (0, 255, 0)
                else:
                    color_right_pushup = (0, 0, 255)

                #left
                if 40 <= per_left_pushup <= 90:
                    # Increment the time within range
                    within_range_time1_pushup += time.time() - start_time2_pushup

                    # Check if peak value has been within range for the specified time
                    if within_range_time1_pushup >= time_threshold_pushup:
                        if dir_left_unsuccessful_pushup == 0:
                            unsuccessful_reps_count_left_pushup += 0.5
                            print("left", unsuccessful_reps_count_right_pushup)
                            dir_left_unsuccessful_pushup = 1

                else:
                    within_range_time1_pushup = 0
                    # Update the start time to the current time
                    start_time2_pushup = time.time()

                if 1 <= per_left_pushup <= 10:
                    if dir_left_unsuccessful_pushup == 1:
                        unsuccessful_reps_count_left_pushup += 0.5
                        print("left", unsuccessful_reps_count_right_pushup)
                        dir_left_unsuccessful_pushup = 0

                if per_left_pushup == success_threshold_pushup:
                    if dir_left_pushup == 0:
                        successful_reps_count_left_pushup += 0.5
                        dir_left_pushup = 1
                    
                elif per_left_pushup == atrest_value_pushup:
                    if dir_left_pushup == 1:
                        successful_reps_count_left_pushup += 0.5
                        dir_left_pushup = 0

                # right
                if 40 <= per_right_pushup <= 90:
                    # Increment the time within range
                    within_range_time2_pushup += time.time() - start_time3_pushup

                    # Check if peak value has been within range for the specified time
                    if within_range_time2_pushup >= time_threshold_pushup:
                        if dir_right_unsuccessful_pushup == 0:
                            unsuccessful_reps_count_right_pushup += 0.5
                            dir_right_unsuccessful_pushup = 1
                            print("right", unsuccessful_reps_count_right_pushup)

                else:
                    within_range_time2_pushup = 0
                    # Update the start time to the current time
                    start_time3_pushup = time.time()

                if 1 <= per_right_pushup <= 10:
                    #print("left down val: ", per_left)
                    if dir_right_unsuccessful_pushup == 1:
                        unsuccessful_reps_count_right_pushup += 0.5
                        dir_right_unsuccessful_pushup = 0
                        print("right", unsuccessful_reps_count_right_pushup)

                if per_right_pushup == success_threshold_pushup:
                    if dir_right_pushup == 0:
                        successful_reps_count_right_pushup += 0.5
                        dir_right_pushup = 1
                    
                elif per_right_pushup == atrest_value_pushup:
                    if dir_right_pushup == 1:
                        successful_reps_count_right_pushup += 0.5
                        dir_right_pushup = 0

                # feedback for left hand  # TO BE FETCHED 
                feedback_left_pushup = detector_pushup.feedback_pushup(per_left_pushup)

                detector_pushup.update_next_per_left(per_left_pushup)

                # feedback for right hand  # TO BE FETCHED 
                feedback_right_pushup = detector_pushup.feedback_pushup(per_right_pushup)

                detector_pushup.update_next_per_left(per_right_pushup)

        cvzone.putTextRect(img, 'Front Facing Push-Up', [430, 30], thickness=2, border=2, scale=1.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time_pushup)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # Draw bars for left and right angles
        cv2.putText(img, f"R {int(per_right_pushup)}%", (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_pushup)), (50, 400), color_right_pushup, -1)

        cv2.putText(img, f"L {int(per_left_pushup)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_pushup)), (995, 400), color_left_pushup, -1)

    cv2.rectangle(img, (20, 20), (200, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(successful_reps_count_right_pushup)}/5", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (210, 20), (390, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(successful_reps_count_left_pushup)}/5", (220, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    if remaining_time_pushup <= 0:
        cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
        display_info_pushup = False


    total_reps_count_left_pushup = successful_reps_count_left_pushup + unsuccessful_reps_count_left_pushup
    total_reps_count_right_pushup = successful_reps_count_right_pushup + unsuccessful_reps_count_right_pushup  

    if successful_reps_count_right_pushup >= 10 and successful_reps_count_left_pushup >= 10:
        cvzone.putTextRect(img, 'All Repetitions Completed', [420, 30], thickness=2, border=2, scale=2.5)
        display_info_pushup = False
        # General feedback after finishing the exercise # TO BE FETCHED
        if dir_gen_feedback_pushup == 0:
            general_feedback_left_pushup = detector_pushup.left_arm_feedback(total_reps_count_left_pushup)
            general_feedback_right_pushup = detector_pushup.right_arm_feedback(total_reps_count_right_pushup)
            dir_gen_feedback_pushup = 1
            print(f"{general_feedback_left_pushup} {general_feedback_right_pushup}")
        
    # To check for unsuccessful arm rep counter # CHANGED
    if unsuccessful_reps_count_left_pushup >= 3 and unsuccessful_reps_count_right_pushup >= 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for both arms. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_pushup = False

        if dir_gen_feedback_unsuccessful_pushup == 0:
            general_feedback_left_pushup = detector_pushup.left_arm_unsuccessful_feedback(total_reps_count_left_pushup)
            dir_gen_feedback_unsuccessful_pushup = 1

    elif unsuccessful_reps_count_left_pushup >= 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for left arm. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_pushup = False

        if dir_gen_feedback_unsuccessful_pushup == 0:
            general_feedback_left_pushup = detector_pushup.left_arm_unsuccessful_feedback(total_reps_count_left_pushup)
            dir_gen_feedback_unsuccessful_pushup = 1

    elif unsuccessful_reps_count_right_pushup >= 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for right arm. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_pushup = False

        if dir_gen_feedback_unsuccessful_pushup == 0:
            general_feedback_right_pushup = detector_pushup.right_arm_unsuccessful_feedback(total_reps_count_right_pushup)
            dir_gen_feedback_unsuccessful_pushup == 1



   
    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


