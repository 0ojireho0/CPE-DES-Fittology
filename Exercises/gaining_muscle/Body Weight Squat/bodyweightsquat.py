import math
import cv2
import numpy as np
import time
import bodyweightsquat_PoseModule as pm
import cvzone

cap = cv2.VideoCapture(r'D:\CPEDES\Flask\Exercises\gaining_muscle\Body Weight Squat\bwscomplete.mp4')
detector_BodyWeightSquat = pm.poseDetectorBodyWeightSquat()

count_body_weight_squat = 0
dir_body_weight_squat = 0


start_time_bws = time.time()
repetition_time_bws = 60
display_info_bws = True

leftbody_bws = 0
rightbody_bws = 0

per_left_body_bws = 0
bar_left_body_bws = 0

per_right_body_bws = 0
bar_right_body_bws = 0

color_right_body_bws = 0
color_left_body_bws = 0



while True:
    success, img = cap.read()
    img = cv2.resize(img, (1280, 720))

    elapsed_time = time.time() - start_time_bws
    remaining_time = max(0, repetition_time_bws - elapsed_time)

    if display_info_bws:  # Check if to display counter, bar, and percentage
        img = detector_BodyWeightSquat.findPose(img, False)
        lmList_jumping_jacks = detector_BodyWeightSquat.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_jumping_jacks) != 0:
            
            leftbody_bws, orientation = detector_BodyWeightSquat.WeightSquat(img, 12, 24, 26, True)
            rightbody_bws, orientation2 = detector_BodyWeightSquat.WeightSquat(img, 11, 23, 25, True)
            
            if orientation == 'right' and orientation2 == 'right':
                per_right_body_bws = np.interp(rightbody_bws, (180, 280), (0, 100))
                bar_right_body_bws = np.interp(rightbody_bws, (180, 280), (400, 200))

                per_left_body_bws = np.interp(leftbody_bws, (180, 280), (0, 100))
                bar_left_body_bws = np.interp(leftbody_bws, (180, 280), (400, 200))

                if int(per_left_body_bws) == 100 and int(per_left_body_bws) == 100:
                    color_left_body_bws = (0, 255, 0)
                    color_right_body_bws = (0, 255, 0)  
                else:
                    color_left_body_bws = (0, 0, 255)  
                    color_right_body_bws = (0, 0, 255)  
            
                if leftbody_bws >= 280 and rightbody_bws >= 280:
                    if dir_body_weight_squat == 0:
                        count_body_weight_squat += 0.5
                        dir_body_weight_squat = 1
                elif leftbody_bws <= 180 and rightbody_bws <= 180:
                    if dir_body_weight_squat == 1:
                        count_body_weight_squat +=0.5
                        dir_body_weight_squat = 0
                    
            elif orientation =='left' and orientation2 == 'left':
                if leftbody_bws is not None and rightbody_bws is not None:

                    per_right_body_bws = np.interp(rightbody_bws, (90, 170), (100, 0))
                    bar_right_body_bws = np.interp(rightbody_bws, (90, 170), (200, 400))

                    per_left_body_bws = np.interp(leftbody_bws, (90, 170), (100, 0))
                    bar_left_body_bws = np.interp(leftbody_bws, (90, 170), (200, 400))

                    if int(per_left_body_bws) == 100 and int(per_left_body_bws) == 100:
                        color_left_body_bws = (0, 255, 0)
                        color_right_body_bws = (0, 255, 0)  
                    else:
                        color_left_body_bws = (0, 0, 255)  
                        color_right_body_bws = (0, 0, 255)  
 
                    if leftbody_bws <= 90 and rightbody_bws <= 90:
                        if dir_body_weight_squat == 0:
                            count_body_weight_squat += 0.5
                            dir_body_weight_squat = 1
                    elif leftbody_bws >= 170 and rightbody_bws >= 170:
                        if dir_body_weight_squat == 1:
                            count_body_weight_squat +=0.5
                            dir_body_weight_squat = 0

            elif orientation == 'front' and orientation2 == 'front':
                    
                    per_right_body_bws = np.interp(rightbody_bws, (180, 270), (100, 0))
                    bar_right_body_bws = np.interp(rightbody_bws, (180, 270), (200, 400))

                    per_left_body_bws = np.interp(leftbody_bws, (180, 270), (100, 0))
                    bar_left_body_bws = np.interp(leftbody_bws, (180, 270), (200, 400))

                    if int(per_left_body_bws) == 100 and int(per_left_body_bws) == 100:
                        color_left_body_bws = (0, 255, 0)
                        color_right_body_bws = (0, 255, 0)  
                    else:
                        color_left_body_bws = (0, 0, 255)  
                        color_right_body_bws = (0, 0, 255)  

                    if rightbody_bws <= 180 and leftbody_bws <= 180: 
                        if dir_body_weight_squat == 0:
                            count_body_weight_squat += 0.5
                            dir_body_weight_squat =1
                    elif rightbody_bws >= 270 and leftbody_bws >= 270:
                        if dir_body_weight_squat == 1:
                            count_body_weight_squat += 0.5
                            dir_body_weight_squat = 0
                    

        cvzone.putTextRect(img, 'Body Weight Squat Tracker', [220, 30], thickness=2, border=2, scale=2.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # RIGHT LEG
        cv2.putText(img, f"R {int(per_right_body_bws)}%", (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_body_bws)), (50, 400), color_right_body_bws, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_left_body_bws)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_body_bws)), (995, 400), color_left_body_bws, -1)

    cv2.rectangle(img, (20, 10), (140, 120), (255, 0, 0), -1)
    cv2.putText(img, f"{int(count_body_weight_squat)}/6", (30, 80), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
        display_info_bws = False

    if count_body_weight_squat >= 6:  
        cvzone.putTextRect(img, 'Exercise Complete', [390, 30], thickness=2, border=2, scale=2.5)
        display_info_bws = False

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



