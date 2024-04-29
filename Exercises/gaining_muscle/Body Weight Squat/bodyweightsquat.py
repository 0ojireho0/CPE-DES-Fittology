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


body_weight_squat_start_time = time.time()
body_weight_squat_repetition_time = 60
body_weight_squat_display_info = True

body_weight_squat_leftbody = 0
body_weight_squat_rightbody = 0

body_weight_squat_per_left_body = 0
body_weight_squat_bar_left_body = 0

body_weight_squat_per_right_body = 0
body_weight_squat_bar_right_body = 0

body_weight_squat_color_right_body = 0
body_weight_squat_color_left_body = 0



while True:
    success, img = cap.read()
    img = cv2.resize(img, (1280, 720))

    elapsed_time = time.time() - body_weight_squat_start_time
    remaining_time = max(0, body_weight_squat_repetition_time - elapsed_time)

    if body_weight_squat_display_info:  # Check if to display counter, bar, and percentage
        img = detector_BodyWeightSquat.findPose(img, False)
        lmList_jumping_jacks = detector_BodyWeightSquat.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_jumping_jacks) != 0:
            
            body_weight_squat_leftbody, orientation = detector_BodyWeightSquat.WeightSquat(img, 12, 24, 26, True)
            body_weight_squat_rightbody, orientation2 = detector_BodyWeightSquat.WeightSquat(img, 11, 23, 25, True)
            
            if orientation == 'right' and orientation2 == 'right':
                body_weight_squat_per_right_body = np.interp(body_weight_squat_rightbody, (180, 280), (0, 100))
                body_weight_squat_bar_right_body = np.interp(body_weight_squat_rightbody, (180, 280), (400, 200))

                body_weight_squat_per_left_body = np.interp(body_weight_squat_leftbody, (180, 280), (0, 100))
                body_weight_squat_bar_left_body = np.interp(body_weight_squat_leftbody, (180, 280), (400, 200))

                if int(body_weight_squat_per_left_body) == 100 and int(body_weight_squat_per_left_body) == 100:
                    body_weight_squat_color_left_body = (0, 255, 0)
                    body_weight_squat_color_right_body = (0, 255, 0)  
                else:
                    body_weight_squat_color_left_body = (0, 0, 255)  
                    body_weight_squat_color_right_body = (0, 0, 255)  
            
                if body_weight_squat_leftbody >= 280 and body_weight_squat_rightbody >= 280:
                    if dir_body_weight_squat == 0:
                        count_body_weight_squat += 0.5
                        dir_body_weight_squat = 1
                elif body_weight_squat_leftbody <= 180 and body_weight_squat_rightbody <= 180:
                    if dir_body_weight_squat == 1:
                        count_body_weight_squat +=0.5
                        dir_body_weight_squat = 0
                    
            elif orientation =='left' and orientation2 == 'left':
                if body_weight_squat_leftbody is not None and body_weight_squat_rightbody is not None:

                    body_weight_squat_per_right_body = np.interp(body_weight_squat_rightbody, (90, 170), (100, 0))
                    body_weight_squat_bar_right_body = np.interp(body_weight_squat_rightbody, (90, 170), (200, 400))

                    body_weight_squat_per_left_body = np.interp(body_weight_squat_leftbody, (90, 170), (100, 0))
                    body_weight_squat_bar_left_body = np.interp(body_weight_squat_leftbody, (90, 170), (200, 400))

                    if int(body_weight_squat_per_left_body) == 100 and int(body_weight_squat_per_left_body) == 100:
                        body_weight_squat_color_left_body = (0, 255, 0)
                        body_weight_squat_color_right_body = (0, 255, 0)  
                    else:
                        body_weight_squat_color_left_body = (0, 0, 255)  
                        body_weight_squat_color_right_body = (0, 0, 255)  
 
                    if body_weight_squat_leftbody <= 90 and body_weight_squat_rightbody <= 90:
                        if dir_body_weight_squat == 0:
                            count_body_weight_squat += 0.5
                            dir_body_weight_squat = 1
                    elif body_weight_squat_leftbody >= 170 and body_weight_squat_rightbody >= 170:
                        if dir_body_weight_squat == 1:
                            count_body_weight_squat +=0.5
                            dir_body_weight_squat = 0

            elif orientation == 'front facing' and orientation2 == 'front facing':
                    
                    body_weight_squat_per_right_body = np.interp(body_weight_squat_rightbody, (180, 270), (100, 0))
                    body_weight_squat_bar_right_body = np.interp(body_weight_squat_rightbody, (180, 270), (200, 400))

                    body_weight_squat_per_left_body = np.interp(body_weight_squat_leftbody, (180, 270), (100, 0))
                    body_weight_squat_bar_left_body = np.interp(body_weight_squat_leftbody, (180, 270), (200, 400))

                    if int(body_weight_squat_per_left_body) == 100 and int(body_weight_squat_per_left_body) == 100:
                        body_weight_squat_color_left_body = (0, 255, 0)
                        body_weight_squat_color_right_body = (0, 255, 0)  
                    else:
                        body_weight_squat_color_left_body = (0, 0, 255)  
                        body_weight_squat_color_right_body = (0, 0, 255)  

                    if body_weight_squat_rightbody <= 180 and body_weight_squat_leftbody <= 180: 
                        if dir_body_weight_squat == 0:
                            count_body_weight_squat += 0.5
                            dir_body_weight_squat =1
                    elif body_weight_squat_rightbody >= 270 and body_weight_squat_leftbody >= 270:
                        if dir_body_weight_squat == 1:
                            count_body_weight_squat += 0.5
                            dir_body_weight_squat = 0
                    

        cvzone.putTextRect(img, 'Body Weight Squat Tracker', [345, 30], thickness=2, border=2, scale=2.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # RIGHT LEG
        cv2.putText(img, f"R {int(body_weight_squat_per_right_body)}%", (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(body_weight_squat_bar_right_body)), (50, 400), body_weight_squat_color_right_body, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(body_weight_squat_per_left_body)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(body_weight_squat_bar_left_body)), (995, 400), body_weight_squat_color_left_body, -1)

    cv2.rectangle(img, (0, 0), (130, 120), (255, 0, 0), -1)
    cv2.putText(img, f"{int(count_body_weight_squat)}/6", (20, 70), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (0, 0, 255), 7)

    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [345, 30], thickness=2, border=2, scale=2.5)
        body_weight_squat_display_info = False

    if count_body_weight_squat >= 6:  
        cvzone.putTextRect(img, 'Exercise Complete', [345, 30], thickness=2, border=2, scale=2.5)
        body_weight_squat_display_info = False

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



