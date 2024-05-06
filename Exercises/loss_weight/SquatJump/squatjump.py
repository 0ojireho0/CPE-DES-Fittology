import cv2
import numpy as np
import time
import squatjump_PoseModule as pm
import cvzone

cap = cv2.VideoCapture(r'D:\CPEDES\Flask\Exercises\loss_weight\SquatJump\jumpsquatcomplete.mp4')
detector_squatjump = pm.poseDetectorsquatjump()

count_squat_jump = 0
dir_squat_jump = 0

start_time_squatjump = time.time()
repetition_time_squatjump = 60
display_info_squatjump = True

per_left_leg_squatjump = 0
bar_left_leg_squatjump = 0

per_right_leg_squatjump = 0
bar_right_leg_squatjump = 0

leftleg_squatjump = 0
rightleg_squatjump = 0


cooldown_duration_squatjump = 5
cooldown_timer_squatjump = 0

color_left_leg_squatjump = (0, 0, 255)
color_right_leg_squatjump = (0, 0, 255)

orientation = ''
orientation2 = ''

while True:
    success, img = cap.read()
    img = cv2.resize(img, (1280, 720))

    elapsed_time = time.time() - start_time_squatjump
    remaining_time = max(0, 10 - elapsed_time)

    if display_info_squatjump:  # Check if to display counter, bar, and percentage
        img = detector_squatjump.findPose(img, False)
        lmList_squat_jump = detector_squatjump.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_squat_jump) != 0:

            # Right and Left keypoints
            rightleg_squatjump, orientation, lift_off = detector_squatjump.SquatJump(img, 12, 24, 26, True)
            leftleg_squatjump, orientation2, lift_off = detector_squatjump.SquatJump(img, 11, 23, 25, True)

            if cooldown_timer_squatjump > 0:
                cooldown_timer_squatjump -= 1

            if orientation == 'right' and orientation2 == 'right':
                    
                    per_right_leg_squatjump = np.interp(rightleg_squatjump, (190, 290), (0, 100))
                    bar_right_leg_squatjump = np.interp(rightleg_squatjump, (190, 290), (680, 480))
                    per_left_leg_squatjump = np.interp(leftleg_squatjump, (190, 290), (0, 100))
                    bar_left_leg_squatjump = np.interp(leftleg_squatjump, (190, 290), (680, 480))

                    if int(per_left_leg_squatjump) == 100 and int(per_right_leg_squatjump) == 100:
                        color_left_leg_squatjump = (0, 255, 0)
                        color_right_leg_squatjump = (0, 255, 0)  # Change color of left leg bar to green
                    else:
                        color_left_leg_squatjump = (0, 0, 255)  # Keep color of left leg bar as red
                        color_right_leg_squatjump = (0, 0, 255)

                    if rightleg_squatjump >= 290:
                        if dir_squat_jump == 0:
                            count_squat_jump += 0.5
                            dir_squat_jump = 1
                            cooldown_timer_squatjump = cooldown_duration_squatjump
                    elif rightleg_squatjump <= 190:
                        if dir_squat_jump == 1:
                            count_squat_jump += 0.5
                            dir_squat_jump = 0
                            cooldown_timer_squatjump = cooldown_duration_squatjump
                    
                    if leftleg_squatjump >= 290:
                        if dir_squat_jump == 0:
                            count_squat_jump += 0.5
                            dir_squat_jump = 1
                            cooldown_timer_squatjump = cooldown_duration_squatjump
                    elif leftleg_squatjump <= 190:
                        if dir_squat_jump == 1:
                            count_squat_jump += 0.5
                            dir_squat_jump = 0
                            cooldown_timer_squatjump = cooldown_duration_squatjump


            elif orientation =='left' and orientation2 == 'left':
                if leftleg_squatjump is not None and rightleg_squatjump is not None:
                    per_right_leg_squatjump = np.interp(rightleg_squatjump, (70, 150), (100, 0))
                    bar_right_leg_squatjump = np.interp(rightleg_squatjump, (70, 150), (480, 680))
                    per_left_leg_squatjump = np.interp(leftleg_squatjump, (70, 150), (100 ,0))
                    bar_left_leg_squatjump = np.interp(leftleg_squatjump, (70, 150), (480, 680))

                    if int(per_left_leg_squatjump) == 100 and int(per_right_leg_squatjump) == 100:
                        color_left_leg_squatjump = (0, 255, 0)
                        color_right_leg_squatjump = (0, 255, 0)  # Change color of left leg bar to green
                    else:
                        color_left_leg_squatjump = (0, 0, 255)  # Keep color of left leg bar as red
                        color_right_leg_squatjump = (0, 0, 255)
              
                    if rightleg_squatjump <= 70:
                        if dir_squat_jump == 0:
                            count_squat_jump += 0.5
                            dir_squat_jump = 1
                            cooldown_timer_squatjump = cooldown_duration_squatjump
                    elif rightleg_squatjump >= 150:
                        if dir_squat_jump == 1:
                            count_squat_jump += 0.5
                            dir_squat_jump = 0
                            cooldown_timer_squatjump = cooldown_duration_squatjump

                    if leftleg_squatjump <= 70:
                        if dir_squat_jump == 0:
                            count_squat_jump += 0.5
                            dir_squat_jump = 1
                            cooldown_timer_squatjump = cooldown_duration_squatjump
                    elif leftleg_squatjump >= 150:
                        if dir_squat_jump == 1:
                            count_squat_jump += 0.5
                            dir_squat_jump = 0
                            cooldown_timer_squatjump = cooldown_duration_squatjump

            elif orientation == 'front' and orientation2 == 'front':
                    
                    per_right_leg_squatjump = np.interp(rightleg_squatjump, (170, 280), (100, 0))
                    bar_right_leg_squatjump = np.interp(rightleg_squatjump, (170, 280), (480, 680))
                    per_left_leg_squatjump = np.interp(leftleg_squatjump, (170, 280), (100, 0))
                    bar_left_leg_squatjump = np.interp(leftleg_squatjump, (170, 280), (480, 680))

                    if int(per_left_leg_squatjump) == 100 and int(per_right_leg_squatjump) == 100:
                        color_left_leg_squatjump = (0, 255, 0)
                        color_right_leg_squatjump = (0, 255, 0)  # Change color of left leg bar to green
                    else:
                        color_left_leg_squatjump = (0, 0, 255)  # Keep color of left leg bar as red
                        color_right_leg_squatjump = (0, 0, 255)  # Keep color of right leg bar as red

                    if rightleg_squatjump <= 170:
                        if dir_squat_jump == 0:
                            count_squat_jump += 0.5
                            dir_squat_jump = 1
                            cooldown_timer_squatjump = cooldown_duration_squatjump
                    elif rightleg_squatjump >= 280: 
                        if dir_squat_jump == 1:
                            count_squat_jump += 0.5
                            dir_squat_jump = 0
                            cooldown_timer_squatjump = cooldown_duration_squatjump
                    if leftleg_squatjump <= 170:
                        if dir_squat_jump == 0:
                            count_squat_jump += 0.5
                            dir_squat_jump = 1
                            cooldown_timer = cooldown_duration_squatjump
                    elif leftleg_squatjump >= 280:
                        if dir_squat_jump == 1:
                            count_squat_jump += 0.5
                            dir_squat_jump = 0
                            cooldown_timer_squatjump = cooldown_duration_squatjump

        cvzone.putTextRect(img, 'Squat Jump Tracker', [420, 30], thickness=2, border=2, scale=2.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)
       
        # Orientation
        cv2.rectangle(img, (890, 100), (1180, 160), (0, 0, 255), -2)
        cv2.putText(img, f"Orientation: {orientation}", (900, 140), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)

        # RIGHT LEG
        cv2.putText(img, f"R {int(per_right_leg_squatjump)}%", (24, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 480), (50, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_leg_squatjump)), (50, 680), color_right_leg_squatjump, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_left_leg_squatjump)}%", (962, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 480), (995, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_leg_squatjump)), (995, 680), color_left_leg_squatjump, -1)

    # Counter 
    cv2.rectangle(img, (20, 20), (200, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(count_squat_jump)}/5", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    # Timer
    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
        display_info_squatjump = False

    # Repetition
    if count_squat_jump == 5:  # Assuming 10 jumping jacks for demonstration
        cvzone.putTextRect(img, 'Exercise Complete', [390, 30], thickness=2, border=2, scale=2.5)
        display_info_squatjump = False

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break


cap.release()

cv2.destroyAllWindows()



