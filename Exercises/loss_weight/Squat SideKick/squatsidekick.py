import math
import cv2
import numpy as np
import time
import squatsidekick_PoseModule as pm
import cvzone

cap = cv2.VideoCapture(r'C:\Users\RID\Desktop\pose_estimation\aipose2\Exercise\weightloss\squatsidekick.mp4')
detector_SquatSideKick = pm.poseDetectorSquatSideKick()

count_squat = 0
dir_squat = 0

count_left_kick = 0
dir_kick_left = 0

count_right_kick = 0
dir_kick_right = 0


pTime = 0
start_time = time.time()
repetition_time = 60
display_info = True

per_left_leg = 0
bar_left_leg = 0
per_left_leg_left_kick = 0
bar_left_leg_left_kick = 0

per_right_leg = 0
bar_right_leg = 0
per_right_leg_right_kick = 0
bar_right_leg_right_kick = 0

cooldown_duration = 5
cooldown_timer = 0

color_left_leg = (0, 0, 255)
color_right_leg = (0, 0, 255)

color_left_leg_left_kick = (0, 0, 255)
color_right_leg_right_kick = (0, 0, 255)

rightleg = 0
leftleg = 0
kickleft = 0
kickright = 0
legdistance = 0
legdistance2 = 0

orientation = ''
orientation2 = ''

done = 0

squat_completed = False
performing_squat = True

while True:
    success, img = cap.read()
    img = cv2.resize(img, (1280, 720))

    elapsed_time = time.time() - start_time
    remaining_time = max(0, repetition_time - elapsed_time)

    if display_info:  # Check if to display counter, bar, and percentage
        img = detector_SquatSideKick.findPose(img, False)
        lmList_squat_side_kick = detector_SquatSideKick.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_squat_side_kick) != 0:

            rightleg = detector_SquatSideKick.Squat(img, 24, 26, 28, True)
            leftleg = detector_SquatSideKick.Squat(img, 23, 25, 27, True)

            kickleft = detector_SquatSideKick.SideKick(img, 11, 23 ,25,True)
            kickright = detector_SquatSideKick.SideKick(img, 12, 24, 26, True)

            if cooldown_timer > 0:
                cooldown_timer -= 1

            per_right_leg_right_kick = np.interp(240, (150, 240), (100, 0))
            bar_right_leg_right_kick = np.interp(240, (150, 240), (200, 400))
            per_left_leg_left_kick = np.interp(240, (150, 240), (100, 0))
            bar_left_leg_left_kick = np.interp(240, (150, 240), (200, 400))

            per_right_leg = np.interp(rightleg, (150, 240), (100, 0))
            bar_right_leg = np.interp(rightleg, (150, 240), (480, 680))
            per_left_leg = np.interp(leftleg, (150, 240), (100, 0))
            bar_left_leg = np.interp(leftleg, (150, 240), (480, 680))

            if int(per_left_leg) == 100 and int(per_right_leg) == 100:
                color_left_leg = (0, 255, 0) 
                color_right_leg = (0, 255, 0) 
            else:
                color_left_leg = (0, 0, 255)  
                color_right_leg = (0, 0, 255) 

            if performing_squat:
                if rightleg <= 160 and leftleg <= 160:
                    if dir_squat == 0:
                        count_squat += 0.5
                        dir_squat = 1
                        cooldown_timer = cooldown_duration
                elif rightleg >= 240 and leftleg >= 240: 
                    if dir_squat == 1:
                        count_squat += 0.5
                        dir_squat = 0
                        cooldown_timer = cooldown_duration
                        squat_completed = True
                        performing_squat = False

            if squat_completed:
                performing_squat = True
                per_right_leg = np.interp(240, (150, 240), (100, 0))
                bar_right_leg = np.interp(240, (150, 240), (480, 680))
                per_left_leg = np.interp(240, (150, 240), (100, 0))
                bar_left_leg = np.interp(240, (150, 240), (480, 680))
                    
                per_right_leg_right_kick = np.interp(kickright, (180, 250), (0, 100))
                bar_right_leg_right_kick = np.interp(kickright, (180, 250), (400, 200))
                per_left_leg_left_kick = np.interp(kickleft, (100, 160), (100, 0))
                bar_left_leg_left_kick = np.interp(kickleft, (100, 160), (200, 400))

                if int(per_left_leg_left_kick) == 100:
                    color_left_leg_left_kick = (0, 255, 0) 
                elif int (per_right_leg_right_kick) == 100:
                    color_right_leg_right_kick = (0, 255, 0)
                else:
                    color_left_leg_left_kick = (0, 0, 255)  
                    color_right_leg_right_kick = (0, 0, 255)

                if kickright >= 250:
                    if dir_kick_right == 0:
                        count_right_kick += 0.5
                        dir_kick_right = 1
                elif kickright <= 190:
                    if dir_kick_right == 1:
                        count_right_kick += 0.5
                        dir_kick_right = 0
                        performing_squat = True
                        squat_completed = False
                if kickleft <= 100:
                    if dir_kick_left == 0:
                        count_left_kick += 0.5
                        dir_kick_left = 1
                
                elif kickleft >= 160:
                    if dir_kick_left == 1:
                        count_left_kick += 0.5
                        dir_kick_left = 0
                        performing_squat = True
                        squat_completed = False

        #Delay Timer for Pose Estimation
        fps = cap.get(cv2.CAP_PROP_FPS)
        if cooldown_timer > 0:
            cooldown_timer -= 1 / fps

        cvzone.putTextRect(img, 'Squat Side Kick Tracker', [420, 30], thickness=2, border=2, scale=2)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        cv2.putText(img, f"R {int(per_right_leg_right_kick)}%", (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_leg_right_kick)), (50, 400), color_right_leg_right_kick, -1)

        # ARM LEFT
        cv2.putText(img, f"L {int(per_left_leg_left_kick)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_leg_left_kick)), (995, 400), color_left_leg_left_kick, -1)

        # RIGHT LEG
        cv2.putText(img, f"R {int(per_right_leg)}%", (24, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 480), (50, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_leg)), (50, 680), color_right_leg, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_left_leg)}%", (962, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 480), (995, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_leg)), (995, 680), color_left_leg, -1)

    # Counter 
    cv2.rectangle(img, (20, 10), (370, 90), (0, 100, 0), -1)  # Adjusted rectangle size
    cv2.putText(img, f"{int(count_squat)}/5", (145, 65), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.5, (255, 255, 255), 4)  # Adjusted text position and size

    cv2.rectangle(img, (20, 100), (180, 150), (255, 0, 0), -1)  # Adjusted rectangle size
    cv2.putText(img, f"{int(count_right_kick)}/5", (70, 135), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.0, (255, 255, 255), 4)  # Adjusted text position and size

    cv2.rectangle(img, (190, 100), (370, 150), (0, 0, 255), -1) 
    cv2.putText(img, f"{int(count_left_kick)}/5", (250, 135), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.0, (255, 255, 255), 4)  # Adjusted text position and size

    #Timer
    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [420, 30], thickness=2, border=2, scale=2.5)
        display_info = False

    # Repetition
    if count_squat >= 6:  # Assuming 10 jumping jacks for demonstration
        cvzone.putTextRect(img, 'Exercise Complete', [420, 30], thickness=2, border=2, scale=2.5)
        display_info = False

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()



