import math
import cv2
import numpy as np
import time
import dumbbellhiphinge_front_PoseModule as pm  # Assuming you have a PoseModule for hip hinge
import cvzone

# Load video
# r'C:\Users\RID\Desktop\pose_estimation\aipose2\Exercise\gainingmuscle\hiphinge.mp4'
cap = cv2.VideoCapture(r'D:\CPEDES\Flask\Exercises\gaining_muscle\Dumbbell Hip Hinge\dumbbellhiphinge.mp4')

# Initialize pose detector
detector_dumbbellhiphinge = pm.poseDetectordumbbellhiphinge()

dir_left_dumbbellhiphinge = 0
dir_right_dumbbellhiphinge = 0

repetition_time_dumbbellhiphinge = 60  # Repetition time

# Display info
display_info_dumbbellhiphinge = True

orientation_dumbbellhiphinge = ""
orientation2_dumbbellhiphinge = ""

per_right_dumbbellhiphinge = 0
per_left_dumbbellhiphinge = 0
bar_left_dumbbellhiphinge = 0
bar_right_dumbbellhiphinge = 0 


color_right_dumbbellhiphinge = (0, 0, 255)
color_left_dumbbellhiphinge = (0, 0, 255)

feedback_left_dumbbellhiphinge = ""
feedback_right_dumbbellhiphinge = ""

success_threshold_dumbbellhiphinge = 100

atrest_value_dumbbellhiphinge = 0

unsuccessful_reps_count_left_dumbbellhiphinge = 0
successful_reps_count_left_dumbbellhiphinge = 0

unsuccessful_reps_count_right_dumbbellhiphinge = 0
successful_reps_count_right_dumbbellhiphinge = 0

dir_left_unsuccessful_dumbbellhiphinge = 0
dir_right_unsuccessful_dumbbellhiphinge = 0

total_reps_count_dumbbellhiphinge = 0

total_reps_count_left_dumbbellhiphinge = 0
total_reps_count_right_dumbbellhiphinge = 0

start_time1_dumbbellhiphinge = time.time()
start_time2_dumbbellhiphinge = time.time()
start_time3_dumbbellhiphinge = time.time()
time_threshold_dumbbellhiphinge = 10 # Specify the time threshold in seconds # can be changed for testing but default should be 1, 0.2 is for testing
within_range_time1_dumbbellhiphinge = 0
within_range_time2_dumbbellhiphinge = 0

# gen feedback success
general_feedback_left_dumbbellhiphinge = ""
general_feedback_right_dumbbellhiphinge = ""

# gen feedback unsuccess
dir_gen_feedback_dumbbellhiphinge = 0
dir_gen_feedback_unsuccessful_dumbbellhiphinge = 0

cooldown_timer_dumbbellhiphinge = 0
cooldown_duration_dumbbellhiphinge = 5

leftbody_dumbbellhiphinge = 0
rightbody_dumbbellhiphinge = 0

while True:
    success, img = cap.read()
    if not success:
        break
    img = cv2.resize(img, (1280, 720))
    #img = cv2.cvtColor(cv2.flip(img, 1), cv2.COLOR_BGR2RGB)

    elapsed_time_dumbbellhiphinge = time.time() - start_time1_dumbbellhiphinge
    remaining_time_dumbbellhiphinge = max(0, repetition_time_dumbbellhiphinge - elapsed_time_dumbbellhiphinge)

    if display_info_dumbbellhiphinge:
        img = detector_dumbbellhiphinge.findPose(img, False)
        lmList_hip_hinge = detector_dumbbellhiphinge.findPosition(img, False)

        if len(lmList_hip_hinge) != 0:
            leftbody_dumbbellhiphinge = detector_dumbbellhiphinge.HipHinge(img, 11, 23, 25, True)
            rightbody_dumbbellhiphinge  = detector_dumbbellhiphinge.HipHinge(img, 12, 24, 26, True)

            if leftbody_dumbbellhiphinge is not None and rightbody_dumbbellhiphinge is not None:
                per_left_dumbbellhiphinge = np.interp(int(leftbody_dumbbellhiphinge), (90, 240), (100, 0))
                bar_left_dumbbellhiphinge = np.interp(int(leftbody_dumbbellhiphinge), (90, 240), (200, 400))

                per_right_dumbbellhiphinge = np.interp(int(rightbody_dumbbellhiphinge), (90, 240), (100, 0))
                bar_right_dumbbellhiphinge= np.interp(int(rightbody_dumbbellhiphinge), (90, 240), (200, 400))

            if int(per_left_dumbbellhiphinge) == 100:
                color_left_dumbbellhiphinge = (0, 255, 0)  # Change color of left leg bar to green
            else:
                color_left_dumbbellhiphinge = (0, 0, 255)
            
            if int(per_right_dumbbellhiphinge) == 100:
                color_right_dumbbellhiphinge = (0, 255, 0)
            else:
                color_right_dumbbellhiphinge = (0, 0, 255)

            #left
            if 40 <= per_left_dumbbellhiphinge <= 90:
                # Increment the time within range
                within_range_time1_dumbbellhiphinge += time.time() - start_time2_dumbbellhiphinge

                # Check if peak value has been within range for the specified time
                if within_range_time1_dumbbellhiphinge >= time_threshold_dumbbellhiphinge:
                    if dir_left_unsuccessful_dumbbellhiphinge == 0:
                        unsuccessful_reps_count_left_dumbbellhiphinge += 0.5
                        dir_left_unsuccessful_dumbbellhiphinge = 1
            else:
                within_range_time1_dumbbellhiphinge = 0
                # Update the start time to the current time
                start_time2_dumbbellhiphinge = time.time()

            if 1 <= per_left_dumbbellhiphinge <= 10:
                if dir_left_unsuccessful_dumbbellhiphinge == 1:
                    unsuccessful_reps_count_left_dumbbellhiphinge += 0.5
                    dir_left_unsuccessful_dumbbellhiphinge = 0

            if per_left_dumbbellhiphinge == success_threshold_dumbbellhiphinge:
                if dir_left_dumbbellhiphinge == 0:
                    successful_reps_count_left_dumbbellhiphinge += 0.5
                    dir_left_dumbbellhiphinge = 1

            elif per_left_dumbbellhiphinge == atrest_value_dumbbellhiphinge:
                if dir_left_dumbbellhiphinge == 1:
                    successful_reps_count_left_dumbbellhiphinge += 0.5
                    dir_left_dumbbellhiphinge = 0

            # right
            if 40 <= per_right_dumbbellhiphinge <= 90:
                # Increment the time within range
                within_range_time2_dumbbellhiphinge += time.time() - start_time3_dumbbellhiphinge

                # Check if peak value has been within range for the specified time
                if within_range_time2_dumbbellhiphinge >= time_threshold_dumbbellhiphinge:
                    if dir_right_unsuccessful_dumbbellhiphinge == 0:
                        unsuccessful_reps_count_right_dumbbellhiphinge += 0.5
                        dir_right_unsuccessful_dumbbellhiphinge = 1
            else:
                within_range_time2_dumbbellhiphinge = 0
                # Update the start time to the current time
                start_time3_dumbbellhiphinge = time.time()

            if 1 <= per_right_dumbbellhiphinge <= 10:
                if dir_right_unsuccessful_dumbbellhiphinge == 1:
                    unsuccessful_reps_count_right_dumbbellhiphinge += 0.5
                    dir_right_unsuccessful_dumbbellhiphinge = 0

            if per_right_dumbbellhiphinge == success_threshold_dumbbellhiphinge:
                if dir_right_dumbbellhiphinge == 0:
                    successful_reps_count_right_dumbbellhiphinge += 0.5
                    dir_right_dumbbellhiphinge = 1
                    cooldown_timer_dumbbellhiphinge = cooldown_duration_dumbbellhiphinge
            elif per_right_dumbbellhiphinge == atrest_value_dumbbellhiphinge: 
                if dir_right_dumbbellhiphinge == 1:
                    successful_reps_count_right_dumbbellhiphinge += 0.5
                    dir_right_dumbbellhiphinge = 0
                    cooldown_timer_dumbbellhiphinge = cooldown_duration_dumbbellhiphinge

            # feedback for left hand  # TO BE FETCHED 
            feedback_left_dumbbellhiphinge = detector_dumbbellhiphinge.feedback_dumbbellhiphinge(per_left_dumbbellhiphinge)

            detector_dumbbellhiphinge.update_next_per_left(per_left_dumbbellhiphinge)

            # feedback for right hand  # TO BE FETCHED 
            feedback_right_dumbbellhiphinge = detector_dumbbellhiphinge.feedback_dumbbellhiphinge(per_right_dumbbellhiphinge)

            detector_dumbbellhiphinge.update_next_per_left(per_right_dumbbellhiphinge)



        cvzone.putTextRect(img, 'Front Dumbbell Hip Hinge', [370, 30], thickness=2, border=2, scale=1.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time_dumbbellhiphinge)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # Draw angle information
        cv2.putText(img, f"R: {int(per_right_dumbbellhiphinge)}", (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_dumbbellhiphinge)),(50, 400), color_right_dumbbellhiphinge, -1)

        cv2.putText(img, f"L: {int(per_left_dumbbellhiphinge)}", (924, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_dumbbellhiphinge)), (995, 400), color_left_dumbbellhiphinge,-1)

    
    # count
    cv2.rectangle(img, (20, 20), (140, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(successful_reps_count_right_dumbbellhiphinge)}/5", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (150, 20), (270, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(successful_reps_count_left_dumbbellhiphinge)}/5", (160, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    # Check if time's up
    if remaining_time_dumbbellhiphinge <= 0:
        cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
        display_info_dumbbellhiphinge = False


    if successful_reps_count_right_dumbbellhiphinge >= 2 and successful_reps_count_left_dumbbellhiphinge >= 2:
            cvzone.putTextRect(img, 'All Repetitions Completed', [420, 30], thickness=2, border=2, scale=2.5)
            display_info_dumbbellhiphinge = False
            # General feedback after finishing the exercise # TO BE FETCHED
            if dir_gen_feedback_dumbbellhiphinge == 0:
                general_feedback_left_dumbbellhiphinge = detector_dumbbellhiphinge.left_arm_feedback(total_reps_count_left_dumbbellhiphinge)
                general_feedback_right_dumbbellhiphinge = detector_dumbbellhiphinge.right_arm_feedback(total_reps_count_right_dumbbellhiphinge)
                dir_gen_feedback_dumbbellhiphinge = 1

    if unsuccessful_reps_count_left_dumbbellhiphinge >= 3 and unsuccessful_reps_count_right_dumbbellhiphinge >= 3:
        cvzone.putTextRect(img, 'You have made 2 unsuccessful tries for both arms. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_dumbbellhiphinge = False

        if dir_gen_feedback_unsuccessful_dumbbellhiphinge == 0:
            general_feedback_left_dumbbellhiphinge = detector_dumbbellhiphinge.left_arm_unsuccessful_feedback(total_reps_count_left_dumbbellhiphinge)
            general_feedback_right_dumbbellhiphinge = detector_dumbbellhiphinge.right_arm_unsuccessful_feedback(total_reps_count_right_dumbbellhiphinge)
            dir_gen_feedback_unsuccessful_dumbbellhiphinge = 1

    if unsuccessful_reps_count_left_dumbbellhiphinge >= 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for left arm. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_dumbbellhiphinge = False

        if dir_gen_feedback_unsuccessful_dumbbellhiphinge == 0:
            general_feedback_left_dumbbellhiphinge = detector_dumbbellhiphinge.left_arm_unsuccessful_feedback(total_reps_count_left_dumbbellhiphinge)
            dir_gen_feedback_unsuccessful_dumbbellhiphinge = 1

    if unsuccessful_reps_count_right_dumbbellhiphinge >= 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for right arm. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_dumbbellhiphinge = False

        if dir_gen_feedback_unsuccessful_dumbbellhiphinge == 0:
            general_feedback_right_dumbbellhiphinge = detector_dumbbellhiphinge.right_arm_unsuccessful_feedback(total_reps_count_right_dumbbellhiphinge)
            dir_gen_feedback_unsuccessful_dumbbellhiphinge == 1

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


