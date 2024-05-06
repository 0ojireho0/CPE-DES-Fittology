import math
import cv2
import numpy as np
import time
import squatsidekick_PoseModule as pm
import cvzone

cap = cv2.VideoCapture(r'D:\CPEDES\Flask\Exercises\loss_weight\Squat SideKick\squatsidekick.mp4')
detector_SquatSideKick = pm.poseDetectorSquatSideKick()

count_squatsidekick = 0
dir_squatsidekick = 0

count_left_kick_squatsidekick = 0
dir_kick_left_squatsidekick = 0

count_right_kick_squatsidekick = 0
dir_kick_right_squatsidekick = 0


start_time_squatsidekick = time.time()
repetition_time_squatsidekick = 60
display_info_squatsidekick = True

per_left_leg_squatsidekick = 0
bar_left_leg_squatsidekick = 0
per_left_leg_left_kick_squatsidekick = 0
bar_left_leg_left_kick_squatsidekick = 0

per_right_leg_squatsidekick = 0
bar_right_leg_squatsidekick = 0
per_right_leg_right_kick_squatsidekick = 0
bar_right_leg_right_kick_squatsidekick = 0

cooldown_duration_squatsidekick = 5
cooldown_timer_squatsidekick = 0

color_left_leg_squatsidekick = (0, 0, 255)
color_right_leg_squatsidekick = (0, 0, 255)

color_left_leg_left_kick_squatsidekick = (0, 0, 255)
color_right_leg_right_kick_squatsidekick = (0, 0, 255)

rightleg_squatsidekick = 0
leftleg_squatsidekick = 0
kickleft_squatsidekick = 0
kickright_squatsidekick = 0


squat_completed_squatsidekick = False
performing_squat_squatsidekick = True



orientation = ''
orientation2 = ''



while True:
    success, img = cap.read()
    img = cv2.resize(img, (1280, 720))

    elapsed_time = time.time() - start_time_squatsidekick
    remaining_time = max(0, 10 - elapsed_time) #repetition_time_squatsidekick

    if display_info_squatsidekick:  # Check if to display counter, bar, and percentage
        img = detector_SquatSideKick.findPose(img, False)
        lmList_squat_side_kick = detector_SquatSideKick.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_squat_side_kick) != 0:

            rightleg_squatsidekick = detector_SquatSideKick.Squat(img, 24, 26, 28, True)
            leftleg_squatsidekick = detector_SquatSideKick.Squat(img, 23, 25, 27, True)

            kickleft_squatsidekick = detector_SquatSideKick.SideKick(img, 11, 23 ,25,True)
            kickright_squatsidekick = detector_SquatSideKick.SideKick(img, 12, 24, 26, True)

            if cooldown_timer_squatsidekick > 0:
                cooldown_timer_squatsidekick -= 1

            per_right_leg_right_kick_squatsidekick = np.interp(240, (150, 240), (100, 0))
            bar_right_leg_right_kick_squatsidekick = np.interp(240, (150, 240), (200, 400))
            per_left_leg_left_kick_squatsidekick = np.interp(240, (150, 240), (100, 0))
            bar_left_leg_left_kick_squatsidekick = np.interp(240, (150, 240), (200, 400))

            per_right_leg_squatsidekick = np.interp(rightleg_squatsidekick, (150, 240), (100, 0))
            bar_right_leg_squatsidekick = np.interp(rightleg_squatsidekick, (150, 240), (480, 680))
            per_left_leg_squatsidekick = np.interp(leftleg_squatsidekick, (150, 240), (100, 0))
            bar_left_leg_squatsidekick = np.interp(leftleg_squatsidekick, (150, 240), (480, 680))

            if int(per_left_leg_squatsidekick) == 100 and int(per_right_leg_squatsidekick) == 100:
                color_left_leg_squatsidekick = (0, 255, 0) 
                color_right_leg_squatsidekick = (0, 255, 0) 
            else:
                color_left_leg_squatsidekick = (0, 0, 255)  
                color_right_leg_squatsidekick = (0, 0, 255) 

            if performing_squat_squatsidekick:
                if rightleg_squatsidekick <= 160 and leftleg_squatsidekick <= 160:
                    if dir_squatsidekick == 0:
                        count_squatsidekick += 0.5
                        dir_squatsidekick = 1
                        cooldown_timer_squatsidekick = cooldown_duration_squatsidekick
                elif rightleg_squatsidekick >= 240 and leftleg_squatsidekick >= 240: 
                    if dir_squatsidekick == 1:
                        count_squatsidekick += 0.5
                        dir_squatsidekick = 0
                        cooldown_timer_squatsidekick = cooldown_duration_squatsidekick
                        squat_completed_squatsidekick = True
                        performing_squat_squatsidekick = False

            if squat_completed_squatsidekick:
                performing_squat_squatsidekick = True
                per_right_leg_squatsidekick = np.interp(240, (150, 240), (100, 0))
                bar_right_leg_squatsidekick = np.interp(240, (150, 240), (480, 680))
                per_left_leg_squatsidekick = np.interp(240, (150, 240), (100, 0))
                bar_left_leg_squatsidekick = np.interp(240, (150, 240), (480, 680))
                    
                per_right_leg_right_kick_squatsidekick = np.interp(kickright_squatsidekick, (180, 250), (0, 100))
                bar_right_leg_right_kick_squatsidekick = np.interp(kickright_squatsidekick, (180, 250), (400, 200))
                per_left_leg_left_kick_squatsidekick = np.interp(kickleft_squatsidekick, (100, 160), (100, 0))
                bar_left_leg_left_kick_squatsidekick = np.interp(kickleft_squatsidekick, (100, 160), (200, 400))

                if int(per_left_leg_left_kick_squatsidekick) == 100:
                    color_left_leg_left_kick_squatsidekick = (0, 255, 0) 
                elif int (per_right_leg_right_kick_squatsidekick) == 100:
                    color_right_leg_right_kick_squatsidekick = (0, 255, 0)
                else:
                    color_left_leg_left_kick_squatsidekick = (0, 0, 255)  
                    color_right_leg_right_kick_squatsidekick = (0, 0, 255)

                if kickright_squatsidekick >= 250:
                    if dir_kick_right_squatsidekick == 0:
                        count_right_kick_squatsidekick += 0.5
                        dir_kick_right_squatsidekick = 1
                elif kickright_squatsidekick <= 190:
                    if dir_kick_right_squatsidekick == 1:
                        count_right_kick_squatsidekick += 0.5
                        dir_kick_right_squatsidekick = 0
                        performing_squat_squatsidekick = True
                        squat_completed_squatsidekick = False
                if kickleft_squatsidekick <= 100:
                    if dir_kick_left_squatsidekick == 0:
                        count_left_kick_squatsidekick += 0.5
                        dir_kick_left_squatsidekick = 1
                
                elif kickleft_squatsidekick >= 160:
                    if dir_kick_left_squatsidekick == 1:
                        count_left_kick_squatsidekick += 0.5
                        dir_kick_left_squatsidekick = 0
                        performing_squat_squatsidekick = True
                        squat_completed_squatsidekick = False


        cvzone.putTextRect(img, 'Squat Side Kick', [420, 30], thickness=2, border=2, scale=2)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        cv2.putText(img, f"R {int(per_right_leg_right_kick_squatsidekick)}%", (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_leg_right_kick_squatsidekick)), (50, 400), color_right_leg_right_kick_squatsidekick, -1)

        # ARM LEFT
        cv2.putText(img, f"L {int(per_left_leg_left_kick_squatsidekick)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_leg_left_kick_squatsidekick)), (995, 400), color_left_leg_left_kick_squatsidekick, -1)

        # RIGHT LEG
        cv2.putText(img, f"R {int(per_right_leg_squatsidekick)}%", (24, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 480), (50, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_leg_squatsidekick)), (50, 680), color_right_leg_squatsidekick, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_left_leg_squatsidekick)}%", (962, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 480), (995, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_leg_squatsidekick)), (995, 680), color_left_leg_squatsidekick, -1)

    # Counter 
    cv2.rectangle(img, (20, 10), (370, 90), (0, 100, 0), -1)  # Adjusted rectangle size
    cv2.putText(img, f"{int(count_squatsidekick)}/10", (145, 65), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.5, (255, 255, 255), 4)  # Adjusted text position and size

    cv2.rectangle(img, (20, 100), (180, 150), (255, 0, 0), -1)  # Adjusted rectangle size
    cv2.putText(img, f"{int(count_right_kick_squatsidekick)}/5", (70, 135), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.0, (255, 255, 255), 4)  # Adjusted text position and size

    cv2.rectangle(img, (190, 100), (370, 150), (0, 0, 255), -1) 
    cv2.putText(img, f"{int(count_left_kick_squatsidekick)}/5", (250, 135), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.0, (255, 255, 255), 4)  # Adjusted text position and size

    #Timer
    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [420, 30], thickness=2, border=2, scale=2.5)
        display_info_squatsidekick = False

    # Repetition
    if count_squatsidekick == 10 and count_right_kick_squatsidekick == 5 and count_left_kick_squatsidekick == 5:  # Assuming 10 jumping jacks for demonstration
        cvzone.putTextRect(img, 'Exercise Complete', [420, 30], thickness=2, border=2, scale=2.5)
        display_info_squatsidekick = False

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()



