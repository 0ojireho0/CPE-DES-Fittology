import cv2
import mediapipe as mp
import time
import math
import numpy as np

class poseDetectorPlankToeTaps():

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

    def PlankToeTaps(self, img, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, drawpoints):
        if len(self.lmList) != 0:

            x1, y1 = self.lmList[p1][1], self.lmList[p1][2]
            x2, y2 = self.lmList[p2][1], self.lmList[p2][2]
            x3, y3 = self.lmList[p3][1], self.lmList[p3][2]
            x4, y4 = self.lmList[p4][1], self.lmList[p4][2]
            x5, y5 = self.lmList[p5][1], self.lmList[p5][2]
            x6, y6 = self.lmList[p6][1], self.lmList[p6][2]
            x7, y7 = self.lmList[p7][1], self.lmList[p7][2]
            x8, y8 = self.lmList[p8][1], self.lmList[p8][2]
            x9, y9 = self.lmList[p9][1], self.lmList[p9][2]
            x10, y10 = self.lmList[p10][1], self.lmList[p10][2]
            x11, y11 = self.lmList[p11][1], self.lmList[p11][2]
            x12, y12 = self.lmList[p12][1], self.lmList[p12][2]
            x13, y13 = self.lmList[p13][1], self.lmList[p13][2]
            x14, y14 = self.lmList[p14][1], self.lmList[p14][2]


            distance1 = math.sqrt((x14 - x1) ** 2 + (y14 - y1) ** 2)
            midpoint_x = int((x1 + x14) / 2)
            midpoint_y = int((y1 + y14) / 2)

            distance2 = math.sqrt((x8 - x7) ** 2 + (y8 - y7) ** 2)
            midpoint_x = int((x7 + x8) / 2)
            midpoint_y = int((y7 + y8) / 2)
                    
            if drawpoints:
                cv2.circle(img, (x1, y1), 10, (255, 0, 255), 5)
                cv2.circle(img, (x1, y1), 15, (0, 255, 0), 5)
                cv2.circle(img, (x2, y2), 10, (255, 0, 255), 5)
                cv2.circle(img, (x2, y2), 15, (0, 255, 0), 5)
                cv2.circle(img, (x3, y3), 10, (255, 0, 255), 5)
                cv2.circle(img, (x3, y3), 15, (0, 255, 0), 5)
                cv2.circle(img, (x4, y4), 10, (255, 0, 255), 5)
                cv2.circle(img, (x4, y4), 15, (0, 255, 0), 5)
                cv2.circle(img, (x5, y5), 10, (255, 0, 255), 5)
                cv2.circle(img, (x5, y5), 15, (0, 255, 0), 5)
                cv2.circle(img, (x6, y6), 10, (255, 0, 255), 5)
                cv2.circle(img, (x6, y6), 15, (0, 255, 0), 5)
                cv2.circle(img, (x7, y7), 10, (255, 0, 255), 5)
                cv2.circle(img, (x7, y7), 15, (0, 255, 0), 5)
                cv2.circle(img, (x8, y8), 10, (255, 0, 255), 5)
                cv2.circle(img, (x8, y8), 15, (0, 255, 0), 5)
                cv2.circle(img, (x9, y9), 10, (255, 0, 255), 5)
                cv2.circle(img, (x9, y9), 15, (0, 255, 0), 5)
                cv2.circle(img, (x10, y10), 10, (255, 0, 255), 5)
                cv2.circle(img, (x10, y10), 15, (0, 255, 0), 5)
                cv2.circle(img, (x11, y11), 10, (255, 0, 255), 5)
                cv2.circle(img, (x11, y11), 15, (0, 255, 0), 5)
                cv2.circle(img, (x12, y12), 10, (255, 0, 255), 5)
                cv2.circle(img, (x12, y12), 15, (0, 255, 0), 5)
                cv2.circle(img, (x13, y13), 10, (255, 0, 255), 5)
                cv2.circle(img, (x13, y13), 15, (0, 255, 0), 5)
                cv2.circle(img, (x14, y14), 10, (255, 0, 255), 5)
                cv2.circle(img, (x14, y14), 15, (0, 255, 0), 5)

                cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 6)
                cv2.line(img, (x2, y2), (x3, y3), (0, 0, 255), 6)
                cv2.line(img, (x3, y3), (x4, y4), (0, 0, 255), 6)
                cv2.line(img, (x4, y4), (x5, y5), (0, 0, 255), 6)
                cv2.line(img, (x5, y5), (x6, y6), (0, 0, 255), 6)
                cv2.line(img, (x6, y6), (x7, y7), (0, 0, 255), 6)

                cv2.line(img, (x8, y8), (x9, y9), (0, 0, 255), 6)
                cv2.line(img, (x9, y9), (x10, y10), (0, 0, 255), 6)
                cv2.line(img, (x10, y10), (x11, y11), (0, 0, 255), 6)
                cv2.line(img, (x11, y11), (x12, y12), (0, 0, 255), 6)
                cv2.line(img, (x12, y12), (x13, y13), (0, 0, 255), 6)
                cv2.line(img, (x13, y13), (x14, y14), (0, 0, 255), 6)

                cv2.putText(img, f"{int(distance1)}", (midpoint_x, midpoint_y), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
                cv2.putText(img, f"{int(distance2)}", (midpoint_x, midpoint_y), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
                return int(distance1), int(distance2)
            