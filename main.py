from flask import Flask, render_template, request, redirect, url_for, session, Response, jsonify
from flask_mysqldb import MySQL
import os


# -------------- FOR GAINING MUSCLE ---------------
import cv2
import numpy as np
import time
import BicepCurl_PoseModule as pm_bicep
import PushUp_PoseModule as pm_pushup
import shouldertap_PoseModule as pm_shouldertap
import chestpress_PoseModule as pm_chestpress
import dumbbellfrontraise_PoseModule as pm_dumbbellfrontraise
import alternatinglunge_PoseModule as pm_alternatinglunge
import bodyweightsquat_PoseModule as pm_bws
import gobletsquat_PoseModule as pm_gs
import highkneetap_PoseModule as pm_hkt
import dumbbellhiphinge_PoseModule as pm_dhh
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
start_time_pushup = time.time()  # Start time
repetition_time_pushup = 60  # Repetition time

# Display info
display_pushup = True
rest_pushup_start_time = time.time()


per_right_pushup = 0
per_left_pushup = 0
bar_left_pushup = 0
bar_right_pushup = 0 

leftangle_pushup = 0
rightangle_pushup = 0
# ----------- END FOR PUSH UP --------------

# ----------- FOR PUSH UP SET 2---------------
# Import class
detector_pushup = pm_pushup.poseDetectorPushUp()

# Initialize variables
count_pushup_set2 = 0  # count_pushup of reps
pushup_dir_set2 = 0  # pushup_direction
start_time_pushup_set2 = time.time()  # Start time
repetition_time_pushup_set2 = 60  # Repetition time

# Display info
display_pushup_set2 = True
rest_pushup_start_time_set2 = time.time()

per_right_pushup_set2 = 0
per_left_pushup_set2 = 0
bar_left_pushup_set2 = 0
bar_right_pushup_set2 = 0 

leftangle_pushup_set2 = 0
rightangle_pushup_set2 = 0
# ----------- END FOR PUSH UP SET 2 --------------

# ----------- FOR PUSH UP SET 3---------------
# Import class
detector_pushup = pm_pushup.poseDetectorPushUp()

# Initialize variables
count_pushup_set3 = 0  # count_pushup of reps
pushup_dir_set3 = 0  # pushup_direction
start_time_pushup_set3 = time.time()  # Start time
repetition_time_pushup_set3 = 60  # Repetition time

# Display info
display_pushup_set3 = True
rest_pushup_start_time_set3 = time.time()

per_right_pushup_set3 = 0
per_left_pushup_set3 = 0
bar_left_pushup_set3 = 0
bar_right_pushup_set3 = 0 

leftangle_pushup_set3 = 0
rightangle_pushup_set3 = 0
# ----------- END FOR PUSH UP SET 3 --------------

# ----------- FOR SHOULDER TAP ---------------
detector_ShoulderTap = pm_shouldertap.poseDetectorShoulderTap()

count_shoulder_tap_right = 0
count_shoulder_tap_left = 0
dir_shoulder_tap_right = 0
dir_shoulder_tap_left = 0

start_time_shouldertap = time.time()
repetition_time_shouldertap = 60
display_info_shouldertap = True

per_left_arm_shouldertap = 0
bar_left_arm_shouldertap = 0

per_right_arm_shouldertap = 0
bar_right_arm_shouldertap = 0

color_left_arm_shouldertap = 0
color_right_arm_shouldertap = 0

rest_shouldertap_start_time = time.time()

# ----------- END FOR SHOULDER TAP ---------------

# ----------- FOR SHOULDER TAP SET 2---------------
detector_ShoulderTap = pm_shouldertap.poseDetectorShoulderTap()

count_shoulder_tap_right_set2 = 0
count_shoulder_tap_left_set2 = 0
dir_shoulder_tap_right_set2 = 0
dir_shoulder_tap_left_set2 = 0

start_time_shouldertap_set2 = time.time()
repetition_time_shouldertap_set2 = 60
display_info_shouldertap_set2 = True

per_left_arm_shouldertap_set2 = 0
bar_left_arm_shouldertap_set2 = 0

per_right_arm_shouldertap_set2 = 0
bar_right_arm_shouldertap_set2 = 0

color_left_arm_shouldertap_set2 = 0
color_right_arm_shouldertap_set2 = 0

rest_shouldertap_start_time_set2 = time.time()

# ----------- END FOR SHOULDER TAP SET 2---------------

# ----------- FOR SHOULDER TAP SET 3---------------
detector_ShoulderTap = pm_shouldertap.poseDetectorShoulderTap()

count_shoulder_tap_right_set3 = 0
count_shoulder_tap_left_set3 = 0
dir_shoulder_tap_right_set3 = 0
dir_shoulder_tap_left_set3 = 0

start_time_shouldertap_set3 = time.time()
repetition_time_shouldertap_set3 = 60
display_info_shouldertap_set3 = True

per_left_arm_shouldertap_set3 = 0
bar_left_arm_shouldertap_set3 = 0

per_right_arm_shouldertap_set3 = 0
bar_right_arm_shouldertap_set3 = 0

color_left_arm_shouldertap_set3 = 0
color_right_arm_shouldertap_set3 = 0

rest_shouldertap_start_time_set3 = time.time()

# ----------- END FOR SHOULDER TAP SET 3---------------

# ----------- FOR CHEST PRESS---------------

#import class
detector_chestpress = pm_chestpress.poseDetector()

#Initialize Variables
count_chestpress_left = 0
count_chestpress_right = 0

dir_chestpress_left = 0
dir_chestpress_right = 0

start_time_chestpress = time.time() # starts time
repetition_time_chestpress = 60 # duration time
display_info_chestpress = True # display features

bar_left_chestpress = 0
bar_right_chestpress = 0
per_left_chestpress = 0
per_right_chestpress = 0
angle_left_chestpress = 0
angle_right_chestpress = 0

rest_chestpress_start_time = time.time()

# ----------- END FOR CHEST PRESS---------------

# ----------- FOR CHEST PRESS SET 2---------------

#import class
detector_chestpress = pm_chestpress.poseDetector()

#Initialize Variables
count_chestpress_left_set2 = 0
count_chestpress_right_set2 = 0

dir_chestpress_left_set2 = 0
dir_chestpress_right_set2 = 0

start_time_chestpress_set2 = time.time() # starts time
repetition_time_chestpress_set2 = 60 # duration time
display_info_chestpress_set2 = True # display features

bar_left_chestpress_set2 = 0
bar_right_chestpress_set2 = 0
per_left_chestpress_set2 = 0
per_right_chestpress_set2 = 0
angle_left_chestpress_set2 = 0
angle_right_chestpress_set2 = 0

rest_chestpress_start_time_set2 = time.time()

# ----------- END FOR CHEST PRESS SET 2---------------

# ----------- FOR CHEST PRESS SET 3---------------

#import class
detector_chestpress = pm_chestpress.poseDetector()

#Initialize Variables
count_chestpress_left_set3 = 0
count_chestpress_right_set3 = 0

dir_chestpress_left_set3 = 0
dir_chestpress_right_set3 = 0

start_time_chestpress_set3 = time.time() # starts time
repetition_time_chestpress_set3 = 60 # duration time
display_info_chestpress_set3 = True # display features

bar_left_chestpress_set3 = 0
bar_right_chestpress_set3 = 0
per_left_chestpress_set3 = 0
per_right_chestpress_set3 = 0
angle_left_chestpress_set3 = 0
angle_right_chestpress_set3 = 0

rest_chestpress_start_time_set3 = time.time()

# ----------- END FOR CHEST PRESS SET 3---------------

# ----------- FOR DUMBBELL FRONT RAISE ---------------
detector_dumbbell = pm_dumbbellfrontraise.poseDetector()

# Initialize Variables
count_left_dumbbellfrontraise = 0
count_right_dumbbellfrontraise = 0

dir_left_dumbbellfrontraise = 0
dir_right_dumbbellfrontraise = 0

start_time_dumbbellfrontraise = time.time()  # starts time
repetition_time_dumbbellfrontraise = 60  # duration time
display_info_dumbbellfrontraise = True  # display features

bar_left_dumbbellfrontraise = 0
bar_right_dumbbellfrontraise = 0
per_left_dumbbellfrontraise = 0
per_right_dumbbellfrontraise = 0
angle_left_dumbbellfrontraise = 0
angle_right_dumbbellfrontraise = 0

rest_dumbbellfrontraise_start_time = time.time()
# ----------- END FOR DUMBBELL FRONT RAISE ---------------

# ----------- FOR DUMBBELL FRONT RAISE SET 2 ---------------
detector_dumbbell = pm_dumbbellfrontraise.poseDetector()

# Initialize Variables
count_left_dumbbellfrontraise_set2 = 0
count_right_dumbbellfrontraise_set2 = 0

dir_left_dumbbellfrontraise_set2 = 0
dir_right_dumbbellfrontraise_set2 = 0

start_time_dumbbellfrontraise_set2 = time.time()  # starts time
repetition_time_dumbbellfrontraise_set2 = 60  # duration time
display_info_dumbbellfrontraise_set2 = True  # display features

bar_left_dumbbellfrontraise_set2 = 0
bar_right_dumbbellfrontraise_set2 = 0
per_left_dumbbellfrontraise_set2 = 0
per_right_dumbbellfrontraise_set2 = 0
angle_left_dumbbellfrontraise_set2 = 0
angle_right_dumbbellfrontraise_set2 = 0

rest_dumbbellfrontraise_start_time_set2 = time.time()
# ----------- END FOR DUMBBELL FRONT RAISE SET 2---------------

# ----------- FOR DUMBBELL FRONT RAISE SET 3 ---------------
detector_dumbbell = pm_dumbbellfrontraise.poseDetector()

# Initialize Variables
count_left_dumbbellfrontraise_set3 = 0
count_right_dumbbellfrontraise_set3 = 0

dir_left_dumbbellfrontraise_set3 = 0
dir_right_dumbbellfrontraise_set3 = 0

start_time_dumbbellfrontraise_set3 = time.time()  # starts time
repetition_time_dumbbellfrontraise_set3 = 60  # duration time
display_info_dumbbellfrontraise_set3 = True  # display features

bar_left_dumbbellfrontraise_set3 = 0
bar_right_dumbbellfrontraise_set3 = 0
per_left_dumbbellfrontraise_set3 = 0
per_right_dumbbellfrontraise_set3 = 0
angle_left_dumbbellfrontraise_set3 = 0
angle_right_dumbbellfrontraise_set3 = 0

rest_dumbbellfrontraise_start_time_set3 = time.time()
# ----------- END FOR DUMBBELL FRONT RAISE SET 3---------------

# ----------- FOR ALTERNATING LUNGE ---------------
detector_alternatingleftlunge = pm_alternatinglunge.poseDetectoralternatinglunge()
count_alternating_right_lunge = 0
count_alternating_left_lunge = 0

dir_alternating_left_lunge = 0
dir_alternating_right_lunge = 0


start_time_alternatinglunge = time.time()
repetition_time_alternatinglunge = 60
display_info_alternatinglunge = True

per_left_leg_alternatinglunge = 0
bar_left_leg_alternatinglunge = 0

per_right_leg_alternatinglunge = 0
bar_right_leg_alternatinglunge = 0

leftleg_alternatinglunge  = 0
rightleg_alternatinglunge = 0


cooldown_duration_alternatinglunge = 5
cooldown_timer_alternatinglunge = 0

color_right_leg_alternatinglunge = (0, 0, 255)
color_left_leg_alternatinglunge = (0, 0, 255)
rest_alternatinglunge_start_time = time.time()

orientation = ''
orientation2 = ''
# ----------- END FOR ALTERNATING LUNGE ---------------

# ----------- FOR ALTERNATING LUNGE SET 2 ---------------
detector_alternatingleftlunge = pm_alternatinglunge.poseDetectoralternatinglunge()
count_alternating_right_lunge_set2 = 0
count_alternating_left_lunge_set2 = 0

dir_alternating_left_lunge_set2 = 0
dir_alternating_right_lunge_set2 = 0


start_time_alternatinglunge_set2 = time.time()
repetition_time_alternatinglunge_set2 = 60
display_info_alternatinglunge_set2 = True

per_left_leg_alternatinglunge_set2 = 0
bar_left_leg_alternatinglunge_set2 = 0

per_right_leg_alternatinglunge_set2 = 0
bar_right_leg_alternatinglunge_set2 = 0

leftleg_alternatinglunge_set2 = 0
rightleg_alternatinglunge_set2 = 0


cooldown_duration_alternatinglunge_set2 = 5
cooldown_timer_alternatinglunge_set2 = 0

color_right_leg_alternatinglunge_set2 = (0, 0, 255)
color_left_leg_alternatinglunge_set2 = (0, 0, 255)
rest_alternatinglunge_start_time_set2 = time.time()
# ----------- END FOR ALTERNATING LUNGE SET 2 ---------------

# ----------- FOR ALTERNATING LUNGE SET 3 ---------------
detector_alternatingleftlunge = pm_alternatinglunge.poseDetectoralternatinglunge()
count_alternating_right_lunge_set3 = 0
count_alternating_left_lunge_set3 = 0

dir_alternating_left_lunge_set3 = 0
dir_alternating_right_lunge_set3 = 0


start_time_alternatinglunge_set3 = time.time()
repetition_time_alternatinglunge_set3 = 60
display_info_alternatinglunge_set3 = True

per_left_leg_alternatinglunge_set3 = 0
bar_left_leg_alternatinglunge_set3 = 0

per_right_leg_alternatinglunge_set3 = 0
bar_right_leg_alternatinglunge_set3 = 0

leftleg_alternatinglunge_set3  = 0
rightleg_alternatinglunge_set3 = 0


cooldown_duration_alternatinglunge_set3 = 5
cooldown_timer_alternatinglunge_set3 = 0

color_right_leg_alternatinglunge_set3 = (0, 0, 255)
color_left_leg_alternatinglunge_set3 = (0, 0, 255)
rest_alternatinglunge_start_time_set3 = time.time()
# ----------- END FOR ALTERNATING LUNGE SET 3 ---------------

# ----------- FOR BODY WEIGHT SQUAT ---------------
detector_BodyWeightSquat = pm_bws.poseDetectorBodyWeightSquat()

count_body_weight_squat = 0
dir_body_weight_squat = 0


start_time_bws = time.time()
repetition_time_bws = 60
display_info_bws = True

leftbody_bws = 0
rightbody_bws = 0

per_left_body_bws = 0
bar_left_body_bws = 0

per_right_body_bws = 0
bar_right_body_bws = 0

color_right_body_bws = 0
color_left_body_bws = 0

rest_bws_start_time = time.time()

# ----------- END FOR BODY WEIGHT SQUAT ---------------

# ----------- FOR BODY WEIGHT SQUAT SET 2 ---------------
detector_BodyWeightSquat = pm_bws.poseDetectorBodyWeightSquat()

count_body_weight_squat_set2 = 0
dir_body_weight_squat_set2 = 0


start_time_bws_set2 = time.time()
repetition_time_bws_set2 = 60
display_info_bws_set2 = True

leftbody_bws_set2 = 0
rightbody_bws_set2 = 0

per_left_body_bws_set2 = 0
bar_left_body_bws_set2 = 0

per_right_body_bws_set2 = 0
bar_right_body_bws_set2 = 0

color_right_body_bws_set2 = 0
color_left_body_bws_set2 = 0

rest_bws_start_time_set2 = time.time()

# ----------- END FOR BODY WEIGHT SQUAT SET 2 ---------------

# ----------- FOR BODY WEIGHT SQUAT SET 3 ---------------
detector_BodyWeightSquat = pm_bws.poseDetectorBodyWeightSquat()

count_body_weight_squat_set3 = 0
dir_body_weight_squat_set3 = 0


start_time_bws_set3 = time.time()
repetition_time_bws_set3 = 60
display_info_bws_set3 = True

leftbody_bws_set3 = 0
rightbody_bws_set3 = 0

per_left_body_bws_set3 = 0
bar_left_body_bws_set3 = 0

per_right_body_bws_set3 = 0
bar_right_body_bws_set3 = 0

color_right_body_bws_set3 = 0
color_left_body_bws_set3 = 0

rest_bws_start_time_set3 = time.time()

# ----------- END FOR BODY WEIGHT SQUAT SET 3 ---------------

# ------------- FOR GOBLET SQUAT ---------------------
detector_gobletsquat = pm_gs.poseDetectorGobletSquat()

count_goblet_squat = 0
dir_goblet_squat = 0


start_time_goblet_squat = time.time()
repetition_time_goblet_squat = 60
display_info_goblet_squat = True

cooldown_duration_goblet_squat = 5
cooldown_timer_goblet_squat = 0

color_left_leg_goblet_squat = (0, 0, 255)
color_right_leg_goblet_squat = (0, 0, 255)
rest_goblet_squat_start_time = time.time()
per_right_leg = 0
per_left_leg = 0
bar_right_leg = 0
bar_left_leg = 0
color_left_leg = (0, 0, 255)
color_right_leg = (0, 0, 255)

# ------------- END FOR GOBLET SQUAT -----------------

# ------------- FOR GOBLET SQUAT SET 2 ---------------------
detector_gobletsquat = pm_gs.poseDetectorGobletSquat()

count_goblet_squat_set2 = 0
dir_goblet_squat_set2 = 0


start_time_goblet_squat_set2 = time.time()
repetition_time_goblet_squat_set2 = 60
display_info_goblet_squat_set2 = True

cooldown_duration_goblet_squat_set2 = 5
cooldown_timer_goblet_squat_set2 = 0

color_left_leg_goblet_squat_set2 = (0, 0, 255)
color_right_leg_goblet_squat_set2 = (0, 0, 255)
rest_goblet_squat_start_time_set2 = time.time()

# ------------- END FOR GOBLET SQUAT SET 2 -----------------

# ------------- FOR GOBLET SQUAT SET 3---------------------
detector_gobletsquat = pm_gs.poseDetectorGobletSquat()

count_goblet_squat_set3 = 0
dir_goblet_squat_set3 = 0


start_time_goblet_squat_set3 = time.time()
repetition_time_goblet_squat_set3 = 60
display_info_goblet_squat_set3 = True

cooldown_duration_goblet_squat_set3 = 5
cooldown_timer_goblet_squat_set3 = 0

color_left_leg_goblet_squat_set3 = (0, 0, 255)
color_right_leg_goblet_squat_set3 = (0, 0, 255)
rest_goblet_squat_start_time_set3 = time.time()

# ------------- END FOR GOBLET SQUAT SET 3-----------------

# ------------- FOR HIGH KNEE TAP --------------------
detector_HighKneeTap = pm_hkt.poseDetectorHighKneeTap()

count_high_knee_tap_right = 0
count_high_knee_tap_left = 0

dir_high_knee_tap_right = 0

dir_high_knee_tap_left = 0


start_time_hkt = time.time()
repetition_time_hkt = 60
display_info_hkt = True

leftbody_hkt = 0
rightbody_hkt = 0

per_left_leg_hkt = 0
bar_left_leg_hkt = 0

per_right_leg_hkt = 0
bar_right_leg_hkt = 0

cooldown_duration_hkt = 5
cooldown_timer_hkt = 0

color_left_leg_hkt = (0, 0, 255)
color_right_leg_hkt = (0, 0, 255)
rest_hkt_start_time = time.time()
# ------------- FOR HIGH KNEE TAP --------------------

# ------------- FOR HIGH KNEE TAP SET 2 --------------------
detector_HighKneeTap = pm_hkt.poseDetectorHighKneeTap()

count_high_knee_tap_right_set2 = 0
count_high_knee_tap_left_set2 = 0

dir_high_knee_tap_right_set2 = 0

dir_high_knee_tap_left_set2 = 0


start_time_hkt_set2 = time.time()
repetition_time_hkt_set2 = 60
display_info_hkt_set2 = True

leftbody_hkt_set2 = 0
rightbody_hkt_set2 = 0

per_left_leg_hkt_set2 = 0
bar_left_leg_hkt_set2 = 0

per_right_leg_hkt_set2 = 0
bar_right_leg_hkt_set2 = 0

cooldown_duration_hkt_set2 = 5
cooldown_timer_hkt_set2 = 0

color_left_leg_hkt_set2 = (0, 0, 255)
color_right_leg_hkt_set2 = (0, 0, 255)
rest_hkt_start_time_set2 = time.time()
# ------------- FOR HIGH KNEE TAP SET 2 --------------------

# ------------- FOR HIGH KNEE TAP SET 3 --------------------
detector_HighKneeTap = pm_hkt.poseDetectorHighKneeTap()

count_high_knee_tap_right_set3 = 0
count_high_knee_tap_left_set3 = 0

dir_high_knee_tap_right_set3 = 0

dir_high_knee_tap_left_set3 = 0


start_time_hkt_set3 = time.time()
repetition_time_hkt_set3 = 60
display_info_hkt_set3 = True

leftbody_hkt_set3 = 0
rightbody_hkt_set3 = 0

per_left_leg_hkt_set3 = 0
bar_left_leg_hkt_set3 = 0

per_right_leg_hkt_set3 = 0
bar_right_leg_hkt_set3 = 0

cooldown_duration_hkt_set3 = 5
cooldown_timer_hkt_set3 = 0

color_left_leg_hkt_set3 = (0, 0, 255)
color_right_leg_hkt_set3 = (0, 0, 255)
rest_hkt_start_time_set3 = time.time()
# ------------- FOR HIGH KNEE TAP SET 3 --------------------

# ------------- FOR DUMBBELL HIP HINGE ---------------------
detector_HipHinge = pm_dhh.poseDetectorBodyHipHinge()

# Initialize variables
count_hip_hinge = 0
dir_hip_hinge = 0

start_time_hpp = time.time()
repetition_time_hpp = 60
display_info_hpp = True

per_left_hip_angle = 0
bar_left_hip_angle = 0

per_right_hip_angle = 0
bar_right_hip_angle = 0

leftbody_hpp = 0
rightbody_hpp = 0

color_hip = (0, 0, 255)
rest_dhh_start_time = time.time()
# ------------- END FOR DUMBBELL HIP HINGE ---------------------

# ------------- FOR DUMBBELL HIP HINGE SET 2---------------------
detector_HipHinge = pm_dhh.poseDetectorBodyHipHinge()

# Initialize variables
count_hip_hinge_set2 = 0
dir_hip_hinge_set2 = 0

start_time_hpp_set2 = time.time()
repetition_time_hpp_set2 = 60
display_info_hpp_set2 = True

per_left_hip_angle_set2 = 0
bar_left_hip_angle_set2 = 0

per_right_hip_angle_set2 = 0
bar_right_hip_angle_set2 = 0

leftbody_hpp_set2 = 0
rightbody_hpp_set2 = 0

color_hip_set2 = (0, 0, 255)
rest_dhh_start_time_set2 = time.time()
# ------------- END FOR DUMBBELL HIP HINGE SET 2 ---------------------

# ------------- FOR DUMBBELL HIP HINGE SET 3 ---------------------
detector_HipHinge = pm_dhh.poseDetectorBodyHipHinge()

# Initialize variables
count_hip_hinge_set3 = 0
dir_hip_hinge_set3 = 0

start_time_hpp_set3 = time.time()
repetition_time_hpp_set3 = 60
display_info_hpp_set3 = True

per_left_hip_angle_set3 = 0
bar_left_hip_angle_set3 = 0

per_right_hip_angle_set3 = 0
bar_right_hip_angle_set3 = 0

leftbody_hpp_set3 = 0
rightbody_hpp_set3 = 0

color_hip_set3 = (0, 0, 255)
rest_dhh_start_time_set3 = time.time()
# ------------- END FOR DUMBBELL HIP HINGE SET 3 ---------------------


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
            # ---------- FOR GAINING MUSCLES ------------
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
            if exercise_mode == "rest_pushup":
                img_with_faces = rest_pushup(img)
            if exercise_mode == "push_up_set2":
                img_with_faces = detect_push_up_set2(img)
            if exercise_mode == "rest_pushup_set2":
                img_with_faces = rest_pushup_set2(img)
            if exercise_mode == "push_up_set3":
                img_with_faces = detect_push_up_set3(img)
            if exercise_mode == "rest_pushup_set3":
                img_with_faces = rest_pushup_set3(img)
            if exercise_mode == "shoulder_tap":
                img_with_faces = detect_shouldertap(img)
            if exercise_mode == "rest_shouldertap":
                img_with_faces = rest_shouldertap(img)
            if exercise_mode == "shoulder_tap_set2":
                img_with_faces = detect_shouldertap_set2(img)
            if exercise_mode == "rest_shouldertap_rest2":
                img_with_faces = rest_shouldertap_set2(img)
            if exercise_mode == "shoulder_tap_set3":
                img_with_faces = detect_shouldertap_set3(img)
            if exercise_mode == "rest_shouldertap_rest3":
                img_with_faces = rest_shouldertap_set3(img)
            if exercise_mode == "chest_press":
                img_with_faces = detect_chestpress(img)
            if exercise_mode == "rest_chestpress":
                img_with_faces = rest_chestpress(img)
            if exercise_mode == "chest_press_set2":
                img_with_faces = detect_chestpress_set2(img)
            if exercise_mode == "rest_chestpress_set2":
                img_with_faces = rest_chestpress_set2(img)
            if exercise_mode == "chest_press_set3":
                img_with_faces = detect_chestpress_set3(img)
            if exercise_mode == "rest_chestpress_set3":
                img_with_faces = rest_chestpress_set3(img)
            if exercise_mode == "dumbbell_frontraise":
                img_with_faces = detect_dumbbellfrontraise(img)
            if exercise_mode == "rest_dumbbellfrontraise":
                img_with_faces = rest_dumbbellfrontraise(img)
            if exercise_mode == "dumbbell_frontraise_set2":
                img_with_faces = detect_dumbbellfrontraise_set2(img)
            if exercise_mode == "rest_dumbbellfrontraise_set2":
                img_with_faces = rest_dumbbellfrontraise_set2(img)
            if exercise_mode == "dumbbell_frontraise_set3":
                img_with_faces = detect_dumbbellfrontraise_set3(img)
            if exercise_mode == "rest_dumbbellfrontraise_set3":
                img_with_faces = rest_dumbbellfrontraise_set3(img)
            if exercise_mode == "alternating_lunge":
                img_with_faces = detect_alternatinglunge(img)
            if exercise_mode == "rest_alternatinglunge":
                img_with_faces = rest_alternatinglunge(img)
            if exercise_mode == "alternating_lunge_set2":
                img_with_faces = detect_alternatinglunge_set2(img)
            if exercise_mode == "rest_alternatinglunge_set2":
                img_with_faces = rest_alternatinglunge_set2(img)
            if exercise_mode == "alternating_lunge_set3":
                img_with_faces = detect_alternatinglunge_set3(img)
            if exercise_mode == "rest_alternatinglunge_set3":
                img_with_faces = rest_alternatinglunge_set3(img)
            if exercise_mode == "bws":
                img_with_faces = detect_bws(img)
            if exercise_mode == "rest_bws":
                img_with_faces = rest_bws(img)
            if exercise_mode == "bws_set2":
                img_with_faces = detect_bws_set2(img)
            if exercise_mode == "rest_bws_set2":
                img_with_faces = rest_bws_set2(img)
            if exercise_mode == "bws_set3":
                img_with_faces = detect_bws_set3(img)
            if exercise_mode == "rest_bws_set3":
                img_with_faces = rest_bws_set3(img)
            if exercise_mode == "goblet_squat":
                img_with_faces = detect_gs(img)
            if exercise_mode == "rest_gs":
                img_with_faces = rest_gs(img)
            if exercise_mode == "goblet_squat_set2":
                img_with_faces = detect_gs_set2(img)
            if exercise_mode == "rest_gs_set2":
                img_with_faces = rest_gs_set2(img)
            if exercise_mode == "goblet_squat_set3":
                img_with_faces = detect_gs_set3(img)
            if exercise_mode == "rest_gs_set3":
                img_with_faces = rest_gs_set3(img)
            if exercise_mode == "highkneetap":
                img_with_faces = detect_hkt(img)
            if exercise_mode == "rest_hkt":
                img_with_faces = rest_hkt(img)
            if exercise_mode == "highkneetap_set2":
                img_with_faces = detect_hkt_set2(img)
            if exercise_mode == "rest_hkt_set2":
                img_with_faces = rest_hkt_set2(img)
            if exercise_mode == "highkneetap_set3":
                img_with_faces = detect_hkt_set3(img)
            if exercise_mode == "rest_hkt_set3":
                img_with_faces = rest_hkt_set3(img)
            if exercise_mode == "dhh":
                img_with_faces = detect_dhh(img)
            if exercise_mode == "rest_dhh":
                img_with_faces = rest_dhh(img)
            if exercise_mode == "dhh_set2":
                img_with_faces = detect_dhh_set2(img)
            if exercise_mode == "rest_dhh_set2":
                img_with_faces = rest_dhh_set2(img)
            if exercise_mode == "dhh_set3":
                img_with_faces = detect_dhh_set3(img)
            if exercise_mode == "rest_dhh_set3":
                img_with_faces = rest_dhh_set3(img)
            # ---------- END FOR GAINING MUSCLES ------------



            ret, buffer = cv2.imencode('.jpg', img_with_faces)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/gainMuscle')
def muscleGain():
    if 'username' in session and session['exercise'] == "muscle_gain":
        bicep_curl = os.path.join(app.config['UPLOAD_FOLDER'], 'bicep_curl.jpg')
        push_up = os.path.join(app.config['UPLOAD_FOLDER'], 'Pushups.jpg')
        shoulder_tap = os.path.join(app.config['UPLOAD_FOLDER'], 'shoulder_tap.jpg')
        dumbbell_frontraise = os.path.join(app.config['UPLOAD_FOLDER'], 'dumbbell_frontraise.jpg')
        chest_press = os.path.join(app.config['UPLOAD_FOLDER'], 'chest_press.jpg')
        return render_template('gainingMuscle.html', bicep_curl = bicep_curl, push_up = push_up, shoulder_tap = shoulder_tap, dumbbell_frontraise = dumbbell_frontraise, chest_press = chest_press)
    else:
        return redirect(url_for('home'))

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/exercise_mode')
def get_exercise_mode():
    global exercise_mode
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
    remaining_time = max(0, repetition_time - elapsed_time) #repetition_time



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
    rest_remaining_time = max(0, 10 - rest_elapsed_time)

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
    rest_remaining_time = max(0, 10 - rest_elapsed_time)

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
    rest_remaining_time = max(0, 10 - rest_elapsed_time)

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
    global exercise_mode, per_left_pushup, per_right_pushup, count_pushup, display_pushup, bar_left_pushup, bar_right_pushup, leftangle_pushup, rightangle_pushup, pushup_dir, rest_pushup_start_time

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
                    if leftangle_pushup <= 190 and rightangle_pushup <= 190:
                        if pushup_dir == 0:
                            count_pushup += 0.5
                            pushup_dir = 1
                      

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
            exercise_mode = "rest_pushup"
            rest_pushup_start_time = time.time()

        if int(count_pushup) >= 5:
            cvzone.putTextRect(img, 'Repetition completed', [390, 30], thickness=2, border=2, scale=2.5)
            display_pushup = False
            exercise_mode = "rest_pushup"
            rest_pushup_start_time = time.time()

    return img

def rest_pushup(img):
    global exercise_mode, rest_pushup_start_time, start_time_pushup_set2
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_pushup_start_time
    rest_remaining_time = max(0, 10 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "push_up_set2"
        start_time_pushup_set2 = time.time()
    return img


def detect_push_up_set2(img):
    global exercise_mode, per_left_pushup_set2, per_right_pushup_set2, count_pushup_set2, display_pushup_set2, bar_left_pushup_set2, bar_right_pushup_set2, leftangle_pushup_set2, rightangle_pushup_set2, pushup_dir_set2, rest_pushup_start_time_set2

    img = cv2.resize(img, (1280, 720))

    elapsed_time = time.time() - start_time_pushup_set2
    remaining_time = max(0, repetition_time_pushup_set2 - elapsed_time)
    if exercise_mode == "push_up_set2":
        if display_pushup_set2:  # Check if to display count_pushup, bar, and percentage

            img = detector_pushup.findPose(img, False)
            lmList = detector_pushup.findPosition(img, False)

            # Define hand angles outside the if statement
            if len(lmList) != 0:
                leftangle_pushup_set2, rightangle_pushup_set2 = detector_pushup.findPushupAngle(img, 11, 13, 15, 12, 14, 16, drawpoints=True)

                # Interpolate angles to percentage and position on screen
                per_left_pushup_set2 = np.interp(leftangle_pushup_set2, (190, 300), (100, 0))
                bar_left_pushup_set2 = np.interp(leftangle_pushup_set2, (190, 300), (200, 400))

                per_right_pushup_set2 = np.interp(rightangle_pushup_set2, (30, 170), (0, 100))
                bar_right_pushup_set2 = np.interp(rightangle_pushup_set2, (30, 170), (400, 200))

                
                
                #Check if the person is in a proper push-up posture
                if detector_pushup.isPushUpPosture(lmList):
                    if leftangle_pushup_set2 >= 260 and rightangle_pushup_set2 >= 45:
                        if pushup_dir_set2 == 1:
                            count_pushup_set2 += 0.5
                            pushup_dir_set2 = 0
                    if leftangle_pushup_set2 <= 190 and rightangle_pushup_set2 <= 190:
                        if pushup_dir_set2 == 0:
                            count_pushup_set2 += 0.5
                            pushup_dir_set2 = 1
                            

            cvzone.putTextRect(img, 'Push-Up Counter SET 2', [345, 30], thickness=2, border=2, scale=2.5)

            # Draw rectangle behind the timer text
            cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

            # Draw timer text above the rectangle
            timer_text = f"Time left: {int(remaining_time)}s"
            cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

            # Draw bars for left and right angles
            cv2.putText(img, f"R {int(per_right_pushup_set2)}%", (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
            cv2.rectangle(img, (8, 200), (50, 400), (255, 255, 255), 5)
            cv2.rectangle(img, (8, int(bar_right_pushup_set2)), (50, 400), (0, 0, 255), -1)

            cv2.putText(img, f"L {int(per_left_pushup_set2)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
            cv2.rectangle(img, (952, 200), (995, 400), (255, 255, 255), 5)
            cv2.rectangle(img, (952, int(bar_left_pushup_set2)), (995, 400), (0, 0, 255), -1)

            if leftangle_pushup_set2 <= 190:
                cv2.rectangle(img, (952, int(bar_left_pushup_set2)), (995, 400), (0, 255, 0), -1)

            if rightangle_pushup_set2 >= 170:
                cv2.rectangle(img, (8, int(bar_right_pushup_set2)), (50, 400), (0, 255, 0), -1)

        cv2.rectangle(img, (20, 10), (140, 120), (255, 0, 0), -1)
        cv2.putText(img, f"{int(count_pushup_set2)}/5", (30, 80), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

        if remaining_time <= 0:
            cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
            display_pushup_set2 = False
            exercise_mode = "rest_pushup_set2"
            rest_pushup_start_time_set2 = time.time()

        if int(count_pushup_set2) >= 5:
            cvzone.putTextRect(img, 'Repetition completed', [390, 30], thickness=2, border=2, scale=2.5)
            display_pushup_set2 = False
            exercise_mode = "rest_pushup_set2"
            rest_pushup_start_time_set2 = time.time()

    return img

def rest_pushup_set2(img):
    global exercise_mode, rest_pushup_start_time_set2, start_time_pushup_set3
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_pushup_start_time_set2
    rest_remaining_time = max(0, 10 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "push_up_set3"
        start_time_pushup_set3 = time.time()

    return img

def detect_push_up_set3(img):
    global exercise_mode, per_left_pushup_set3, per_right_pushup_set3, count_pushup_set3, display_pushup_set3, bar_left_pushup_set3, bar_right_pushup_set3, leftangle_pushup_set3, rightangle_pushup_set3, pushup_dir_set3, rest_pushup_start_time_set3

    img = cv2.resize(img, (1280, 720))

    elapsed_time = time.time() - start_time_pushup_set3
    remaining_time = max(0, repetition_time_pushup_set3 - elapsed_time)
    if exercise_mode == "push_up_set3":
        if display_pushup_set3:  # Check if to display count_pushup, bar, and percentage

            img = detector_pushup.findPose(img, False)
            lmList = detector_pushup.findPosition(img, False)

            # Define hand angles outside the if statement
            if len(lmList) != 0:
                leftangle_pushup_set3, rightangle_pushup_set3 = detector_pushup.findPushupAngle(img, 11, 13, 15, 12, 14, 16, drawpoints=True)

                # Interpolate angles to percentage and position on screen
                per_left_pushup_set3 = np.interp(leftangle_pushup_set3, (190, 300), (100, 0))
                bar_left_pushup_set3 = np.interp(leftangle_pushup_set3, (190, 300), (200, 400))

                per_right_pushup_set3 = np.interp(rightangle_pushup_set3, (30, 170), (0, 100))
                bar_right_pushup_set3 = np.interp(rightangle_pushup_set3, (30, 170), (400, 200))

                
                
                #Check if the person is in a proper push-up posture
                if detector_pushup.isPushUpPosture(lmList):
                    if leftangle_pushup_set3 >= 260 and rightangle_pushup_set3 >= 45:
                        if pushup_dir_set3 == 1:
                            count_pushup_set3 += 0.5
                            pushup_dir_set3 = 0
                    if leftangle_pushup_set3 <= 190 and rightangle_pushup_set3 <= 190:
                        if pushup_dir_set3 == 0:
                            count_pushup_set3 += 0.5
                            pushup_dir_set3 = 1
                            

            cvzone.putTextRect(img, 'Push-Up Counter SET 3', [345, 30], thickness=2, border=2, scale=2.5)

            # Draw rectangle behind the timer text
            cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

            # Draw timer text above the rectangle
            timer_text = f"Time left: {int(remaining_time)}s"
            cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

            # Draw bars for left and right angles
            cv2.putText(img, f"R {int(per_right_pushup_set3)}%", (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
            cv2.rectangle(img, (8, 200), (50, 400), (255, 255, 255), 5)
            cv2.rectangle(img, (8, int(bar_right_pushup_set3)), (50, 400), (0, 0, 255), -1)

            cv2.putText(img, f"L {int(per_left_pushup_set3)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
            cv2.rectangle(img, (952, 200), (995, 400), (255, 255, 255), 5)
            cv2.rectangle(img, (952, int(bar_left_pushup_set3)), (995, 400), (0, 0, 255), -1)

            if leftangle_pushup_set3 <= 190:
                cv2.rectangle(img, (952, int(bar_left_pushup_set3)), (995, 400), (0, 255, 0), -1)

            if rightangle_pushup_set3 >= 170:
                cv2.rectangle(img, (8, int(bar_right_pushup_set3)), (50, 400), (0, 255, 0), -1)

        cv2.rectangle(img, (20, 10), (140, 120), (255, 0, 0), -1)
        cv2.putText(img, f"{int(count_pushup_set3)}/5", (30, 80), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

        if remaining_time <= 0:
            cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
            display_pushup_set3 = False
            exercise_mode = "rest_pushup_set3"
            rest_pushup_start_time_set3 = time.time()

        if int(count_pushup_set3) >= 5:
            cvzone.putTextRect(img, 'Repetition completed', [390, 30], thickness=2, border=2, scale=2.5)
            display_pushup_set3 = False
            exercise_mode = "rest_pushup_set3"
            rest_pushup_start_time_set3 = time.time()
    return img

def rest_pushup_set3(img):
    global exercise_mode, rest_pushup_start_time_set3, start_time_shouldertap
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_pushup_start_time_set3
    rest_remaining_time = max(0, 10 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "shoulder_tap"
        start_time_shouldertap = time.time()

    return img

def detect_shouldertap(img):
    global count_shoulder_tap_left, count_shoulder_tap_right, dir_shoulder_tap_left, dir_shoulder_tap_right, start_time_shouldertap, display_info_shouldertap, per_left_arm_shouldertap, per_right_arm_shouldertap, bar_left_arm_shouldertap, bar_right_arm_shouldertap, color_left_arm_shouldertap, color_right_arm_shouldertap, exercise_mode, rest_shouldertap_start_time

    img = cv2.resize(img, (1280, 720))

    elapsed_time = time.time() - start_time_shouldertap
    remaining_time = max(0, repetition_time_shouldertap - elapsed_time) #repetition_time_shouldertap

    if display_info_shouldertap:  # Check if to display counter, bar, and percentage
        img = detector_ShoulderTap.findPose(img, False)
        lmList_jumping_jacks = detector_ShoulderTap.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_jumping_jacks) != 0:

            distance1, distance2 = detector_ShoulderTap.ShoulderTap(img, 12, 14, 16, 11, 13, 15, drawpoints=True) 

            #Interpolate angle to percentage and position on screen
            per_right_arm_shouldertap = np.interp(distance1, (180, 350), (100, 0))
            bar_right_arm_shouldertap = np.interp(distance1, (180, 350), (200, 400))

            per_left_arm_shouldertap = np.interp(distance2, (180, 350), (100, 0))
            bar_left_arm_shouldertap = np.interp(distance2, (180, 350), (200, 400))


            if int(per_left_arm_shouldertap) == 100 :
                color_left_arm_shouldertap = (0, 255, 0) 
            elif int(per_right_arm_shouldertap) == 100:
                color_right_arm_shouldertap = (0, 255, 0)
            else:
                color_left_arm_shouldertap = (0, 0, 255)  
                color_right_arm_shouldertap = (0, 0, 255)

            if distance1 <= 180:
                if dir_shoulder_tap_right == 0 and count_shoulder_tap_right < 5:
                    count_shoulder_tap_right += 0.5
                    if count_shoulder_tap_right == 5:
                        dir_shoulder_tap_right = -1
                    else:
                        dir_shoulder_tap_right = 1
            elif distance1 >= 350:
                if dir_shoulder_tap_right == 1 and count_shoulder_tap_right < 5:
                    count_shoulder_tap_right += 0.5
                    if count_shoulder_tap_right == 5:
                        dir_shoulder_tap_right = -1
                    else:
                        dir_shoulder_tap_right = 0

            if distance2 <= 180:
                if dir_shoulder_tap_left == 0 and count_shoulder_tap_left < 5:
                    count_shoulder_tap_left += 0.5
                    if count_shoulder_tap_left == 5:
                        dir_shoulder_tap_left = -1
                    else:
                        dir_shoulder_tap_left = 1
            elif distance2 >= 350:
                if dir_shoulder_tap_left == 1 and count_shoulder_tap_left < 5:
                    count_shoulder_tap_left += 0.5
                    if count_shoulder_tap_left == 5:
                        dir_shoulder_tap_left = -1
                    else:
                        dir_shoulder_tap_left = 0

        cvzone.putTextRect(img, 'Shoulder Tap Tracker', [370, 30], thickness=2, border=2, scale=2.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color


        #Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # ARM RIGHT
        cv2.putText(img, f"R {int(per_right_arm_shouldertap)}%", (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_arm_shouldertap)), (50, 400), color_right_arm_shouldertap, -1)

        # ARM LEFT
        cv2.putText(img, f"L {int(per_left_arm_shouldertap)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_arm_shouldertap)), (995, 400), color_left_arm_shouldertap, -1)

    # Counter 
    cv2.rectangle(img, (20, 20), (150, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(count_shoulder_tap_right)}/5", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (170, 20), (300, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(count_shoulder_tap_left)}/5", (180, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [370, 30], thickness=2, border=2, scale=2.5)
        display_info_shouldertap = False
        exercise_mode = "rest_shouldertap"
        rest_shouldertap_start_time = time.time()

    if count_shoulder_tap_right >= 5 and count_shoulder_tap_left >= 5:  # Assuming 10 jumping jacks for demonstration
        cvzone.putTextRect(img, 'Exercise Complete', [370, 30], thickness=2, border=2, scale=2.5)
        display_info_shouldertap = False
        exercise_mode = "rest_shouldertap"
        rest_shouldertap_start_time = time.time()

    return img

def rest_shouldertap(img):
    global exercise_mode, rest_shouldertap_start_time, start_time_shouldertap_set2
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_shouldertap_start_time
    rest_remaining_time = max(0, 10 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "shoulder_tap_set2"
        start_time_shouldertap_set2 = time.time()
    return img

def detect_shouldertap_set2(img):
    global count_shoulder_tap_left_set2, count_shoulder_tap_right_set2, dir_shoulder_tap_left_set2, dir_shoulder_tap_right_set2, start_time_shouldertap_set2, display_info_shouldertap_set2, per_left_arm_shouldertap_set2, per_right_arm_shouldertap_set2, bar_left_arm_shouldertap_set2, bar_right_arm_shouldertap_set2, color_left_arm_shouldertap_set2, color_right_arm_shouldertap_set2, exercise_mode, rest_shouldertap_start_time_set2

    img = cv2.resize(img, (1280, 720))

    elapsed_time = time.time() - start_time_shouldertap_set2
    remaining_time = max(0, repetition_time_shouldertap_set2 - elapsed_time) #repetition_time_shouldertap

    if display_info_shouldertap_set2:  # Check if to display counter, bar, and percentage
        img = detector_ShoulderTap.findPose(img, False)
        lmList_jumping_jacks = detector_ShoulderTap.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_jumping_jacks) != 0:

            distance1, distance2 = detector_ShoulderTap.ShoulderTap(img, 12, 14, 16, 11, 13, 15, drawpoints=True) 

            #Interpolate angle to percentage and position on screen
            per_right_arm_shouldertap_set2 = np.interp(distance1, (180, 350), (100, 0))
            bar_right_arm_shouldertap_set2 = np.interp(distance1, (180, 350), (200, 400))

            per_left_arm_shouldertap_set2 = np.interp(distance2, (180, 350), (100, 0))
            bar_left_arm_shouldertap_set2 = np.interp(distance2, (180, 350), (200, 400))


            if int(per_left_arm_shouldertap_set2) == 100 :
                color_left_arm_shouldertap_set2 = (0, 255, 0) 
            elif int(per_right_arm_shouldertap_set2) == 100:
                color_right_arm_shouldertap_set2 = (0, 255, 0)
            else:
                color_left_arm_shouldertap_set2 = (0, 0, 255)  
                color_right_arm_shouldertap_set2 = (0, 0, 255)

            if distance1 <= 180:
                if dir_shoulder_tap_right_set2 == 0 and count_shoulder_tap_right_set2 < 5:
                    count_shoulder_tap_right_set2 += 0.5
                    if count_shoulder_tap_right_set2 == 5:
                        dir_shoulder_tap_right_set2 = -1
                    else:
                        dir_shoulder_tap_right_set2 = 1
            elif distance1 >= 350:
                if dir_shoulder_tap_right_set2 == 1 and count_shoulder_tap_right_set2 < 5:
                    count_shoulder_tap_right_set2 += 0.5
                    if count_shoulder_tap_right_set2 == 5:
                        dir_shoulder_tap_right_set2 = -1
                    else:
                        dir_shoulder_tap_right_set2 = 0

            if distance2 <= 180:
                if dir_shoulder_tap_left_set2 == 0 and count_shoulder_tap_left_set2 < 5:
                    count_shoulder_tap_left_set2 += 0.5
                    if count_shoulder_tap_left_set2 == 5:
                        dir_shoulder_tap_left_set2 = -1
                    else:
                        dir_shoulder_tap_left_set2 = 1
            elif distance2 >= 350:
                if dir_shoulder_tap_left_set2 == 1 and count_shoulder_tap_left_set2 < 5:
                    count_shoulder_tap_left_set2 += 0.5
                    if count_shoulder_tap_left_set2 == 5:
                        dir_shoulder_tap_left_set2 = -1
                    else:
                        dir_shoulder_tap_left_set2 = 0

        cvzone.putTextRect(img, 'Shoulder Tap Tracker SET 2', [370, 30], thickness=2, border=2, scale=2.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color


        #Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # ARM RIGHT
        cv2.putText(img, f"R {int(per_right_arm_shouldertap_set2)}%", (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_arm_shouldertap_set2)), (50, 400), color_right_arm_shouldertap_set2, -1)

        # ARM LEFT
        cv2.putText(img, f"L {int(per_left_arm_shouldertap_set2)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_arm_shouldertap_set2)), (995, 400), color_left_arm_shouldertap_set2, -1)

    # Counter 
    cv2.rectangle(img, (20, 20), (150, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(count_shoulder_tap_right_set2)}/5", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (170, 20), (300, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(count_shoulder_tap_left_set2)}/5", (180, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [370, 30], thickness=2, border=2, scale=2.5)
        display_info_shouldertap_set2 = False
        exercise_mode = "rest_shouldertap_rest2"
        rest_shouldertap_start_time_set2 = time.time()

    if count_shoulder_tap_right_set2 >= 5 and count_shoulder_tap_left_set2 >= 5:  # Assuming 10 jumping jacks for demonstration
        cvzone.putTextRect(img, 'Exercise Complete', [370, 30], thickness=2, border=2, scale=2.5)
        display_info_shouldertap_set2 = False
        exercise_mode = "rest_shouldertap_rest2"
        rest_shouldertap_start_time_set2 = time.time()
    return img

def rest_shouldertap_set2(img):
    global exercise_mode, rest_shouldertap_start_time_set2, start_time_shouldertap_set3
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_shouldertap_start_time_set2
    rest_remaining_time = max(0, 10 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "shoulder_tap_set3"
        start_time_shouldertap_set3 = time.time()
    return img

def detect_shouldertap_set3(img):
    global count_shoulder_tap_left_set3, count_shoulder_tap_right_set3, dir_shoulder_tap_left_set3, dir_shoulder_tap_right_set3, start_time_shouldertap_set3, display_info_shouldertap_set3, per_left_arm_shouldertap_set3, per_right_arm_shouldertap_set3, bar_left_arm_shouldertap_set3, bar_right_arm_shouldertap_set3, color_left_arm_shouldertap_set3, color_right_arm_shouldertap_set3, exercise_mode, rest_shouldertap_start_time_set3

    img = cv2.resize(img, (1280, 720))

    elapsed_time = time.time() - start_time_shouldertap_set3
    remaining_time = max(0, repetition_time_shouldertap_set3 - elapsed_time) #repetition_time_shouldertap

    if display_info_shouldertap_set3:  # Check if to display counter, bar, and percentage
        img = detector_ShoulderTap.findPose(img, False)
        lmList_jumping_jacks = detector_ShoulderTap.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_jumping_jacks) != 0:

            distance1, distance2 = detector_ShoulderTap.ShoulderTap(img, 12, 14, 16, 11, 13, 15, drawpoints=True) 

            #Interpolate angle to percentage and position on screen
            per_right_arm_shouldertap_set3 = np.interp(distance1, (180, 350), (100, 0))
            bar_right_arm_shouldertap_set3 = np.interp(distance1, (180, 350), (200, 400))

            per_left_arm_shouldertap_set3 = np.interp(distance2, (180, 350), (100, 0))
            bar_left_arm_shouldertap_set3 = np.interp(distance2, (180, 350), (200, 400))


            if int(per_left_arm_shouldertap_set3) == 100 :
                color_left_arm_shouldertap_set3 = (0, 255, 0) 
            elif int(per_right_arm_shouldertap_set3) == 100:
                color_right_arm_shouldertap_set3 = (0, 255, 0)
            else:
                color_left_arm_shouldertap_set3 = (0, 0, 255)  
                color_right_arm_shouldertap_set3 = (0, 0, 255)

            if distance1 <= 180:
                if dir_shoulder_tap_right_set3 == 0 and count_shoulder_tap_right_set3 < 5:
                    count_shoulder_tap_right_set3 += 0.5
                    if count_shoulder_tap_right_set3 == 5:
                        dir_shoulder_tap_right_set3 = -1
                    else:
                        dir_shoulder_tap_right_set3 = 1
            elif distance1 >= 350:
                if dir_shoulder_tap_right_set3 == 1 and count_shoulder_tap_right_set3 < 5:
                    count_shoulder_tap_right_set3 += 0.5
                    if count_shoulder_tap_right_set3 == 5:
                        dir_shoulder_tap_right_set3 = -1
                    else:
                        dir_shoulder_tap_right_set3 = 0

            if distance2 <= 180:
                if dir_shoulder_tap_left_set3 == 0 and count_shoulder_tap_left_set3 < 5:
                    count_shoulder_tap_left_set3 += 0.5
                    if count_shoulder_tap_left_set3 == 5:
                        dir_shoulder_tap_left_set3 = -1
                    else:
                        dir_shoulder_tap_left_set3 = 1
            elif distance2 >= 350:
                if dir_shoulder_tap_left_set3 == 1 and count_shoulder_tap_left_set3 < 5:
                    count_shoulder_tap_left_set3 += 0.5
                    if count_shoulder_tap_left_set3 == 5:
                        dir_shoulder_tap_left_set3 = -1
                    else:
                        dir_shoulder_tap_left_set3 = 0

        cvzone.putTextRect(img, 'Shoulder Tap Tracker SET 3', [370, 30], thickness=2, border=2, scale=2.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color


        #Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # ARM RIGHT
        cv2.putText(img, f"R {int(per_right_arm_shouldertap_set3)}%", (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_arm_shouldertap_set3)), (50, 400), color_right_arm_shouldertap_set3, -1)

        # ARM LEFT
        cv2.putText(img, f"L {int(per_left_arm_shouldertap_set3)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_arm_shouldertap_set3)), (995, 400), color_left_arm_shouldertap_set3, -1)

    # Counter 
    cv2.rectangle(img, (20, 20), (150, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(count_shoulder_tap_right_set3)}/5", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (170, 20), (300, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(count_shoulder_tap_left_set3)}/5", (180, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [370, 30], thickness=2, border=2, scale=2.5)
        display_info_shouldertap_set3 = False
        exercise_mode = "rest_shouldertap_rest3"
        rest_shouldertap_start_time_set3 = time.time()

    if count_shoulder_tap_right_set3 >= 5 and count_shoulder_tap_left_set3 >= 5:  # Assuming 10 jumping jacks for demonstration
        cvzone.putTextRect(img, 'Exercise Complete', [370, 30], thickness=2, border=2, scale=2.5)
        display_info_shouldertap_set3 = False
        exercise_mode = "rest_shouldertap_rest3"
        rest_shouldertap_start_time_set3 = time.time()
    return img

def rest_shouldertap_set3(img):
    global exercise_mode, rest_shouldertap_start_time_set3, start_time_chestpress
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_shouldertap_start_time_set3
    rest_remaining_time = max(0, 10 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "chest_press"
        start_time_chestpress = time.time()
    return img


def detect_chestpress(img):
    global count_chestpress_left, count_chestpress_right, dir_chestpress_right, dir_chestpress_left, start_time_chestpress, repetition_time_chestpress, display_info_chestpress, bar_left_chestpress, bar_right_chestpress, per_left_chestpress, per_right_chestpress, angle_left_chestpress, angle_right_chestpress, exercise_mode, rest_chestpress_start_time

    img = cv2.resize(img, (1280, 720))

    # Timer - starts timer based on set duration
    elapsed_time = time.time() - start_time_chestpress
    remaining_time = max(0, repetition_time_chestpress - elapsed_time)


    if display_info_chestpress:  # Check if to display counter, bar, and percentage
        img = detector_chestpress.findPose(img, False) # initializes img as variable for findpose function
        lmList_bicep = detector_chestpress.findPosition(img, False) # initializes lmList_bicep as variable for findPosition function

        # Define hand angles outside the if statement
        if len(lmList_bicep) != 0:
            angle_left_chestpress = detector_chestpress.findAngle(img, 11, 13, 15)
            angle_right_chestpress = detector_chestpress.findAngle(img, 12, 14, 16) # defines right arm landmark keypoints
            # (refer to mediapipe landmark mapping for number equivalent)

            # Interpolate angle to percentage and position on screen
            per_left_chestpress = np.interp(angle_left_chestpress, (50, 155), (0, 100)) # first parenthesis, the value threshold of the angle. Second, represents the interp value
            bar_left_chestpress = np.interp(angle_left_chestpress, (50, 165), (400, 200)) # 

            per_right_chestpress = np.interp(angle_right_chestpress, (190, 300), (100, 0)) # 
            bar_right_chestpress = np.interp(angle_right_chestpress, (190, 300), (200, 400)) # 

            if angle_left_chestpress >= 155:
                if dir_chestpress_left == 0 and count_chestpress_left < 5:
                    count_chestpress_left += 0.5
                    if count_chestpress_left == 5:
                        dir_chestpress_left = -1
                    else:
                        dir_chestpress_left = 1 
            elif angle_left_chestpress <= 50:
                if dir_chestpress_left == 1 and count_chestpress_left < 5:
                    count_chestpress_left += 0.5
                    if count_chestpress_left == 5:
                        dir_chestpress_left = -1
                    else:
                        dir_chestpress_left = 0  

            if angle_right_chestpress <= 190: 
                if dir_chestpress_right == 0 and count_chestpress_right < 5:
                    count_chestpress_right += 0.5
                    if count_chestpress_right == 5:
                        dir_chestpress_right = -1
                    else:
                        dir_chestpress_right = 1 

            if angle_right_chestpress >= 270:
                if dir_chestpress_right == 1 and count_chestpress_right < 5:
                    count_chestpress_right += 0.5
                    if count_chestpress_right == 5:
                        dir_chestpress_right = -1
                    else:
                        dir_chestpress_right = 0

        # label
        cvzone.putTextRect(img, 'Chest Press Tracker', [345, 30], thickness=2, border=2, scale=2.5) 

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # bar
        cv2.putText(img, f"R {int(per_right_chestpress)}%" , (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_chestpress)), (50, 400), (0, 0, 255), -1)

        cv2.putText(img, f"L {int(per_left_chestpress)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_chestpress)), (995, 400), (0, 0, 255), -1)
        
        if angle_left_chestpress >= 155:
            cv2.rectangle(img, (952, int(bar_left_chestpress)), (995, 400), (0, 255, 0), -1)

        if angle_right_chestpress <= 190:
            cv2.rectangle(img, (8, int(bar_right_chestpress)), (50, 400), (0, 255, 0), -1)

    #count
    cv2.rectangle(img, (20, 20), (140, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(count_chestpress_right)}/5", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (150, 20), (270, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(count_chestpress_right)}/5", (160, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255 ,255), 7)

    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
        display_info_chestpress = False
        exercise_mode = "rest_chestpress"
        rest_chestpress_start_time = time.time()

    if count_chestpress_right == 5 and count_chestpress_left == 5:
        cvzone.putTextRect(img, 'All Repetitions Completed', [390, 30], thickness=2, border=2, scale=2.5)
        display_info_chestpress = False
        exercise_mode = "rest_chestpress"
        rest_chestpress_start_time = time.time()
    return img

def rest_chestpress(img):
    global exercise_mode, rest_chestpress_start_time, start_time_chestpress_set2
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_chestpress_start_time
    rest_remaining_time = max(0, 10 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "chest_press_set2"
        start_time_chestpress_set2 = time.time()
    return img

def detect_chestpress_set2(img):
    global count_chestpress_left_set2, count_chestpress_right_set2, dir_chestpress_right_set2, dir_chestpress_left_set2, start_time_chestpress_set2, repetition_time_chestpress_set2, display_info_chestpress_set2, bar_left_chestpress_set2, bar_right_chestpress_set2, per_left_chestpress_set2, per_right_chestpress_set2, angle_left_chestpress_set2, angle_right_chestpress_set2, exercise_mode, rest_chestpress_start_time_set2

    img = cv2.resize(img, (1280, 720))

    # Timer - starts timer based on set duration
    elapsed_time = time.time() - start_time_chestpress_set2
    remaining_time = max(0, repetition_time_chestpress_set2 - elapsed_time)


    if display_info_chestpress_set2:  # Check if to display counter, bar, and percentage
        img = detector_chestpress.findPose(img, False) # initializes img as variable for findpose function
        lmList_bicep = detector_chestpress.findPosition(img, False) # initializes lmList_bicep as variable for findPosition function

        # Define hand angles outside the if statement
        if len(lmList_bicep) != 0:
            angle_left_chestpress_set2 = detector_chestpress.findAngle(img, 11, 13, 15)
            angle_right_chestpress_set2 = detector_chestpress.findAngle(img, 12, 14, 16) # defines right arm landmark keypoints
            # (refer to mediapipe landmark mapping for number equivalent)

            # Interpolate angle to percentage and position on screen
            per_left_chestpress_set2 = np.interp(angle_left_chestpress_set2, (50, 155), (0, 100)) # first parenthesis, the value threshold of the angle. Second, represents the interp value
            bar_left_chestpress_set2 = np.interp(angle_left_chestpress_set2, (50, 165), (400, 200)) # 

            per_right_chestpress_set2 = np.interp(angle_right_chestpress_set2, (190, 300), (100, 0)) # 
            bar_right_chestpress_set2 = np.interp(angle_right_chestpress_set2, (190, 300), (200, 400)) # 

            if angle_left_chestpress_set2 >= 155:
                if dir_chestpress_left_set2 == 0 and count_chestpress_left_set2 < 5:
                    count_chestpress_left_set2 += 0.5
                    if count_chestpress_left_set2 == 5:
                        dir_chestpress_left_set2 = -1
                    else:
                        dir_chestpress_left_set2 = 1 
            elif angle_left_chestpress_set2 <= 50:
                if dir_chestpress_left_set2 == 1 and count_chestpress_left_set2 < 5:
                    count_chestpress_left_set2 += 0.5
                    if count_chestpress_left_set2 == 5:
                        dir_chestpress_left_set2 = -1
                    else:
                        dir_chestpress_left_set2 = 0  

            if angle_right_chestpress_set2 <= 190: 
                if dir_chestpress_right_set2 == 0 and count_chestpress_right_set2 < 5:
                    count_chestpress_right_set2 += 0.5
                    if count_chestpress_right_set2 == 5:
                        dir_chestpress_right_set2 = -1
                    else:
                        dir_chestpress_right_set2 = 1 

            if angle_right_chestpress_set2 >= 270:
                if dir_chestpress_right_set2 == 1 and count_chestpress_right_set2 < 5:
                    count_chestpress_right_set2 += 0.5
                    if count_chestpress_right_set2 == 5:
                        dir_chestpress_right_set2 = -1
                    else:
                        dir_chestpress_right_set2 = 0

        # label
        cvzone.putTextRect(img, 'Chest Press Tracker SET 2', [345, 30], thickness=2, border=2, scale=2.5) 

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # bar
        cv2.putText(img, f"R {int(per_right_chestpress_set2)}%" , (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_chestpress_set2)), (50, 400), (0, 0, 255), -1)

        cv2.putText(img, f"L {int(per_left_chestpress_set2)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_chestpress_set2)), (995, 400), (0, 0, 255), -1)
        
        if angle_left_chestpress_set2 >= 155:
            cv2.rectangle(img, (952, int(bar_left_chestpress_set2)), (995, 400), (0, 255, 0), -1)

        if angle_right_chestpress_set2 <= 190:
            cv2.rectangle(img, (8, int(bar_right_chestpress_set2)), (50, 400), (0, 255, 0), -1)

    #count
    cv2.rectangle(img, (20, 20), (140, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(count_chestpress_right_set2)}/5", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (150, 20), (270, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(count_chestpress_right_set2)}/5", (160, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255 ,255), 7)

    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
        display_info_chestpress_set2 = False
        exercise_mode = "rest_chestpress_set2"
        rest_chestpress_start_time_set2 = time.time()

    if count_chestpress_right_set2 == 5 and count_chestpress_left_set2 == 5:
        cvzone.putTextRect(img, 'All Repetitions Completed', [390, 30], thickness=2, border=2, scale=2.5)
        display_info_chestpress_set2 = False
        exercise_mode = "rest_chestpress_set2"
        rest_chestpress_start_time_set2 = time.time()

    return img

def rest_chestpress_set2(img):
    global exercise_mode, rest_chestpress_start_time_set2, start_time_chestpress_set3
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_chestpress_start_time_set2
    rest_remaining_time = max(0, 10 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "chest_press_set3"
        start_time_chestpress_set3 = time.time()

    return img

def detect_chestpress_set3(img):
    global count_chestpress_left_set3, count_chestpress_right_set3, dir_chestpress_right_set3, dir_chestpress_left_set3, start_time_chestpress_set3, repetition_time_chestpress_set3, display_info_chestpress_set3, bar_left_chestpress_set3, bar_right_chestpress_set3, per_left_chestpress_set3, per_right_chestpress_set3, angle_left_chestpress_set3, angle_right_chestpress_set3, exercise_mode, rest_chestpress_start_time_set3

    img = cv2.resize(img, (1280, 720))

    # Timer - starts timer based on set duration
    elapsed_time = time.time() - start_time_chestpress_set3
    remaining_time = max(0, repetition_time_chestpress_set3 - elapsed_time)


    if display_info_chestpress_set3:  # Check if to display counter, bar, and percentage
        img = detector_chestpress.findPose(img, False) # initializes img as variable for findpose function
        lmList_bicep = detector_chestpress.findPosition(img, False) # initializes lmList_bicep as variable for findPosition function

        # Define hand angles outside the if statement
        if len(lmList_bicep) != 0:
            angle_left_chestpress_set3 = detector_chestpress.findAngle(img, 11, 13, 15)
            angle_right_chestpress_set3 = detector_chestpress.findAngle(img, 12, 14, 16) # defines right arm landmark keypoints
            # (refer to mediapipe landmark mapping for number equivalent)

            # Interpolate angle to percentage and position on screen
            per_left_chestpress_set3 = np.interp(angle_left_chestpress_set3, (50, 155), (0, 100)) # first parenthesis, the value threshold of the angle. Second, represents the interp value
            bar_left_chestpress_set3 = np.interp(angle_left_chestpress_set3, (50, 165), (400, 200)) # 

            per_right_chestpress_set3 = np.interp(angle_right_chestpress_set3, (190, 300), (100, 0)) # 
            bar_right_chestpress_set3 = np.interp(angle_right_chestpress_set3, (190, 300), (200, 400)) # 

            if angle_left_chestpress_set3 >= 155:
                if dir_chestpress_left_set3 == 0 and count_chestpress_left_set3 < 5:
                    count_chestpress_left_set3 += 0.5
                    if count_chestpress_left_set3 == 5:
                        dir_chestpress_left_set3 = -1
                    else:
                        dir_chestpress_left_set3 = 1 
            elif angle_left_chestpress_set3 <= 50:
                if dir_chestpress_left_set3 == 1 and count_chestpress_left_set3 < 5:
                    count_chestpress_left_set3 += 0.5
                    if count_chestpress_left_set3 == 5:
                        dir_chestpress_left_set3 = -1
                    else:
                        dir_chestpress_left_set3 = 0  

            if angle_right_chestpress_set3 <= 190: 
                if dir_chestpress_right_set3 == 0 and count_chestpress_right_set3 < 5:
                    count_chestpress_right_set3 += 0.5
                    if count_chestpress_right_set3 == 5:
                        dir_chestpress_right_set3 = -1
                    else:
                        dir_chestpress_right_set3 = 1 

            if angle_right_chestpress_set3 >= 270:
                if dir_chestpress_right_set3 == 1 and count_chestpress_right_set3 < 5:
                    count_chestpress_right_set3 += 0.5
                    if count_chestpress_right_set3 == 5:
                        dir_chestpress_right_set3 = -1
                    else:
                        dir_chestpress_right_set3 = 0

        # label
        cvzone.putTextRect(img, 'Chest Press Tracker SET 3', [345, 30], thickness=2, border=2, scale=2.5) 

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # bar
        cv2.putText(img, f"R {int(per_right_chestpress_set3)}%" , (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_chestpress_set3)), (50, 400), (0, 0, 255), -1)

        cv2.putText(img, f"L {int(per_left_chestpress_set3)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_chestpress_set3)), (995, 400), (0, 0, 255), -1)
        
        if angle_left_chestpress_set3 >= 155:
            cv2.rectangle(img, (952, int(bar_left_chestpress_set3)), (995, 400), (0, 255, 0), -1)

        if angle_right_chestpress_set3 <= 190:
            cv2.rectangle(img, (8, int(bar_right_chestpress_set3)), (50, 400), (0, 255, 0), -1)

    #count
    cv2.rectangle(img, (20, 20), (140, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(count_chestpress_right_set3)}/5", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (150, 20), (270, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(count_chestpress_right_set3)}/5", (160, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255 ,255), 7)

    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
        display_info_chestpress_set3 = False
        exercise_mode = "rest_chestpress_set3"
        rest_chestpress_start_time_set3 = time.time()

    if count_chestpress_right_set3 == 5 and count_chestpress_left_set3 == 5:
        cvzone.putTextRect(img, 'All Repetitions Completed', [390, 30], thickness=2, border=2, scale=2.5)
        display_info_chestpress_set3 = False
        exercise_mode = "rest_chestpress_set3"
        rest_chestpress_start_time_set3 = time.time()
    return img

def rest_chestpress_set3(img):
    global exercise_mode, rest_chestpress_start_time_set3, start_time_dumbbellfrontraise
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_chestpress_start_time_set3
    rest_remaining_time = max(0, 10 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "dumbbell_frontraise"
        start_time_dumbbellfrontraise = time.time()
    return img

def detect_dumbbellfrontraise(img):
    global count_left_dumbbellfrontraise, count_right_dumbbellfrontraise, dir_left_dumbbellfrontraise, dir_right_dumbbellfrontraise, start_time_dumbbellfrontraise, repetition_time_dumbbellfrontraise, display_info_dumbbellfrontraise, bar_left_dumbbellfrontraise, bar_right_dumbbellfrontraise, per_left_dumbbellfrontraise, per_right_dumbbellfrontraise, angle_left_dumbbellfrontraise, angle_right_dumbbellfrontraise, rest_dumbbellfrontraise_start_time, exercise_mode

    img = cv2.resize(img, (1280, 720))

    # Timer - starts timer based on set duration
    elapsed_time = time.time() - start_time_dumbbellfrontraise
    remaining_time = max(0, repetition_time_dumbbellfrontraise - elapsed_time)

    if display_info_dumbbellfrontraise:  # Check if to display counter, bar, and percentage
        img = detector_dumbbell.findPose(img, False)  # initializes img as variable for findpose function
        lmList = detector_dumbbell.findPosition(img, False)  # initializes lmList as variable for findPosition function

        # Define hand angles outside the if statement
        if len(lmList) != 0:

            angle_left_dumbbellfrontraise = detector_dumbbell.findAngle(img, 15, 11, 23, 13)
            angle_right_dumbbellfrontraise = detector_dumbbell.findAngle2(img, 24, 12, 16, 14) 


            # # Interpolate angle to percentage and position on screen
            per_left_dumbbellfrontraise = np.interp(angle_left_dumbbellfrontraise, (20, 150), (0, 100))
            bar_left_dumbbellfrontraise = np.interp(angle_left_dumbbellfrontraise, (20, 160), (400, 200))

            per_right_dumbbellfrontraise = np.interp(angle_right_dumbbellfrontraise, (20, 150), (0, 100))
            bar_right_dumbbellfrontraise = np.interp(angle_right_dumbbellfrontraise, (20, 160), (400, 200))

            #Check for the left dumbbell front raises
            if angle_left_dumbbellfrontraise >= 150:
                if dir_left_dumbbellfrontraise == 0 and count_left_dumbbellfrontraise < 5:
                    count_left_dumbbellfrontraise += 0.5
                    if count_left_dumbbellfrontraise == 5:
                        dir_left_dumbbellfrontraise = -1
                    else:
                        dir_left_dumbbellfrontraise = 1
            elif angle_left_dumbbellfrontraise <= 20:
                if dir_left_dumbbellfrontraise == 1 and count_left_dumbbellfrontraise < 5:
                    count_left_dumbbellfrontraise += 0.5
                    if count_left_dumbbellfrontraise == 5:
                        dir_left_dumbbellfrontraise = -1
                    else:
                        dir_left_dumbbellfrontraise = 0

            # Check for the right dumbbell front raises
            if angle_right_dumbbellfrontraise >= 150:
                if dir_right_dumbbellfrontraise == 0 and count_right_dumbbellfrontraise < 5:
                    count_right_dumbbellfrontraise += 0.5
                    if count_right_dumbbellfrontraise == 5:
                        dir_right_dumbbellfrontraise = -1
                    else:
                        dir_right_dumbbellfrontraise = 1
            if angle_right_dumbbellfrontraise <= 20:
                if dir_right_dumbbellfrontraise == 1 and count_right_dumbbellfrontraise < 5:
                    count_right_dumbbellfrontraise += 0.5
                    if count_right_dumbbellfrontraise == 5:
                        dir_right_dumbbellfrontraise = -1
                    else:
                        dir_right_dumbbellfrontraise = 0

        # label
        cvzone.putTextRect(img, 'Dumbbell Raise Tracker', [345, 30], thickness=2, border=2, scale=2.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # bar
        cv2.putText(img, f"R {int(per_right_dumbbellfrontraise)}%", (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_dumbbellfrontraise)), (50, 400), (0, 0, 255), -1)

        cv2.putText(img, f"L {int(per_left_dumbbellfrontraise)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_dumbbellfrontraise)), (995, 400), (0, 0, 255), -1)

        if angle_left_dumbbellfrontraise >= 150:
            cv2.rectangle(img, (952, int(bar_left_dumbbellfrontraise)), (995, 400), (0, 255, 0), -1)

        if angle_right_dumbbellfrontraise >= 150:
            cv2.rectangle(img, (8, int(bar_right_dumbbellfrontraise)), (50, 400), (0, 255, 0), -1)

    # count
    cv2.rectangle(img, (20, 20), (140, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(count_right_dumbbellfrontraise)}/5", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (150, 20), (270, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(count_left_dumbbellfrontraise)}/5", (160, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
        display_info_dumbbellfrontraise = False
        exercise_mode = "rest_dumbbellfrontraise"
        rest_dumbbellfrontraise_start_time = time.time()

    if count_right_dumbbellfrontraise == 5 and count_left_dumbbellfrontraise == 5:
        cvzone.putTextRect(img, 'All Repetitions Completed', [390, 30], thickness=2, border=2, scale=2.5)
        display_info_dumbbellfrontraise = False
        exercise_mode = "rest_dumbbellfrontraise"
        rest_dumbbellfrontraise_start_time = time.time()
    return img

def rest_dumbbellfrontraise(img):
    global exercise_mode, rest_dumbbellfrontraise_start_time, start_time_dumbbellfrontraise_set2
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_dumbbellfrontraise_start_time
    rest_remaining_time = max(0, 10 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "dumbbell_frontraise_set2"
        start_time_dumbbellfrontraise_set2 = time.time()

    return img

def detect_dumbbellfrontraise_set2(img):
    global count_left_dumbbellfrontraise_set2, count_right_dumbbellfrontraise_set2, dir_left_dumbbellfrontraise_set2, dir_right_dumbbellfrontraise_set2, start_time_dumbbellfrontraise_set2, repetition_time_dumbbellfrontraise_set2, display_info_dumbbellfrontraise_set2, bar_left_dumbbellfrontraise_set2, bar_right_dumbbellfrontraise_set2, per_left_dumbbellfrontraise_set2, per_right_dumbbellfrontraise_set2, angle_left_dumbbellfrontraise_set2, angle_right_dumbbellfrontraise_set2, rest_dumbbellfrontraise_start_time_set2, exercise_mode

    img = cv2.resize(img, (1280, 720))

    # Timer - starts timer based on set duration
    elapsed_time = time.time() - start_time_dumbbellfrontraise_set2
    remaining_time = max(0, repetition_time_dumbbellfrontraise_set2 - elapsed_time)

    if display_info_dumbbellfrontraise_set2:  # Check if to display counter, bar, and percentage
        img = detector_dumbbell.findPose(img, False)  # initializes img as variable for findpose function
        lmList = detector_dumbbell.findPosition(img, False)  # initializes lmList as variable for findPosition function

        # Define hand angles outside the if statement
        if len(lmList) != 0:

            angle_left_dumbbellfrontraise_set2 = detector_dumbbell.findAngle(img, 15, 11, 23, 13)
            angle_right_dumbbellfrontraise_set2 = detector_dumbbell.findAngle2(img, 24, 12, 16, 14) 


            # # Interpolate angle to percentage and position on screen
            per_left_dumbbellfrontraise_set2 = np.interp(angle_left_dumbbellfrontraise_set2, (20, 150), (0, 100))
            bar_left_dumbbellfrontraise_set2 = np.interp(angle_left_dumbbellfrontraise_set2, (20, 160), (400, 200))

            per_right_dumbbellfrontraise_set2 = np.interp(angle_right_dumbbellfrontraise_set2, (20, 150), (0, 100))
            bar_right_dumbbellfrontraise_set2 = np.interp(angle_right_dumbbellfrontraise_set2, (20, 160), (400, 200))

            #Check for the left dumbbell front raises
            if angle_left_dumbbellfrontraise_set2 >= 150:
                if dir_left_dumbbellfrontraise_set2 == 0 and count_left_dumbbellfrontraise_set2 < 5:
                    count_left_dumbbellfrontraise_set2 += 0.5
                    if count_left_dumbbellfrontraise_set2 == 5:
                        dir_left_dumbbellfrontraise_set2 = -1
                    else:
                        dir_left_dumbbellfrontraise_set2 = 1
            elif angle_left_dumbbellfrontraise_set2 <= 20:
                if dir_left_dumbbellfrontraise_set2 == 1 and count_left_dumbbellfrontraise_set2 < 5:
                    count_left_dumbbellfrontraise_set2 += 0.5
                    if count_left_dumbbellfrontraise_set2 == 5:
                        dir_left_dumbbellfrontraise_set2 = -1
                    else:
                        dir_left_dumbbellfrontraise_set2 = 0

            # Check for the right dumbbell front raises
            if angle_right_dumbbellfrontraise_set2 >= 150:
                if dir_right_dumbbellfrontraise_set2 == 0 and count_right_dumbbellfrontraise_set2 < 5:
                    count_right_dumbbellfrontraise_set2 += 0.5
                    if count_right_dumbbellfrontraise_set2 == 5:
                        dir_right_dumbbellfrontraise_set2 = -1
                    else:
                        dir_right_dumbbellfrontraise_set2 = 1
            if angle_right_dumbbellfrontraise_set2 <= 20:
                if dir_right_dumbbellfrontraise_set2 == 1 and count_right_dumbbellfrontraise_set2 < 5:
                    count_right_dumbbellfrontraise_set2 += 0.5
                    if count_right_dumbbellfrontraise_set2 == 5:
                        dir_right_dumbbellfrontraise_set2 = -1
                    else:
                        dir_right_dumbbellfrontraise_set2 = 0

        # label
        cvzone.putTextRect(img, 'Dumbbell Raise SET 2', [345, 30], thickness=2, border=2, scale=2.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # bar
        cv2.putText(img, f"R {int(per_right_dumbbellfrontraise_set2)}%", (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_dumbbellfrontraise_set2)), (50, 400), (0, 0, 255), -1)

        cv2.putText(img, f"L {int(per_left_dumbbellfrontraise_set2)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_dumbbellfrontraise_set2)), (995, 400), (0, 0, 255), -1)

        if angle_left_dumbbellfrontraise_set2 >= 150:
            cv2.rectangle(img, (952, int(bar_left_dumbbellfrontraise_set2)), (995, 400), (0, 255, 0), -1)

        if angle_right_dumbbellfrontraise_set2 >= 150:
            cv2.rectangle(img, (8, int(bar_right_dumbbellfrontraise_set2)), (50, 400), (0, 255, 0), -1)

    # count
    cv2.rectangle(img, (20, 20), (140, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(count_right_dumbbellfrontraise_set2)}/5", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (150, 20), (270, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(count_left_dumbbellfrontraise_set2)}/5", (160, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
        display_info_dumbbellfrontraise_set2 = False
        exercise_mode = "rest_dumbbellfrontraise_set2"
        rest_dumbbellfrontraise_start_time_set2 = time.time()

    if count_right_dumbbellfrontraise == 5 and count_left_dumbbellfrontraise == 5:
        cvzone.putTextRect(img, 'All Repetitions Completed', [390, 30], thickness=2, border=2, scale=2.5)
        display_info_dumbbellfrontraise_set2 = False
        exercise_mode = "rest_dumbbellfrontraise_set2"
        rest_dumbbellfrontraise_start_time_set2 = time.time()
    return img

def rest_dumbbellfrontraise_set2(img):
    global exercise_mode, rest_dumbbellfrontraise_start_time_set2, start_time_dumbbellfrontraise_set3
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_dumbbellfrontraise_start_time_set2
    rest_remaining_time = max(0, 10 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "dumbbell_frontraise_set3"
        start_time_dumbbellfrontraise_set3 = time.time()
    return img

def detect_dumbbellfrontraise_set3(img):
    global count_left_dumbbellfrontraise_set3, count_right_dumbbellfrontraise_set3, dir_left_dumbbellfrontraise_set3, dir_right_dumbbellfrontraise_set3, start_time_dumbbellfrontraise_set3, repetition_time_dumbbellfrontraise_set3, display_info_dumbbellfrontraise_set3, bar_left_dumbbellfrontraise_set3, bar_right_dumbbellfrontraise_set3, per_left_dumbbellfrontraise_set3, per_right_dumbbellfrontraise_set3, angle_left_dumbbellfrontraise_set3, angle_right_dumbbellfrontraise_set3, rest_dumbbellfrontraise_start_time_set3, exercise_mode

    img = cv2.resize(img, (1280, 720))

    # Timer - starts timer based on set duration
    elapsed_time = time.time() - start_time_dumbbellfrontraise_set3
    remaining_time = max(0, repetition_time_dumbbellfrontraise_set3 - elapsed_time)

    if display_info_dumbbellfrontraise_set3:  # Check if to display counter, bar, and percentage
        img = detector_dumbbell.findPose(img, False)  # initializes img as variable for findpose function
        lmList = detector_dumbbell.findPosition(img, False)  # initializes lmList as variable for findPosition function

        # Define hand angles outside the if statement
        if len(lmList) != 0:

            angle_left_dumbbellfrontraise_set3 = detector_dumbbell.findAngle(img, 15, 11, 23, 13)
            angle_right_dumbbellfrontraise_set3 = detector_dumbbell.findAngle2(img, 24, 12, 16, 14) 


            # # Interpolate angle to percentage and position on screen
            per_left_dumbbellfrontraise_set3 = np.interp(angle_left_dumbbellfrontraise_set3, (20, 150), (0, 100))
            bar_left_dumbbellfrontraise_set3 = np.interp(angle_left_dumbbellfrontraise_set3, (20, 160), (400, 200))

            per_right_dumbbellfrontraise_set3 = np.interp(angle_right_dumbbellfrontraise_set3, (20, 150), (0, 100))
            bar_right_dumbbellfrontraise_set3 = np.interp(angle_right_dumbbellfrontraise_set3, (20, 160), (400, 200))

            #Check for the left dumbbell front raises
            if angle_left_dumbbellfrontraise_set3 >= 150:
                if dir_left_dumbbellfrontraise_set3 == 0 and count_left_dumbbellfrontraise_set3 < 5:
                    count_left_dumbbellfrontraise_set3 += 0.5
                    if count_left_dumbbellfrontraise_set3 == 5:
                        dir_left_dumbbellfrontraise_set3 = -1
                    else:
                        dir_left_dumbbellfrontraise_set3 = 1
            elif angle_left_dumbbellfrontraise_set3 <= 20:
                if dir_left_dumbbellfrontraise_set3 == 1 and count_left_dumbbellfrontraise_set3 < 5:
                    count_left_dumbbellfrontraise += 0.5
                    if count_left_dumbbellfrontraise_set3 == 5:
                        dir_left_dumbbellfrontraise_set3 = -1
                    else:
                        dir_left_dumbbellfrontraise_set3 = 0

            # Check for the right dumbbell front raises
            if angle_right_dumbbellfrontraise_set3 >= 150:
                if dir_right_dumbbellfrontraise_set3 == 0 and count_right_dumbbellfrontraise_set3 < 5:
                    count_right_dumbbellfrontraise_set3 += 0.5
                    if count_right_dumbbellfrontraise_set3 == 5:
                        dir_right_dumbbellfrontraise_set3 = -1
                    else:
                        dir_right_dumbbellfrontraise_set3 = 1
            if angle_right_dumbbellfrontraise_set3 <= 20:
                if dir_right_dumbbellfrontraise_set3 == 1 and count_right_dumbbellfrontraise_set3 < 5:
                    count_right_dumbbellfrontraise_set3 += 0.5
                    if count_right_dumbbellfrontraise_set3 == 5:
                        dir_right_dumbbellfrontraise_set3 = -1
                    else:
                        dir_right_dumbbellfrontraise_set3 = 0

        # label
        cvzone.putTextRect(img, 'Dumbbell Raise SET 3', [345, 30], thickness=2, border=2, scale=2.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # bar
        cv2.putText(img, f"R {int(per_right_dumbbellfrontraise_set3)}%", (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_dumbbellfrontraise_set3)), (50, 400), (0, 0, 255), -1)

        cv2.putText(img, f"L {int(per_left_dumbbellfrontraise_set3)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_dumbbellfrontraise_set3)), (995, 400), (0, 0, 255), -1)

        if angle_left_dumbbellfrontraise_set3 >= 150:
            cv2.rectangle(img, (952, int(bar_left_dumbbellfrontraise_set3)), (995, 400), (0, 255, 0), -1)

        if angle_right_dumbbellfrontraise_set3 >= 150:
            cv2.rectangle(img, (8, int(bar_right_dumbbellfrontraise_set3)), (50, 400), (0, 255, 0), -1)

    # count
    cv2.rectangle(img, (20, 20), (140, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(count_right_dumbbellfrontraise_set3)}/5", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (150, 20), (270, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(count_left_dumbbellfrontraise_set3)}/5", (160, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
        display_info_dumbbellfrontraise_set3 = False
        exercise_mode = "rest_dumbbellfrontraise_set3"
        rest_dumbbellfrontraise_start_time_set3 = time.time()

    if count_right_dumbbellfrontraise == 5 and count_left_dumbbellfrontraise == 5:
        cvzone.putTextRect(img, 'All Repetitions Completed', [390, 30], thickness=2, border=2, scale=2.5)
        display_info_dumbbellfrontraise_set3 = False
        exercise_mode = "rest_dumbbellfrontraise_set3"
        rest_dumbbellfrontraise_start_time_set3 = time.time()

    return img

def rest_dumbbellfrontraise_set3(img):
    global exercise_mode, rest_dumbbellfrontraise_start_time_set3, start_time_alternatinglunge
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_dumbbellfrontraise_start_time_set3
    rest_remaining_time = max(0, 10 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "alternating_lunge"
        start_time_alternatinglunge = time.time()
    return img

def detect_alternatinglunge(img):
    global count_alternating_left_lunge, count_alternating_right_lunge, dir_alternating_left_lunge, dir_alternating_right_lunge, start_time_alternatinglunge, repetition_time_alternatinglunge, per_left_leg_alternatinglunge, per_right_leg_alternatinglunge, display_info_alternatinglunge, bar_left_leg_alternatinglunge, bar_right_leg_alternatinglunge, leftleg_alternatinglunge, rightleg_alternatinglunge, cooldown_duration_alternatinglunge, cooldown_timer_alternatinglunge, color_right_leg_alternatinglunge, color_left_leg_alternatinglunge, exercise_mode, rest_alternatinglunge_start_time, orientation, orientation2

    img = cv2.resize(img, (1280, 720))

    elapsed_time = time.time() - start_time_alternatinglunge
    remaining_time = max(0, repetition_time_alternatinglunge - elapsed_time)

    if display_info_alternatinglunge:  # Check if to display counter, bar, and percentage
        img = detector_alternatingleftlunge.findPose(img, False)
        lmList_jumping_jacks = detector_alternatingleftlunge.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_jumping_jacks) != 0:

            # Right and Left keypoints
            rightleg_alternatinglunge, orientation = detector_alternatingleftlunge.AlternatingLunge(img, 24, 26, 28, True)
            leftleg_alternatinglunge, orientation2 = detector_alternatingleftlunge.AlternatingLunge(img, 23, 25, 27, True)

            if cooldown_timer_alternatinglunge > 0:
                cooldown_timer_alternatinglunge -= 1

            #print(orientation, orientation2)
            if orientation == 'right' and orientation2 == 'right':
                    per_right_leg_alternatinglunge = np.interp(rightleg_alternatinglunge, (90, 170), (100, 0))
                    bar_right_leg_alternatinglunge = np.interp(rightleg_alternatinglunge, (90, 170), (480, 680))
                    per_left_leg_alternatinglunge = np.interp(leftleg_alternatinglunge, (90, 170), (100, 0))
                    bar_left_leg_alternatinglunge = np.interp(leftleg_alternatinglunge, (90, 170), (480, 680))

                    if int(per_left_leg_alternatinglunge) == 100:
                        color_left_leg_alternatinglunge = (0, 255, 0)  # Change color of left leg bar to green
                    elif int(per_right_leg_alternatinglunge) == 100:
                        color_right_leg_alternatinglunge = (0, 255, 0)
                    else:
                        color_left_leg_alternatinglunge = (0, 0, 255)  # Keep color of left leg bar as red
                        color_right_leg_alternatinglunge = (0, 0, 255)

                    if rightleg_alternatinglunge <= 80:
                        if dir_alternating_right_lunge == 0:
                            count_alternating_right_lunge += 0.5
                            dir_alternating_right_lunge = 1
                            cooldown_timer_alternatinglunge = cooldown_duration_alternatinglunge
                    elif rightleg_alternatinglunge >= 150:
                        if dir_alternating_right_lunge == 1:
                            count_alternating_right_lunge += 0.5
                            dir_alternating_right_lunge = 0
                            cooldown_timer_alternatinglunge = cooldown_duration_alternatinglunge
                    
                    if leftleg_alternatinglunge <= 80:
                        if dir_alternating_left_lunge == 0:
                            count_alternating_left_lunge += 0.5
                            dir_alternating_left_lunge = 1
                            cooldown_timer_alternatinglunge = cooldown_duration_alternatinglunge
                    elif leftleg_alternatinglunge >= 150:
                        if dir_alternating_left_lunge == 1:
                            count_alternating_left_lunge += 0.5
                            dir_alternating_left_lunge = 0
                            cooldown_timer_alternatinglunge = cooldown_duration_alternatinglunge

            elif orientation =='left' and orientation2 == 'left':
                if leftleg_alternatinglunge is not None and rightleg_alternatinglunge is not None:
                    per_right_leg_alternatinglunge = np.interp(rightleg_alternatinglunge, (190, 280), (0, 100))
                    bar_right_leg_alternatinglunge = np.interp(rightleg_alternatinglunge, (190, 280), (680, 480))
                    per_left_leg_alternatinglunge = np.interp(leftleg_alternatinglunge, (190, 280), (0, 100))
                    bar_left_leg_alternatinglunge = np.interp(leftleg_alternatinglunge, (190, 280), (680, 480))

                    if int(per_left_leg_alternatinglunge) == 100:
                        color_left_leg_alternatinglunge = (0, 255, 0)  # Change color of left leg bar to green
                    elif int(per_right_leg_alternatinglunge) == 100:
                        color_right_leg_alternatinglunge = (0, 255, 0)
                    else:
                        color_left_leg_alternatinglunge = (0, 0, 255)  # Keep color of left leg bar as red
                        color_right_leg_alternatinglunge = (0, 0, 255)

                    if rightleg_alternatinglunge > 280:
                        if dir_alternating_right_lunge == 0:
                            count_alternating_right_lunge += 0.5
                            dir_alternating_right_lunge = 1
                            cooldown_timer_alternatinglunge = cooldown_duration_alternatinglunge
                    elif rightleg_alternatinglunge < 179:
                        if dir_alternating_right_lunge == 1:
                            count_alternating_right_lunge += 0.5
                            dir_alternating_right_lunge = 0
                            cooldown_timer_alternatinglunge = cooldown_duration_alternatinglunge
                    if leftleg_alternatinglunge > 280:
                        if dir_alternating_left_lunge == 0:
                            count_alternating_left_lunge += 0.5
                            dir_alternating_left_lunge = 1
                            cooldown_timer_alternatinglunge = cooldown_duration_alternatinglunge
                    elif leftleg_alternatinglunge < 179:
                        if dir_alternating_left_lunge == 1:
                            count_alternating_left_lunge += 0.5
                            dir_alternating_left_lunge = 0
                            cooldown_timer_alternatinglunge = cooldown_duration_alternatinglunge

            elif orientation == 'front' and orientation2 == 'front':
                    
                    per_right_leg_alternatinglunge = np.interp(rightleg_alternatinglunge, (100, 200), (100, 0))
                    bar_right_leg_alternatinglunge = np.interp(rightleg_alternatinglunge, (100, 200), (480, 680))
                    per_left_leg_alternatinglunge = np.interp(leftleg_alternatinglunge, (100, 200), (100, 0))
                    bar_left_leg_alternatinglunge = np.interp(leftleg_alternatinglunge, (100, 200), (480, 680))


                    if int(per_left_leg_alternatinglunge) == 100:
                        color_left_leg_alternatinglunge = (0, 255, 0)  # Change color of left leg bar to green
                    elif int(per_right_leg_alternatinglunge) == 100:
                        color_right_leg_alternatinglunge = (0, 255, 0)
                    else:
                        color_left_leg_alternatinglunge = (0, 0, 255)  # Keep color of left leg bar as red
                        color_right_leg_alternatinglunge = (0, 0, 255)

                    if rightleg_alternatinglunge <= 150 and leftleg_alternatinglunge <= 100:
                        if dir_alternating_right_lunge == 0:
                            count_alternating_right_lunge += 0.5
                            dir_alternating_right_lunge = 1
                            cooldown_timer_alternatinglunge = cooldown_duration_alternatinglunge
                    else: 
                        if dir_alternating_right_lunge == 1:
                            count_alternating_right_lunge += 0.5
                            dir_alternating_right_lunge = 0
                            cooldown_timer_alternatinglunge = cooldown_duration_alternatinglunge

                    if rightleg_alternatinglunge <= 100 and leftleg_alternatinglunge <= 150:
                        if dir_alternating_left_lunge == 0:
                            count_alternating_left_lunge += 0.5
                            dir_alternating_left_lunge = 1
                            cooldown_timer_alternatinglunge = cooldown_duration_alternatinglunge
                    else:
                        if dir_alternating_left_lunge == 1:
                            count_alternating_left_lunge += 0.5
                            dir_alternating_left_lunge = 0
                            cooldown_timer_alternatinglunge = cooldown_duration_alternatinglunge

  
        cvzone.putTextRect(img, 'Leg Lunge (alternate)', [345, 30], thickness=2, border=2, scale=2.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # Orientation
        cv2.rectangle(img, (890, 100), (1180, 160), (0, 0, 255), -2)
        cv2.putText(img, f"Orientation: {orientation}", (900, 140), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)

        # RIGHT LEG
        cv2.putText(img, f"R {int(per_right_leg_alternatinglunge)}%", (24, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 480), (50, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_leg_alternatinglunge)), (50, 680), color_right_leg_alternatinglunge, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_left_leg_alternatinglunge)}%", (962, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 480), (995, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_leg_alternatinglunge)), (995, 680), color_left_leg_alternatinglunge, -1)

    # Counter 
    cv2.rectangle(img, (20, 20), (140, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(count_alternating_right_lunge)}/5", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (150, 20), (270, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(count_alternating_left_lunge)}/5", (160, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    # Timer
    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
        display_info_alternatinglunge = False
        exercise_mode = "rest_alternatinglunge"
        rest_alternatinglunge_start_time = time.time()

    # Repetition
    if count_alternating_left_lunge >= 5:  # Assuming 10 jumping jacks for demonstration
        cvzone.putTextRect(img, 'Exercise Complete', [390, 30], thickness=2, border=2, scale=2.5)
        display_info_alternatinglunge = False
        exercise_mode = "rest_alternatinglunge"
        rest_alternatinglunge_start_time = time.time()

    return img

def rest_alternatinglunge(img):
    global exercise_mode, rest_alternatinglunge_start_time, start_time_alternatinglunge_set2
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_alternatinglunge_start_time
    rest_remaining_time = max(0, 10 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "alternating_lunge_set2"
        start_time_alternatinglunge_set2 = time.time()

    return img

def detect_alternatinglunge_set2(img):
    global count_alternating_left_lunge_set2, count_alternating_right_lunge_set2, dir_alternating_left_lunge_set2, dir_alternating_right_lunge_set2, start_time_alternatinglunge_set2, repetition_time_alternatinglunge_set2, per_left_leg_alternatinglunge_set2, per_right_leg_alternatinglunge_set2, display_info_alternatinglunge_set2, bar_left_leg_alternatinglunge_set2, bar_right_leg_alternatinglunge_set2, leftleg_alternatinglunge_set2, rightleg_alternatinglunge_set2, cooldown_duration_alternatinglunge_set2, cooldown_timer_alternatinglunge_set2, color_right_leg_alternatinglunge_set2, color_left_leg_alternatinglunge_set2, exercise_mode, rest_alternatinglunge_start_time_set2, orientation, orientation2

    img = cv2.resize(img, (1280, 720))

    elapsed_time = time.time() - start_time_alternatinglunge_set2
    remaining_time = max(0, repetition_time_alternatinglunge_set2 - elapsed_time) #repetition_time_alternatinglunge_set2

    if display_info_alternatinglunge_set2:  # Check if to display counter, bar, and percentage
        img = detector_alternatingleftlunge.findPose(img, False)
        lmList_jumping_jacks = detector_alternatingleftlunge.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_jumping_jacks) != 0:

            # Right and Left keypoints
            rightleg_alternatinglunge_set2, orientation = detector_alternatingleftlunge.AlternatingLunge(img, 24, 26, 28, True)
            leftleg_alternatinglunge_set2, orientation2 = detector_alternatingleftlunge.AlternatingLunge(img, 23, 25, 27, True)

            if cooldown_timer_alternatinglunge_set2 > 0:
                cooldown_timer_alternatinglunge_set2 -= 1

            #print(orientation, orientation2)
            if orientation == 'right' and orientation2 == 'right':
                    per_right_leg_alternatinglunge_set2 = np.interp(rightleg_alternatinglunge_set2, (90, 170), (100, 0))
                    bar_right_leg_alternatinglunge_set2 = np.interp(rightleg_alternatinglunge_set2, (90, 170), (480, 680))
                    per_left_leg_alternatinglunge_set2 = np.interp(leftleg_alternatinglunge_set2, (90, 170), (100, 0))
                    bar_left_leg_alternatinglunge_set2 = np.interp(leftleg_alternatinglunge_set2, (90, 170), (480, 680))

                    if int(per_left_leg_alternatinglunge_set2) == 100:
                        color_left_leg_alternatinglunge_set2 = (0, 255, 0)  # Change color of left leg bar to green
                    elif int(per_right_leg_alternatinglunge_set2) == 100:
                        color_right_leg_alternatinglunge_set2 = (0, 255, 0)
                    else:
                        color_left_leg_alternatinglunge_set2 = (0, 0, 255)  # Keep color of left leg bar as red
                        color_right_leg_alternatinglunge_set2 = (0, 0, 255)

                    if rightleg_alternatinglunge_set2 <= 80:
                        if dir_alternating_right_lunge_set2 == 0:
                            count_alternating_right_lunge_set2 += 0.5
                            dir_alternating_right_lunge_set2 = 1
                            cooldown_timer_alternatinglunge_set2 = cooldown_duration_alternatinglunge_set2
                    elif rightleg_alternatinglunge_set2 >= 150:
                        if dir_alternating_right_lunge_set2 == 1:
                            count_alternating_right_lunge_set2 += 0.5
                            dir_alternating_right_lunge_set2 = 0
                            cooldown_timer_alternatinglunge_set2 = cooldown_duration_alternatinglunge_set2
                    
                    if leftleg_alternatinglunge_set2 <= 80:
                        if dir_alternating_left_lunge_set2 == 0:
                            count_alternating_left_lunge_set2 += 0.5
                            dir_alternating_left_lunge_set2 = 1
                            cooldown_timer_alternatinglunge_set2 = cooldown_duration_alternatinglunge_set2
                    elif leftleg_alternatinglunge_set2 >= 150:
                        if dir_alternating_left_lunge_set2 == 1:
                            count_alternating_left_lunge_set2 += 0.5
                            dir_alternating_left_lunge_set2 = 0
                            cooldown_timer_alternatinglunge_set2 = cooldown_duration_alternatinglunge_set2

            elif orientation =='left' and orientation2 == 'left':
                if leftleg_alternatinglunge_set2 is not None and rightleg_alternatinglunge_set2 is not None:
                    per_right_leg_alternatinglunge_set2 = np.interp(rightleg_alternatinglunge_set2, (190, 280), (0, 100))
                    bar_right_leg_alternatinglunge_set2 = np.interp(rightleg_alternatinglunge_set2, (190, 280), (680, 480))
                    per_left_leg_alternatinglunge_set2 = np.interp(leftleg_alternatinglunge_set2, (190, 280), (0, 100))
                    bar_left_leg_alternatinglunge_set2 = np.interp(leftleg_alternatinglunge_set2, (190, 280), (680, 480))

                    if int(per_left_leg_alternatinglunge_set2) == 100:
                        color_left_leg_alternatinglunge_set2 = (0, 255, 0)  # Change color of left leg bar to green
                    elif int(per_right_leg_alternatinglunge_set2) == 100:
                        color_right_leg_alternatinglunge_set2 = (0, 255, 0)
                    else:
                        color_left_leg_alternatinglunge_set2 = (0, 0, 255)  # Keep color of left leg bar as red
                        color_right_leg_alternatinglunge_set2 = (0, 0, 255)

                    if rightleg_alternatinglunge_set2 > 280:
                        if dir_alternating_right_lunge_set2 == 0:
                            count_alternating_right_lunge_set2 += 0.5
                            dir_alternating_right_lunge_set2 = 1
                            cooldown_timer_alternatinglunge_set2 = cooldown_duration_alternatinglunge_set2
                    elif rightleg_alternatinglunge_set2 < 179:
                        if dir_alternating_right_lunge_set2 == 1:
                            count_alternating_right_lunge_set2 += 0.5
                            dir_alternating_right_lunge_set2 = 0
                            cooldown_timer_alternatinglunge_set2 = cooldown_duration_alternatinglunge_set2
                    if leftleg_alternatinglunge_set2 > 280:
                        if dir_alternating_left_lunge_set2 == 0:
                            count_alternating_left_lunge_set2 += 0.5
                            dir_alternating_left_lunge_set2 = 1
                            cooldown_timer_alternatinglunge_set2 = cooldown_duration_alternatinglunge_set2
                    elif leftleg_alternatinglunge_set2 < 179:
                        if dir_alternating_left_lunge_set2 == 1:
                            count_alternating_left_lunge_set2 += 0.5
                            dir_alternating_left_lunge_set2 = 0
                            cooldown_timer_alternatinglunge_set2 = cooldown_duration_alternatinglunge_set2

            elif orientation == 'front' and orientation2 == 'front':
                    
                    per_right_leg_alternatinglunge_set2 = np.interp(rightleg_alternatinglunge_set2, (100, 200), (100, 0))
                    bar_right_leg_alternatinglunge_set2 = np.interp(rightleg_alternatinglunge_set2, (100, 200), (480, 680))
                    per_left_leg_alternatinglunge_set2 = np.interp(leftleg_alternatinglunge_set2, (100, 200), (100, 0))
                    bar_left_leg_alternatinglunge_set2 = np.interp(leftleg_alternatinglunge_set2, (100, 200), (480, 680))


                    if int(per_left_leg_alternatinglunge_set2) == 100:
                        color_left_leg_alternatinglunge_set2 = (0, 255, 0)  # Change color of left leg bar to green
                    elif int(per_right_leg_alternatinglunge_set2) == 100:
                        color_right_leg_alternatinglunge_set2 = (0, 255, 0)
                    else:
                        color_left_leg_alternatinglunge_set2 = (0, 0, 255)  # Keep color of left leg bar as red
                        color_right_leg_alternatinglunge_set2 = (0, 0, 255)

                    if rightleg_alternatinglunge_set2 <= 150 and leftleg_alternatinglunge_set2 <= 100:
                        if dir_alternating_right_lunge_set2 == 0:
                            count_alternating_right_lunge_set2 += 0.5
                            dir_alternating_right_lunge_set2 = 1
                            cooldown_timer_alternatinglunge_set2 = cooldown_duration_alternatinglunge_set2
                    else: 
                        if dir_alternating_right_lunge_set2 == 1:
                            count_alternating_right_lunge_set2 += 0.5
                            dir_alternating_right_lunge_set2 = 0
                            cooldown_timer_alternatinglunge_set2 = cooldown_duration_alternatinglunge_set2

                    if rightleg_alternatinglunge_set2 <= 100 and leftleg_alternatinglunge_set2 <= 150:
                        if dir_alternating_left_lunge_set2 == 0:
                            count_alternating_left_lunge_set2 += 0.5
                            dir_alternating_left_lunge_set2 = 1
                            cooldown_timer_alternatinglunge_set2 = cooldown_duration_alternatinglunge_set2
                    else:
                        if dir_alternating_left_lunge_set2 == 1:
                            count_alternating_left_lunge_set2 += 0.5
                            dir_alternating_left_lunge_set2 = 0
                            cooldown_timer_alternatinglunge_set2 = cooldown_duration_alternatinglunge_set2

  
        cvzone.putTextRect(img, 'Leg Lunge (alternate) SET 2', [345, 30], thickness=2, border=2, scale=2.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # Orientation
        cv2.rectangle(img, (890, 100), (1180, 160), (0, 0, 255), -2)
        cv2.putText(img, f"Orientation: {orientation}", (900, 140), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)

        # RIGHT LEG
        cv2.putText(img, f"R {int(per_right_leg_alternatinglunge_set2)}%", (24, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 480), (50, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_leg_alternatinglunge_set2)), (50, 680), color_right_leg_alternatinglunge_set2, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_left_leg_alternatinglunge_set2)}%", (962, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 480), (995, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_leg_alternatinglunge_set2)), (995, 680), color_left_leg_alternatinglunge_set2, -1)

    # Counter 
    cv2.rectangle(img, (20, 20), (140, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(count_alternating_right_lunge_set2)}/5", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (150, 20), (270, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(count_alternating_left_lunge_set2)}/5", (160, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    # Timer
    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
        display_info_alternatinglunge_set2 = False
        exercise_mode = "rest_alternatinglunge_set2"
        rest_alternatinglunge_start_time_set2 = time.time()

    # Repetition
    if count_alternating_left_lunge_set2 >= 5:  # Assuming 10 jumping jacks for demonstration
        cvzone.putTextRect(img, 'Exercise Complete', [390, 30], thickness=2, border=2, scale=2.5)
        display_info_alternatinglunge_set2 = False
        exercise_mode = "rest_alternatinglunge_set2"
        rest_alternatinglunge_start_time_set2 = time.time()
    return img

def rest_alternatinglunge_set2(img):
    global exercise_mode, rest_alternatinglunge_start_time_set2, start_time_alternatinglunge_set3
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_alternatinglunge_start_time_set2
    rest_remaining_time = max(0, 10 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "alternating_lunge_set3"
        start_time_alternatinglunge_set3 = time.time()
    return img

def detect_alternatinglunge_set3(img):
    global count_alternating_left_lunge_set3, count_alternating_right_lunge_set3, dir_alternating_left_lunge_set3, dir_alternating_right_lunge_set3, start_time_alternatinglunge_set3, repetition_time_alternatinglunge_set3, per_left_leg_alternatinglunge_set3, per_right_leg_alternatinglunge_set3, display_info_alternatinglunge_set3, bar_left_leg_alternatinglunge_set3, bar_right_leg_alternatinglunge_set3, leftleg_alternatinglunge_set3, rightleg_alternatinglunge_set3, cooldown_duration_alternatinglunge_set3, cooldown_timer_alternatinglunge_set3, color_right_leg_alternatinglunge_set3, color_left_leg_alternatinglunge_set3, exercise_mode, rest_alternatinglunge_start_time_set3, orientation, orientation2

    img = cv2.resize(img, (1280, 720))

    elapsed_time = time.time() - start_time_alternatinglunge_set3
    remaining_time = max(0, 10 - elapsed_time) #repetition_time_alternatinglunge_set3

    if display_info_alternatinglunge_set3:  # Check if to display counter, bar, and percentage
        img = detector_alternatingleftlunge.findPose(img, False)
        lmList_jumping_jacks = detector_alternatingleftlunge.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_jumping_jacks) != 0:

            # Right and Left keypoints
            rightleg_alternatinglunge_set3, orientation = detector_alternatingleftlunge.AlternatingLunge(img, 24, 26, 28, True)
            leftleg_alternatinglunge_set3, orientation2 = detector_alternatingleftlunge.AlternatingLunge(img, 23, 25, 27, True)

            if cooldown_timer_alternatinglunge_set3 > 0:
                cooldown_timer_alternatinglunge_set3 -= 1

            #print(orientation, orientation2)
            if orientation == 'right' and orientation2 == 'right':
                    per_right_leg_alternatinglunge_set3 = np.interp(rightleg_alternatinglunge_set3, (90, 170), (100, 0))
                    bar_right_leg_alternatinglunge_set3 = np.interp(rightleg_alternatinglunge_set3, (90, 170), (480, 680))
                    per_left_leg_alternatinglunge_set3 = np.interp(leftleg_alternatinglunge_set3, (90, 170), (100, 0))
                    bar_left_leg_alternatinglunge_set3 = np.interp(leftleg_alternatinglunge_set3, (90, 170), (480, 680))

                    if int(per_left_leg_alternatinglunge_set3) == 100:
                        color_left_leg_alternatinglunge_set3 = (0, 255, 0)  # Change color of left leg bar to green
                    elif int(per_right_leg_alternatinglunge_set3) == 100:
                        color_right_leg_alternatinglunge_set3 = (0, 255, 0)
                    else:
                        color_left_leg_alternatinglunge_set3 = (0, 0, 255)  # Keep color of left leg bar as red
                        color_right_leg_alternatinglunge_set3 = (0, 0, 255)

                    if rightleg_alternatinglunge_set3 <= 80:
                        if dir_alternating_right_lunge_set3 == 0:
                            count_alternating_right_lunge_set3 += 0.5
                            dir_alternating_right_lunge_set3 = 1
                            cooldown_timer_alternatinglunge_set3 = cooldown_duration_alternatinglunge_set3
                    elif rightleg_alternatinglunge_set3 >= 150:
                        if dir_alternating_right_lunge_set3 == 1:
                            count_alternating_right_lunge_set3 += 0.5
                            dir_alternating_right_lunge_set3 = 0
                            cooldown_timer_alternatinglunge_set3 = cooldown_duration_alternatinglunge_set3
                    
                    if leftleg_alternatinglunge_set3 <= 80:
                        if dir_alternating_left_lunge_set3 == 0:
                            count_alternating_left_lunge_set3 += 0.5
                            dir_alternating_left_lunge_set3 = 1
                            cooldown_timer_alternatinglunge_set3 = cooldown_duration_alternatinglunge_set3
                    elif leftleg_alternatinglunge_set3 >= 150:
                        if dir_alternating_left_lunge_set3 == 1:
                            count_alternating_left_lunge_set3 += 0.5
                            dir_alternating_left_lunge_set3 = 0
                            cooldown_timer_alternatinglunge_set3 = cooldown_duration_alternatinglunge_set3

            elif orientation =='left' and orientation2 == 'left':
                if leftleg_alternatinglunge_set3 is not None and rightleg_alternatinglunge_set3 is not None:
                    per_right_leg_alternatinglunge_set3 = np.interp(rightleg_alternatinglunge_set3, (190, 280), (0, 100))
                    bar_right_leg_alternatinglunge_set3 = np.interp(rightleg_alternatinglunge_set3, (190, 280), (680, 480))
                    per_left_leg_alternatinglunge_set3 = np.interp(leftleg_alternatinglunge_set3, (190, 280), (0, 100))
                    bar_left_leg_alternatinglunge_set3 = np.interp(leftleg_alternatinglunge_set3, (190, 280), (680, 480))

                    if int(per_left_leg_alternatinglunge_set3) == 100:
                        color_left_leg_alternatinglunge_set3 = (0, 255, 0)  # Change color of left leg bar to green
                    elif int(per_right_leg_alternatinglunge_set3) == 100:
                        color_right_leg_alternatinglunge_set3 = (0, 255, 0)
                    else:
                        color_left_leg_alternatinglunge_set3 = (0, 0, 255)  # Keep color of left leg bar as red
                        color_right_leg_alternatinglunge_set3 = (0, 0, 255)

                    if rightleg_alternatinglunge_set3 > 280:
                        if dir_alternating_right_lunge_set3 == 0:
                            count_alternating_right_lunge_set3 += 0.5
                            dir_alternating_right_lunge_set3 = 1
                            cooldown_timer_alternatinglunge_set3 = cooldown_duration_alternatinglunge_set3
                    elif rightleg_alternatinglunge_set3 < 179:
                        if dir_alternating_right_lunge_set3 == 1:
                            count_alternating_right_lunge_set3 += 0.5
                            dir_alternating_right_lunge_set3 = 0
                            cooldown_timer_alternatinglunge_set3 = cooldown_duration_alternatinglunge_set3
                    if leftleg_alternatinglunge_set3 > 280:
                        if dir_alternating_left_lunge_set3 == 0:
                            count_alternating_left_lunge_set3 += 0.5
                            dir_alternating_left_lunge_set3 = 1
                            cooldown_timer_alternatinglunge_set3 = cooldown_duration_alternatinglunge_set3
                    elif leftleg_alternatinglunge_set3 < 179:
                        if dir_alternating_left_lunge_set3 == 1:
                            count_alternating_left_lunge_set3 += 0.5
                            dir_alternating_left_lunge_set3 = 0
                            cooldown_timer_alternatinglunge_set3 = cooldown_duration_alternatinglunge_set3

            elif orientation == 'front' and orientation2 == 'front':
                    
                    per_right_leg_alternatinglunge_set3 = np.interp(rightleg_alternatinglunge_set3, (100, 200), (100, 0))
                    bar_right_leg_alternatinglunge_set3 = np.interp(rightleg_alternatinglunge_set3, (100, 200), (480, 680))
                    per_left_leg_alternatinglunge_set3 = np.interp(leftleg_alternatinglunge_set3, (100, 200), (100, 0))
                    bar_left_leg_alternatinglunge_set3 = np.interp(leftleg_alternatinglunge_set3, (100, 200), (480, 680))


                    if int(per_left_leg_alternatinglunge_set3) == 100:
                        color_left_leg_alternatinglunge_set3 = (0, 255, 0)  # Change color of left leg bar to green
                    elif int(per_right_leg_alternatinglunge_set3) == 100:
                        color_right_leg_alternatinglunge_set3 = (0, 255, 0)
                    else:
                        color_left_leg_alternatinglunge_set3 = (0, 0, 255)  # Keep color of left leg bar as red
                        color_right_leg_alternatinglunge_set3 = (0, 0, 255)

                    if rightleg_alternatinglunge_set3 <= 150 and leftleg_alternatinglunge_set3 <= 100:
                        if dir_alternating_right_lunge_set3 == 0:
                            count_alternating_right_lunge_set3 += 0.5
                            dir_alternating_right_lunge_set3 = 1
                            cooldown_timer_alternatinglunge_set3 = cooldown_duration_alternatinglunge_set3
                    else: 
                        if dir_alternating_right_lunge_set3 == 1:
                            count_alternating_right_lunge_set3 += 0.5
                            dir_alternating_right_lunge_set3 = 0
                            cooldown_timer_alternatinglunge_set3 = cooldown_duration_alternatinglunge_set3

                    if rightleg_alternatinglunge_set3 <= 100 and leftleg_alternatinglunge_set3 <= 150:
                        if dir_alternating_left_lunge_set3 == 0:
                            count_alternating_left_lunge_set3 += 0.5
                            dir_alternating_left_lunge_set3 = 1
                            cooldown_timer_alternatinglunge_set3 = cooldown_duration_alternatinglunge_set3
                    else:
                        if dir_alternating_left_lunge_set3 == 1:
                            count_alternating_left_lunge_set3 += 0.5
                            dir_alternating_left_lunge_set3 = 0
                            cooldown_timer_alternatinglunge_set3 = cooldown_duration_alternatinglunge_set3

  
        cvzone.putTextRect(img, 'Leg Lunge (alternate) SET 3', [345, 30], thickness=2, border=2, scale=2.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # Orientation
        cv2.rectangle(img, (890, 100), (1180, 160), (0, 0, 255), -2)
        cv2.putText(img, f"Orientation: {orientation}", (900, 140), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)

        # RIGHT LEG
        cv2.putText(img, f"R {int(per_right_leg_alternatinglunge_set3)}%", (24, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 480), (50, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_leg_alternatinglunge_set3)), (50, 680), color_right_leg_alternatinglunge_set3, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_left_leg_alternatinglunge_set3)}%", (962, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 480), (995, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_leg_alternatinglunge_set3)), (995, 680), color_left_leg_alternatinglunge_set3, -1)

    # Counter 
    cv2.rectangle(img, (20, 20), (140, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(count_alternating_right_lunge_set3)}/5", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (150, 20), (270, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(count_alternating_left_lunge_set3)}/5", (160, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    # Timer
    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
        display_info_alternatinglunge_set3 = False
        exercise_mode = "rest_alternatinglunge_set3"
        rest_alternatinglunge_start_time_set3 = time.time()

    # Repetition
    if count_alternating_left_lunge_set2 >= 5:  # Assuming 10 jumping jacks for demonstration
        cvzone.putTextRect(img, 'Exercise Complete', [390, 30], thickness=2, border=2, scale=2.5)
        display_info_alternatinglunge_set3 = False
        exercise_mode = "rest_alternatinglunge_set3"
        rest_alternatinglunge_start_time_set3 = time.time()
    return img

def rest_alternatinglunge_set3(img):
    global exercise_mode, rest_alternatinglunge_start_time_set3, start_time_bws
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_alternatinglunge_start_time_set3
    rest_remaining_time = max(0, 10 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "bws"
        start_time_bws = time.time()

    return img

def detect_bws(img):
    global count_body_weight_squat, dir_body_weight_squat, start_time_bws, repetition_time_bws, display_info_bws, leftbody_bws, rightbody_bws, per_left_body_bws, bar_left_body_bws, per_right_body_bws, bar_right_body_bws, color_right_body_bws, color_left_body_bws, rest_bws_start_time, exercise_mode

    img = cv2.resize(img, (1280, 720))

    elapsed_time = time.time() - start_time_bws
    remaining_time = max(0, repetition_time_bws - elapsed_time) #repetition_time_bws

    if display_info_bws:  # Check if to display counter, bar, and percentage
        img = detector_BodyWeightSquat.findPose(img, False)
        lmList_jumping_jacks = detector_BodyWeightSquat.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_jumping_jacks) != 0:
            
            leftbody_bws, orientation = detector_BodyWeightSquat.WeightSquat(img, 12, 24, 26, True)
            rightbody_bws, orientation2 = detector_BodyWeightSquat.WeightSquat(img, 11, 23, 25, True)
            
            if orientation == 'right' and orientation2 == 'right':
                per_right_body_bws = np.interp(rightbody_bws, (180, 280), (0, 100))
                bar_right_body_bws = np.interp(rightbody_bws, (180, 280), (400, 200))

                per_left_body_bws = np.interp(leftbody_bws, (180, 280), (0, 100))
                bar_left_body_bws = np.interp(leftbody_bws, (180, 280), (400, 200))

                if int(per_left_body_bws) == 100 and int(per_left_body_bws) == 100:
                    color_left_body_bws = (0, 255, 0)
                    color_right_body_bws = (0, 255, 0)  
                else:
                    color_left_body_bws = (0, 0, 255)  
                    color_right_body_bws = (0, 0, 255)  
            
                if leftbody_bws >= 280 and rightbody_bws >= 280:
                    if dir_body_weight_squat == 0:
                        count_body_weight_squat += 0.5
                        dir_body_weight_squat = 1
                elif leftbody_bws <= 180 and rightbody_bws <= 180:
                    if dir_body_weight_squat == 1:
                        count_body_weight_squat +=0.5
                        dir_body_weight_squat = 0
                    
            elif orientation =='left' and orientation2 == 'left':
                if leftbody_bws is not None and rightbody_bws is not None:

                    per_right_body_bws = np.interp(rightbody_bws, (90, 170), (100, 0))
                    bar_right_body_bws = np.interp(rightbody_bws, (90, 170), (200, 400))

                    per_left_body_bws = np.interp(leftbody_bws, (90, 170), (100, 0))
                    bar_left_body_bws = np.interp(leftbody_bws, (90, 170), (200, 400))

                    if int(per_left_body_bws) == 100 and int(per_left_body_bws) == 100:
                        color_left_body_bws = (0, 255, 0)
                        color_right_body_bws = (0, 255, 0)  
                    else:
                        color_left_body_bws = (0, 0, 255)  
                        color_right_body_bws = (0, 0, 255)  
 
                    if leftbody_bws <= 90 and rightbody_bws <= 90:
                        if dir_body_weight_squat == 0:
                            count_body_weight_squat += 0.5
                            dir_body_weight_squat = 1
                    elif leftbody_bws >= 170 and rightbody_bws >= 170:
                        if dir_body_weight_squat == 1:
                            count_body_weight_squat +=0.5
                            dir_body_weight_squat = 0

            elif orientation == 'front' and orientation2 == 'front':
                    
                    per_right_body_bws = np.interp(rightbody_bws, (180, 270), (100, 0))
                    bar_right_body_bws = np.interp(rightbody_bws, (180, 270), (200, 400))

                    per_left_body_bws = np.interp(leftbody_bws, (180, 270), (100, 0))
                    bar_left_body_bws = np.interp(leftbody_bws, (180, 270), (200, 400))

                    if int(per_left_body_bws) == 100 and int(per_left_body_bws) == 100:
                        color_left_body_bws = (0, 255, 0)
                        color_right_body_bws = (0, 255, 0)  
                    else:
                        color_left_body_bws = (0, 0, 255)  
                        color_right_body_bws = (0, 0, 255)  

                    if rightbody_bws <= 180 and leftbody_bws <= 180: 
                        if dir_body_weight_squat == 0:
                            count_body_weight_squat += 0.5
                            dir_body_weight_squat =1
                    elif rightbody_bws >= 270 and leftbody_bws >= 270:
                        if dir_body_weight_squat == 1:
                            count_body_weight_squat += 0.5
                            dir_body_weight_squat = 0
                    

        cvzone.putTextRect(img, 'Body Weight Squat Tracker', [220, 30], thickness=2, border=2, scale=2.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # RIGHT LEG
        cv2.putText(img, f"R {int(per_right_body_bws)}%", (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_body_bws)), (50, 400), color_right_body_bws, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_left_body_bws)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_body_bws)), (995, 400), color_left_body_bws, -1)

    cv2.rectangle(img, (20, 10), (140, 120), (255, 0, 0), -1)
    cv2.putText(img, f"{int(count_body_weight_squat)}/6", (30, 80), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
        display_info_bws = False
        exercise_mode = "rest_bws"
        rest_bws_start_time = time.time()

    if count_body_weight_squat >= 6:  
        cvzone.putTextRect(img, 'Exercise Complete', [390, 30], thickness=2, border=2, scale=2.5)
        display_info_bws = False
        exercise_mode = "rest_bws"
        rest_bws_start_time = time.time()
    return img

def rest_bws(img):
    global exercise_mode, rest_bws_start_time, start_time_bws_set2
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_bws_start_time
    rest_remaining_time = max(0, 10 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "bws_set2"
        start_time_bws_set2 = time.time()
    return img

def detect_bws_set2(img):
    global count_body_weight_squat_set2, dir_body_weight_squat_set2, start_time_bws_set2, repetition_time_bws_set2, display_info_bws_set2, leftbody_bws_set2, rightbody_bws_set2, per_left_body_bws_set2, bar_left_body_bws_set2, per_right_body_bws_set2, bar_right_body_bws_set2, color_right_body_bws_set2, color_left_body_bws_set2, rest_bws_start_time_set2, exercise_mode

    img = cv2.resize(img, (1280, 720))

    elapsed_time = time.time() - start_time_bws_set2
    remaining_time = max(0, repetition_time_bws_set2 - elapsed_time) #repetition_time_bws_set2

    if display_info_bws_set2:  # Check if to display counter, bar, and percentage
        img = detector_BodyWeightSquat.findPose(img, False)
        lmList_jumping_jacks = detector_BodyWeightSquat.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_jumping_jacks) != 0:
            
            leftbody_bws_set2, orientation = detector_BodyWeightSquat.WeightSquat(img, 12, 24, 26, True)
            rightbody_bws_set2, orientation2 = detector_BodyWeightSquat.WeightSquat(img, 11, 23, 25, True)
            
            if orientation == 'right' and orientation2 == 'right':
                per_right_body_bws_set2 = np.interp(rightbody_bws_set2, (180, 280), (0, 100))
                bar_right_body_bws_set2 = np.interp(rightbody_bws_set2, (180, 280), (400, 200))

                per_left_body_bws_set2 = np.interp(leftbody_bws_set2, (180, 280), (0, 100))
                bar_left_body_bws_set2 = np.interp(leftbody_bws_set2, (180, 280), (400, 200))

                if int(per_left_body_bws_set2) == 100 and int(per_left_body_bws_set2) == 100:
                    color_left_body_bws_set2 = (0, 255, 0)
                    color_right_body_bws_set2 = (0, 255, 0)  
                else:
                    color_left_body_bws_set2 = (0, 0, 255)  
                    color_right_body_bws_set2 = (0, 0, 255)  
            
                if leftbody_bws_set2 >= 280 and rightbody_bws_set2 >= 280:
                    if dir_body_weight_squat_set2 == 0:
                        count_body_weight_squat_set2 += 0.5
                        dir_body_weight_squat_set2 = 1
                elif leftbody_bws_set2 <= 180 and rightbody_bws_set2 <= 180:
                    if dir_body_weight_squat_set2 == 1:
                        count_body_weight_squat_set2 +=0.5
                        dir_body_weight_squat_set2 = 0
                    
            elif orientation =='left' and orientation2 == 'left':
                if leftbody_bws_set2 is not None and rightbody_bws_set2 is not None:

                    per_right_body_bws_set2 = np.interp(rightbody_bws_set2, (90, 170), (100, 0))
                    bar_right_body_bws_set2 = np.interp(rightbody_bws_set2, (90, 170), (200, 400))

                    per_left_body_bws_set2 = np.interp(leftbody_bws_set2, (90, 170), (100, 0))
                    bar_left_body_bws_set2 = np.interp(leftbody_bws_set2, (90, 170), (200, 400))

                    if int(per_left_body_bws_set2) == 100 and int(per_left_body_bws_set2) == 100:
                        color_left_body_bws_set2 = (0, 255, 0)
                        color_right_body_bws_set2 = (0, 255, 0)  
                    else:
                        color_left_body_bws_set2 = (0, 0, 255)  
                        color_right_body_bws_set2 = (0, 0, 255)  
 
                    if leftbody_bws_set2 <= 90 and rightbody_bws_set2 <= 90:
                        if dir_body_weight_squat_set2 == 0:
                            count_body_weight_squat_set2 += 0.5
                            dir_body_weight_squat_set2 = 1
                    elif leftbody_bws_set2 >= 170 and rightbody_bws_set2 >= 170:
                        if dir_body_weight_squat_set2 == 1:
                            count_body_weight_squat_set2 +=0.5
                            dir_body_weight_squat_set2 = 0

            elif orientation == 'front' and orientation2 == 'front':
                    
                    per_right_body_bws_set2 = np.interp(rightbody_bws_set2, (180, 270), (100, 0))
                    bar_right_body_bws_set2 = np.interp(rightbody_bws_set2, (180, 270), (200, 400))

                    per_left_body_bws_set2 = np.interp(leftbody_bws_set2, (180, 270), (100, 0))
                    bar_left_body_bws_set2 = np.interp(leftbody_bws_set2, (180, 270), (200, 400))

                    if int(per_left_body_bws_set2) == 100 and int(per_left_body_bws_set2) == 100:
                        color_left_body_bws_set2 = (0, 255, 0)
                        color_right_body_bws_set2 = (0, 255, 0)  
                    else:
                        color_left_body_bws_set2 = (0, 0, 255)  
                        color_right_body_bws_set2 = (0, 0, 255)  

                    if rightbody_bws_set2 <= 180 and leftbody_bws_set2 <= 180: 
                        if dir_body_weight_squat_set2 == 0:
                            count_body_weight_squat_set2 += 0.5
                            dir_body_weight_squat_set2 =1
                    elif rightbody_bws_set2 >= 270 and leftbody_bws_set2 >= 270:
                        if dir_body_weight_squat_set2 == 1:
                            count_body_weight_squat_set2 += 0.5
                            dir_body_weight_squat_set2 = 0
                    

        cvzone.putTextRect(img, 'Body Weight Squat Tracker SET 2', [220, 30], thickness=2, border=2, scale=2.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # RIGHT LEG
        cv2.putText(img, f"R {int(per_right_body_bws_set2)}%", (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_body_bws_set2)), (50, 400), color_right_body_bws_set2, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_left_body_bws_set2)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_body_bws_set2)), (995, 400), color_left_body_bws_set2, -1)

    cv2.rectangle(img, (20, 10), (140, 120), (255, 0, 0), -1)
    cv2.putText(img, f"{int(count_body_weight_squat_set2)}/6", (30, 80), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
        display_info_bws_set2 = False
        exercise_mode = "rest_bws_set2"
        rest_bws_start_time_set2 = time.time()

    if count_body_weight_squat_set2 >= 6:  
        cvzone.putTextRect(img, 'Exercise Complete', [390, 30], thickness=2, border=2, scale=2.5)
        display_info_bws_set2 = False
        exercise_mode = "rest_bws_set2"
        rest_bws_start_time_set2 = time.time()
    return img

def rest_bws_set2(img):
    global exercise_mode, rest_bws_start_time_set2, start_time_bws_set3
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_bws_start_time_set2
    rest_remaining_time = max(0, 10 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "bws_set3"
        start_time_bws_set3 = time.time()
    return img

def detect_bws_set3(img):
    global count_body_weight_squat_set3, dir_body_weight_squat_set3, start_time_bws_set3, repetition_time_bws_set3, display_info_bws_set3, leftbody_bws_set3, rightbody_bws_set3, per_left_body_bws_set3, bar_left_body_bws_set3, per_right_body_bws_set3, bar_right_body_bws_set3, color_right_body_bws_set3, color_left_body_bws_set3, rest_bws_start_time_set3, exercise_mode

    img = cv2.resize(img, (1280, 720))

    elapsed_time = time.time() - start_time_bws_set3
    remaining_time = max(0, repetition_time_bws_set3 - elapsed_time) #repetition_time_bws_set3

    if display_info_bws_set3:  # Check if to display counter, bar, and percentage
        img = detector_BodyWeightSquat.findPose(img, False)
        lmList_jumping_jacks = detector_BodyWeightSquat.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_jumping_jacks) != 0:
            
            leftbody_bws_set3, orientation = detector_BodyWeightSquat.WeightSquat(img, 12, 24, 26, True)
            rightbody_bws_set3, orientation2 = detector_BodyWeightSquat.WeightSquat(img, 11, 23, 25, True)
            
            if orientation == 'right' and orientation2 == 'right':
                per_right_body_bws_set3 = np.interp(rightbody_bws_set3, (180, 280), (0, 100))
                bar_right_body_bws_set3 = np.interp(rightbody_bws_set3, (180, 280), (400, 200))

                per_left_body_bws_set3 = np.interp(leftbody_bws_set3, (180, 280), (0, 100))
                bar_left_body_bws_set3 = np.interp(leftbody_bws_set3, (180, 280), (400, 200))

                if int(per_left_body_bws_set3) == 100 and int(per_left_body_bws_set3) == 100:
                    color_left_body_bws_set3 = (0, 255, 0)
                    color_right_body_bws_set3 = (0, 255, 0)  
                else:
                    color_left_body_bws_set3 = (0, 0, 255)  
                    color_right_body_bws_set3 = (0, 0, 255)  
            
                if leftbody_bws_set3 >= 280 and rightbody_bws_set3 >= 280:
                    if dir_body_weight_squat_set3 == 0:
                        count_body_weight_squat_set3 += 0.5
                        dir_body_weight_squat_set3 = 1
                elif leftbody_bws_set3 <= 180 and rightbody_bws_set3 <= 180:
                    if dir_body_weight_squat_set3 == 1:
                        count_body_weight_squat_set3 +=0.5
                        dir_body_weight_squat_set3 = 0
                    
            elif orientation =='left' and orientation2 == 'left':
                if leftbody_bws_set3 is not None and rightbody_bws_set3 is not None:

                    per_right_body_bws_set3 = np.interp(rightbody_bws_set3, (90, 170), (100, 0))
                    bar_right_body_bws_set3 = np.interp(rightbody_bws_set3, (90, 170), (200, 400))

                    per_left_body_bws_set3 = np.interp(leftbody_bws_set3, (90, 170), (100, 0))
                    bar_left_body_bws_set3 = np.interp(leftbody_bws_set3, (90, 170), (200, 400))

                    if int(per_left_body_bws_set3) == 100 and int(per_left_body_bws_set3) == 100:
                        color_left_body_bws_set3 = (0, 255, 0)
                        color_right_body_bws_set3 = (0, 255, 0)  
                    else:
                        color_left_body_bws_set3 = (0, 0, 255)  
                        color_right_body_bws_set3 = (0, 0, 255)  
 
                    if leftbody_bws_set3 <= 90 and rightbody_bws_set3 <= 90:
                        if dir_body_weight_squat_set3 == 0:
                            count_body_weight_squat_set3 += 0.5
                            dir_body_weight_squat_set3 = 1
                    elif leftbody_bws_set3 >= 170 and rightbody_bws_set3 >= 170:
                        if dir_body_weight_squat_set3 == 1:
                            count_body_weight_squat_set3 +=0.5
                            dir_body_weight_squat_set3 = 0

            elif orientation == 'front' and orientation2 == 'front':
                    
                    per_right_body_bws_set3 = np.interp(rightbody_bws_set3, (180, 270), (100, 0))
                    bar_right_body_bws_set3 = np.interp(rightbody_bws_set3, (180, 270), (200, 400))

                    per_left_body_bws_set3 = np.interp(leftbody_bws_set3, (180, 270), (100, 0))
                    bar_left_body_bws_set3 = np.interp(leftbody_bws_set3, (180, 270), (200, 400))

                    if int(per_left_body_bws_set3) == 100 and int(per_left_body_bws_set3) == 100:
                        color_left_body_bws_set3 = (0, 255, 0)
                        color_right_body_bws_set3 = (0, 255, 0)  
                    else:
                        color_left_body_bws_set3 = (0, 0, 255)  
                        color_right_body_bws_set3 = (0, 0, 255)  

                    if rightbody_bws_set3 <= 180 and leftbody_bws_set3 <= 180: 
                        if dir_body_weight_squat_set3 == 0:
                            count_body_weight_squat_set3 += 0.5
                            dir_body_weight_squat_set3 =1
                    elif rightbody_bws_set3 >= 270 and leftbody_bws_set3 >= 270:
                        if dir_body_weight_squat_set3 == 1:
                            count_body_weight_squat_set3 += 0.5
                            dir_body_weight_squat_set3 = 0
                    

        cvzone.putTextRect(img, 'Body Weight Squat Tracker SET 3', [220, 30], thickness=2, border=2, scale=2.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # RIGHT LEG
        cv2.putText(img, f"R {int(per_right_body_bws_set3)}%", (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_body_bws_set3)), (50, 400), color_right_body_bws_set3, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_left_body_bws_set3)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_body_bws_set3)), (995, 400), color_left_body_bws_set3, -1)

    cv2.rectangle(img, (20, 10), (140, 120), (255, 0, 0), -1)
    cv2.putText(img, f"{int(count_body_weight_squat_set3)}/6", (30, 80), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
        display_info_bws_set3 = False
        exercise_mode = "rest_bws_set3"
        rest_bws_start_time_set3 = time.time()

    if count_body_weight_squat_set2 >= 6:  
        cvzone.putTextRect(img, 'Exercise Complete', [390, 30], thickness=2, border=2, scale=2.5)
        display_info_bws_set3 = False
        exercise_mode = "rest_bws_set3"
        rest_bws_start_time_set3 = time.time()
    return img

def rest_bws_set3(img):
    global exercise_mode, rest_bws_start_time_set3, start_time_goblet_squat
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_bws_start_time_set3
    rest_remaining_time = max(0, 10 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "goblet_squat"
        start_time_goblet_squat = time.time()
    return img

def detect_gs(img):
    global count_goblet_squat, dir_goblet_squat, start_time_goblet_squat, repetition_time_goblet_squat, display_info_goblet_squat, cooldown_timer_goblet_squat, cooldown_duration_goblet_squat, color_left_leg_goblet_squat, color_right_leg_goblet_squat, rest_goblet_squat_start_time, orientation, orientation2, exercise_mode, per_right_leg, per_left_leg, bar_right_leg, bar_left_leg, color_left_leg, color_right_leg

    img = cv2.resize(img, (1280, 720))

    elapsed_time = time.time() - start_time_goblet_squat
    remaining_time = max(0, 20 - elapsed_time) #repetition_time_goblet_squat

    if display_info_goblet_squat:  # Check if to display counter, bar, and percentage
        img = detector_gobletsquat.findPose(img, False)
        lmList_jumping_jacks = detector_gobletsquat.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_jumping_jacks) != 0:

            # Right and Left keypoints
            rightleg, orientation = detector_gobletsquat.GobletSquat(img, 24, 26, 28, True)
            leftleg, orientation2 = detector_gobletsquat.GobletSquat(img, 23, 25, 27, True)

            if cooldown_timer_goblet_squat > 0:
                cooldown_timer_goblet_squat -= 1

            if orientation == 'right' and orientation2 == 'right':
                    
                    per_right_leg = np.interp(rightleg, (90, 170), (100, 0))
                    bar_right_leg = np.interp(rightleg, (90, 170), (480, 680))
                    per_left_leg = np.interp(leftleg, (90, 170), (100, 0))
                    bar_left_leg = np.interp(leftleg, (90, 170), (480, 680))

                    if int(per_left_leg) == 100 and int(per_right_leg) == 100:
                        color_left_leg = (0, 255, 0) 
                        color_right_leg = (0, 255, 0) 
                    else:
                        color_left_leg = (0, 0, 255)  
                        color_right_leg = (0, 0, 255)

                    if rightleg <= 90 and leftleg <= 90:
                        if dir_goblet_squat == 0:
                            count_goblet_squat += 0.5
                            dir_goblet_squat = 1
                            cooldown_timer_goblet_squat = cooldown_duration_goblet_squat
                    elif rightleg >= 170 and leftleg >= 170:
                        if dir_goblet_squat == 1:
                            count_goblet_squat += 0.5
                            dir_goblet_squat = 0
                            cooldown_timer_goblet_squat = cooldown_duration_goblet_squat

            elif orientation =='left' and orientation2 == 'left':
                if leftleg is not None and rightleg is not None:
                    per_right_leg = np.interp(rightleg, (190, 270), (0, 100))
                    bar_right_leg = np.interp(rightleg, (190, 270), (680, 480))
                    per_left_leg = np.interp(leftleg, (190, 270), (0, 100))
                    bar_left_leg = np.interp(leftleg, (190, 270), (680, 480))

                    if int(per_left_leg) == 100 and int(per_right_leg) == 100:
                        color_left_leg = (0, 255, 0) 
                        color_right_leg = (0, 255, 0) 
                    else:
                        color_left_leg = (0, 0, 255)  
                        color_right_leg = (0, 0, 255)
              
                    if rightleg >= 270 and leftleg >= 270:
                        if dir_goblet_squat == 0:
                            count_goblet_squat += 0.5
                            dir_goblet_squat = 1
                            cooldown_timer_goblet_squat = cooldown_duration_goblet_squat
                    elif rightleg <= 190 and leftleg <= 190:
                        if dir_goblet_squat == 1:
                            count_goblet_squat += 0.5
                            dir_goblet_squat = 0
                            cooldown_timer_goblet_squat = cooldown_duration_goblet_squat



            elif orientation == 'front' and orientation2 == 'front':

                    per_right_leg = np.interp(rightleg, (150, 240), (100, 0))
                    bar_right_leg = np.interp(rightleg, (150, 240), (480, 680))
                    per_left_leg = np.interp(leftleg, (150, 240), (100, 0))
                    bar_left_leg = np.interp(leftleg, (150, 240), (480, 680))
                    
                    
                    if int(per_left_leg) == 100 and int(per_right_leg) == 100:
                        color_left_leg = (0, 255, 0) 
                        color_right_leg = (0, 255, 0) 
                    else:
                        color_left_leg = (0, 0, 255)  
                        color_right_leg = (0, 0, 255)  # Keep color of right leg bar as red

                    if rightleg <= 160 and leftleg <= 160:
                        if dir_goblet_squat == 0:
                            count_goblet_squat += 0.5
                            dir_goblet_squat = 1
                            cooldown_timer_goblet_squat = cooldown_duration_goblet_squat
                    elif rightleg >= 240 and leftleg >= 240: 
                        if dir_goblet_squat == 1:
                            count_goblet_squat += 0.5
                            dir_goblet_squat = 0
                            cooldown_timer_goblet_squat = cooldown_duration_goblet_squat

        cvzone.putTextRect(img, 'Goblet Squat Tracker', [450, 30], thickness=2, border=2, scale=2)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        
        # Orientation
        cv2.rectangle(img, (890, 100), (1180, 160), (0, 0, 255), -2)
        cv2.putText(img, f"Orientation: {orientation}", (900, 140), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)

        # RIGHT LEG
        cv2.putText(img, f"R {int(per_right_leg)}%", (24, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 480), (50, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_leg)), (50, 680), color_right_leg, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_left_leg)}%", (962, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 480), (995, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_leg)), (995, 680), color_left_leg, -1)

    # Counter 
    cv2.rectangle(img, (20, 20), (200, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(count_goblet_squat)}/5", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (210, 20), (390, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(count_goblet_squat)}/5", (220, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)



    #Timer
    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
        display_info_goblet_squat = False
        exercise_mode = "rest_gs"
        rest_goblet_squat_start_time = time.time()

    # Repetition
    if count_goblet_squat >= 6:  # Assuming 10 jumping jacks for demonstration
        cvzone.putTextRect(img, 'Exercise Complete', [390, 30], thickness=2, border=2, scale=2.5)
        display_info_goblet_squat = False
        exercise_mode = "rest_gs"
        rest_goblet_squat_start_time = time.time()

    return img

def rest_gs(img):
    global exercise_mode, rest_goblet_squat_start_time, start_time_goblet_squat_set2
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_goblet_squat_start_time
    rest_remaining_time = max(0, 10 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "goblet_squat_set2"
        start_time_goblet_squat_set2 = time.time()
    return img

def detect_gs_set2(img):
    global count_goblet_squat_set2, dir_goblet_squat_set2, start_time_goblet_squat_set2, repetition_time_goblet_squat_set2, display_info_goblet_squat_set2, cooldown_timer_goblet_squat_set2, cooldown_duration_goblet_squat_set2, color_left_leg_goblet_squat_set2, color_right_leg_goblet_squat_set2, rest_goblet_squat_start_time_set2, orientation, orientation2, exercise_mode, per_right_leg, per_left_leg, bar_right_leg, bar_left_leg, color_left_leg, color_right_leg

    img = cv2.resize(img, (1280, 720))

    elapsed_time = time.time() - start_time_goblet_squat_set2
    remaining_time = max(0, 20 - elapsed_time) #repetition_time_goblet_squat_set2

    if display_info_goblet_squat_set2:  # Check if to display counter, bar, and percentage
        img = detector_gobletsquat.findPose(img, False)
        lmList_jumping_jacks = detector_gobletsquat.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_jumping_jacks) != 0:

            # Right and Left keypoints
            rightleg, orientation = detector_gobletsquat.GobletSquat(img, 24, 26, 28, True)
            leftleg, orientation2 = detector_gobletsquat.GobletSquat(img, 23, 25, 27, True)

            if cooldown_timer_goblet_squat_set2 > 0:
                cooldown_timer_goblet_squat_set2 -= 1

            if orientation == 'right' and orientation2 == 'right':
                    
                    per_right_leg = np.interp(rightleg, (90, 170), (100, 0))
                    bar_right_leg = np.interp(rightleg, (90, 170), (480, 680))
                    per_left_leg = np.interp(leftleg, (90, 170), (100, 0))
                    bar_left_leg = np.interp(leftleg, (90, 170), (480, 680))

                    if int(per_left_leg) == 100 and int(per_right_leg) == 100:
                        color_left_leg = (0, 255, 0) 
                        color_right_leg = (0, 255, 0) 
                    else:
                        color_left_leg = (0, 0, 255)  
                        color_right_leg = (0, 0, 255)

                    if rightleg <= 90 and leftleg <= 90:
                        if dir_goblet_squat_set2 == 0:
                            count_goblet_squat_set2 += 0.5
                            dir_goblet_squat_set2 = 1
                            cooldown_timer_goblet_squat_set2 = cooldown_duration_goblet_squat_set2
                    elif rightleg >= 170 and leftleg >= 170:
                        if dir_goblet_squat_set2 == 1:
                            count_goblet_squat_set2 += 0.5
                            dir_goblet_squat_set2 = 0
                            cooldown_timer_goblet_squat_set2 = cooldown_duration_goblet_squat_set2

            elif orientation =='left' and orientation2 == 'left':
                if leftleg is not None and rightleg is not None:
                    per_right_leg = np.interp(rightleg, (190, 270), (0, 100))
                    bar_right_leg = np.interp(rightleg, (190, 270), (680, 480))
                    per_left_leg = np.interp(leftleg, (190, 270), (0, 100))
                    bar_left_leg = np.interp(leftleg, (190, 270), (680, 480))

                    if int(per_left_leg) == 100 and int(per_right_leg) == 100:
                        color_left_leg = (0, 255, 0) 
                        color_right_leg = (0, 255, 0) 
                    else:
                        color_left_leg = (0, 0, 255)  
                        color_right_leg = (0, 0, 255)
              
                    if rightleg >= 270 and leftleg >= 270:
                        if dir_goblet_squat_set2 == 0:
                            count_goblet_squat_set2 += 0.5
                            dir_goblet_squat_set2 = 1
                            cooldown_timer_goblet_squat_set2 = cooldown_duration_goblet_squat_set2
                    elif rightleg <= 190 and leftleg <= 190:
                        if dir_goblet_squat_set2 == 1:
                            count_goblet_squat_set2 += 0.5
                            dir_goblet_squat_set2 = 0
                            cooldown_timer_goblet_squat_set2 = cooldown_duration_goblet_squat_set2



            elif orientation == 'front' and orientation2 == 'front':

                    per_right_leg = np.interp(rightleg, (150, 240), (100, 0))
                    bar_right_leg = np.interp(rightleg, (150, 240), (480, 680))
                    per_left_leg = np.interp(leftleg, (150, 240), (100, 0))
                    bar_left_leg = np.interp(leftleg, (150, 240), (480, 680))
                    
                    
                    if int(per_left_leg) == 100 and int(per_right_leg) == 100:
                        color_left_leg = (0, 255, 0) 
                        color_right_leg = (0, 255, 0) 
                    else:
                        color_left_leg = (0, 0, 255)  
                        color_right_leg = (0, 0, 255)  # Keep color of right leg bar as red

                    if rightleg <= 160 and leftleg <= 160:
                        if dir_goblet_squat_set2 == 0:
                            count_goblet_squat_set2 += 0.5
                            dir_goblet_squat_set2 = 1
                            cooldown_timer_goblet_squat_set2 = cooldown_duration_goblet_squat_set2
                    elif rightleg >= 240 and leftleg >= 240: 
                        if dir_goblet_squat_set2 == 1:
                            count_goblet_squat_set2 += 0.5
                            dir_goblet_squat_set2 = 0
                            cooldown_timer_goblet_squat_set2 = cooldown_duration_goblet_squat_set2

        cvzone.putTextRect(img, 'Goblet Squat Tracker SET 2', [450, 30], thickness=2, border=2, scale=2)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        
        # Orientation
        cv2.rectangle(img, (890, 100), (1180, 160), (0, 0, 255), -2)
        cv2.putText(img, f"Orientation: {orientation}", (900, 140), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)

        # RIGHT LEG
        cv2.putText(img, f"R {int(per_right_leg)}%", (24, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 480), (50, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_leg)), (50, 680), color_right_leg, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_left_leg)}%", (962, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 480), (995, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_leg)), (995, 680), color_left_leg, -1)

    # Counter 
    cv2.rectangle(img, (20, 20), (200, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(count_goblet_squat_set2)}/5", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (210, 20), (390, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(count_goblet_squat_set2)}/5", (220, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)



    #Timer
    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
        display_info_goblet_squat_set2 = False
        exercise_mode = "rest_gs_set2"
        rest_goblet_squat_start_time_set2 = time.time()

    # Repetition
    if count_goblet_squat_set2 >= 6:  # Assuming 10 jumping jacks for demonstration
        cvzone.putTextRect(img, 'Exercise Complete', [390, 30], thickness=2, border=2, scale=2.5)
        display_info_goblet_squat_set2 = False
        exercise_mode = "rest_gs_set2"
        rest_goblet_squat_start_time_set2 = time.time()

    return img

def rest_gs_set2(img):
    global exercise_mode, rest_goblet_squat_start_time_set2, start_time_goblet_squat_set3
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_goblet_squat_start_time_set2
    rest_remaining_time = max(0, 10 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "goblet_squat_set3"
        start_time_goblet_squat_set3 = time.time()
    return img

def detect_gs_set3(img):
    global count_goblet_squat_set3, dir_goblet_squat_set3, start_time_goblet_squat_set3, repetition_time_goblet_squat_set3, display_info_goblet_squat_set3, cooldown_timer_goblet_squat_set3, cooldown_duration_goblet_squat_set3, color_left_leg_goblet_squat_set3, color_right_leg_goblet_squat_set3, rest_goblet_squat_start_time_set3, orientation, orientation2, exercise_mode, per_right_leg, per_left_leg, bar_right_leg, bar_left_leg, color_left_leg, color_right_leg

    img = cv2.resize(img, (1280, 720))

    elapsed_time = time.time() - start_time_goblet_squat_set3
    remaining_time = max(0, 20 - elapsed_time) #repetition_time_goblet_squat_set3

    if display_info_goblet_squat_set3:  # Check if to display counter, bar, and percentage
        img = detector_gobletsquat.findPose(img, False)
        lmList_jumping_jacks = detector_gobletsquat.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_jumping_jacks) != 0:

            # Right and Left keypoints
            rightleg, orientation = detector_gobletsquat.GobletSquat(img, 24, 26, 28, True)
            leftleg, orientation2 = detector_gobletsquat.GobletSquat(img, 23, 25, 27, True)

            if cooldown_timer_goblet_squat_set3 > 0:
                cooldown_timer_goblet_squat_set3 -= 1

            if orientation == 'right' and orientation2 == 'right':
                    
                    per_right_leg = np.interp(rightleg, (90, 170), (100, 0))
                    bar_right_leg = np.interp(rightleg, (90, 170), (480, 680))
                    per_left_leg = np.interp(leftleg, (90, 170), (100, 0))
                    bar_left_leg = np.interp(leftleg, (90, 170), (480, 680))

                    if int(per_left_leg) == 100 and int(per_right_leg) == 100:
                        color_left_leg = (0, 255, 0) 
                        color_right_leg = (0, 255, 0) 
                    else:
                        color_left_leg = (0, 0, 255)  
                        color_right_leg = (0, 0, 255)

                    if rightleg <= 90 and leftleg <= 90:
                        if dir_goblet_squat_set3 == 0:
                            count_goblet_squat_set3 += 0.5
                            dir_goblet_squat_set3 = 1
                            cooldown_timer_goblet_squat_set3 = cooldown_duration_goblet_squat_set3
                    elif rightleg >= 170 and leftleg >= 170:
                        if dir_goblet_squat_set3 == 1:
                            count_goblet_squat_set3 += 0.5
                            dir_goblet_squat_set3 = 0
                            cooldown_timer_goblet_squat_set3 = cooldown_duration_goblet_squat_set3

            elif orientation =='left' and orientation2 == 'left':
                if leftleg is not None and rightleg is not None:
                    per_right_leg = np.interp(rightleg, (190, 270), (0, 100))
                    bar_right_leg = np.interp(rightleg, (190, 270), (680, 480))
                    per_left_leg = np.interp(leftleg, (190, 270), (0, 100))
                    bar_left_leg = np.interp(leftleg, (190, 270), (680, 480))

                    if int(per_left_leg) == 100 and int(per_right_leg) == 100:
                        color_left_leg = (0, 255, 0) 
                        color_right_leg = (0, 255, 0) 
                    else:
                        color_left_leg = (0, 0, 255)  
                        color_right_leg = (0, 0, 255)
              
                    if rightleg >= 270 and leftleg >= 270:
                        if dir_goblet_squat_set3 == 0:
                            count_goblet_squat_set3 += 0.5
                            dir_goblet_squat_set3 = 1
                            cooldown_timer_goblet_squat_set3 = cooldown_duration_goblet_squat_set3
                    elif rightleg <= 190 and leftleg <= 190:
                        if dir_goblet_squat_set3 == 1:
                            count_goblet_squat_set3 += 0.5
                            dir_goblet_squat_set3 = 0
                            cooldown_timer_goblet_squat_set3 = cooldown_duration_goblet_squat_set3



            elif orientation == 'front' and orientation2 == 'front':

                    per_right_leg = np.interp(rightleg, (150, 240), (100, 0))
                    bar_right_leg = np.interp(rightleg, (150, 240), (480, 680))
                    per_left_leg = np.interp(leftleg, (150, 240), (100, 0))
                    bar_left_leg = np.interp(leftleg, (150, 240), (480, 680))
                    
                    
                    if int(per_left_leg) == 100 and int(per_right_leg) == 100:
                        color_left_leg = (0, 255, 0) 
                        color_right_leg = (0, 255, 0) 
                    else:
                        color_left_leg = (0, 0, 255)  
                        color_right_leg = (0, 0, 255)  # Keep color of right leg bar as red

                    if rightleg <= 160 and leftleg <= 160:
                        if dir_goblet_squat_set3 == 0:
                            count_goblet_squat_set3 += 0.5
                            dir_goblet_squat_set3 = 1
                            cooldown_timer_goblet_squat_set3 = cooldown_duration_goblet_squat_set3
                    elif rightleg >= 240 and leftleg >= 240: 
                        if dir_goblet_squat_set3 == 1:
                            count_goblet_squat_set3 += 0.5
                            dir_goblet_squat_set3 = 0
                            cooldown_timer_goblet_squat_set3 = cooldown_duration_goblet_squat_set3

        cvzone.putTextRect(img, 'Goblet Squat Tracker SET 3', [450, 30], thickness=2, border=2, scale=2)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        
        # Orientation
        cv2.rectangle(img, (890, 100), (1180, 160), (0, 0, 255), -2)
        cv2.putText(img, f"Orientation: {orientation}", (900, 140), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)

        # RIGHT LEG
        cv2.putText(img, f"R {int(per_right_leg)}%", (24, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 480), (50, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_leg)), (50, 680), color_right_leg, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_left_leg)}%", (962, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 480), (995, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_leg)), (995, 680), color_left_leg, -1)

    # Counter 
    cv2.rectangle(img, (20, 20), (200, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(count_goblet_squat_set3)}/5", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (210, 20), (390, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(count_goblet_squat_set3)}/5", (220, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)



    #Timer
    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
        display_info_goblet_squat_set3 = False
        exercise_mode = "rest_gs_set3"
        rest_goblet_squat_start_time_set3 = time.time()

    # Repetition
    if count_goblet_squat_set3 >= 6:  # Assuming 10 jumping jacks for demonstration
        cvzone.putTextRect(img, 'Exercise Complete', [390, 30], thickness=2, border=2, scale=2.5)
        display_info_goblet_squat_set3 = False
        exercise_mode = "rest_gs_set3"
        rest_goblet_squat_start_time_set3 = time.time()
    return img

def rest_gs_set3(img):
    global exercise_mode, rest_goblet_squat_start_time_set3, start_time_hkt
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_goblet_squat_start_time_set3
    rest_remaining_time = max(0, 10 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "highkneetap"
        start_time_hkt = time.time()
    return img

def detect_hkt(img):
    global count_high_knee_tap_left, count_high_knee_tap_right, dir_high_knee_tap_left, dir_high_knee_tap_right, start_time_hkt, repetition_time_hkt, display_info_hkt, leftbody_hkt, rightbody_hkt, per_left_leg_hkt, per_right_leg_hkt, bar_left_leg_hkt, bar_right_leg_hkt, cooldown_duration_hkt, cooldown_timer_hkt, color_left_leg_hkt, color_right_leg_hkt, exercise_mode, orientation, orientation2, rest_hkt_start_time

    img = cv2.resize(img, (1280, 720))

    elapsed_time = time.time() - start_time_hkt
    remaining_time = max(0, 20 - elapsed_time) #repetition_time_hkt

    if display_info_hkt:  # Check if to display counter, bar, and percentage
        img = detector_HighKneeTap.findPose(img, False)
        lmList_jumping_jacks = detector_HighKneeTap.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_jumping_jacks) != 0:

            # Right and Left keypoints
            rightleg_hkt, orientation = detector_HighKneeTap.HighKneeTap(img, 24, 26, 28, True)
            leftleg_hkt, orientation2 = detector_HighKneeTap.HighKneeTap(img, 23, 25, 27, True)

            if cooldown_timer_hkt > 0:
                cooldown_timer_hkt -= 1

            if orientation == 'right' and orientation2 == 'right':
                    per_right_leg_hkt = np.interp(rightleg_hkt, (70, 170), (100, 0))
                    bar_right_leg_hkt = np.interp(rightleg_hkt, (70, 170), (480, 680))
                    per_left_leg_hkt = np.interp(leftleg_hkt, (70, 170), (100, 0))
                    bar_left_leg_hkt = np.interp(leftleg_hkt, (70, 170), (480, 680))

                    if int(per_left_leg_hkt) == 100 :
                        color_left_leg_hkt = (0, 255, 0) 
                    elif int(per_right_leg_hkt) == 100:
                        color_right_leg_hkt = (0, 255, 0)
                    else:
                        color_left_leg_hkt = (0, 0, 255)  
                        color_right_leg_hkt = (0, 0, 255)
                    
                    if 50 <= rightleg_hkt <= 60:
                        if dir_high_knee_tap_right == 0:
                            count_high_knee_tap_right += 1
                            dir_high_knee_tap_right = 1
                            cooldown_timer_hkt = cooldown_duration_hkt
                            print("Up Right: ",count_high_knee_tap_right)
                    elif rightleg_hkt >= 155: 
                        if dir_high_knee_tap_right == 1:
                            dir_high_knee_tap_right = 0

                    if 50 <= leftleg_hkt <= 60:
                        if dir_high_knee_tap_left == 0:
                            count_high_knee_tap_left += 1
                            dir_high_knee_tap_left = 1
                            cooldown_timer_hkt = cooldown_duration_hkt
                            print("Up Left: ",count_high_knee_tap_left)

                    elif leftleg_hkt >= 155:
                        if dir_high_knee_tap_left == 1:
                            dir_high_knee_tap_left = 0

            elif orientation =='left' and orientation2 == 'left':
                    per_right_leg_hkt = np.interp(rightleg_hkt, (210, 300), (0, 100))
                    bar_right_leg_hkt = np.interp(rightleg_hkt, (210, 300), (680, 480))
                    per_left_leg_hkt = np.interp(leftleg_hkt, (210, 300), (0, 100))
                    bar_left_leg_hkt = np.interp(leftleg_hkt, (210, 300), (680, 480))

                    if int(per_left_leg_hkt) == 100 :
                        color_left_leg_hkt = (0, 255, 0) 
                    elif int(per_right_leg_hkt) == 100:
                        color_right_leg_hkt = (0, 255, 0)
                    else:
                        color_left_leg_hkt = (0, 0, 255)  
                        color_right_leg_hkt = (0, 0, 255)

                    if rightleg_hkt >= 295:
                        if dir_high_knee_tap_right == 0:
                            count_high_knee_tap_right += 1
                            dir_high_knee_tap_right = 1
                            cooldown_timer_hkt = cooldown_duration_hkt
                    elif rightleg_hkt <= 210: 
                        if dir_high_knee_tap_right == 1:
                            dir_high_knee_tap_right = 0

                    if leftleg_hkt >= 300:
                        if dir_high_knee_tap_left == 0:
                            count_high_knee_tap_left += 1
                            dir_high_knee_tap_left = 1
                            cooldown_timer_hkt = cooldown_duration_hkt
                    elif leftleg_hkt <= 210:
                        if dir_high_knee_tap_left == 1:
                            dir_high_knee_tap_left = 0

            elif orientation == 'front' and orientation2 == 'front':
                    per_right_leg_hkt = np.interp(rightleg_hkt, (150, 240), (100, 0))
                    bar_right_leg_hkt = np.interp(rightleg_hkt, (150, 240), (480, 680))
                    per_left_leg_hkt = np.interp(leftleg_hkt, (150, 240), (100, 0))
                    bar_left_leg_hkt = np.interp(leftleg_hkt, (150, 240), (480, 680))
                    
                    if int(per_left_leg_hkt) == 100 :
                        color_left_leg_hkt = (0, 255, 0) 
                    elif int(per_right_leg_hkt) == 100:
                        color_right_leg_hkt = (0, 255, 0)
                    else:
                        color_left_leg_hkt = (0, 0, 255)  
                        color_right_leg_hkt = (0, 0, 255)

                    if rightleg_hkt <= 150:
                        if dir_high_knee_tap_right == 0:
                            count_high_knee_tap_right += 1
                            dir_high_knee_tap_right = 1
                            cooldown_timer_hkt = cooldown_duration_hkt
                    elif rightleg_hkt >= 240: 
                        if dir_high_knee_tap_right == 1:
                            dir_high_knee_tap_right = 0

                    if leftleg_hkt <= 150:
                        if dir_high_knee_tap_left == 0:
                            count_high_knee_tap_left += 1
                            dir_high_knee_tap_left = 1
                            cooldown_timer_hkt = cooldown_duration_hkt
                    elif leftleg_hkt >= 240:
                        if dir_high_knee_tap_left == 1:
                            dir_high_knee_tap_left = 0


        

        cvzone.putTextRect(img, 'High Knee Tap Tracker', [450, 30], thickness=2, border=2, scale=2)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # Orientation
        cv2.rectangle(img, (890, 100), (1180, 160), (0, 0, 255), -2)
        cv2.putText(img, f"Orientation: {orientation}", (900, 140), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)

        # RIGHT LEG
        cv2.putText(img, f"R {int(per_right_leg_hkt)}%", (24, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 480), (50, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_leg_hkt)), (50, 680), color_right_leg_hkt, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_left_leg_hkt)}%", (962, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 480), (995, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_leg_hkt)), (995, 680), color_left_leg_hkt, -1)
    
    # Counter 
    cv2.rectangle(img, (20, 20), (200, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(count_high_knee_tap_right)}/5", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (210, 20), (390, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(count_high_knee_tap_left)}/5", (220, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    #Timer
    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
        display_info_hkt = False
        exercise_mode = "rest_hkt"
        rest_hkt_start_time = time.time()

    # Repetition
    if count_high_knee_tap_right >= 5 and count_high_knee_tap_left >= 5:  # Changeable
        cvzone.putTextRect(img, 'Exercise Complete', [390, 30], thickness=2, border=2, scale=2.5)
        display_info_hkt = False
        exercise_mode = "rest_hkt"
        rest_hkt_start_time = time.time()
    return img

def rest_hkt(img):
    global exercise_mode, rest_hkt_start_time, start_time_hkt_set2
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_hkt_start_time
    rest_remaining_time = max(0, 10 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "highkneetap_set2"
        start_time_hkt_set2 = time.time()
    return img

def detect_hkt_set2(img):
    global count_high_knee_tap_left_set2, count_high_knee_tap_right_set2, dir_high_knee_tap_left_set2, dir_high_knee_tap_right_set2, start_time_hkt_set2, repetition_time_hkt_set2, display_info_hkt_set2, leftbody_hkt_set2, rightbody_hkt_set2, per_left_leg_hkt_set2, per_right_leg_hkt_set2, bar_left_leg_hkt_set2, bar_right_leg_hkt_set2, cooldown_duration_hkt_set2, cooldown_timer_hkt_set2, color_left_leg_hkt_set2, color_right_leg_hkt_set2, exercise_mode, orientation, orientation2, rest_hkt_start_time_set2

    img = cv2.resize(img, (1280, 720))

    elapsed_time = time.time() - start_time_hkt_set2
    remaining_time = max(0, 20 - elapsed_time) #repetition_time_hkt_set2

    if display_info_hkt_set2:  # Check if to display counter, bar, and percentage
        img = detector_HighKneeTap.findPose(img, False)
        lmList_jumping_jacks = detector_HighKneeTap.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_jumping_jacks) != 0:

            # Right and Left keypoints
            rightleg_hkt_set2, orientation = detector_HighKneeTap.HighKneeTap(img, 24, 26, 28, True)
            leftleg_hkt_set2, orientation2 = detector_HighKneeTap.HighKneeTap(img, 23, 25, 27, True)

            if cooldown_timer_hkt_set2 > 0:
                cooldown_timer_hkt_set2 -= 1

            if orientation == 'right' and orientation2 == 'right':
                    per_right_leg_hkt_set2 = np.interp(rightleg_hkt_set2, (70, 170), (100, 0))
                    bar_right_leg_hkt_set2 = np.interp(rightleg_hkt_set2, (70, 170), (480, 680))
                    per_left_leg_hkt_set2 = np.interp(leftleg_hkt_set2, (70, 170), (100, 0))
                    bar_left_leg_hkt_set2 = np.interp(leftleg_hkt_set2, (70, 170), (480, 680))

                    if int(per_left_leg_hkt_set2) == 100 :
                        color_left_leg_hkt_set2 = (0, 255, 0) 
                    elif int(per_right_leg_hkt_set2) == 100:
                        color_right_leg_hkt_set2 = (0, 255, 0)
                    else:
                        color_left_leg_hkt_set2 = (0, 0, 255)  
                        color_right_leg_hkt_set2 = (0, 0, 255)
                    
                    if 50 <= rightleg_hkt_set2 <= 60:
                        if dir_high_knee_tap_right_set2 == 0:
                            count_high_knee_tap_right_set2 += 1
                            dir_high_knee_tap_right_set2 = 1
                            cooldown_timer_hkt_set2 = cooldown_duration_hkt_set2
                            #print("Up Right: ",count_high_knee_tap_right)
                    elif rightleg_hkt_set2 >= 155: 
                        if dir_high_knee_tap_right_set2 == 1:
                            dir_high_knee_tap_right_set2 = 0

                    if 50 <= leftleg_hkt_set2 <= 60:
                        if dir_high_knee_tap_left_set2 == 0:
                            count_high_knee_tap_left_set2 += 1
                            dir_high_knee_tap_left_set2 = 1
                            cooldown_timer_hkt_set2 = cooldown_duration_hkt_set2
                            #print("Up Left: ",count_high_knee_tap_left)

                    elif leftleg_hkt_set2 >= 155:
                        if dir_high_knee_tap_left_set2 == 1:
                            dir_high_knee_tap_left_set2 = 0

            elif orientation =='left' and orientation2 == 'left':
                    per_right_leg_hkt_set2 = np.interp(rightleg_hkt_set2, (210, 300), (0, 100))
                    bar_right_leg_hkt_set2 = np.interp(rightleg_hkt_set2, (210, 300), (680, 480))
                    per_left_leg_hkt_set2 = np.interp(leftleg_hkt_set2, (210, 300), (0, 100))
                    bar_left_leg_hkt_set2 = np.interp(leftleg_hkt_set2, (210, 300), (680, 480))

                    if int(per_left_leg_hkt_set2) == 100 :
                        color_left_leg_hkt_set2 = (0, 255, 0) 
                    elif int(per_right_leg_hkt_set2) == 100:
                        color_right_leg_hkt_set2 = (0, 255, 0)
                    else:
                        color_left_leg_hkt_set2 = (0, 0, 255)  
                        color_right_leg_hkt_set2 = (0, 0, 255)

                    if rightleg_hkt_set2 >= 295:
                        if dir_high_knee_tap_right_set2 == 0:
                            count_high_knee_tap_right_set2 += 1
                            dir_high_knee_tap_right_set2 = 1
                            cooldown_timer_hkt_set2 = cooldown_duration_hkt_set2
                    elif rightleg_hkt_set2 <= 210: 
                        if dir_high_knee_tap_right_set2 == 1:
                            dir_high_knee_tap_right_set2 = 0

                    if leftleg_hkt_set2 >= 300:
                        if dir_high_knee_tap_left_set2 == 0:
                            count_high_knee_tap_left_set2 += 1
                            dir_high_knee_tap_left_set2 = 1
                            cooldown_timer_hkt_set2 = cooldown_duration_hkt_set2
                    elif leftleg_hkt_set2 <= 210:
                        if dir_high_knee_tap_left_set2 == 1:
                            dir_high_knee_tap_left_set2 = 0

            elif orientation == 'front' and orientation2 == 'front':
                    per_right_leg_hkt_set2 = np.interp(rightleg_hkt_set2, (150, 240), (100, 0))
                    bar_right_leg_hkt_set2 = np.interp(rightleg_hkt_set2, (150, 240), (480, 680))
                    per_left_leg_hkt_set2 = np.interp(leftleg_hkt_set2, (150, 240), (100, 0))
                    bar_left_leg_hkt_set2 = np.interp(leftleg_hkt_set2, (150, 240), (480, 680))
                    
                    if int(per_left_leg_hkt_set2) == 100 :
                        color_left_leg_hkt_set2 = (0, 255, 0) 
                    elif int(per_right_leg_hkt_set2) == 100:
                        color_right_leg_hkt_set2 = (0, 255, 0)
                    else:
                        color_left_leg_hkt_set2 = (0, 0, 255)  
                        color_right_leg_hkt_set2 = (0, 0, 255)

                    if rightleg_hkt_set2 <= 150:
                        if dir_high_knee_tap_right_set2 == 0:
                            count_high_knee_tap_right_set2 += 1
                            dir_high_knee_tap_right_set2 = 1
                            cooldown_timer_hkt_set2 = cooldown_duration_hkt_set2
                    elif rightleg_hkt_set2 >= 240: 
                        if dir_high_knee_tap_right_set2 == 1:
                            dir_high_knee_tap_right_set2 = 0

                    if leftleg_hkt_set2 <= 150:
                        if dir_high_knee_tap_left_set2 == 0:
                            count_high_knee_tap_left_set2 += 1
                            dir_high_knee_tap_left_set2 = 1
                            cooldown_timer_hkt_set2 = cooldown_duration_hkt_set2
                    elif leftleg_hkt_set2 >= 240:
                        if dir_high_knee_tap_left_set2 == 1:
                            dir_high_knee_tap_left_set2 = 0


        

        cvzone.putTextRect(img, 'High Knee Tap SET 2', [450, 30], thickness=2, border=2, scale=2)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # Orientation
        cv2.rectangle(img, (890, 100), (1180, 160), (0, 0, 255), -2)
        cv2.putText(img, f"Orientation: {orientation}", (900, 140), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)

        # RIGHT LEG
        cv2.putText(img, f"R {int(per_right_leg_hkt_set2)}%", (24, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 480), (50, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_leg_hkt_set2)), (50, 680), color_right_leg_hkt_set2, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_left_leg_hkt_set2)}%", (962, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 480), (995, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_leg_hkt_set2)), (995, 680), color_left_leg_hkt_set2, -1)
    
    # Counter 
    cv2.rectangle(img, (20, 20), (200, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(count_high_knee_tap_right_set2)}/5", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (210, 20), (390, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(count_high_knee_tap_left_set2)}/5", (220, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    #Timer
    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
        display_info_hkt_set2 = False
        exercise_mode = "rest_hkt_set2"
        rest_hkt_start_time_set2 = time.time()

    # Repetition
    if count_high_knee_tap_right_set2 >= 5 and count_high_knee_tap_left_set2 >= 5:  # Changeable
        cvzone.putTextRect(img, 'Exercise Complete', [390, 30], thickness=2, border=2, scale=2.5)
        display_info_hkt_set2 = False
        exercise_mode = "rest_hkt_set2"
        rest_hkt_start_time_set2 = time.time()

    return img

def rest_hkt_set2(img):
    global exercise_mode, rest_hkt_start_time_set2, start_time_hkt_set3
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_hkt_start_time_set2
    rest_remaining_time = max(0, 10 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "highkneetap_set3"
        start_time_hkt_set3 = time.time()

    return img

def detect_hkt_set3(img):
    global count_high_knee_tap_left_set3, count_high_knee_tap_right_set3, dir_high_knee_tap_left_set3, dir_high_knee_tap_right_set3, start_time_hkt_set3, repetition_time_hkt_set3, display_info_hkt_set3, leftbody_hkt_set3, rightbody_hkt_set3, per_left_leg_hkt_set3, per_right_leg_hkt_set3, bar_left_leg_hkt_set3, bar_right_leg_hkt_set3, cooldown_duration_hkt_set3, cooldown_timer_hkt_set3, color_left_leg_hkt_set3, color_right_leg_hkt_set3, exercise_mode, orientation, orientation2, rest_hkt_start_time_set3

    img = cv2.resize(img, (1280, 720))

    elapsed_time = time.time() - start_time_hkt_set3
    remaining_time = max(0, 20 - elapsed_time) #repetition_time_hkt_set3

    if display_info_hkt_set3:  # Check if to display counter, bar, and percentage
        img = detector_HighKneeTap.findPose(img, False)
        lmList_jumping_jacks = detector_HighKneeTap.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_jumping_jacks) != 0:

            # Right and Left keypoints
            rightleg_hkt_set3, orientation = detector_HighKneeTap.HighKneeTap(img, 24, 26, 28, True)
            leftleg_hkt_set3, orientation2 = detector_HighKneeTap.HighKneeTap(img, 23, 25, 27, True)

            if cooldown_timer_hkt_set3 > 0:
                cooldown_timer_hkt_set3 -= 1

            if orientation == 'right' and orientation2 == 'right':
                    per_right_leg_hkt_set3 = np.interp(rightleg_hkt_set3, (70, 170), (100, 0))
                    bar_right_leg_hkt_set3 = np.interp(rightleg_hkt_set3, (70, 170), (480, 680))
                    per_left_leg_hkt_set3 = np.interp(leftleg_hkt_set3, (70, 170), (100, 0))
                    bar_left_leg_hkt_set3 = np.interp(leftleg_hkt_set3, (70, 170), (480, 680))

                    if int(per_left_leg_hkt_set3) == 100 :
                        color_left_leg_hkt_set3 = (0, 255, 0) 
                    elif int(per_right_leg_hkt_set3) == 100:
                        color_right_leg_hkt_set3 = (0, 255, 0)
                    else:
                        color_left_leg_hkt_set3 = (0, 0, 255)  
                        color_right_leg_hkt_set3 = (0, 0, 255)
                    
                    if 50 <= rightleg_hkt_set3 <= 60:
                        if dir_high_knee_tap_right_set3 == 0:
                            count_high_knee_tap_right_set3 += 1
                            dir_high_knee_tap_right_set3 = 1
                            cooldown_timer_hkt_set3 = cooldown_duration_hkt_set3
                            #print("Up Right: ",count_high_knee_tap_right)
                    elif rightleg_hkt_set3 >= 155: 
                        if dir_high_knee_tap_right_set3 == 1:
                            dir_high_knee_tap_right_set3 = 0

                    if 50 <= leftleg_hkt_set3 <= 60:
                        if dir_high_knee_tap_left_set3 == 0:
                            count_high_knee_tap_left_set3 += 1
                            dir_high_knee_tap_left_set3 = 1
                            cooldown_timer_hkt_set3 = cooldown_duration_hkt_set3
                            #print("Up Left: ",count_high_knee_tap_left)

                    elif leftleg_hkt_set3 >= 155:
                        if dir_high_knee_tap_left_set3 == 1:
                            dir_high_knee_tap_left_set3 = 0

            elif orientation =='left' and orientation2 == 'left':
                    per_right_leg_hkt_set3 = np.interp(rightleg_hkt_set3, (210, 300), (0, 100))
                    bar_right_leg_hkt_set3 = np.interp(rightleg_hkt_set3, (210, 300), (680, 480))
                    per_left_leg_hkt_set3 = np.interp(leftleg_hkt_set3, (210, 300), (0, 100))
                    bar_left_leg_hkt_set3 = np.interp(leftleg_hkt_set3, (210, 300), (680, 480))

                    if int(per_left_leg_hkt_set3) == 100 :
                        color_left_leg_hkt_set3 = (0, 255, 0) 
                    elif int(per_right_leg_hkt_set3) == 100:
                        color_right_leg_hkt_set3 = (0, 255, 0)
                    else:
                        color_left_leg_hkt_set3 = (0, 0, 255)  
                        color_right_leg_hkt_set3 = (0, 0, 255)

                    if rightleg_hkt_set3 >= 295:
                        if dir_high_knee_tap_right_set3 == 0:
                            count_high_knee_tap_right_set3 += 1
                            dir_high_knee_tap_right_set3 = 1
                            cooldown_timer_hkt_set3 = cooldown_duration_hkt_set3
                    elif rightleg_hkt_set3 <= 210: 
                        if dir_high_knee_tap_right_set3 == 1:
                            dir_high_knee_tap_right_set3 = 0

                    if leftleg_hkt_set3 >= 300:
                        if dir_high_knee_tap_left_set3 == 0:
                            count_high_knee_tap_left_set3 += 1
                            dir_high_knee_tap_left_set3 = 1
                            cooldown_timer_hkt_set3 = cooldown_duration_hkt_set3
                    elif leftleg_hkt_set3 <= 210:
                        if dir_high_knee_tap_left_set3 == 1:
                            dir_high_knee_tap_left_set3 = 0

            elif orientation == 'front' and orientation2 == 'front':
                    per_right_leg_hkt_set3 = np.interp(rightleg_hkt_set3, (150, 240), (100, 0))
                    bar_right_leg_hkt_set3 = np.interp(rightleg_hkt_set3, (150, 240), (480, 680))
                    per_left_leg_hkt_set3 = np.interp(leftleg_hkt_set3, (150, 240), (100, 0))
                    bar_left_leg_hkt_set3= np.interp(leftleg_hkt_set3, (150, 240), (480, 680))
                    
                    if int(per_left_leg_hkt_set3) == 100 :
                        color_left_leg_hkt_set3 = (0, 255, 0) 
                    elif int(per_right_leg_hkt_set3) == 100:
                        color_right_leg_hkt_set3 = (0, 255, 0)
                    else:
                        color_left_leg_hkt_set3 = (0, 0, 255)  
                        color_right_leg_hkt_set3 = (0, 0, 255)

                    if rightleg_hkt_set3 <= 150:
                        if dir_high_knee_tap_right_set3 == 0:
                            count_high_knee_tap_right_set3 += 1
                            dir_high_knee_tap_right_set3 = 1
                            cooldown_timer_hkt_set3 = cooldown_duration_hkt_set3
                    elif rightleg_hkt_set3 >= 240: 
                        if dir_high_knee_tap_right_set3 == 1:
                            dir_high_knee_tap_right_set3 = 0

                    if leftleg_hkt_set3 <= 150:
                        if dir_high_knee_tap_left_set3 == 0:
                            count_high_knee_tap_left_set3 += 1
                            dir_high_knee_tap_left_set3 = 1
                            cooldown_timer_hkt_set3 = cooldown_duration_hkt_set3
                    elif leftleg_hkt_set3 >= 240:
                        if dir_high_knee_tap_left_set3 == 1:
                            dir_high_knee_tap_left_set3 = 0


        

        cvzone.putTextRect(img, 'High Knee Tap SET 3', [450, 30], thickness=2, border=2, scale=2)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # Orientation
        cv2.rectangle(img, (890, 100), (1180, 160), (0, 0, 255), -2)
        cv2.putText(img, f"Orientation: {orientation}", (900, 140), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)

        # RIGHT LEG
        cv2.putText(img, f"R {int(per_right_leg_hkt_set3)}%", (24, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 480), (50, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_leg_hkt_set3)), (50, 680), color_right_leg_hkt_set3, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_left_leg_hkt_set3)}%", (962, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 480), (995, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_leg_hkt_set3)), (995, 680), color_left_leg_hkt_set3, -1)
    
    # Counter 
    cv2.rectangle(img, (20, 20), (200, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(count_high_knee_tap_right_set3)}/5", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (210, 20), (390, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(count_high_knee_tap_left_set3)}/5", (220, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    #Timer
    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
        display_info_hkt_set3 = False
        exercise_mode = "rest_hkt_set3"
        rest_hkt_start_time_set3 = time.time()

    # Repetition
    if count_high_knee_tap_right_set3 >= 5 and count_high_knee_tap_left_set3 >= 5:  # Changeable
        cvzone.putTextRect(img, 'Exercise Complete', [390, 30], thickness=2, border=2, scale=2.5)
        display_info_hkt_set3 = False
        exercise_mode = "rest_hkt_set3"
        rest_hkt_start_time_set3 = time.time()
    return img

def rest_hkt_set3(img):
    global exercise_mode, rest_hkt_start_time_set3, start_time_hpp
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_hkt_start_time_set3
    rest_remaining_time = max(0, 10 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "dhh"
        start_time_hpp = time.time()
    return img

def detect_dhh(img):
    global count_hip_hinge, dir_hip_hinge, start_time_hpp, repetition_time_hpp, display_info_hpp, per_left_hip_angle, bar_left_hip_angle, per_right_hip_angle, bar_right_hip_angle, leftbody_hpp, rightbody_hpp, color_hip, rest_dhh_start_time, orientation, orientation2, exercise_mode


    img = cv2.resize(img, (1280, 720))


    elapsed_time = time.time() - start_time_hpp
    remaining_time = max(0, 20 - elapsed_time) #repetition_time_hpp

    if display_info_hpp:
        img = detector_HipHinge.findPose(img, False)
        lmList_hip_hinge = detector_HipHinge.findPosition(img, False)

        if len(lmList_hip_hinge) != 0:
            leftbody_hpp, orientation = detector_HipHinge.HipHinge(img, 11, 23, 25, True)
            rightbody_hpp, orientation2 = detector_HipHinge.HipHinge(img, 12, 24, 26, True)

            if orientation == 'right' and orientation2 == 'right':
                if leftbody_hpp is not None and rightbody_hpp is not None:

                    per_left_hip_angle = np.interp(int(leftbody_hpp), (230, 280), (0, 100))
                    bar_left_hip_angle = np.interp(int(leftbody_hpp), (230, 280), (400, 200))

                    per_right_hip_angle = np.interp(int(rightbody_hpp), (230, 280), (0, 100))
                    bar_right_hip_angle = np.interp(int(rightbody_hpp), (230, 280), (400, 200))

                    if per_left_hip_angle >= 100 and per_right_hip_angle >= 100:
                        color_hip = (0, 255, 0)
                    else: 
                        color_hip = (0, 0, 255)
                    
                    if leftbody_hpp >= 270 and rightbody_hpp >= 270:
                        if dir_hip_hinge == 0:
                            count_hip_hinge += 0.5
                            dir_hip_hinge = 1
                    elif leftbody_hpp <= 230 and rightbody_hpp <= 230:
                        if dir_hip_hinge == 1:
                            dir_hip_hinge = 0
                            count_hip_hinge += 0.5

            elif orientation =='left' and orientation2 == 'left':
                if leftbody_hpp is not None and rightbody_hpp is not None:
                    per_left_hip_angle = np.interp(int(leftbody_hpp), (70, 150), (100, 0))
                    bar_left_hip_angle = np.interp(int(leftbody_hpp), (70, 140), (200, 400))

                    per_right_hip_angle = np.interp(int(rightbody_hpp), (70, 150), (100, 0))
                    bar_right_hip_angle = np.interp(int(rightbody_hpp), (70, 140), (200, 400))

                    
                    if per_left_hip_angle >= 100 and per_right_hip_angle >= 100:
                        color_hip = (0, 255, 0)
                    else: 
                        color_hip = (0, 0, 255)
                    
                    if leftbody_hpp <= 70 and rightbody_hpp <= 70:
                        if dir_hip_hinge == 0:
                            count_hip_hinge += 0.5
                            dir_hip_hinge = 1
                    elif leftbody_hpp >= 150 and rightbody_hpp >= 150:
                        if dir_hip_hinge == 1:
                            count_hip_hinge += 0.5
                            dir_hip_hinge = 0

            elif orientation == 'front' and orientation2 == 'front':
                if leftbody_hpp is not None and rightbody_hpp is not None:
                    per_left_hip_angle = np.interp(int(leftbody_hpp), (90, 240), (100, 0))
                    bar_left_hip_angle = np.interp(int(leftbody_hpp), (80, 240), (200, 400))

                    per_right_hip_angle = np.interp(int(rightbody_hpp), (90, 240), (100, 0))
                    bar_right_hip_angle = np.interp(int(rightbody_hpp), (80, 240), (200, 400))

                    
                    if per_left_hip_angle >= 100 and per_right_hip_angle >= 100:
                        color_hip = (0, 255, 0)
                    else: 
                        color_hip = (0, 0, 255)
                    

                    if leftbody_hpp <= 90 and rightbody_hpp <= 90:
                        if dir_hip_hinge == 0:
                            count_hip_hinge += 0.5
                            dir_hip_hinge = 1
                    elif leftbody_hpp >= 240 and rightbody_hpp >= 240:
                        if dir_hip_hinge == 1:
                            count_hip_hinge += 0.5
                            dir_hip_hinge = 0

        cvzone.putTextRect(img, 'Dumbbell Hip Hinge Tracker', [220, 30], thickness=2, border=2, scale=2.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # Orientation
        cv2.rectangle(img, (890, 100), (1180, 160), (0, 0, 255), -2)
        cv2.putText(img, f"Orientation: {orientation}", (900, 140), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)

        # Draw angle information
        cv2.putText(img, f"R: {int(per_right_hip_angle)}", (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_hip_angle)),(50, 400), color_hip, -1)

        cv2.putText(img, f"L: {int(per_left_hip_angle)}", (924, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_hip_angle)), (995, 400), color_hip, -1)

    # Draw count
    cv2.rectangle(img, (0, 0), (130, 120), (255, 0, 0), -1)
    cv2.putText(img, f"{int(count_hip_hinge)}/5", (20, 70), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    # Check if time's up
    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
        display_info_hpp = False
        exercise_mode = "rest_dhh"
        rest_dhh_start_time = time.time()

    # Check if exercise is complete
    if count_hip_hinge >= 5:  
        cvzone.putTextRect(img, 'Exercise Complete', [390, 30], thickness=2, border=2, scale=2.5)
        display_info_hpp = False
        exercise_mode = "rest_dhh"
        rest_dhh_start_time = time.time()

    return img

def rest_dhh(img):
    global exercise_mode, rest_dhh_start_time, start_time_hpp_set2
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_dhh_start_time
    rest_remaining_time = max(0, 10 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "dhh_set2"
        start_time_hpp_set2 = time.time()
    return img

def detect_dhh_set2(img):
    global count_hip_hinge_set2, dir_hip_hinge_set2, start_time_hpp_set2, repetition_time_hpp_set2, display_info_hpp_set2, per_left_hip_angle_set2, bar_left_hip_angle_set2, per_right_hip_angle_set2, bar_right_hip_angle_set2, leftbody_hpp_set2, rightbody_hpp_set2, color_hip_set2, rest_dhh_start_time_set2, orientation, orientation2, exercise_mode


    img = cv2.resize(img, (1280, 720))


    elapsed_time = time.time() - start_time_hpp_set2
    remaining_time = max(0, 20 - elapsed_time) #repetition_time_hpp_set2

    if display_info_hpp_set2:
        img = detector_HipHinge.findPose(img, False)
        lmList_hip_hinge = detector_HipHinge.findPosition(img, False)

        if len(lmList_hip_hinge) != 0:
            leftbody_hpp_set2, orientation = detector_HipHinge.HipHinge(img, 11, 23, 25, True)
            rightbody_hpp_set2, orientation2 = detector_HipHinge.HipHinge(img, 12, 24, 26, True)

            if orientation == 'right' and orientation2 == 'right':
                if leftbody_hpp_set2 is not None and rightbody_hpp_set2 is not None:

                    per_left_hip_angle_set2 = np.interp(int(leftbody_hpp_set2), (230, 280), (0, 100))
                    bar_left_hip_angle_set2 = np.interp(int(leftbody_hpp_set2), (230, 280), (400, 200))

                    per_right_hip_angle_set2 = np.interp(int(rightbody_hpp_set2), (230, 280), (0, 100))
                    bar_right_hip_angle_set2 = np.interp(int(rightbody_hpp_set2), (230, 280), (400, 200))

                    if per_left_hip_angle_set2 >= 100 and per_right_hip_angle_set2 >= 100:
                        color_hip_set2 = (0, 255, 0)
                    else: 
                        color_hip_set2 = (0, 0, 255)
                    
                    if leftbody_hpp_set2 >= 270 and rightbody_hpp_set2 >= 270:
                        if dir_hip_hinge_set2 == 0:
                            count_hip_hinge_set2 += 0.5
                            dir_hip_hinge_set2 = 1
                    elif leftbody_hpp_set2 <= 230 and rightbody_hpp_set2 <= 230:
                        if dir_hip_hinge_set2 == 1:
                            dir_hip_hinge_set2 = 0
                            count_hip_hinge_set2 += 0.5

            elif orientation =='left' and orientation2 == 'left':
                if leftbody_hpp_set2 is not None and rightbody_hpp_set2 is not None:
                    per_left_hip_angle_set2 = np.interp(int(leftbody_hpp_set2), (70, 150), (100, 0))
                    bar_left_hip_angle_set2 = np.interp(int(leftbody_hpp_set2), (70, 140), (200, 400))

                    per_right_hip_angle_set2 = np.interp(int(rightbody_hpp_set2), (70, 150), (100, 0))
                    bar_right_hip_angle_set2 = np.interp(int(rightbody_hpp_set2), (70, 140), (200, 400))

                    
                    if per_left_hip_angle_set2 >= 100 and per_right_hip_angle_set2 >= 100:
                        color_hip_set2 = (0, 255, 0)
                    else: 
                        color_hip_set2 = (0, 0, 255)
                    
                    if leftbody_hpp_set2 <= 70 and rightbody_hpp_set2 <= 70:
                        if dir_hip_hinge_set2 == 0:
                            count_hip_hinge_set2 += 0.5
                            dir_hip_hinge_set2 = 1
                    elif leftbody_hpp_set2 >= 150 and rightbody_hpp_set2 >= 150:
                        if dir_hip_hinge_set2 == 1:
                            count_hip_hinge_set2 += 0.5
                            dir_hip_hinge_set2 = 0

            elif orientation == 'front' and orientation2 == 'front':
                if leftbody_hpp_set2 is not None and rightbody_hpp_set2 is not None:
                    per_left_hip_angle_set2 = np.interp(int(leftbody_hpp_set2), (90, 240), (100, 0))
                    bar_left_hip_angle_set2 = np.interp(int(leftbody_hpp_set2), (80, 240), (200, 400))

                    per_right_hip_angle_set2 = np.interp(int(rightbody_hpp_set2), (90, 240), (100, 0))
                    bar_right_hip_angle_set2 = np.interp(int(rightbody_hpp_set2), (80, 240), (200, 400))

                    
                    if per_left_hip_angle_set2 >= 100 and per_right_hip_angle_set2 >= 100:
                        color_hip_set2 = (0, 255, 0)
                    else: 
                        color_hip_set2 = (0, 0, 255)
                    

                    if leftbody_hpp_set2 <= 90 and rightbody_hpp_set2 <= 90:
                        if dir_hip_hinge_set2 == 0:
                            count_hip_hinge_set2 += 0.5
                            dir_hip_hinge_set2 = 1
                    elif leftbody_hpp_set2 >= 240 and rightbody_hpp_set2 >= 240:
                        if dir_hip_hinge_set2 == 1:
                            count_hip_hinge_set2 += 0.5
                            dir_hip_hinge_set2 = 0

        cvzone.putTextRect(img, 'Dumbbell Hip Hinge SET 2', [220, 30], thickness=2, border=2, scale=2.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # Orientation
        cv2.rectangle(img, (890, 100), (1180, 160), (0, 0, 255), -2)
        cv2.putText(img, f"Orientation: {orientation}", (900, 140), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)

        # Draw angle information
        cv2.putText(img, f"R: {int(per_right_hip_angle_set2)}", (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_hip_angle_set2)),(50, 400), color_hip_set2, -1)

        cv2.putText(img, f"L: {int(per_left_hip_angle_set2)}", (924, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_hip_angle_set2)), (995, 400), color_hip_set2, -1)

    # Draw count
    cv2.rectangle(img, (0, 0), (130, 120), (255, 0, 0), -1)
    cv2.putText(img, f"{int(count_hip_hinge_set2)}/5", (20, 70), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    # Check if time's up
    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
        display_info_hpp_set2 = False
        exercise_mode = "rest_dhh_set2"
        rest_dhh_start_time_set2 = time.time()

    # Check if exercise is complete
    if count_hip_hinge_set2 >= 5:  
        cvzone.putTextRect(img, 'Exercise Complete', [390, 30], thickness=2, border=2, scale=2.5)
        display_info_hpp_set2 = False
        exercise_mode = "rest_dhh_set2"
        rest_dhh_start_time_set2 = time.time()

    return img

def rest_dhh_set2(img):
    global exercise_mode, rest_dhh_start_time_set2, start_time_hpp_set3
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_dhh_start_time_set2
    rest_remaining_time = max(0, 10 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "dhh_set3"
        start_time_hpp_set3 = time.time()
    return img

def detect_dhh_set3(img):
    global count_hip_hinge_set3, dir_hip_hinge_set3, start_time_hpp_set3, repetition_time_hpp_set3, display_info_hpp_set3, per_left_hip_angle_set3, bar_left_hip_angle_set3, per_right_hip_angle_set3, bar_right_hip_angle_set3, leftbody_hpp_set3, rightbody_hpp_set3, color_hip_set3, rest_dhh_start_time_set3, orientation, orientation2, exercise_mode


    img = cv2.resize(img, (1280, 720))


    elapsed_time = time.time() - start_time_hpp_set3
    remaining_time = max(0, 20 - elapsed_time) #repetition_time_hpp_set3

    if display_info_hpp_set3:
        img = detector_HipHinge.findPose(img, False)
        lmList_hip_hinge = detector_HipHinge.findPosition(img, False)

        if len(lmList_hip_hinge) != 0:
            leftbody_hpp_set3, orientation = detector_HipHinge.HipHinge(img, 11, 23, 25, True)
            rightbody_hpp_set3, orientation2 = detector_HipHinge.HipHinge(img, 12, 24, 26, True)

            if orientation == 'right' and orientation2 == 'right':
                if leftbody_hpp_set3 is not None and rightbody_hpp_set3 is not None:

                    per_left_hip_angle_set3 = np.interp(int(leftbody_hpp_set3), (230, 280), (0, 100))
                    bar_left_hip_angle_set3 = np.interp(int(leftbody_hpp_set3), (230, 280), (400, 200))

                    per_right_hip_angle_set3 = np.interp(int(rightbody_hpp_set3), (230, 280), (0, 100))
                    bar_right_hip_angle_set3 = np.interp(int(rightbody_hpp_set3), (230, 280), (400, 200))

                    if per_left_hip_angle_set3 >= 100 and per_right_hip_angle_set3 >= 100:
                        color_hip_set3 = (0, 255, 0)
                    else: 
                        color_hip_set3 = (0, 0, 255)
                    
                    if leftbody_hpp_set3 >= 270 and rightbody_hpp_set3 >= 270:
                        if dir_hip_hinge_set3 == 0:
                            count_hip_hinge_set3 += 0.5
                            dir_hip_hinge_set3 = 1
                    elif leftbody_hpp_set3 <= 230 and rightbody_hpp_set3 <= 230:
                        if dir_hip_hinge_set3 == 1:
                            dir_hip_hinge_set3 = 0
                            count_hip_hinge_set3 += 0.5

            elif orientation =='left' and orientation2 == 'left':
                if leftbody_hpp_set3 is not None and rightbody_hpp_set3 is not None:
                    per_left_hip_angle_set3 = np.interp(int(leftbody_hpp_set3), (70, 150), (100, 0))
                    bar_left_hip_angle_set3 = np.interp(int(leftbody_hpp_set3), (70, 140), (200, 400))

                    per_right_hip_angle_set3 = np.interp(int(rightbody_hpp_set3), (70, 150), (100, 0))
                    bar_right_hip_angle_set3 = np.interp(int(rightbody_hpp_set3), (70, 140), (200, 400))

                    
                    if per_left_hip_angle_set3 >= 100 and per_right_hip_angle_set3 >= 100:
                        color_hip_set3 = (0, 255, 0)
                    else: 
                        color_hip_set3 = (0, 0, 255)
                    
                    if leftbody_hpp_set3 <= 70 and rightbody_hpp_set3 <= 70:
                        if dir_hip_hinge_set3 == 0:
                            count_hip_hinge_set3 += 0.5
                            dir_hip_hinge_set3 = 1
                    elif leftbody_hpp_set3 >= 150 and rightbody_hpp_set3 >= 150:
                        if dir_hip_hinge_set3 == 1:
                            count_hip_hinge_set3 += 0.5
                            dir_hip_hinge_set3 = 0

            elif orientation == 'front' and orientation2 == 'front':
                if leftbody_hpp_set3 is not None and rightbody_hpp_set3 is not None:
                    per_left_hip_angle_set3 = np.interp(int(leftbody_hpp_set3), (90, 240), (100, 0))
                    bar_left_hip_angle_set3 = np.interp(int(leftbody_hpp_set3), (80, 240), (200, 400))

                    per_right_hip_angle_set3 = np.interp(int(rightbody_hpp_set3), (90, 240), (100, 0))
                    bar_right_hip_angle_set3 = np.interp(int(rightbody_hpp_set3), (80, 240), (200, 400))

                    
                    if per_left_hip_angle_set3 >= 100 and per_right_hip_angle_set3 >= 100:
                        color_hip_set3 = (0, 255, 0)
                    else: 
                        color_hip_set3 = (0, 0, 255)
                    

                    if leftbody_hpp_set3 <= 90 and rightbody_hpp_set3 <= 90:
                        if dir_hip_hinge_set3== 0:
                            count_hip_hinge_set3 += 0.5
                            dir_hip_hinge_set3 = 1
                    elif leftbody_hpp_set3 >= 240 and rightbody_hpp_set3 >= 240:
                        if dir_hip_hinge_set3 == 1:
                            count_hip_hinge_set3 += 0.5
                            dir_hip_hinge_set3 = 0

        cvzone.putTextRect(img, 'Dumbbell Hip Hinge SET 3', [220, 30], thickness=2, border=2, scale=2.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # Orientation
        cv2.rectangle(img, (890, 100), (1180, 160), (0, 0, 255), -2)
        cv2.putText(img, f"Orientation: {orientation}", (900, 140), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)

        # Draw angle information
        cv2.putText(img, f"R: {int(per_right_hip_angle_set3)}", (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_hip_angle_set3)),(50, 400), color_hip_set3, -1)

        cv2.putText(img, f"L: {int(per_left_hip_angle_set3)}", (924, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_hip_angle_set3)), (995, 400), color_hip_set3, -1)

    # Draw count
    cv2.rectangle(img, (0, 0), (130, 120), (255, 0, 0), -1)
    cv2.putText(img, f"{int(count_hip_hinge_set3)}/5", (20, 70), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    # Check if time's up
    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
        display_info_hpp_set3 = False
        exercise_mode = "rest_dhh_set3"
        rest_dhh_start_time_set3 = time.time()

    # Check if exercise is complete
    if count_hip_hinge_set3 >= 5:  
        cvzone.putTextRect(img, 'Exercise Complete', [390, 30], thickness=2, border=2, scale=2.5)
        display_info_hpp_set3 = False
        exercise_mode = "rest_dhh_set3"
        rest_dhh_start_time_set3 = time.time()
    return img

def rest_dhh_set3(img):
    global exercise_mode, rest_dhh_start_time_set3, start_time_hpp_set3
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_dhh_start_time_set3
    rest_remaining_time = max(0, 10 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "done exercise"
        print(exercise_mode)
        #start_time_hpp_set3 = time.time()
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
