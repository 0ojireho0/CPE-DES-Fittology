from flask import Flask, render_template, request, redirect, url_for, session, Response, jsonify
from flask_mysqldb import MySQL
import os


# -------------- FOR GAINING MUSCLE ---------------
import cv2
import numpy as np
import time
import BicepCurl_PoseModule as pm_bicep
import PushUp_PoseModule as pm_pushup
import cvzone
import math
# ----------------- FOR GAINING MUSCLE -------------

app = Flask(__name__, template_folder='./templates')
app.secret_key = 'your-secret-key'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask_users'

mysql = MySQL(app)


# --------- FOR BICEP ------------
# Initialize posemodule as detector
detector_bicep = pm_bicep.poseDetector()

# Initialize variables for counting curls
count_bicep_left = 0
count_bicep_right = 0
dir_bicep_left = 0
dir_bicep_right = 0

start_time = None # starts time
countdown_before_exercise = None
countdown_repetition_time = 10
repetition_time = 70 # duration time
display_bicep = False

rest_bicep_start_time = time.time()

bar_left = 0
bar_right = 0
per_left = 0
per_right = 0
angle_left = 0
angle_right = 0
# --------- END FOR BICEP ---------------------

# --------- FOR BICEP SET 2 ------------
# Initialize posemodule as detector
detector_bicep = pm_bicep.poseDetector()

# Initialize variables for counting curls
count_bicep_left_set2 = 0
count_bicep_right_set2 = 0
dir_bicep_left_set2 = 0
dir_bicep_right_set2 = 0

start_time_bicep_set2 = time.time() # starts time
countdown_before_exercise_bicep_set2 = None
countdown_repetition_time_bicep_set2 = 10
repetition_time_bicep_set2 = 60 # duration time
display_bicep_set2 = True

rest_bicep_start_time_set2 = time.time()

bar_left_set2 = 0
bar_right_set2 = 0
per_left_set2 = 0
per_right_set2 = 0
angle_left_set2 = 0
angle_right_set2 = 0
# --------- END FOR BICEP SET 2 ---------------------

# --------- FOR BICEP SET 3 ------------
# Initialize posemodule as detector
detector_bicep = pm_bicep.poseDetector()

# Initialize variables for counting curls
count_bicep_left_set3 = 0
count_bicep_right_set3 = 0
dir_bicep_left_set3 = 0
dir_bicep_right_set3 = 0

start_time_bicep_set3 = time.time() # starts time
countdown_before_exercise_bicep_set3 = None
countdown_repetition_time_bicep_set3 = 10
repetition_time_bicep_set3 = 60 # duration time
display_bicep_set3 = True

rest_bicep_start_time_set3 = time.time()

bar_left_set3 = 0
bar_right_set3 = 0
per_left_set3 = 0
per_right_set3 = 0
angle_left_set3 = 0
angle_right_set3 = 0
# --------- END FOR BICEP SET 3 ---------------------

# ----------- FOR PUSH UP ---------------
# Import class
detector_pushup = pm_pushup.poseDetectorPushUp()

# Initialize variables
count_pushup = 0  # count_pushup of reps
pushup_dir = 0  # pushup_direction
pTime = 0  # Time
start_time_pushup = time.time()  # Start time
repetition_time_pushup = 60  # Repetition time

# Display info
display_pushup = True

per_right_pushup = 0
per_left_pushup = 0
bar_left_pushup = 0
bar_right_pushup = 0 

leftangle_pushup = 0
rightangle_pushup = 0
# ----------- END FOR PUSH UP --------------

# Add this variable at the beginning of your code


picFolder = os.path.join('static', 'images')
app.config['UPLOAD_FOLDER'] = picFolder


# ----------------------- THIS IS FOR LOGIN -------------------------------------
@app.route('/')
def home():
    if 'username' in session:
        return render_template('home.html', username=session.get('username'))
    else:
        return render_template('home.html')


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     login_hagdanan = os.path.join(app.config['UPLOAD_FOLDER'], 'login_hagdanan.png')
#     logo = os.path.join(app.config['UPLOAD_FOLDER'], 'Logo.png')
   
    
#     if request.method == 'POST':
#         username = request.form['username']
#         pwd = request.form['password']
#         cur = mysql.connection.cursor()
#         cur.execute(f"SELECT username, fullname, exercise, password FROM tbl_users WHERE username = '{username}' ")
#         user = cur.fetchone()
#         cur.close()
#         if user and pwd == user[3]:  # assuming password is the fourth column
#             session['username'] = user[0]
#             session['fullname'] = user[1]  # storing full name in session
#             session['exercise'] = user[2]  # storing exercise in session
#             return redirect(url_for('home'))
#         else:
#             return render_template('login.html', error='Invalid username or password', login_hagdanan = login_hagdanan, logo = logo)
#     return render_template('login.html', login_hagdanan = login_hagdanan, logo = logo)




@app.route('/register', methods=['GET', 'POST'])
def register():
    logo = os.path.join(app.config['UPLOAD_FOLDER'], 'Logo.png')
    if request.method == "POST":
        username = request.form['username']
        fullname = request.form['fullname']
        # pwd = request.form['password']
        injuries = request.form['injuries']
        injuries2 = request.form['injuries2']
        exercise = request.form['exercise']
        
        # Check if either injuries or injuries2 is set to "yes"
        if injuries == "yes" or injuries2 == "yes":
            # If yes, return some message or redirect back to the registration page
            return render_template('register.html', not_allowed="Sorry, registration not allowed for users with injuries", logo = logo)
        
        # If neither injuries nor injuries2 is set to "yes", proceed with registration
        session['username'] = username
        session['fullname'] = fullname
        session['exercise'] = exercise
        
        return redirect(url_for('home'))
    
    return render_template('register.html', logo = logo)


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

# ------------------------------ END FOR LOGIN ------------------------------------ 

@app.route('/start_exercise')
def start_exercise():
    global exercise_mode
    if session['exercise'] == "muscle_gain":
        exercise_mode = "bicep_curl"
        return redirect(url_for('muscleGain')) #THIS URL IS SUPPOSED FOR GAINING MUSCLES
    elif session['exercise'] == "loss_weight":
        #LALAGYAN KO NG FIRST EXERCISE FOR LOSS WEIGHT
        return redirect(url_for('lossWeight')) #THIS URL IS SUPPOSED FOR LOSS WEIGHT



# -------------- FOR GAINING MUSCLE --------------------
# Generator function to stream frames
def gen_frames():

    cap = cv2.VideoCapture(0)
    while True:
        success, img = cap.read()
        if not success:
            break
        else:

            if exercise_mode == "bicep_curl":
                img_with_faces = detect_bicep_curls(img)
            if exercise_mode == "rest_bicep":
                img_with_faces = rest_bicep(img)
            if exercise_mode == "bicep_curl_set2":
                img_with_faces = detect_bicep_curls_set2(img)
            if exercise_mode == "rest_bicep_set2":
                img_with_faces = rest_bicep_set2(img)
            if exercise_mode == "bicep_curl_set3":
                img_with_faces = detect_bicep_curls_set3(img)
            if exercise_mode == "rest_bicep_set3":
                img_with_faces = rest_bicep_set3(img)
            if exercise_mode == "push_up":
                img_with_faces = detect_push_up(img)


            ret, buffer = cv2.imencode('.jpg', img_with_faces)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/gainMuscle')
def muscleGain():
    if 'username' in session and session['exercise'] == "muscle_gain":
        bicep_curl = os.path.join(app.config['UPLOAD_FOLDER'], 'bicep_curl.jpg')
        push_up = os.path.join(app.config['UPLOAD_FOLDER'], 'Pushups.jpg')
        return render_template('gainingMuscle.html', bicep_curl = bicep_curl, push_up = push_up)
    else:
        return redirect(url_for('home'))

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/exercise_mode')
def get_exercise_mode():
    return jsonify({'exercise_mode': exercise_mode})

@app.route('/start_timer', methods=['POST'])
def start_timer():
    global start_time, countdown_before_exercise
    countdown_before_exercise = time.time()
    start_time = time.time()  # Start the timer
    return jsonify({'message': 'Timer started'}), 200



# Function to detect bicep curls
def detect_bicep_curls(img):
    global display_bicep, count_bicep_left, count_bicep_right, dir_bicep_left, dir_bicep_right, start_time, color_left, color_right, exercise_mode, per_right, per_left, bar_right, angle_left, angle_right, bar_left, countdown_before_exercise, countdown_repetition_time, rest_bicep_start_time

    img = cv2.resize(img, (1280, 720))


    countdown_elapsed_time = time.time() - countdown_before_exercise
    countdown_remaining_time = max(0, countdown_repetition_time - countdown_elapsed_time)
    if countdown_remaining_time <= 0:
        display_bicep = True

    # Timer - starts timer based on set duration
    elapsed_time = time.time() - start_time
    remaining_time = max(0, repetition_time - elapsed_time)



    # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Starting: {int(countdown_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

 
    

    if exercise_mode == "bicep_curl":
        if display_bicep:  # Check if to display counter, bar, and percentage
            img = detector_bicep.findPose(img, False) # initializes img as variable for findpose function
            lmList_bicep = detector_bicep.findPosition(img, False) # initializes lmList_bicep as variable for findPosition function

            # Define hand angles outside the if statement
            if len(lmList_bicep) != 0:
                angle_left = detector_bicep.findAngle(img, 11, 13, 15)
                angle_right = detector_bicep.findAngle(img, 12, 14, 16) # defines right arm landmark keypoints
                # (refer to mediapipe landmark mapping for number equivalent)
        
                # Interpolate angle to percentage and position on screen
                per_left = np.interp(angle_left, (30, 130), (100, 0)) # first parenthesis, the value threshold of the angle. Second, represents the interp value
                bar_left = np.interp(angle_left, (30, 140), (200, 400)) # *

                per_right = np.interp(angle_right, (200, 340), (0, 100)) # *
                bar_right = np.interp(angle_right, (200, 350), (400, 200)) # *

                # Check for the left dumbbell curls
                color_left = (255, 0, 255)
                if per_left == 100: 
                    color_left = (0, 255, 0)
                    if dir_bicep_left == 0 and count_bicep_left < 5:
                        count_bicep_left += 0.5
                        if count_bicep_left == 5:  # Check if count reaches 5
                            dir_bicep_left = -1  # Set direction to stop incrementing
                        else:
                            dir_bicep_left = 1


                if per_left == 0:
                    color_left = (0, 255, 0) 
                    if dir_bicep_left == 1 and count_bicep_left < 5:
                        count_bicep_left += 0.5
                        if count_bicep_left == 5:  # Check if count reaches 5
                            dir_bicep_left = -1  # Set direction to stop incrementing
                        else:
                            dir_bicep_left = 0  

                # Check for the right dumbbell curls
                color_right = (255, 0, 255)
                if per_right == 100: 
                    color_right = (0, 255, 0)
                    if dir_bicep_right == 0 and count_bicep_right < 5:
                        count_bicep_right += 0.5
                        if count_bicep_right == 5:  # Check if count reaches 5
                            dir_bicep_right = -1  # Set direction to stop incrementing
                        else:
                            dir_bicep_right = 1

                if per_right == 0:
                    color_right = (0, 255, 0) 
                    if dir_bicep_right == 1 and count_bicep_right < 5:
                        count_bicep_right += 0.5
                        if count_bicep_right == 5:  # Check if count reaches 5
                            dir_bicep_right = -1  # Set direction to stop incrementing
                        else:
                            dir_bicep_right = 0 

            # label
            cvzone.putTextRect(img, 'Bicep Curl Tracker', [345, 30], thickness=2, border=2, scale=2.5) 

            # Draw rectangle behind the timer text
            cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

            # Draw timer text above the rectangle
            timer_text = f"Time left: {int(remaining_time)}s"
            cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

            # bar
            cv2.putText(img, f"R {int(per_right)}%" , (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
            cv2.rectangle(img, (8, 200), (50, 400), (255, 255, 255), 5)
            cv2.rectangle(img, (8, int(bar_right)), (50, 400), (0, 0, 255), -1)

            cv2.putText(img, f"L {int(per_left)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
            cv2.rectangle(img, (952, 200), (995, 400), (255, 255, 255), 5)
            cv2.rectangle(img, (952, int(bar_left)), (995, 400), (0, 0, 255), -1)
            
            
            if angle_left < 40:
                cv2.rectangle(img, (952, int(bar_left)), (995, 400), (0, 255, 0), -1)

            if angle_right > 280:
                cv2.rectangle(img, (8, int(bar_right)), (50, 400), (0, 255, 0), -1)

        #count
        cv2.rectangle(img, (20, 20), (140, 130), (0, 0, 255), -1)
        cv2.putText(img, f"{int(count_bicep_right)}/5", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

        cv2.rectangle(img, (150, 20), (270, 130), (255, 0, 0), -1)
        cv2.putText(img, f"{int(count_bicep_left)}/5", (160, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

        if remaining_time <= 0:
            cvzone.putTextRect(img, "Time's Up", [345, 30], thickness=2, border=2, scale=2.5)
            display_bicep = False
            exercise_mode = "rest_bicep"
            # Reset variables for push-ups
            rest_bicep_start_time = time.time()

        if count_bicep_right == 5 and count_bicep_left == 5:
            cvzone.putTextRect(img, 'All Repetitions Completed', [345, 30], thickness=2, border=2, scale=2.5)
            display_bicep = False
            exercise_mode = "rest_bicep"
            # Reset variables for push-ups
            rest_bicep_start_time = time.time()

    return img

def rest_bicep(img):
    global exercise_mode, rest_bicep_start_time, start_time_bicep_set2
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_bicep_start_time
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "bicep_curl_set2"
        start_time_bicep_set2 = time.time()
    return img


def detect_bicep_curls_set2(img):
    global detector_bicep, count_bicep_left_set2, count_bicep_right_set2, dir_bicep_left_set2, dir_bicep_right_set2, start_time_bicep_set2, display_bicep_set2,rest_bicep_start_time_set2, bar_left_set2, bar_right_set2, per_left_set2, per_right_set2, angle_left_set2, angle_right_set2, color_left, color_right, exercise_mode, repetition_time_bicep_set2

    img = cv2.resize(img, (1280, 720))

    elapsed_time = time.time() - start_time_bicep_set2
    remaining_time = max(0, repetition_time_bicep_set2 - elapsed_time)

    if exercise_mode == "bicep_curl_set2":
        if display_bicep_set2:  # Check if to display counter, bar, and percentage
            img = detector_bicep.findPose(img, False) # initializes img as variable for findpose function
            lmList_bicep = detector_bicep.findPosition(img, False) # initializes lmList_bicep as variable for findPosition function

            # Define hand angles outside the if statement
            if len(lmList_bicep) != 0:
                angle_left_set2 = detector_bicep.findAngle(img, 11, 13, 15)
                angle_right_set2 = detector_bicep.findAngle(img, 12, 14, 16) # defines right arm landmark keypoints
                # (refer to mediapipe landmark mapping for number equivalent)
                
                # Interpolate angle to percentage and position on screen
                per_left_set2 = np.interp(angle_left_set2, (30, 130), (100, 0)) # first parenthesis, the value threshold of the angle. Second, represents the interp value
                bar_left_set2 = np.interp(angle_left_set2, (30, 140), (200, 400)) # *

                per_right_set2 = np.interp(angle_right_set2, (200, 340), (0, 100)) # *
                bar_right_set2 = np.interp(angle_right_set2, (200, 350), (400, 200)) # *

                # Check for the left dumbbell curls
                color_left = (255, 0, 255)
                if per_left_set2 == 100: 
                    color_left = (0, 255, 0)
                    if dir_bicep_left_set2 == 0 and count_bicep_left_set2 < 5:
                        count_bicep_left_set2 += 0.5
                        if count_bicep_left_set2 == 5:  # Check if count reaches 5
                            dir_bicep_left_set2 = -1  # Set direction to stop incrementing
                        else:
                            dir_bicep_left_set2 = 1


                if per_left_set2 == 0:
                    color_left = (0, 255, 0) 
                    if dir_bicep_left_set2 == 1 and count_bicep_left_set2 < 5:
                        count_bicep_left_set2 += 0.5
                        if count_bicep_left_set2 == 5:  # Check if count reaches 5
                            dir_bicep_left_set2 = -1  # Set direction to stop incrementing
                        else:
                            dir_bicep_left_set2 = 0  

                # Check for the right dumbbell curls
                color_right = (255, 0, 255)
                if per_right_set2 == 100: 
                    color_right = (0, 255, 0)
                    if dir_bicep_right_set2 == 0 and count_bicep_right_set2 < 5:
                        count_bicep_right_set2 += 0.5
                        if count_bicep_right_set2 == 5:  # Check if count reaches 5
                            dir_bicep_right_set2 = -1  # Set direction to stop incrementing
                        else:
                            dir_bicep_right_set2 = 1

                if per_right_set2 == 0:
                    color_right = (0, 255, 0) 
                    if dir_bicep_right_set2 == 1 and count_bicep_right_set2 < 5:
                        count_bicep_right_set2 += 0.5
                        if count_bicep_right_set2 == 5:  # Check if count reaches 5
                            dir_bicep_right_set2 = -1  # Set direction to stop incrementing
                        else:
                            dir_bicep_right_set2 = 0 

            # label
            cvzone.putTextRect(img, 'Bicep Curl Tracker SET 2', [345, 30], thickness=2, border=2, scale=2.5) 

            # Draw rectangle behind the timer text
            cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

            # Draw timer text above the rectangle
            timer_text = f"Time left: {int(remaining_time)}s"
            cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

            # bar
            cv2.putText(img, f"R {int(per_right_set2)}%" , (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
            cv2.rectangle(img, (8, 200), (50, 400), (255, 255, 255), 5)
            cv2.rectangle(img, (8, int(bar_right_set2)), (50, 400), (0, 0, 255), -1)

            cv2.putText(img, f"L {int(per_left_set2)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
            cv2.rectangle(img, (952, 200), (995, 400), (255, 255, 255), 5)
            cv2.rectangle(img, (952, int(bar_left_set2)), (995, 400), (0, 0, 255), -1)
                    
                    
            if angle_left_set2 < 40:
                cv2.rectangle(img, (952, int(bar_left_set2)), (995, 400), (0, 255, 0), -1)

            if angle_right_set2 > 280:
                cv2.rectangle(img, (8, int(bar_right_set2)), (50, 400), (0, 255, 0), -1)

        #count
        cv2.rectangle(img, (20, 20), (140, 130), (0, 0, 255), -1)
        cv2.putText(img, f"{int(count_bicep_right_set2)}/5", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

        cv2.rectangle(img, (150, 20), (270, 130), (255, 0, 0), -1)
        cv2.putText(img, f"{int(count_bicep_left_set2)}/5", (160, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

        if remaining_time <= 0:
            cvzone.putTextRect(img, "Time's Up", [345, 30], thickness=2, border=2, scale=2.5)
            display_bicep_set2 = False
            exercise_mode = "rest_bicep_set2"
            # Reset variables for push-ups
            rest_bicep_start_time_set2 = time.time()

        if count_bicep_right_set2 == 5 and count_bicep_left_set2 == 5:
            cvzone.putTextRect(img, 'All Repetitions Completed', [345, 30], thickness=2, border=2, scale=2.5)
            display_bicep_set2 = False
            exercise_mode = "rest_bicep_set2"
            # Reset variables for push-ups
            rest_bicep_start_time_set2 = time.time()

    return img 

def rest_bicep_set2(img):
    global exercise_mode, rest_bicep_start_time_set2, start_time_bicep_set3
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_bicep_start_time_set2
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "bicep_curl_set3"
        start_time_bicep_set3 = time.time()

    return img

def detect_bicep_curls_set3(img):
    global detector_bicep, count_bicep_left_set3, count_bicep_right_set3, dir_bicep_left_set3, dir_bicep_right_set3, start_time_bicep_set3, display_bicep_set3,rest_bicep_start_time_set3, bar_left_set3, bar_right_set3, per_left_set3, per_right_set3, angle_left_set3, angle_right_set3, color_left, color_right, exercise_mode, repetition_time_bicep_set3

    img = cv2.resize(img, (1280, 720))

    elapsed_time = time.time() - start_time_bicep_set3
    remaining_time = max(0, repetition_time_bicep_set3 - elapsed_time)

    if exercise_mode == "bicep_curl_set3":
        if display_bicep_set3:  # Check if to display counter, bar, and percentage
            img = detector_bicep.findPose(img, False) # initializes img as variable for findpose function
            lmList_bicep = detector_bicep.findPosition(img, False) # initializes lmList_bicep as variable for findPosition function

            # Define hand angles outside the if statement
            if len(lmList_bicep) != 0:
                angle_left_set3 = detector_bicep.findAngle(img, 11, 13, 15)
                angle_right_set3 = detector_bicep.findAngle(img, 12, 14, 16) # defines right arm landmark keypoints
                # (refer to mediapipe landmark mapping for number equivalent)
                
                # Interpolate angle to percentage and position on screen
                per_left_set3 = np.interp(angle_left_set3, (30, 130), (100, 0)) # first parenthesis, the value threshold of the angle. Second, represents the interp value
                bar_left_set3 = np.interp(angle_left_set3, (30, 140), (200, 400)) # *

                per_right_set3 = np.interp(angle_right_set3, (200, 340), (0, 100)) # *
                bar_right_set3 = np.interp(angle_right_set3, (200, 350), (400, 200)) # *

                # Check for the left dumbbell curls
                color_left = (255, 0, 255)
                if per_left_set3 == 100: 
                    color_left = (0, 255, 0)
                    if dir_bicep_left_set3 == 0 and count_bicep_left_set3 < 5:
                        count_bicep_left_set3 += 0.5
                        if count_bicep_left_set3 == 5:  # Check if count reaches 5
                            dir_bicep_left_set3 = -1  # Set direction to stop incrementing
                        else:
                            dir_bicep_left_set3 = 1


                if per_left_set3 == 0:
                    color_left = (0, 255, 0) 
                    if dir_bicep_left_set3 == 1 and count_bicep_left_set3 < 5:
                        count_bicep_left_set3 += 0.5
                        if count_bicep_left_set3 == 5:  # Check if count reaches 5
                            dir_bicep_left_set3 = -1  # Set direction to stop incrementing
                        else:
                            dir_bicep_left_set3 = 0  

                # Check for the right dumbbell curls
                color_right = (255, 0, 255)
                if per_right_set3 == 100: 
                    color_right = (0, 255, 0)
                    if dir_bicep_right_set3 == 0 and count_bicep_right_set3 < 5:
                        count_bicep_right_set3 += 0.5
                        if count_bicep_right_set3 == 5:  # Check if count reaches 5
                            dir_bicep_right_set3 = -1  # Set direction to stop incrementing
                        else:
                            dir_bicep_right_set3 = 1

                if per_right_set3 == 0:
                    color_right = (0, 255, 0) 
                    if dir_bicep_right_set3 == 1 and count_bicep_right_set3 < 5:
                        count_bicep_right_set3 += 0.5
                        if count_bicep_right_set3 == 5:  # Check if count reaches 5
                            dir_bicep_right_set3 = -1  # Set direction to stop incrementing
                        else:
                            dir_bicep_right_set3 = 0 

            # label
            cvzone.putTextRect(img, 'Bicep Curl Tracker SET 3', [345, 30], thickness=2, border=2, scale=2.5) 

            # Draw rectangle behind the timer text
            cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

            # Draw timer text above the rectangle
            timer_text = f"Time left: {int(remaining_time)}s"
            cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

            # bar
            cv2.putText(img, f"R {int(per_right_set3)}%" , (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
            cv2.rectangle(img, (8, 200), (50, 400), (255, 255, 255), 5)
            cv2.rectangle(img, (8, int(bar_right_set3)), (50, 400), (0, 0, 255), -1)

            cv2.putText(img, f"L {int(per_left_set3)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
            cv2.rectangle(img, (952, 200), (995, 400), (255, 255, 255), 5)
            cv2.rectangle(img, (952, int(bar_left_set3)), (995, 400), (0, 0, 255), -1)
                    
                    
            if angle_left_set3 < 40:
                cv2.rectangle(img, (952, int(bar_left_set3)), (995, 400), (0, 255, 0), -1)

            if angle_right_set3 > 280:
                cv2.rectangle(img, (8, int(bar_right_set3)), (50, 400), (0, 255, 0), -1)

        #count
        cv2.rectangle(img, (20, 20), (140, 130), (0, 0, 255), -1)
        cv2.putText(img, f"{int(count_bicep_right_set3)}/5", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

        cv2.rectangle(img, (150, 20), (270, 130), (255, 0, 0), -1)
        cv2.putText(img, f"{int(count_bicep_left_set3)}/5", (160, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

        if remaining_time <= 0:
            cvzone.putTextRect(img, "Time's Up", [345, 30], thickness=2, border=2, scale=2.5)
            display_bicep_set3 = False
            exercise_mode = "rest_bicep_set3"
            # Reset variables for push-ups
            rest_bicep_start_time_set3 = time.time()

        if count_bicep_right_set3 == 5 and count_bicep_left_set3 == 5:
            cvzone.putTextRect(img, 'All Repetitions Completed', [345, 30], thickness=2, border=2, scale=2.5)
            display_bicep_set3 = False
            exercise_mode = "rest_bicep_set3"
            # Reset variables for push-ups
            rest_bicep_start_time_set3 = time.time()
    
    return img 

def rest_bicep_set3(img):
    global exercise_mode, rest_bicep_start_time_set3, start_time_pushup
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_bicep_start_time_set3
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "push_up"
        start_time_pushup = time.time()

    return img


# Function to detect push-ups
def detect_push_up(img):
    global exercise_mode, per_left_pushup, per_right_pushup, count_pushup, display_pushup, bar_left_pushup, bar_right_pushup, leftangle_pushup, rightangle_pushup, count_bicep_left, count_bicep_right, dir_bicep_left, dir_bicep_right, start_time, pushup_dir

    img = cv2.resize(img, (1280, 720))

    elapsed_time = time.time() - start_time_pushup
    remaining_time = max(0, repetition_time_pushup - elapsed_time)
    if exercise_mode == "push_up":
        if display_pushup:  # Check if to display count_pushup, bar, and percentage

            img = detector_pushup.findPose(img, False)
            lmList = detector_pushup.findPosition(img, False)

            # Define hand angles outside the if statement
            if len(lmList) != 0:
                leftangle_pushup, rightangle_pushup = detector_pushup.findPushupAngle(img, 11, 13, 15, 12, 14, 16, drawpoints=True)

                # Interpolate angles to percentage and position on screen
                per_left_pushup = np.interp(leftangle_pushup, (190, 300), (100, 0))
                bar_left_pushup = np.interp(leftangle_pushup, (190, 300), (200, 400))

                per_right_pushup = np.interp(rightangle_pushup, (30, 170), (0, 100))
                bar_right_pushup = np.interp(rightangle_pushup, (30, 170), (400, 200))

                
                
                #Check if the person is in a proper push-up posture
                if detector_pushup.isPushUpPosture(lmList):
                    if leftangle_pushup >= 260 and rightangle_pushup >= 45:
                        if pushup_dir == 1:
                            count_pushup += 0.5
                            pushup_dir = 0
                            print(count_pushup)
                    if leftangle_pushup <= 190 and rightangle_pushup <= 190:
                        if pushup_dir == 0:
                            count_pushup += 0.5
                            pushup_dir = 1
                            print(count_pushup)

            cvzone.putTextRect(img, 'Push-Up Counter', [345, 30], thickness=2, border=2, scale=2.5)

            # Draw rectangle behind the timer text
            cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

            # Draw timer text above the rectangle
            timer_text = f"Time left: {int(remaining_time)}s"
            cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

            # Draw bars for left and right angles
            cv2.putText(img, f"R {int(per_right_pushup)}%", (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
            cv2.rectangle(img, (8, 200), (50, 400), (255, 255, 255), 5)
            cv2.rectangle(img, (8, int(bar_right_pushup)), (50, 400), (0, 0, 255), -1)

            cv2.putText(img, f"L {int(per_left_pushup)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
            cv2.rectangle(img, (952, 200), (995, 400), (255, 255, 255), 5)
            cv2.rectangle(img, (952, int(bar_left_pushup)), (995, 400), (0, 0, 255), -1)

            if leftangle_pushup <= 190:
                cv2.rectangle(img, (952, int(bar_left_pushup)), (995, 400), (0, 255, 0), -1)

            if rightangle_pushup >= 170:
                cv2.rectangle(img, (8, int(bar_right_pushup)), (50, 400), (0, 255, 0), -1)

        cv2.rectangle(img, (20, 10), (140, 120), (255, 0, 0), -1)
        cv2.putText(img, f"{int(count_pushup)}/5", (30, 80), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

        if remaining_time <= 0:
            cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
            display_pushup = False

        if int(count_pushup) >= 5:
            cvzone.putTextRect(img, 'Repetition completed', [390, 30], thickness=2, border=2, scale=2.5)
            display_pushup = False
            # exercise_mode = "bicep_curl"
            # # Reset variables for bicep curls
            # count_bicep_left = 0
            # count_bicep_right = 0
            # dir_bicep_left = 0
            # dir_bicep_right = 0
            # start_time = time.time()

    return img

# --------------- FOR GAINING MUSCLE ----------------- 







@app.route('/lossWeight')
def lossWeight():
    if 'username' in session and session['exercise'] == "loss_weight":
        return render_template('lossWeight.html')
    else:
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
