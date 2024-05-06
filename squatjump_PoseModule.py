import cv2
import mediapipe as mp
import time
import math
import numpy as np

class poseDetectorsquatjump():

    def __init__(self, mode=False, upBody=False, smooth=True):

        self.mode = mode
        self.upBody = upBody
        self.smooth = smooth

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode, self.upBody, self.smooth)

    def findPose(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks,
                                           self.mpPose.POSE_CONNECTIONS)
        return img

    def findPosition(self, img, draw=True):
        self.lmList = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                self.lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
        return self.lmList
    
    def get_pose_orientation(self, landmarks):
        # Define the indices of the landmarks for shoulders and hips
        shoulder_indices = [11, 12]  # Left and right shoulders
        hip_indices = [23, 24]  # Left and right hips
        
        # Extract coordinates for shoulders and hips
        shoulders = [landmarks.landmark[index] for index in shoulder_indices]
        hips = [landmarks.landmark[index] for index in hip_indices]
        
        # Extract x-coordinates of shoulders and hips
        shoulder_x = [shoulder.z for shoulder in shoulders]
        hip_x = [hip.z for hip in hips]
        #print(shoulder_x[0], shoulder_x[1], hip_x[0], hip_x[1])
        if shoulder_x[0] <= -0.10 and -0.01 <= shoulder_x[1] >= 0.03 and hip_x[0] <= -0.05 and hip_x[1] >= 0.05:
            return 'right'
        elif shoulder_x[0] >= 0.03 and shoulder_x[1] <= -0.10 and hip_x[0] >= 0.05 and hip_x[1] <= -0.05:
            return 'left'
        elif shoulder_x[0] <= -0.01 and -0.30 <= shoulder_x[1] <= 0.05 and -0.05 <= hip_x[0] <= 0.05 and -0.05 <= hip_x[1] <= 0.05 :
            return 'front'
        else:
            return 'none'

    def detect_feet_lift_off(self, pose_landmarks, threshold=0.80):
        if pose_landmarks is not None:
            # Landmark indices for the left and right feet
            left_foot_indices = [31, 29, 27]  # Adjust as needed
            right_foot_indices = [32, 28, 30]  # Adjust as needed

            # Calculate average vertical position of left and right feet
            left_foot_avg_y = sum([pose_landmarks.landmark[i].y for i in left_foot_indices]) / len(left_foot_indices)
            right_foot_avg_y = sum([pose_landmarks.landmark[i].y for i in right_foot_indices]) / len(right_foot_indices)

            #print(left_foot_avg_y, right_foot_avg_y)
            left_foot_lifted = left_foot_avg_y <= threshold
            right_foot_lifted = right_foot_avg_y <= threshold

            if left_foot_lifted and right_foot_lifted:
                return 0  # Both feet lifted off together
            elif left_foot_lifted:
                return 2  # Only left foot lifted off
            elif right_foot_lifted:
                return 1  # Only right foot lifted off
        return 0  # Neither foot lifted off

    def SquatJump(self, img, p1, p2, p3, drawpoints):
        if len(self.lmList) != 0:

            x1, y1 = self.lmList[p1][1], self.lmList[p1][2]
            x2, y2 = self.lmList[p2][1], self.lmList[p2][2]
            x3, y3 = self.lmList[p3][1], self.lmList[p3][2]

            orientation = self.get_pose_orientation(self.results.pose_landmarks)
            feet_lift_off = self.detect_feet_lift_off(self.results.pose_landmarks)

            # Calculate the angle only if the leg is stepping forward
            if orientation == 'right' and feet_lift_off == 0:

                lift_off = ""
                if feet_lift_off == 1:
                    lift_off = "Only right feet has been lifted please do it simultaneously."
                elif feet_lift_off == 2:
                    lift_off = "Only left feet has been lifted please do it simultaneously"
                
                measure = math.degrees(math.atan2(y3 - y2, x3 - x2) - math.atan2(y1 - y2, x1 - x2))
                if measure < 0:
                    measure += 360
                    
                if drawpoints:
                    cv2.circle(img, (x1, y1), 10, (255, 0, 255), 5)
                    cv2.circle(img, (x1, y1), 15, (0, 255, 0), 5)
                    cv2.circle(img, (x2, y2), 10, (255, 0, 255), 5)
                    cv2.circle(img, (x2, y2), 15, (0, 255, 0), 5)
                    cv2.circle(img, (x3, y3), 10, (255, 0, 255), 5)
                    cv2.circle(img, (x3, y3), 15, (0, 255, 0), 5)

                    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 6)
                    cv2.line(img, (x2, y2), (x3, y3), (0, 0, 255), 6)

                    cv2.putText(img, str(int(measure)), (x2 - 50, y2 + 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
                    return int(measure), 'right', lift_off
            
            elif orientation == 'left' and feet_lift_off == 0:
                measure = math.degrees(math.atan2(y3 - y2, x3 - x2) - math.atan2(y1 - y2, x1 - x2))
                if measure < 0:
                    measure += 360

                lift_off = ""
                if feet_lift_off == 1:
                    lift_off = "Only right feet has been lifted please do it simultaneously."
                elif feet_lift_off == 2:
                    lift_off = "Only left feet has been lifted please do it simultaneously"
                    
                if drawpoints:
                    cv2.circle(img, (x1, y1), 10, (255, 0, 255), 5)
                    cv2.circle(img, (x1, y1), 15, (0, 255, 0), 5)
                    cv2.circle(img, (x2, y2), 10, (255, 0, 255), 5)
                    cv2.circle(img, (x2, y2), 15, (0, 255, 0), 5)
                    cv2.circle(img, (x3, y3), 10, (255, 0, 255), 5)
                    cv2.circle(img, (x3, y3), 15, (0, 255, 0), 5)

                    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 6)
                    cv2.line(img, (x2, y2), (x3, y3), (0, 0, 255), 6)

                    cv2.putText(img, str(int(measure)), (x2 - 50, y2 + 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
                    return int(measure), 'left', lift_off
            
            elif orientation == 'front' and feet_lift_off == 0:
                measure = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
                midpoint_x = int((x1 + x3) / 2)
                midpoint_y = int((y1 + y3) / 2)

                lift_off = ""
                if feet_lift_off == 1:
                    lift_off = "Only right feet has been lifted please do it simultaneously."
                elif feet_lift_off == 2:
                    lift_off = "Only left feet has been lifted please do it simultaneously"

                if drawpoints:

                    cv2.circle(img, (x1, y1), 10, (255, 0, 255), 5)
                    cv2.circle(img, (x1, y1), 15, (0, 255, 0), 5)
                    cv2.circle(img, (x2, y2), 10, (255, 0, 255), 5)
                    cv2.circle(img, (x2, y2), 15, (0, 255, 0), 5)
                    cv2.circle(img, (x3, y3), 10, (255, 0, 255), 5)
                    cv2.circle(img, (x3, y3), 15, (0, 255, 0), 5)

                    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 6)
                    cv2.line(img, (x2, y2), (x3, y3), (0, 0, 255), 6)

                    cv2.putText(img, f"{int(measure)}", (midpoint_x, midpoint_y), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
                    return int(measure), 'front', lift_off
        return None, None, 'None'

def main():
    cap = cv2.VideoCapture(r'C:\Users\RID\Desktop\pose_estimation\aipose2\Exercise\weightloss\JUMP SQUAT.mp4')
    pTime = 0
    detector = poseDetectorsquatjump()
    
    while True:
        # Capture frame from camera
        success, img = cap.read()

        # Find and draw pose on the frame
        img = detector.findPose(img)

        # Find landmark position for specific points (e.g., shoulder)
        lmList = detector.findPosition(img, draw=False)
        
        # Calculate and display angles
        if len(lmList) != 0:
            angle_right = detector.SquatJump(img, 24, 26, 28, True)
            angle_left = detector.SquatJump(img, 23, 25, 27, True)
            #print("Right arm angle:", angle_right, "Left arm angle:", angle_left)

            # Test the detect_feet_lift_off function
            feet_lift_off = detector.detect_feet_lift_off(detector.results.pose_landmarks)
            #print("Feet lift off:", feet_lift_off)

            # # Test the SquatJump function
            # angle, orientation = detector.SquatJump(img, p1, p2, p3, drawpoints)
            # print("Squat Jump angle:", angle)
            # print("Squat Jump orientation:", orientation)

        # Calculate and display FPS
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        # Display the annotated image
        cv2.imshow("Image", img)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

# Run the main function if this script is executed
if __name__ == "__main__":
    main()
