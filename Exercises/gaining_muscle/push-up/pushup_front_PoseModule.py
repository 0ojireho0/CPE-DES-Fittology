import cv2
import mediapipe as mp
import time
import math
import numpy as np

class poseDetectorPushUp():

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

    def findPushupAngle(self, img, p1,p2,p3,p4,p5,p6, drawpoints):

        if len(self.lmList)!= 0:

            for point in [p1, p2, p3, p4, p5, p6]:
                if len(self.lmList[point]) < 3:
                    print(f"Error: Landmark {point} doesn't have enough values")
                    return None, None

            x1, y1 = self.lmList[p1][1], self.lmList[p1][2]
            x2, y2 = self.lmList[p2][1], self.lmList[p2][2]
            x3, y3 = self.lmList[p3][1], self.lmList[p3][2]
            x4, y4 = self.lmList[p4][1], self.lmList[p4][2]
            x5, y5 = self.lmList[p5][1], self.lmList[p5][2]
            x6, y6 = self.lmList[p6][1], self.lmList[p6][2]


            lefthandangle = math.degrees(math.atan2(y3 - y2, x3 - x2) -
                                         math.atan2(y1 - y2, x1 - x2))
            
            if lefthandangle < 0:
                lefthandangle += 360

            righthandangle = math.degrees(math.atan2(y6 - y5, x6 - x5) -
                                          math.atan2(y4 - y5, x4 - x5))
            
            if righthandangle < 0:
                righthandangle += 360

            if drawpoints == True:
                cv2.circle(img,(x1,y1),10,(255,0,255),5)
                cv2.circle(img, (x1, y1), 15, (0,255, 0),5)
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

                cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 6)
                cv2.line(img, (x2, y2), (x3, y3), (0, 0, 255), 6)
                cv2.line(img, (x4, y4), (x5, y5), (0, 0, 255), 6)
                cv2.line(img, (x5, y5), (x6, y6), (0, 0, 255), 6)

                cv2.putText(img, str(int(lefthandangle)), (x2 - 50, y2 + 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
                cv2.putText(img, str(int(righthandangle)), (x5 - 50, y5 + 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)

                return int(lefthandangle), int(righthandangle)
            else:
                return None, None
            

    def isPushUpPosture(self, lmList):
        # Check if keypoints are available
        if len(lmList) < 5:
            return False

        # Extract keypoint coordinates
        x_values = [lm[1] for lm in lmList]
        y_values = [lm[2] for lm in lmList]

        # Calculate torso height as the distance between the shoulders and the hips
        torso_height = np.abs(y_values[11] - y_values[23])

        # Calculate average arm length as the distance between the shoulder and elbow joints
        avg_arm_length = np.mean([np.abs(y_values[11] - y_values[13]), np.abs(y_values[12] - y_values[14])])

        # Calculate the angle of the torso relative to the ground
        torso_angle = np.arctan2(y_values[11] - y_values[23], x_values[11] - x_values[23])

        # Check if the person is in a push-up posture based on the approximate shape of the body
        # and the angle of the torso
        if torso_height > 0.2 * avg_arm_length and torso_angle < np.pi / 5:  # Adjust the thresholds as needed
            return True
        else:
            return False

    def feedback_pushup(self, value):
    # Check if the condition for feedback is met
        if value >= 100:
            return "Well done!"
        elif 90 >= value >= 1:
            return f"Keep pushing! you are at {int(value)}%"
        elif value == 0:
            return "Start any moment now!"
        return None  # No feedback if condition is not met

    def update_next_per_left(self, next_per_left):
        self.next_per_left = next_per_left

    def left_arm_feedback(self, count):
        if count == 10:
            return "Congratulations! You've completed all 10 push-ups with your left arm. Celebrate your accomplishment and take pride in your hard work."
        elif count == 9:
            return "Only one more to go, you're at 9 push-ups with your left arm. Keep pushing! Maintain proper form and breathe rhythmically."
        elif count == 8:
            return "You've accomplished 8 push-ups with your left arm. Great job! Focus on keeping your body aligned and engaging your core."
        elif count == 7:
            return "Well done on completing 7 push-ups with your left arm. Keep up the good work! Focus on steady breathing and controlled movements."
        elif count == 6: 
            return "You're now at 6 push-ups with your left arm. Stay focused and maintain a steady pace. Remember to keep your body stable throughout."
        elif count == 5:
            return "You're halfway there with 5 push-ups completed with your left arm. Keep going strong! Focus on full range of motion and proper form."
        elif count == 4:
            return "Great progress! You've reached 4 push-ups with your left arm. Focus on keeping your elbows close to your body and your back straight."
        elif count == 3:
            return "You've completed 3 push-ups with your left arm. Keep it up! Remember to breathe and engage your chest, arms, and core muscles."
        elif count == 2:
            return "Well done on completing 2 push-ups with your left arm. You're doing great! Focus on maintaining control and powering through each rep."
        elif count == 1:
            return "You've executed 1 push-up with your left arm out of the planned 10. Keep pushing forward! Focus on form and consistency."
        elif count == 0:
            return "You haven't completed a single push-up with your left arm. Don't give up! Take a moment to rest, then try again with determination."
        else:
            return "The count has exceeded the limit. Please reset the program."

    def right_arm_feedback(self, count):
        if count == 10:
            return "Congratulations! You've completed all 10 push-ups with your right arm. Celebrate your accomplishment and take pride in your hard work."
        elif count == 9:
            return "Only one more to go, you're at 9 push-ups with your right arm. Keep pushing! Maintain proper form and breathe rhythmically."
        elif count == 8:
            return "You've accomplished 8 push-ups with your right arm. Great job! Focus on keeping your body aligned and engaging your core."
        elif count == 7:
            return "Well done on completing 7 push-ups with your right arm. Keep up the good work! Focus on steady breathing and controlled movements."
        elif count == 6: 
            return "You're now at 6 push-ups with your right arm. Stay focused and maintain a steady pace. Remember to keep your body stable throughout."
        elif count == 5:
            return "You're halfway there with 5 push-ups completed with your right arm. Keep going strong! Focus on full range of motion and proper form."
        elif count == 4:
            return "Great progress! You've reached 4 push-ups with your right arm. Focus on keeping your elbows close to your body and your back straight."
        elif count == 3:
            return "You've completed 3 push-ups with your right arm. Keep it up! Remember to breathe and engage your chest, arms, and core muscles."
        elif count == 2:
            return "Well done on completing 2 push-ups with your right arm. You're doing great! Focus on maintaining control and powering through each rep."
        elif count == 1:
            return "You've executed 1 push-up with your right arm out of the planned 10. Keep pushing forward! Focus on form and consistency."
        elif count == 0:
            return "You haven't completed a single push-up with your right arm. Don't give up! Take a moment to rest, then try again with determination."
        else:
            return "The count has exceeded the limit. Please reset the program."

    def left_arm_unsuccessful_feedback(self, count):
        if count == 5:
            return "You've reached 5 attempted push-ups with your left arm. Keep pushing! Each attempt is a step closer to your goal."
        elif count == 4:
            return "You've attempted 4 push-ups with your left arm. Don't get discouraged! Use each attempt as a learning experience to improve."
        elif count == 3:
            return "You've attempted 3 push-ups with your left arm. Keep trying! Persistence and practice will lead to progress."
        elif count == 2:
            return "You've attempted 2 push-ups with your left arm. Stay determined! Remember, every effort counts towards your improvement."
        elif count == 1:
            return "You've attempted 1 push-up with your left arm, but faced some challenges. Don't give up! Take a moment to rest, then try again."
        elif count == 0:
            return "You haven't successfully completed a single push-up with your left arm. It's okay! Take it as a chance to learn and grow. Keep practicing!"

    def right_arm_unsuccessful_feedback(self, count):
        if count == 5:
            return "You've reached 5 attempted push-ups with your right arm. Keep pushing! Each attempt is a step closer to your goal."
        elif count == 4:
            return "You've attempted 4 push-ups with your right arm. Don't get discouraged! Use each attempt as a learning experience to improve."
        elif count == 3:
            return "You've attempted 3 push-ups with your right arm. Keep trying! Persistence and practice will lead to progress."
        elif count == 2:
            return "You've attempted 2 push-ups with your right arm. Stay determined! Remember, every effort counts towards your improvement."
        elif count == 1:
            return "You've attempted 1 push-up with your right arm, but faced some challenges. Don't give up! Take a moment to rest, then try again."
        elif count == 0:
            return "You haven't successfully completed a single push-up with your right arm. It's okay! Take it as a chance to learn and grow. Keep practicing!"
