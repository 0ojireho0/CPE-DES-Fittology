import math
import cv2
import numpy as np
import time
import dumbbellhiphinge_PoseModule as pm  # Assuming you have a PoseModule for hip hinge
import cvzone

# Load video
# r'C:\Users\RID\Desktop\pose_estimation\aipose2\Exercise\gainingmuscle\hiphinge.mp4'
cap = cv2.VideoCapture(r'D:\CPEDES\Flask\Exercises\gaining_muscle\Dumbbell Hip Hinge\How to Perform a Dumbbell Hip Hinge.mp4')

# Initialize pose detector
detector_HipHinge = pm.poseDetectorBodyHipHinge()

# Initialize variables
count_hip_hinge = 0
dir_hip_hinge = 0

start_time_hpp = time.time()
repetition_time_hpp = 60
display_info_hpp = True

per_left_hip_angle = 0
bar_left_hip_angle = 0

per_right_hip_angle = 0
bar_right_hip_angle = 0

leftbody_hpp = 0
rightbody_hpp = 0

color_hip = (0, 0, 255)



while True:
    success, img = cap.read()
    if not success:
        break
    img = cv2.resize(img, (1280, 720))
    #img = cv2.cvtColor(cv2.flip(img, 1), cv2.COLOR_BGR2RGB)

    elapsed_time = time.time() - start_time_hpp
    remaining_time = max(0, repetition_time_hpp - elapsed_time)

    if display_info_hpp:
        img = detector_HipHinge.findPose(img, False)
        lmList_hip_hinge = detector_HipHinge.findPosition(img, False)

        if len(lmList_hip_hinge) != 0:
            leftbody_hpp, orientation = detector_HipHinge.HipHinge(img, 11, 23, 25, True)
            rightbody_hpp, orientation2 = detector_HipHinge.HipHinge(img, 12, 24, 26, True)

            if orientation == 'right' and orientation2 == 'right':
                if leftbody_hpp is not None and rightbody_hpp is not None:

                    per_left_hip_angle = np.interp(int(leftbody_hpp), (230, 280), (0, 100))
                    bar_left_hip_angle = np.interp(int(leftbody_hpp), (230, 280), (400, 200))

                    per_right_hip_angle = np.interp(int(rightbody_hpp), (230, 280), (0, 100))
                    bar_right_hip_angle = np.interp(int(rightbody_hpp), (230, 280), (400, 200))

                    if per_left_hip_angle >= 100 and per_right_hip_angle >= 100:
                        color_hip = (0, 255, 0)
                    else: 
                        color_hip = (0, 0, 255)
                    
                    if leftbody_hpp >= 270 and rightbody_hpp >= 270:
                        if dir_hip_hinge == 0:
                            count_hip_hinge += 0.5
                            dir_hip_hinge = 1
                    elif leftbody_hpp <= 230 and rightbody_hpp <= 230:
                        if dir_hip_hinge == 1:
                            dir_hip_hinge = 0
                            count_hip_hinge += 0.5

            elif orientation =='left' and orientation2 == 'left':
                if leftbody_hpp is not None and rightbody_hpp is not None:
                    per_left_hip_angle = np.interp(int(leftbody_hpp), (70, 150), (100, 0))
                    bar_left_hip_angle = np.interp(int(leftbody_hpp), (70, 140), (200, 400))

                    per_right_hip_angle = np.interp(int(rightbody_hpp), (70, 150), (100, 0))
                    bar_right_hip_angle = np.interp(int(rightbody_hpp), (70, 140), (200, 400))

                    
                    if per_left_hip_angle >= 100 and per_right_hip_angle >= 100:
                        color_hip = (0, 255, 0)
                    else: 
                        color_hip = (0, 0, 255)
                    
                    if leftbody_hpp <= 70 and rightbody_hpp <= 70:
                        if dir_hip_hinge == 0:
                            count_hip_hinge += 0.5
                            dir_hip_hinge = 1
                    elif leftbody_hpp >= 150 and rightbody_hpp >= 150:
                        if dir_hip_hinge == 1:
                            count_hip_hinge += 0.5
                            dir_hip_hinge = 0

            elif orientation == 'front' and orientation2 == 'front':
                if leftbody_hpp is not None and rightbody_hpp is not None:
                    per_left_hip_angle = np.interp(int(leftbody_hpp), (90, 240), (100, 0))
                    bar_left_hip_angle = np.interp(int(leftbody_hpp), (80, 240), (200, 400))

                    per_right_hip_angle = np.interp(int(rightbody_hpp), (90, 240), (100, 0))
                    bar_right_hip_angle = np.interp(int(rightbody_hpp), (80, 240), (200, 400))

                    
                    if per_left_hip_angle >= 100 and per_right_hip_angle >= 100:
                        color_hip = (0, 255, 0)
                    else: 
                        color_hip = (0, 0, 255)
                    

                    if leftbody_hpp <= 90 and rightbody_hpp <= 90:
                        if dir_hip_hinge == 0:
                            count_hip_hinge += 0.5
                            dir_hip_hinge = 1
                    elif leftbody_hpp >= 240 and rightbody_hpp >= 240:
                        if dir_hip_hinge == 1:
                            count_hip_hinge += 0.5
                            dir_hip_hinge = 0

        cvzone.putTextRect(img, 'Dumbbell Hip Hinge Tracker', [220, 30], thickness=2, border=2, scale=2.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # Orientation
        cv2.rectangle(img, (890, 100), (1180, 160), (0, 0, 255), -2)
        cv2.putText(img, f"Orientation: {orientation}", (900, 140), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)

        # Draw angle information
        cv2.putText(img, f"R: {int(per_right_hip_angle)}", (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_hip_angle)),(50, 400), color_hip, -1)

        cv2.putText(img, f"L: {int(per_left_hip_angle)}", (924, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_hip_angle)), (995, 400), color_hip, -1)

    # Draw count
    cv2.rectangle(img, (0, 0), (130, 120), (255, 0, 0), -1)
    cv2.putText(img, f"{int(count_hip_hinge)}/5", (20, 70), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    # Check if time's up
    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
        display_info_hpp = False

    # Check if exercise is complete
    if count_hip_hinge >= 5:  
        cvzone.putTextRect(img, 'Exercise Complete', [390, 30], thickness=2, border=2, scale=2.5)
        display_info_hpp = False

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


