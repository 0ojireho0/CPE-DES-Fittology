import cv2
import mediapipe as mp
import time
import math
import numpy as np

class poseDetectorSquatSideKick():

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
    
    def Squat(self, img, p1, p2, p3, drawpoints):
            if len(self.lmList) != 0:

                x1, y1 = self.lmList[p1][1], self.lmList[p1][2]
                x2, y2 = self.lmList[p2][1], self.lmList[p2][2]
                x3, y3 = self.lmList[p3][1], self.lmList[p3][2]

                # Calculate the angle only if the leg is stepping forward
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
                    return int(measure)

    def SideKick(self, img, p1, p2, p3,  draw):
        if len(self.lmList) != 0:

            x1, y1 = self.lmList[p1][1], self.lmList[p1][2]
            x2, y2 = self.lmList[p2][1], self.lmList[p2][2]
            x3, y3 = self.lmList[p3][1], self.lmList[p3][2]

            angle = math.degrees(math.atan2(y3 - y2, x3 - x2) - math.atan2(y1 - y2, x1 - x2))
            
            if angle < 0:
                angle += 360

            if draw:

                cv2.circle(img, (x1, y1), 10, (255, 0, 255), 5) 
                cv2.circle(img, (x1, y1), 15, (0, 255, 0), 5)

                cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 6)

                #right
                # 190 to 260 up
                #left
                # 160 to 90 down
                cv2.putText(img, str(int(angle)), (x2 - 50, y2 + 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)


            return int(angle)
        else:
            return None
        

