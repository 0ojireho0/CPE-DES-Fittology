import cv2
import mediapipe as mp
import time
import math

# Define a class for pose detection
class poseDetector():

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
    def findAngle(self, img, p1, p2, p3, draw=True):
        if len(self.lmList) != 0:
            # Get the landmarks for the right arm
            x1, y1 = self.lmList[p1][1:]
            x2, y2 = self.lmList[p2][1:]
            x3, y3 = self.lmList[p3][1:]

            # Calculate the angle for the right arm
            angle = math.degrees(math.atan2(y3 - y2, x3 - x2) - math.atan2(y1 - y2, x1 - x2))
            
            if angle < 0:
                angle += 360

            # Draw the angle if required
            if draw:
                cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 3)
                cv2.line(img, (x3, y3), (x2, y2), (255, 255, 255), 3)
                cv2.circle(img, (x1, y1), 10, (0, 0, 255), cv2.FILLED)
                cv2.circle(img, (x1, y1), 15, (0, 0, 255), 2)
                cv2.circle(img, (x2, y2), 10, (0, 0, 255), cv2.FILLED)
                cv2.circle(img, (x2, y2), 15, (0, 0, 255), 2)
                cv2.circle(img, (x3, y3), 10, (0, 0, 255), cv2.FILLED)
                cv2.circle(img, (x3, y3), 15, (0, 0, 255), 2)
                cv2.putText(img, str(int(angle)), (x2 - 50, y2 + 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)

            return angle
        else:
            return None
        
    def feedback_chestpress(self, value):
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
            return "Congratulations! You've completed all 10 chest presses. Celebrate your accomplishment and take pride in your hard work."
        elif count == 9:
            return "Only one more to go, you're at 9 chest presses. Keep pushing! Maintain proper form and breathe rhythmically."
        elif count == 8:
            return "You've accomplished 8 chest presses. Great job! Focus on keeping your elbows stable and your movements controlled."
        elif count == 7:
            return "Well done on completing 7 chest presses. Keep up the good work! Focus on steady breathing and engaging your chest muscles."
        elif count == 6: 
            return "You're now at 6 chest presses. Stay focused and maintain a steady pace. Remember to keep your back flat on the bench."
        elif count == 5:
            return "You're halfway there with 5 chest presses completed. Keep going strong! Focus on full range of motion and proper form."
        elif count == 4:
            return "Great progress! You've reached 4 chest presses. Focus on keeping your movements smooth and controlled."
        elif count == 3:
            return "You've completed 3 chest presses. Keep it up! Remember to breathe and engage your chest and arm muscles."
        elif count == 2:
            return "Well done on completing 2 chest presses. You're doing great! Focus on maintaining control and powering through each rep."
        elif count == 1:
            return "You've executed 1 chest press. Keep pushing forward! Focus on form and consistency."
        elif count == 0:
            return "You haven't completed a single chest press. Don't give up! Take a moment to rest, then try again with determination."
        else:
            return "The count has exceeded the limit. Please reset the program."

    def right_arm_feedback(self, count):
        if count == 10:
            return "Congratulations! You've completed all 10 chest presses with your right arm. Celebrate your accomplishment and take pride in your hard work."
        elif count == 9:
            return "Only one more to go, you're at 9 chest presses with your right arm. Keep pushing! Maintain proper form and breathe rhythmically."
        elif count == 8:
            return "You've accomplished 8 chest presses with your right arm. Great job! Focus on keeping your elbows stable and your movements controlled."
        elif count == 7:
            return "Well done on completing 7 chest presses with your right arm. Keep up the good work! Focus on steady breathing and controlled movements."
        elif count == 6: 
            return "You're now at 6 chest presses with your right arm. Stay focused and maintain a steady pace. Remember to keep your back flat on the bench."
        elif count == 5:
            return "You're halfway there with 5 chest presses completed with your right arm. Keep going strong! Focus on full range of motion and proper form."
        elif count == 4:
            return "Great progress! You've reached 4 chest presses with your right arm. Focus on keeping your movements smooth and controlled."
        elif count == 3:
            return "You've completed 3 chest presses with your right arm. Keep it up! Remember to breathe and engage your chest and arm muscles."
        elif count == 2:
            return "Well done on completing 2 chest presses with your right arm. You're doing great! Focus on maintaining control and powering through each rep."
        elif count == 1:
            return "You've executed 1 chest press with your right arm. Keep pushing forward! Focus on form and consistency."
        elif count == 0:
            return "You haven't completed a single chest press with your right arm. Don't give up! Take a moment to rest, then try again with determination."
        else:
            return "The count has exceeded the limit. Please reset the program."

    def left_arm_unsuccessful_feedback(self, count):
        if count == 5:
            return "You've reached 5 attempted chest press with your left arm. Keep pushing! Each attempt is a step closer to your goal."
        elif count == 4:
            return "You've attempted 4 lunges with your left arm. Don't get discouraged! Use each attempt as a learning experience to improve."
        elif count == 3:
            return "You've attempted 3 lunges with your left arm. Keep trying! Persistence and practice will lead to progress."
        elif count == 2:
            return "You've attempted 2 lunges with your left arm. Stay focused! Consistency is key to mastering the movement."
        elif count == 1:
            return "You've attempted 1 lunge with your left arm, but faced some challenges. Don't give up! Take a moment to rest, then try again."
        elif count == 0:
            return "You haven't successfully completed a single chest press with your left leg. It's okay! Take it as a chance to learn and grow. Keep practicing!"

    def right_arm_unsuccessful_feedback(self, count):
        if count == 5:
            return "You've reached 5 attempted chest press with your right arm. Keep pushing! Each attempt is a step closer to your goal."
        elif count == 4:
            return "You've attempted 4 chest press with your right arm. Don't get discouraged! Use each attempt as a learning experience to improve."
        elif count == 3:
            return "You've attempted 3 chest press with your right arm. Keep trying! Persistence and practice will lead to progress."
        elif count == 2:
            return "You've attempted 2 chest press with your right arm. Stay focused! Consistency is key to mastering the movement."
        elif count == 1:
            return "You've attempted 1 lunge with your right leg, but faced some challenges. Don't give up! Take a moment to rest, then try again."
        elif count == 0:
            return "You haven't successfully completed a single lunge with your right leg. It's okay! Take it as a chance to learn and grow. Keep practicing!"

    


