import cv2
import mediapipe as mp

class PoseDetector:
    def __init__(self, mode=False, upBody=False, smooth=True):
        self.mode = mode
        self.upBody = upBody
        self.smooth = smooth

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode, self.upBody, self.smooth)

    def find_Pose(self, img, draw=True):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(img_rgb)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks,
                                           self.mpPose.POSE_CONNECTIONS)
        return img

    def get_pose_landmarks(self):
        return self.results.pose_landmarks

    def detect_feet_lift_off(self, pose_landmarks, threshold=0.80):
        if pose_landmarks is not None:
            # Landmark indices for the left and right feet
            left_foot_indices = [31, 29, 27]  # Adjust as needed
            right_foot_indices = [32, 28, 30]  # Adjust as needed

            # Calculate average vertical position of left and right feet
            left_foot_avg_y = sum([pose_landmarks.landmark[i].y for i in left_foot_indices]) / len(left_foot_indices)
            right_foot_avg_y = sum([pose_landmarks.landmark[i].y for i in right_foot_indices]) / len(right_foot_indices)

            left_foot_lift_off_count = 0
            right_foot_lift_off_count = 0

            self.left_foot_lifted = False
            self.right_foot_lifted = False

            if not self.left_foot_lifted and left_foot_avg_y >= threshold:
                self.left_foot_lifted = True
                left_foot_lift_off_count += 1

            if self.left_foot_lifted and left_foot_avg_y < threshold:
                self.left_foot_lifted = False

            if not self.right_foot_lifted and right_foot_avg_y >= threshold:
                self.right_foot_lifted = True
                right_foot_lift_off_count += 1

            if self.right_foot_lifted and right_foot_avg_y < threshold:
                self.right_foot_lifted = False
            

        return left_foot_lift_off_count, right_foot_lift_off_count
    

    def pose_landmarks_drawings(self, img, pose_landmarks, p1, p2, p3, p4, p5, drawpoints):
        if pose_landmarks is not None:
            x1, y1 = int(pose_landmarks.landmark[p1].x * img.shape[1]), int(pose_landmarks.landmark[p1].y * img.shape[0])
            x2, y2 = int(pose_landmarks.landmark[p2].x * img.shape[1]), int(pose_landmarks.landmark[p2].y * img.shape[0])
            x3, y3 = int(pose_landmarks.landmark[p3].x * img.shape[1]), int(pose_landmarks.landmark[p3].y * img.shape[0])
            x4, y4 = int(pose_landmarks.landmark[p4].x * img.shape[1]), int(pose_landmarks.landmark[p4].y * img.shape[0])
            x5, y5 = int(pose_landmarks.landmark[p5].x * img.shape[1]), int(pose_landmarks.landmark[p5].y * img.shape[0])

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

                # LINE FOR RIGHT ANKLE
                cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 6)
                cv2.line(img, (x2, y2), (x3, y3), (0, 0, 255), 6)
                cv2.line(img, (x3, y3), (x1, y1), (0, 0, 255), 6)
                cv2.line(img, (x2, y2), (x4, y4), (0, 0, 255), 6)
                cv2.line(img, (x4, y4), (x5, y5), (0, 0, 255), 6)

def main():
    cap = cv2.VideoCapture(r'C:\Users\RID\Desktop\pose_estimation\aipose2\Exercise\weightloss\Workout Guide - Jog in Place.mp4')
    detector = PoseDetector()

    left_foot_lift_off_count = 0
    right_foot_lift_off_count = 0
    counter_left = 0
    counter_right = 0

    dir_left = 0
    dir_right = 0


    while True:
        success, img = cap.read()
        img = cv2.resize(img, (640, 480))
        img = detector.find_pose(img)
        pose_landmarks = detector.get_pose_landmarks()

        if pose_landmarks:
            left_foot_lift_off_count, right_foot_lift_off_count = detector.detect_feet_lift_off(pose_landmarks, threshold=0.80)
            
            if left_foot_lift_off_count == 1:
                if dir_left == 0:
                    counter_left += 1
                    dir_left = 1
            else: 
                if dir_left == 1:
                    dir_left = 0

            if right_foot_lift_off_count == 1:
                if dir_right == 0:
                    counter_right += 1
                    dir_right = 1
            else: 
                if dir_right == 1:
                    dir_right = 0

            
            # Add counter text to the image
            cv2.putText(img, f"Left foot lift off count: {counter_left}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(img, f"Right foot lift off count: {counter_right}", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("Image", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()



