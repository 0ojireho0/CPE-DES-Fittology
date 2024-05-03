import cv2
import mediapipe as mp
import time
import math

# Define a class for pose detection
class poseDetectorSideLegRaises():

    def __init__(self, mode=False, upBody=False, smooth=True):

        # Initialize parameters for pose detection
        self.mode = mode
        self.upBody = upBody
        self.smooth = smooth

        # Initialize mediapipe drawing utilities and pose model
        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode, self.upBody, self.smooth)

    # Function find pose landmarks in the image 
    def findPose(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks,
                                           self.mpPose.POSE_CONNECTIONS)
        return img

    # Function to find landmarks positions
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

    # Function to calculate angle between three points for the right arm
    def SideLegRight(self, img, p1, p2, p3, p4, draw):
        if len(self.lmList) != 0:


            x1, y1 = self.lmList[p1][1], self.lmList[p1][2]
            x2, y2 = self.lmList[p2][1], self.lmList[p2][2]
            x3, y3 = self.lmList[p3][1], self.lmList[p3][2]
            x4, y4 = self.lmList[p4][1], self.lmList[p4][2]

            angle = math.degrees(math.atan2(y3 - y2, x3 - x2) - math.atan2(y1 - y2, x1 - x2))
            
            if angle < 0:
                angle += 360

            # Draw the angle if required
            if draw:

                cv2.circle(img, (x2, y2), 10, (255, 0, 255), 5)
                cv2.circle(img, (x2, y2), 15, (0, 255, 0), 5)
                cv2.circle(img, (x3, y3), 10, (255, 0, 255), 5)
                cv2.circle(img, (x3, y3), 15, (0, 255, 0), 5)
                cv2.circle(img, (x4, y4), 10, (255, 0, 255), 5)
                cv2.circle(img, (x4, y4), 15, (0, 255, 0), 5)

                cv2.line(img, (x2, y2), (x3, y3), (0, 0, 255), 6)
                cv2.line(img, (x3, y3), (x4, y4), (0, 0, 255), 6)

                cv2.putText(img, str(int(angle)), (x2 - 50, y2 + 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)

            return int(angle)
        else:
            return None
        
    def SideLegLeft(self, img, p1, p2, p3, p4, draw):
            if len(self.lmList) != 0:

                x1, y1 = self.lmList[p1][1], self.lmList[p1][2]
                x2, y2 = self.lmList[p2][1], self.lmList[p2][2]
                x3, y3 = self.lmList[p3][1], self.lmList[p3][2]
                x4, y4 = self.lmList[p4][1], self.lmList[p4][2]

                angle = math.degrees(math.atan2(y3 - y2, x3 - x2) - math.atan2(y1 - y2, x1 - x2))
                
                if angle < 0:
                    angle += 360

                # Draw the angle if required
                if draw:

                    cv2.circle(img, (x2, y2), 10, (255, 0, 255), 5)
                    cv2.circle(img, (x2, y2), 15, (0, 255, 0), 5)
                    cv2.circle(img, (x3, y3), 10, (255, 0, 255), 5)
                    cv2.circle(img, (x3, y3), 15, (0, 255, 0), 5)
                    cv2.circle(img, (x4, y4), 10, (255, 0, 255), 5)
                    cv2.circle(img, (x4, y4), 15, (0, 255, 0), 5)

                    cv2.line(img, (x4, y4), (x2, y2), (0, 0, 255), 6)

                    cv2.putText(img, str(int(angle)), (x2 - 50, y2 + 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)

                return int(angle)
            else:
                return None
