import cv2
import mediapipe as mp
import time
import math
import numpy as np

class poseDetectorHighKneeTap():

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
    
    def HighKneeTap(self, img, p1, p2, p3, drawpoints):
        if len(self.lmList) != 0:
            x1, y1 = self.lmList[p1][1], self.lmList[p1][2]
            x2, y2 = self.lmList[p2][1], self.lmList[p2][2]
            x3, y3 = self.lmList[p3][1], self.lmList[p3][2]

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
        
    def feedback_highkneetap(self, value):
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

    def left_leg_feedback(self, count):
        if count == 10:
            return "Congratulations! You've completed all 10 high knee taps. Celebrate your accomplishment and take pride in your hard work."
        elif count == 9:
            return "Only one more to go, you're at 9 high knee taps. Keep pushing! Maintain proper form and breathe rhythmically."
        elif count == 8:
            return "You've accomplished 8 high knee taps. Great job! Focus on keeping your back straight and your movements controlled."
        elif count == 7:
            return "Well done on completing 7 high knee taps. Keep up the good work! Focus on steady breathing and engaging your core."
        elif count == 6: 
            return "You're now at 6 high knee taps. Stay focused and maintain a steady pace. Remember to bring your knees up as high as you can with each tap."
        elif count == 5:
            return "You're halfway there with 5 high knee taps completed. Keep going strong! Focus on lifting your knees explosively and maintaining balance."
        elif count == 4:
            return "Great progress! You've reached 4 high knee taps. Focus on maintaining a smooth and controlled motion."
        elif count == 3:
            return "You've completed 3 high knee taps. Keep it up! Remember to engage your core and drive your knees upward with each tap."
        elif count == 2:
            return "Well done on completing 2 high knee taps. You're doing great! Focus on maintaining control and lifting your knees with power."
        elif count == 1:
            return "You've executed 1 high knee tap. Keep pushing forward! Focus on form and consistency."
        elif count == 0:
            return "You haven't completed a single high knee tap. Don't give up! Take a moment to rest, then try again with determination."
        else:
            return "The count has exceeded the limit. Please reset the program."

    def right_leg_feedback(self, count):
        if count == 10:
            return "Congratulations! You've completed all 10 high knee taps with your right leg. Celebrate your accomplishment and take pride in your hard work."
        elif count == 9:
            return "Only one more to go, you're at 9 high knee taps with your right leg. Keep pushing! Maintain proper form and breathe rhythmically."
        elif count == 8:
            return "You've accomplished 8 high knee taps with your right leg. Great job! Focus on keeping your leg steady and your movements controlled."
        elif count == 7:
            return "Well done on completing 7 high knee taps with your right leg. Keep up the good work! Focus on steady breathing and engaging your core muscles."
        elif count == 6: 
            return "You're now at 6 high knee taps with your right leg. Stay focused and maintain a steady pace. Remember to lift your knee as high as possible with each tap."
        elif count == 5:
            return "You're halfway there with 5 high knee taps completed with your right leg. Keep going strong! Focus on lifting your knee explosively and maintaining balance."
        elif count == 4:
            return "Great progress! You've reached 4 high knee taps with your right leg. Focus on maintaining a smooth and controlled motion."
        elif count == 3:
            return "You've completed 3 high knee taps with your right leg. Keep it up! Remember to engage your core and lift your knee upward with each tap."
        elif count == 2:
            return "Well done on completing 2 high knee taps with your right leg. You're doing great! Focus on maintaining control and lifting your knee with power."
        elif count == 1:
            return "You've executed 1 high knee tap with your right leg. Keep pushing forward! Focus on form and consistency."
        elif count == 0:
            return "You haven't completed a single high knee tap with your right leg. Don't give up! Take a moment to rest, then try again with determination."
        else:
            return "The count has exceeded the limit. Please reset the program."

    def left_leg_unsuccessful_feedback(self, count):
        if count == 5:
            return "You've reached 5 attempted high knee taps with your left leg. Keep pushing! Each attempt is a step closer to your goal."
        elif count == 4:
            return "You've attempted 4 high knee taps with your left leg. Don't get discouraged! Use each attempt as a learning experience to improve."
        elif count == 3:
            return "You've attempted 3 high knee taps with your left leg. Keep trying! Persistence and practice will lead to progress."
        elif count == 2:
            return "You've attempted 2 high knee taps with your left leg. Stay focused! Consistency is key to mastering the movement."
        elif count == 1:
            return "You've attempted 1 high knee tap with your left leg, but faced some challenges. Don't give up! Take a moment to rest, then try again."
        elif count == 0:
            return "You haven't successfully completed a single high knee tap with your left leg. It's okay! Take it as a chance to learn and grow. Keep practicing!"

    def right_leg_unsuccessful_feedback(self, count):
        if count == 5:
            return "You've reached 5 attempted high knee taps with your right leg. Keep pushing! Each attempt is a step closer to your goal."
        elif count == 4:
            return "You've attempted 4 high knee taps with your right leg. Don't get discouraged! Use each attempt as a learning experience to improve."
        elif count == 3:
            return "You've attempted 3 high knee taps with your right leg. Keep trying! Persistence and practice will lead to progress."
        elif count == 2:
            return "You've attempted 2 high knee taps with your right leg. Stay focused! Consistency is key to mastering the movement."
        elif count == 1:
            return "You've attempted 1 high knee tap with your right leg, but faced some challenges. Don't give up! Take a moment to rest, then try again."
        elif count == 0:
            return "You haven't successfully completed a single high knee tap with your right leg. It's okay! Take it as a chance to learn and grow. Keep practicing!"




