import cv2
import mediapipe as mp
import time
import math
import numpy as np

class poseDetectorBodyWeightSquat():

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
        if shoulder_x[0] <= -0.10 and shoulder_x[1] >= 0.05 and hip_x[0] <= -0.05 and hip_x[1] >= 0.05:
            return 'right'
        elif shoulder_x[0] >= 0.03 and shoulder_x[1] <= -0.10 and hip_x[0] >= 0.05 and hip_x[1] <= -0.05:
            return 'left'
        elif shoulder_x[0] <= -0.01 and shoulder_x[1] <= -0.01 and -0.04 <= hip_x[0] <= 0.04 and -0.04 <= hip_x[1] <= 0.04 :
            return 'front'
        else:
            return 'none'

    def WeightSquat(self, img, p1, p2, p3, drawpoints):
        if len(self.lmList) != 0:

            x1, y1 = self.lmList[p1][1], self.lmList[p1][2]
            x2, y2 = self.lmList[p2][1], self.lmList[p2][2]
            x3, y3 = self.lmList[p3][1], self.lmList[p3][2]

            orientation = self.get_pose_orientation(self.results.pose_landmarks)

            # Calculate the angle only if the leg is stepping forward
            if orientation == 'right':
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
                    return int(measure), 'right'
            
            elif orientation == 'left':
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
                    return int(measure), 'left'
            
            elif orientation == 'front':
                measure = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
                midpoint_x = int((x1 + x3) / 2)
                midpoint_y = int((y1 + y3) / 2)

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
                    return int(measure), 'front facing' 
        return None, 'None'
