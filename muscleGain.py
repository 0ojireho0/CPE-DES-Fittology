from flask import Blueprint, render_template ,session, Response, jsonify
import cv2
import cvzone
import time
import os
import numpy as np
import poseModules.bicepcurl_front_PoseModule as pm_bicep
import poseModules.pushup_front_PoseModule as pm_pushup
import poseModules.shouldertaps_front_PoseModule as pm_shouldertap
import poseModules.chestpress_front_PoseModule as pm_chestpress
import poseModules.dumbbellfrontraise_front_PoseModule as pm_dumbbellfrontraise
import poseModules.alternating_leg_lunge_front_PoseModule as pm_alternatinglunge
import poseModules.bodyweightsquat_front_PoseModule as pm_bws
import poseModules.gobletsquat_front_PoseModule as pm_gs
import poseModules.highkneetap_front_PoseModule as pm_hkt
import poseModules.dumbbellhiphinge_front_PoseModule as pm_dhh

muscleGain = Blueprint("muscleGain", __name__,static_folder="static", template_folder="templates")


# --------- FOR BICEP ------------
# Initialize posemodule as detector
detector_bicep = pm_bicep.poseDetector()

#Initialize Variables
count_bicep_left = 0
count_bicep_right = 0
dir_bicep_left = 0
dir_bicep_right = 0

start_time_bicep = None # starts time
countdown_before_exercise = None
countdown_repetition_time = 10
repetition_time_bicep = 70 # duration time
display_info_bicep = False

rest_bicep_start_time = time.time()

bar_left_bicep = 0
bar_right_bicep = 0
per_left_bicep = 0
per_right_bicep = 0
angle_left_bicep = 0
angle_right_bicep = 0

color_right_bicep = (0, 0, 255)
color_left_bicep = (0, 0, 255)

feedback_left_bicep = ""
feedback_right_bicep = ""

min_threshold_bicep = 10
max_threshold_bicep = 90
success_threshold_bicep = 100

peak_value_bicep = 0
atrest_value_bicep = 0
reps_count_bicep = 0

unsuccessful_reps_count_left_bicep = 0
successful_reps_count_left_bicep = 0

unsuccessful_reps_count_right_bicep = 0
successful_reps_count_right_bicep = 0

dir_bicep_left_unsuccessful_bicep = 0
dir_bicep_right_unsuccessful_bicep = 0

total_reps_count_bicep = 0

total_reps_count_left_bicep = 0
total_reps_count_right_bicep = 0

#timer
start_time1_bicep = time.time()
start_time2_bicep = time.time()
start_time3_bicep = time.time()
time_threshold_bicep = 1  
within_range_time1_bicep = 0
within_range_time2_bicep = 0

# gen feedback success
general_feedback_left_bicep = ""
general_feedback_right_bicep = ""

# gen feedback unsuccess
dir_gen_feedback_bicep = 0
dir_gen_feedback_unsuccessful_bicep = 0

# --------- END FOR BICEP ---------------------

# --------- FOR BICEP SET 2 ------------
# Initialize posemodule as detector
detector_bicep = pm_bicep.poseDetector()

# Initialize variables for counting curls
count_bicep_left_set2 = 0
count_bicep_right_set2 = 0
dir_bicep_left_set2 = 0
dir_bicep_right_set2 = 0

start_time_bicep_set2= time.time() # starts time
#repetition_time_bicep_set2 = 70 # duration time
display_info_bicep_set2 = True
rest_bicep_start_time_set2 = time.time()

bar_left_bicep_set2 = 0
bar_right_bicep_set2 = 0
per_left_bicep_set2 = 0
per_right_bicep_set2 = 0
angle_left_bicep_set2 = 0
angle_right_bicep_set2 = 0

color_right_bicep_set2 = (0, 0, 255)
color_left_bicep_set2 = (0, 0, 255)

feedback_left_bicep_set2 = ""
feedback_right_bicep_set2 = ""

min_threshold_bicep_set2 = 10
max_threshold_bicep_set2 = 90
success_threshold_bicep_set2 = 100

peak_value_bicep_set2 = 0
atrest_value_bicep_set2 = 0
reps_count_bicep_set2 = 0

unsuccessful_reps_count_left_bicep_set2 = 0
successful_reps_count_left_bicep_set2 = 0

unsuccessful_reps_count_right_bicep_set2 = 0
successful_reps_count_right_bicep_set2 = 0

dir_bicep_left_unsuccessful_bicep_set2 = 0
dir_bicep_right_unsuccessful_bicep_set2 = 0

total_reps_count_bicep_set2 = 0
total_reps_count_left_bicep_set2 = 0
total_reps_count_right_bicep_set2 = 0

#timer
start_time1_bicep_set2 = time.time()
start_time2_bicep_set2 = time.time()
start_time3_bicep_set2 = time.time()
time_threshold_bicep_set2 = 1  
within_range_time1_bicep_set2 = 0
within_range_time2_bicep_set2 = 0

# gen feedback success
general_feedback_left_bicep_set2 = ""
general_feedback_right_bicep_set2 = ""

# gen feedback unsuccess
dir_gen_feedback_bicep_set2 = 0
dir_gen_feedback_unsuccessful_bicep_set2 = 0
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
#repetition_time_bicep = 70 # duration time
display_info_bicep_set3 = True

rest_bicep_start_time_set3 = time.time()

bar_left_bicep_set3 = 0
bar_right_bicep_set3 = 0
per_left_bicep_set3 = 0
per_right_bicep_set3 = 0
angle_left_bicep_set3 = 0
angle_right_bicep_set3 = 0

color_right_bicep_set3 = (0, 0, 255)
color_left_bicep_set3 = (0, 0, 255)

feedback_left_bicep_set3 = ""
feedback_right_bicep_set3 = ""

min_threshold_bicep_set3 = 10
max_threshold_bicep_set3 = 90
success_threshold_bicep_set3 = 100

peak_value_bicep_set3 = 0
atrest_value_bicep_set3 = 0
reps_count_bicep_set3 = 0

unsuccessful_reps_count_left_bicep_set3 = 0
successful_reps_count_left_bicep_set3 = 0

unsuccessful_reps_count_right_bicep_set3 = 0
successful_reps_count_right_bicep_set3 = 0

dir_bicep_left_unsuccessful_bicep_set3 = 0
dir_bicep_right_unsuccessful_bicep_set3 = 0

total_reps_count_bicep_set3 = 0

total_reps_count_left_bicep_set3 = 0
total_reps_count_right_bicep_set3 = 0

#timer
start_time1_bicep_set3 = time.time()
start_time2_bicep_set3 = time.time()
start_time3_bicep_set3 = time.time()
time_threshold_bicep_set3 = 1  
within_range_time1_bicep_set3 = 0
within_range_time2_bicep_set3 = 0

# gen feedback success
general_feedback_left_bicep_set3 = ""
general_feedback_right_bicep_set3 = ""

# gen feedback unsuccess
dir_gen_feedback_bicep_set3 = 0
dir_gen_feedback_unsuccessful_bicep_set3 = 0
# --------- END FOR BICEP SET 3 ---------------------

# ----------- FOR PUSH UP ---------------
# Import class
detector_pushup = pm_pushup.poseDetectorPushUp()


# Display info
display_info_pushup = True
dir_left_pushup = 0

dir_right_pushup = 0
per_right_pushup = 0
per_left_pushup = 0
bar_left_pushup = 0
bar_right_pushup = 0 

leftangle_pushup = 0
rightangle_pushup = 0

color_right_pushup = (0, 0, 255)
color_left_pushup = (0, 0, 255)

feedback_left_pushup = ""
feedback_right_pushup = ""

success_threshold_pushup = 100

peak_value_pushup = 0
atrest_value_pushup = 0

unsuccessful_reps_count_left_pushup = 0
successful_reps_count_left_pushup = 0

unsuccessful_reps_count_right_pushup = 0
successful_reps_count_right_pushup = 0

dir_left_unsuccessful_pushup = 0
dir_right_unsuccessful_pushup = 0

total_reps_count_pushup = 0

total_reps_count_left_pushup = 0
total_reps_count_right_pushup = 0
start_time1_pushup = time.time()
start_time2_pushup = time.time()
start_time3_pushup = time.time()
time_threshold_pushup = 3 
within_range_time1_pushup = 0
within_range_time2_pushup = 0

# gen feedback success
general_feedback_left_pushup = ""
general_feedback_right_pushup = ""

# gen feedback unsuccess
dir_gen_feedback_pushup = 0
dir_gen_feedback_unsuccessful_pushup = 0

rest_pushup_start_time = time.time()
# ----------- END FOR PUSH UP --------------

# ----------- FOR PUSH UP SET 2---------------
# Import class
detector_pushup = pm_pushup.poseDetectorPushUp()

# Display info
display_info_pushup_set2 = True
dir_left_pushup_set2 = 0

dir_right_pushup_set2 = 0
per_right_pushup_set2 = 0
per_left_pushup_set2 = 0
bar_left_pushup_set2 = 0
bar_right_pushup_set2 = 0 

leftangle_pushup_set2 = 0
rightangle_pushup_set2 = 0

color_right_pushup_set2 = (0, 0, 255)
color_left_pushup_set2 = (0, 0, 255)

feedback_left_pushup_set2 = ""
feedback_right_pushup_set2 = ""

success_threshold_pushup_set2 = 100

peak_value_pushup_set2 = 0
atrest_value_pushup_set2 = 0

unsuccessful_reps_count_left_pushup_set2 = 0
successful_reps_count_left_pushup_set2 = 0

unsuccessful_reps_count_right_pushup_set2 = 0
successful_reps_count_right_pushup_set2 = 0

dir_left_unsuccessful_pushup_set2 = 0
dir_right_unsuccessful_pushup_set2 = 0

total_reps_count_pushup_set2 = 0

total_reps_count_left_pushup_set2 = 0
total_reps_count_right_pushup_set2 = 0
start_time1_pushup_set2 = time.time()
start_time2_pushup_set2 = time.time()
start_time3_pushup_set2 = time.time()
time_threshold_pushup_set2 = 3 
within_range_time1_pushup_set2 = 0
within_range_time2_pushup_set2 = 0

# gen feedback success
general_feedback_left_pushup_set2 = ""
general_feedback_right_pushup_set2 = ""

# gen feedback unsuccess
dir_gen_feedback_pushup_set2 = 0
dir_gen_feedback_unsuccessful_pushup_set2 = 0

rest_pushup_start_time_set2 = time.time()
# ----------- END FOR PUSH UP SET 2 --------------

# ----------- FOR PUSH UP SET 3---------------
# Import class
detector_pushup = pm_pushup.poseDetectorPushUp()

# Display info
display_info_pushup_set3 = True
dir_left_pushup_set3 = 0

dir_right_pushup_set3 = 0
per_right_pushup_set3 = 0
per_left_pushup_set3 = 0
bar_left_pushup_set3 = 0
bar_right_pushup_set3 = 0 

leftangle_pushup_set3 = 0
rightangle_pushup_set3 = 0

color_right_pushup_set3 = (0, 0, 255)
color_left_pushup_set3 = (0, 0, 255)

feedback_left_pushup_set3 = ""
feedback_right_pushup_set3 = ""

success_threshold_pushup_set3 = 100

peak_value_pushup_set3 = 0
atrest_value_pushup_set3 = 0

unsuccessful_reps_count_left_pushup_set3 = 0
successful_reps_count_left_pushup_set3 = 0

unsuccessful_reps_count_right_pushup_set3 = 0
successful_reps_count_right_pushup_set3 = 0

dir_left_unsuccessful_pushup_set3 = 0
dir_right_unsuccessful_pushup_set3 = 0

total_reps_count_pushup_set3 = 0

total_reps_count_left_pushup_set3 = 0
total_reps_count_right_pushup_set3 = 0
start_time1_pushup_set3 = time.time()
start_time2_pushup_set3 = time.time()
start_time3_pushup_set3 = time.time()
time_threshold_pushup_set3 = 3 
within_range_time1_pushup_set3 = 0
within_range_time2_pushup_set3 = 0

# gen feedback success
general_feedback_left_pushup_set3 = ""
general_feedback_right_pushup_set3 = ""

# gen feedback unsuccess
dir_gen_feedback_pushup_set3 = 0
dir_gen_feedback_unsuccessful_pushup_set3 = 0

rest_pushup_start_time_set3 = time.time()
# ----------- END FOR PUSH UP SET 3 --------------

# ----------- FOR SHOULDER TAP ---------------
detector_shouldertaps = pm_shouldertap.poseDetectorShoulderTap()


dir_left_shouldertaps = 0
dir_right_shouldertaps = 0

repetition_time_shouldertaps = 60  # Repetition time

# Display info
display_info_shouldertaps = True

orientation_shouldertaps = ""
orientation2_shouldertaps = ""

per_right_shouldertaps = 0
per_left_shouldertaps = 0
bar_left_shouldertaps = 0
bar_right_shouldertaps = 0 


color_right_shouldertaps = (0, 0, 255)
color_left_shouldertaps = (0, 0, 255)

feedback_left_shouldertaps = ""
feedback_right_shouldertaps = ""

success_threshold_shouldertaps = 100

atrest_value_shouldertaps = 0

unsuccessful_reps_count_left_shouldertaps = 0
successful_reps_count_left_shouldertaps = 0

unsuccessful_reps_count_right_shouldertaps = 0
successful_reps_count_right_shouldertaps = 0

dir_left_unsuccessful_shouldertaps = 0
dir_right_unsuccessful_shouldertaps = 0

total_reps_count_shouldertaps = 0

total_reps_count_left_shouldertaps = 0
total_reps_count_right_shouldertaps = 0

start_time1_shouldertaps = time.time()
start_time2_shouldertaps = time.time()
start_time3_shouldertaps = time.time()
time_threshold_shouldertaps = 1 
within_range_time1_shouldertaps = 0
within_range_time2_shouldertaps = 0

# gen feedback success
general_feedback_left_shouldertaps = ""
general_feedback_right_shouldertaps = ""

# gen feedback unsuccess
dir_gen_feedback_shouldertaps = 0
dir_gen_feedback_unsuccessful_shouldertaps = 0

cooldown_timer_shouldertaps = 0
cooldown_duration_shouldertaps = 5

rest_shouldertap_start_time = time.time()

# ----------- END FOR SHOULDER TAP ---------------

# ----------- FOR SHOULDER TAP SET 2---------------


dir_left_shouldertaps_set2 = 0
dir_right_shouldertaps_set2 = 0

repetition_time_shouldertaps_set2 = 60  # Repetition time

# Display info
display_info_shouldertaps_set2 = True

orientation_shouldertaps_set2 = ""
orientation2_shouldertaps_set2 = ""

per_right_shouldertaps_set2 = 0
per_left_shouldertaps_set2 = 0
bar_left_shouldertaps_set2 = 0
bar_right_shouldertaps_set2 = 0 


color_right_shouldertaps_set2 = (0, 0, 255)
color_left_shouldertaps_set2 = (0, 0, 255)

feedback_left_shouldertaps_set2 = ""
feedback_right_shouldertaps_set2 = ""

success_threshold_shouldertaps_set2 = 100

atrest_value_shouldertaps_set2 = 0

unsuccessful_reps_count_left_shouldertaps_set2 = 0
successful_reps_count_left_shouldertaps_set2 = 0

unsuccessful_reps_count_right_shouldertaps_set2 = 0
successful_reps_count_right_shouldertaps_set2 = 0

dir_left_unsuccessful_shouldertaps_set2 = 0
dir_right_unsuccessful_shouldertaps_set2 = 0

total_reps_count_shouldertaps_set2 = 0

total_reps_count_left_shouldertaps_set2 = 0
total_reps_count_right_shouldertaps_set2 = 0

start_time1_shouldertaps_set2 = time.time()
start_time2_shouldertaps_set2 = time.time()
start_time3_shouldertaps_set2 = time.time()
time_threshold_shouldertaps_set2 = 1 
within_range_time1_shouldertaps_set2 = 0
within_range_time2_shouldertaps_set2 = 0

# gen feedback success
general_feedback_left_shouldertaps_set2 = ""
general_feedback_right_shouldertaps_set2 = ""

# gen feedback unsuccess
dir_gen_feedback_shouldertaps_set2 = 0
dir_gen_feedback_unsuccessful_shouldertaps_set2 = 0

cooldown_timer_shouldertaps_set2 = 0
cooldown_duration_shouldertaps_set2 = 5

rest_shouldertap_start_time_set2 = time.time()

# ----------- END FOR SHOULDER TAP SET 2---------------

# ----------- FOR SHOULDER TAP SET 3---------------


dir_left_shouldertaps_set3 = 0
dir_right_shouldertaps_set3 = 0

#repetition_time_shouldertaps_set3 = 60  # Repetition time

# Display info
display_info_shouldertaps_set3 = True

orientation_shouldertaps_set3 = ""
orientation2_shouldertaps_set3 = ""

per_right_shouldertaps_set3 = 0
per_left_shouldertaps_set3 = 0
bar_left_shouldertaps_set3 = 0
bar_right_shouldertaps_set3 = 0 


color_right_shouldertaps_set3 = (0, 0, 255)
color_left_shouldertaps_set3 = (0, 0, 255)

feedback_left_shouldertaps_set3 = ""
feedback_right_shouldertaps_set3 = ""

success_threshold_shouldertaps_set3 = 100

atrest_value_shouldertaps_set3 = 0

unsuccessful_reps_count_left_shouldertaps_set3 = 0
successful_reps_count_left_shouldertaps_set3 = 0

unsuccessful_reps_count_right_shouldertaps_set3 = 0
successful_reps_count_right_shouldertaps_set3 = 0

dir_left_unsuccessful_shouldertaps_set3 = 0
dir_right_unsuccessful_shouldertaps_set3 = 0

total_reps_count_shouldertaps_set3 = 0

total_reps_count_left_shouldertaps_set3 = 0
total_reps_count_right_shouldertaps_set3 = 0

start_time1_shouldertaps_set3 = time.time()
start_time2_shouldertaps_set3 = time.time()
start_time3_shouldertaps_set3 = time.time()
time_threshold_shouldertaps_set3 = 1 
within_range_time1_shouldertaps_set3 = 0
within_range_time2_shouldertaps_set3 = 0

# gen feedback success
general_feedback_left_shouldertaps_set3 = ""
general_feedback_right_shouldertaps_set3 = ""

# gen feedback unsuccess
dir_gen_feedback_shouldertaps_set3 = 0
dir_gen_feedback_unsuccessful_shouldertaps_set3 = 0

cooldown_timer_shouldertaps_set3 = 0
cooldown_duration_shouldertaps_set3 = 5

rest_shouldertap_start_time_set3 = time.time()

# ----------- END FOR SHOULDER TAP SET 3---------------

# ----------- FOR CHEST PRESS---------------

#import class
detector_chestpress = pm_chestpress.poseDetector()


dir_left_chestpress = 0
dir_right_chestpress = 0

repetition_time_chestpress = 60  # Repetition time

# Display info
display_info_chestpress = True

orientation_chestpress = ""
orientation2_chestpress = ""

per_right_chestpress = 0
per_left_chestpress = 0
bar_left_chestpress = 0
bar_right_chestpress = 0 


color_right_chestpress = (0, 0, 255)
color_left_chestpress = (0, 0, 255)

feedback_left_chestpress = ""
feedback_right_chestpress = ""

success_threshold_chestpress = 100

atrest_value_chestpress = 0

unsuccessful_reps_count_left_chestpress = 0
successful_reps_count_left_chestpress = 0

unsuccessful_reps_count_right_chestpress = 0
successful_reps_count_right_chestpress = 0

dir_left_unsuccessful_chestpress = 0
dir_right_unsuccessful_chestpress = 0

total_reps_count_chestpress = 0

total_reps_count_left_chestpress = 0
total_reps_count_right_chestpress = 0

start_time1_chestpress = time.time()
start_time2_chestpress = time.time()
start_time3_chestpress = time.time()
time_threshold_chestpress = 10 
within_range_time1_chestpress = 0
within_range_time2_chestpress = 0

# gen feedback success
general_feedback_left_chestpress = ""
general_feedback_right_chestpress = ""

# gen feedback unsuccess
dir_gen_feedback_chestpress = 0
dir_gen_feedback_unsuccessful_chestpress = 0

cooldown_timer_chestpress = 0
cooldown_duration_chestpress = 5

angle_left_chestpress = 0
angle_right_chestpress = 0

rest_chestpress_start_time = time.time()

# ----------- END FOR CHEST PRESS---------------

# ----------- FOR CHEST PRESS SET 2---------------

#import class
detector_chestpress = pm_chestpress.poseDetector()

dir_left_chestpress_set2 = 0
dir_right_chestpress_set2 = 0

#repetition_time_chestpress_set2 = 60  # Repetition time

# Display info
display_info_chestpress_set2 = True

orientation_chestpress_set2 = ""
orientation2_chestpress_set2 = ""

per_right_chestpress_set2 = 0
per_left_chestpress_set2 = 0
bar_left_chestpress_set2 = 0
bar_right_chestpress_set2 = 0 


color_right_chestpress_set2 = (0, 0, 255)
color_left_chestpress_set2 = (0, 0, 255)

feedback_left_chestpress_set2 = ""
feedback_right_chestpress_set2 = ""

success_threshold_chestpress_set2 = 100

atrest_value_chestpress_set2 = 0

unsuccessful_reps_count_left_chestpress_set2 = 0
successful_reps_count_left_chestpress_set2 = 0

unsuccessful_reps_count_right_chestpress_set2 = 0
successful_reps_count_right_chestpress_set2 = 0

dir_left_unsuccessful_chestpress_set2 = 0
dir_right_unsuccessful_chestpress_set2 = 0

total_reps_count_chestpress_set2 = 0

total_reps_count_left_chestpress_set2 = 0
total_reps_count_right_chestpress_set2 = 0

start_time1_chestpress_set2 = time.time()
start_time2_chestpress_set2 = time.time()
start_time3_chestpress_set2 = time.time()
time_threshold_chestpress_set2 = 10 
within_range_time1_chestpress_set2 = 0
within_range_time2_chestpress_set2 = 0

# gen feedback success
general_feedback_left_chestpress_set2 = ""
general_feedback_right_chestpress_set2 = ""

# gen feedback unsuccess
dir_gen_feedback_chestpress_set2 = 0
dir_gen_feedback_unsuccessful_chestpress = 0

cooldown_timer_chestpress = 0
cooldown_duration_chestpress_set2 = 5

angle_left_chestpress_set2 = 0
angle_right_chestpress_set2 = 0


rest_chestpress_start_time_set2 = time.time()

# ----------- END FOR CHEST PRESS SET 2---------------

# ----------- FOR CHEST PRESS SET 3---------------

#import class
detector_chestpress = pm_chestpress.poseDetector()

dir_left_chestpress_set3 = 0
dir_right_chestpress_set3 = 0

#repetition_time_chestpress_set3 = 60  # Repetition time

# Display info
display_info_chestpress_set3 = True

orientation_chestpress_set3 = ""
orientation2_chestpress_set3 = ""

per_right_chestpress_set3 = 0
per_left_chestpress_set3 = 0
bar_left_chestpress_set3 = 0
bar_right_chestpress_set3 = 0 


color_right_chestpress_set3 = (0, 0, 255)
color_left_chestpress_set3 = (0, 0, 255)

feedback_left_chestpress_set3 = ""
feedback_right_chestpress_set3 = ""

success_threshold_chestpress_set3 = 100

atrest_value_chestpress_set3 = 0

unsuccessful_reps_count_left_chestpress_set3 = 0
successful_reps_count_left_chestpress_set3 = 0

unsuccessful_reps_count_right_chestpress_set3 = 0
successful_reps_count_right_chestpress_set3 = 0

dir_left_unsuccessful_chestpress_set3 = 0
dir_right_unsuccessful_chestpress_set3 = 0

total_reps_count_chestpress_set3 = 0

total_reps_count_left_chestpress_set3 = 0
total_reps_count_right_chestpress_set3 = 0

start_time1_chestpress_set3 = time.time()
start_time2_chestpress_set3 = time.time()
start_time3_chestpress_set3 = time.time()
time_threshold_chestpress_set3 = 10 
within_range_time1_chestpress_set3 = 0
within_range_time2_chestpress_set3 = 0

# gen feedback success
general_feedback_left_chestpress_set3 = ""
general_feedback_right_chestpress_set3 = ""

# gen feedback unsuccess
dir_gen_feedback_chestpress_set3 = 0
dir_gen_feedback_unsuccessful_chestpress_set3 = 0

cooldown_timer_chestpress_set3 = 0
cooldown_duration_chestpress_set3 = 5

angle_left_chestpress_set3 = 0
angle_right_chestpress_set3 = 0

rest_chestpress_start_time_set3 = time.time()

# ----------- END FOR CHEST PRESS SET 3---------------

# ----------- FOR DUMBBELL FRONT RAISE ---------------
detector_dumbbellfrontraise = pm_dumbbellfrontraise.poseDetector()

dir_left_dumbbellfrontraise = 0
dir_right_dumbbellfrontraise = 0

repetition_time_dumbbellfrontraise = 60  # Repetition time

# Display info
display_info_dumbbellfrontraise = True

per_right_dumbbellfrontraise = 0
per_left_dumbbellfrontraise = 0
bar_left_dumbbellfrontraise = 0
bar_right_dumbbellfrontraise = 0 


color_right_dumbbellfrontraise = (0, 0, 255)
color_left_dumbbellfrontraise = (0, 0, 255)

feedback_left_dumbbellfrontraise = ""
feedback_right_dumbbellfrontraise = ""

success_threshold_dumbbellfrontraise = 100

atrest_value_dumbbellfrontraise = 0

unsuccessful_reps_count_left_dumbbellfrontraise = 0
successful_reps_count_left_dumbbellfrontraise = 0

unsuccessful_reps_count_right_dumbbellfrontraise = 0
successful_reps_count_right_dumbbellfrontraise = 0

dir_left_unsuccessful_dumbbellfrontraise = 0
dir_right_unsuccessful_dumbbellfrontraise = 0

total_reps_count_dumbbellfrontraise = 0

total_reps_count_left_dumbbellfrontraise = 0
total_reps_count_right_dumbbellfrontraise = 0

start_time1_dumbbellfrontraise = time.time()
start_time2_dumbbellfrontraise = time.time()
start_time3_dumbbellfrontraise = time.time()
time_threshold_dumbbellfrontraise = 10 # Specify the time threshold in seconds # can be changed for testing but default should be 1, 0.2 is for testing
within_range_time1_dumbbellfrontraise = 0
within_range_time2_dumbbellfrontraise = 0

# gen feedback success
general_feedback_left_dumbbellfrontraise = ""
general_feedback_right_dumbbellfrontraise = ""

# gen feedback unsuccess
dir_gen_feedback_dumbbellfrontraise = 0
dir_gen_feedback_unsuccessful_dumbbellfrontraise = 0

cooldown_timer_dumbbellfrontraise = 0
cooldown_duration_dumbbellfrontraise = 5

angle_left_dumbbellfrontraise = 0
angle_right_dumbbellfrontraise = 0

rest_dumbbellfrontraise_start_time = time.time()
# ----------- END FOR DUMBBELL FRONT RAISE ---------------

# ----------- FOR DUMBBELL FRONT RAISE SET 2 ---------------


dir_left_dumbbellfrontraise_set2 = 0
dir_right_dumbbellfrontraise_set2 = 0

repetition_time_dumbbellfrontraise_set2 = 60  # Repetition time

# Display info
display_info_dumbbellfrontraise_set2 = True

per_right_dumbbellfrontraise_set2 = 0
per_left_dumbbellfrontraise_set2 = 0
bar_left_dumbbellfrontraise_set2 = 0
bar_right_dumbbellfrontraise_set2 = 0 


color_right_dumbbellfrontraise_set2 = (0, 0, 255)
color_left_dumbbellfrontraise_set2 = (0, 0, 255)

feedback_left_dumbbellfrontraise_set2 = ""
feedback_right_dumbbellfrontraise_set2 = ""

success_threshold_dumbbellfrontraise_set2 = 100

atrest_value_dumbbellfrontraise_set2 = 0

unsuccessful_reps_count_left_dumbbellfrontraise_set2 = 0
successful_reps_count_left_dumbbellfrontraise_set2 = 0

unsuccessful_reps_count_right_dumbbellfrontraise_set2 = 0
successful_reps_count_right_dumbbellfrontraise_set2 = 0

dir_left_unsuccessful_dumbbellfrontraise_set2 = 0
dir_right_unsuccessful_dumbbellfrontraise_set2 = 0

total_reps_count_dumbbellfrontraise_set2 = 0

total_reps_count_left_dumbbellfrontraise_set2 = 0
total_reps_count_right_dumbbellfrontraise_set2 = 0

start_time1_dumbbellfrontraise_set2 = time.time()
start_time2_dumbbellfrontraise_set2 = time.time()
start_time3_dumbbellfrontraise_set2 = time.time()
time_threshold_dumbbellfrontraise_set2 = 10 # Specify the time threshold in seconds # can be changed for testing but default should be 1, 0.2 is for testing
within_range_time1_dumbbellfrontraise_set2 = 0
within_range_time2_dumbbellfrontraise_set2 = 0

# gen feedback success
general_feedback_left_dumbbellfrontraise_set2 = ""
general_feedback_right_dumbbellfrontraise_set2 = ""

# gen feedback unsuccess
dir_gen_feedback_dumbbellfrontraise_set2 = 0
dir_gen_feedback_unsuccessful_dumbbellfrontraise_set2 = 0

cooldown_timer_dumbbellfrontraise_set2 = 0
cooldown_duration_dumbbellfrontraise_set2 = 5

angle_left_dumbbellfrontraise_set2 = 0
angle_right_dumbbellfrontraise_set2 = 0

rest_dumbbellfrontraise_start_time_set2 = time.time()
# ----------- END FOR DUMBBELL FRONT RAISE SET 2---------------

# ----------- FOR DUMBBELL FRONT RAISE SET 3 ---------------

dir_left_dumbbellfrontraise_set3 = 0
dir_right_dumbbellfrontraise_set3 = 0

repetition_time_dumbbellfrontraise_set3 = 60  # Repetition time

# Display info
display_info_dumbbellfrontraise_set3 = True

per_right_dumbbellfrontraise_set3 = 0
per_left_dumbbellfrontraise_set3 = 0
bar_left_dumbbellfrontraise_set3 = 0
bar_right_dumbbellfrontraise_set3 = 0 


color_right_dumbbellfrontraise_set3 = (0, 0, 255)
color_left_dumbbellfrontraise_set3 = (0, 0, 255)

feedback_left_dumbbellfrontraise_set3 = ""
feedback_right_dumbbellfrontraise_set3 = ""

success_threshold_dumbbellfrontraise_set3 = 100

atrest_value_dumbbellfrontraise_set3 = 0

unsuccessful_reps_count_left_dumbbellfrontraise_set3 = 0
successful_reps_count_left_dumbbellfrontraise_set3 = 0

unsuccessful_reps_count_right_dumbbellfrontraise_set3 = 0
successful_reps_count_right_dumbbellfrontraise_set3 = 0

dir_left_unsuccessful_dumbbellfrontraise_set3 = 0
dir_right_unsuccessful_dumbbellfrontraise_set3 = 0

total_reps_count_dumbbellfrontraise_set3 = 0

total_reps_count_left_dumbbellfrontraise_set3 = 0
total_reps_count_right_dumbbellfrontraise_set3 = 0

start_time1_dumbbellfrontraise_set3 = time.time()
start_time2_dumbbellfrontraise_set3 = time.time()
start_time3_dumbbellfrontraise_set3 = time.time()
time_threshold_dumbbellfrontraise_set3 = 10
within_range_time1_dumbbellfrontraise_set3 = 0
within_range_time2_dumbbellfrontraise_set3 = 0

# gen feedback success
general_feedback_left_dumbbellfrontraise_set3 = ""
general_feedback_right_dumbbellfrontraise_set3 = ""

# gen feedback unsuccess
dir_gen_feedback_dumbbellfrontraise_set3 = 0
dir_gen_feedback_unsuccessful_dumbbellfrontraise_set3 = 0

cooldown_timer_dumbbellfrontraise_set3 = 0
cooldown_duration_dumbbellfrontraise_set3 = 5

angle_left_dumbbellfrontraise_set3 = 0
angle_right_dumbbellfrontraise_set3 = 0

rest_dumbbellfrontraise_start_time_set3 = time.time()
# ----------- END FOR DUMBBELL FRONT RAISE SET 3---------------

# ----------- FOR ALTERNATING LUNGE ---------------
detector_leglunge = pm_alternatinglunge.poseDetectoralternatinglunge()
dir_left_leglunge = 0
dir_right_leglunge = 0

repetition_time_leglunge = 60  # Repetition time

# Display info
display_info_leglunge = True

per_right_leglunge = 0
per_left_leglunge = 0
bar_left_leglunge = 0
bar_right_leglunge = 0 

leftangle_leglunge = 0
rightangle_leglunge = 0

color_right_leglunge = (0, 0, 255)
color_left_leglunge = (0, 0, 255)

feedback_left_leglunge = ""
feedback_right_leglunge = ""

success_threshold_leglunge = 100

peak_value_leglunge = 0
atrest_value_leglunge = 0

unsuccessful_reps_count_left_leglunge = 0
successful_reps_count_left_leglunge = 0

unsuccessful_reps_count_right_leglunge = 0
successful_reps_count_right_leglunge = 0

dir_left_unsuccessful_leglunge = 0
dir_right_unsuccessful_leglunge = 0

total_reps_count_leglunge = 0

total_reps_count_left_leglunge = 0
total_reps_count_right_leglunge = 0

start_time1_leglunge = time.time()
start_time2_leglunge = time.time()
start_time3_leglunge = time.time()
time_threshold_leglunge = 10 # Specify the time threshold in seconds # can be changed for testing but default should be 1, 0.2 is for testing
within_range_time1_leglunge = 0
within_range_time2_leglunge = 0

# gen feedback success
general_feedback_left_leglunge = ""
general_feedback_right_leglunge = ""

# gen feedback unsuccess
dir_gen_feedback_leglunge = 0
dir_gen_feedback_unsuccessful_leglunge = 0

cooldown_timer_leglunge = 0
cooldown_duration_leglunge = 5

rest_alternatinglunge_start_time = time.time()
# ----------- END FOR ALTERNATING LUNGE ---------------

# ----------- FOR ALTERNATING LUNGE SET 2 ---------------
dir_left_leglunge_set2 = 0
dir_right_leglunge_set2 = 0

repetition_time_leglunge_set2 = 60  # Repetition time

# Display info
display_info_leglunge_set2 = True

per_right_leglunge_set2 = 0
per_left_leglunge_set2 = 0
bar_left_leglunge_set2 = 0
bar_right_leglunge_set2 = 0 

leftangle_leglunge_set2 = 0
rightangle_leglunge_set2 = 0

color_right_leglunge_set2 = (0, 0, 255)
color_left_leglunge_set2 = (0, 0, 255)

feedback_left_leglunge_set2 = ""
feedback_right_leglunge_set2 = ""

success_threshold_leglunge_set2 = 100

peak_value_leglunge_set2 = 0
atrest_value_leglunge_set2 = 0

unsuccessful_reps_count_left_leglunge_set2 = 0
successful_reps_count_left_leglunge_set2 = 0

unsuccessful_reps_count_right_leglunge_set2 = 0
successful_reps_count_right_leglunge_set2 = 0

dir_left_unsuccessful_leglunge_set2 = 0
dir_right_unsuccessful_leglunge_set2 = 0

total_reps_count_leglunge_set2 = 0

total_reps_count_left_leglunge_set2 = 0
total_reps_count_right_leglunge_set2 = 0

start_time1_leglunge_set2 = time.time()
start_time2_leglunge_set2 = time.time()
start_time3_leglunge_set2 = time.time()
time_threshold_leglunge_set2 = 10
within_range_time1_leglunge_set2 = 0
within_range_time2_leglunge_set2 = 0

# gen feedback success
general_feedback_left_leglunge_set2 = ""
general_feedback_right_leglunge_set2 = ""

# gen feedback unsuccess
dir_gen_feedback_leglunge_set2 = 0
dir_gen_feedback_unsuccessful_leglunge_set2 = 0

cooldown_timer_leglunge_set2 = 0
cooldown_duration_leglunge_set2 = 5
rest_alternatinglunge_start_time_set2 = time.time()
# ----------- END FOR ALTERNATING LUNGE SET 2 ---------------

# ----------- FOR ALTERNATING LUNGE SET 3 ---------------
dir_left_leglunge_set3 = 0
dir_right_leglunge_set3 = 0

repetition_time_leglunge_set3 = 60  # Repetition time

# Display info
display_info_leglunge_set3 = True

per_right_leglunge_set3 = 0
per_left_leglunge_set3 = 0
bar_left_leglunge_set3 = 0
bar_right_leglunge_set3 = 0 

leftangle_leglunge_set3 = 0
rightangle_leglunge_set3 = 0

color_right_leglunge_set3 = (0, 0, 255)
color_left_leglunge_set3 = (0, 0, 255)

feedback_left_leglunge_set3 = ""
feedback_right_leglunge_set3 = ""

success_threshold_leglunge_set3 = 100

peak_value_leglunge_set3 = 0
atrest_value_leglunge_set3 = 0

unsuccessful_reps_count_left_leglunge_set3 = 0
successful_reps_count_left_leglunge_set3 = 0

unsuccessful_reps_count_right_leglunge_set3 = 0
successful_reps_count_right_leglunge_set3 = 0

dir_left_unsuccessful_leglunge_set3 = 0
dir_right_unsuccessful_leglunge_set3 = 0

total_reps_count_leglunge_set3 = 0

total_reps_count_left_leglunge_set3 = 0
total_reps_count_right_leglunge_set3 = 0

start_time1_leglunge_set3 = time.time()
start_time2_leglunge_set3 = time.time()
start_time3_leglunge_set3 = time.time()
time_threshold_leglunge_set3 = 10 
within_range_time1_leglunge_set3 = 0
within_range_time2_leglunge_set3 = 0

# gen feedback success
general_feedback_left_leglunge_set3 = ""
general_feedback_right_leglunge_set3 = ""

# gen feedback unsuccess
dir_gen_feedback_leglunge_set3 = 0
dir_gen_feedback_unsuccessful_leglunge_set3 = 0

cooldown_timer_leglunge_set3 = 0
cooldown_duration_leglunge_set3 = 5
rest_alternatinglunge_start_time_set3 = time.time()
# ----------- END FOR ALTERNATING LUNGE SET 3 ---------------

# ----------- FOR BODY WEIGHT SQUAT ---------------
detector_bodyweightsquat = pm_bws.poseDetectorBodyWeightSquat()

dir_left_bodyweightsquat = 0
dir_right_bodyweightsquat = 0

repetition_time_bodyweightsquat = 60  # Repetition time

# Display info
display_info_bodyweightsquat = True


per_right_bodyweightsquat = 0
per_left_bodyweightsquat = 0
bar_left_bodyweightsquat = 0
bar_right_bodyweightsquat = 0 

leftbody_bodyweightsquat = 0
rightbody_bodyweightsquat = 0

color_right_bodyweightsquat = (0, 0, 255)
color_left_bodyweightsquat = (0, 0, 255)

feedback_body_bodyweightsquat = ""

success_threshold_bodyweightsquat = 100

peak_value_bodyweightsquat = 0
atrest_value_bodyweightsquat = 0

unsuccessful_reps_count_body_bodyweightsquat = 0
successful_reps_count_body_bodyweightsquat = 0

dir_left_unsuccessful_bodyweightsquat = 0

total_reps_count_body_bodyweightsquat = 0

start_time1_bodyweightsquat = time.time()
start_time2_bodyweightsquat = time.time()
start_time3_bodyweightsquat = time.time()
time_threshold_bodyweightsquat = 3 
within_range_time1_bodyweightsquat = 0
within_range_time2_bodyweightsquat = 0

# gen feedback success
general_feedback_left_bodyweightsquat = ""

# gen feedback unsuccess
dir_gen_feedback_bodyweightsquat = 0
dir_gen_feedback_unsuccessful_bodyweightsquat = 0

cooldown_timer_bodyweightsquat = 0
cooldown_duration_bodyweightsquat = 5
rest_bws_start_time = time.time()

# ----------- END FOR BODY WEIGHT SQUAT ---------------

# ----------- FOR BODY WEIGHT SQUAT SET 2 ---------------

dir_left_bodyweightsquat_set2 = 0
dir_right_bodyweightsquat_set2 = 0

repetition_time_bodyweightsquat_set2 = 60  # Repetition time

# Display info
display_info_bodyweightsquat_set2 = True


per_right_bodyweightsquat_set2 = 0
per_left_bodyweightsquat_set2 = 0
bar_left_bodyweightsquat_set2 = 0
bar_right_bodyweightsquat_set2 = 0 

leftbody_bodyweightsquat_set2 = 0
rightbody_bodyweightsquat_set2 = 0

color_right_bodyweightsquat_set2 = (0, 0, 255)
color_left_bodyweightsquat_set2 = (0, 0, 255)

general_feedback_left_bodyweightsquat_set2 = ""

success_threshold_bodyweightsquat_set2 = 100

peak_value_bodyweightsquat_set2 = 0
atrest_value_bodyweightsquat_set2 = 0

unsuccessful_reps_count_body_bodyweightsquat_set2 = 0
successful_reps_count_body_bodyweightsquat_set2 = 0

dir_left_unsuccessful_bodyweightsquat_set2 = 0

total_reps_count_body_bodyweightsquat_set2 = 0

start_time1_bodyweightsquat_set2 = time.time()
start_time2_bodyweightsquat_set2 = time.time()
start_time3_bodyweightsquat_set2 = time.time()
time_threshold_bodyweightsquat_set2 = 3 
within_range_time1_bodyweightsquat_set2 = 0
within_range_time2_bodyweightsquat_set2 = 0

# gen feedback success
general_feedback_body_bodyweightsquat_set2 = ""

# gen feedback unsuccess
dir_gen_feedback_bodyweightsquat_set2 = 0
dir_gen_feedback_unsuccessful_bodyweightsquat_set2 = 0

cooldown_timer_bodyweightsquat_set2 = 0
cooldown_duration_bodyweightsquat_set2 = 5

rest_bws_start_time_set2 = time.time()

# ----------- END FOR BODY WEIGHT SQUAT SET 2 ---------------

# ----------- FOR BODY WEIGHT SQUAT SET 3 ---------------
dir_left_bodyweightsquat_set3 = 0
dir_right_bodyweightsquat_set3 = 0

repetition_time_bodyweightsquat_set3 = 60  # Repetition time

# Display info
display_info_bodyweightsquat_set3 = True


per_right_bodyweightsquat_set3 = 0
per_left_bodyweightsquat_set3 = 0
bar_left_bodyweightsquat_set3 = 0
bar_right_bodyweightsquat_set3 = 0 

leftbody_bodyweightsquat_set3 = 0
rightbody_bodyweightsquat_set3 = 0

color_right_bodyweightsquat_set3 = (0, 0, 255)
color_left_bodyweightsquat_set3 = (0, 0, 255)

general_feedback_left_bodyweightsquat_set3 = ""

success_threshold_bodyweightsquat_set3 = 100

peak_value_bodyweightsquat_set3 = 0
atrest_value_bodyweightsquat_set3 = 0

unsuccessful_reps_count_body_bodyweightsquat_set3 = 0
successful_reps_count_body_bodyweightsquat_set3 = 0

dir_left_unsuccessful_bodyweightsquat_set3 = 0

total_reps_count_body_bodyweightsquat_set3 = 0

start_time1_bodyweightsquat_set3 = time.time()
start_time2_bodyweightsquat_set3 = time.time()
start_time3_bodyweightsquat_set3 = time.time()
time_threshold_bodyweightsquat_set3 = 3 
within_range_time1_bodyweightsquat_set3 = 0
within_range_time2_bodyweightsquat_set3 = 0

# gen feedback success
general_feedback_body_bodyweightsquat_set3 = ""

# gen feedback unsuccess
dir_gen_feedback_bodyweightsquat_set3 = 0
dir_gen_feedback_unsuccessful_bodyweightsquat_set3 = 0

cooldown_timer_bodyweightsquat_set3 = 0
cooldown_duration_bodyweightsquat_set3 = 5

rest_bws_start_time_set3 = time.time()

# ----------- END FOR BODY WEIGHT SQUAT SET 3 ---------------

# ------------- FOR GOBLET SQUAT ---------------------
detector_gobletsquat = pm_gs.poseDetectorGobletSquat()

dir_left_gobletsquat = 0
dir_right_gobletsquat = 0

repetition_time_gobletsquat = 60  # Repetition time

# Display info
display_info_gobletsquat = True

per_right_gobletsquat = 0
per_left_gobletsquat = 0
bar_left_gobletsquat = 0
bar_right_gobletsquat = 0 


color_right_gobletsquat = (0, 0, 255)
color_left_gobletsquat = (0, 0, 255)

feedback_left_gobletsquat = ""
feedback_right_gobletsquat = ""

success_threshold_gobletsquat = 100

atrest_value_gobletsquat = 0

unsuccessful_reps_count_left_gobletsquat = 0
successful_reps_count_left_gobletsquat = 0

unsuccessful_reps_count_right_gobletsquat = 0
successful_reps_count_right_gobletsquat = 0

dir_left_unsuccessful_gobletsquat = 0
dir_right_unsuccessful_gobletsquat = 0

total_reps_count_gobletsquat = 0

total_reps_count_left_gobletsquat = 0
total_reps_count_right_gobletsquat = 0

start_time1_gobletsquat = time.time()
start_time2_gobletsquat = time.time()
start_time3_gobletsquat = time.time()
time_threshold_gobletsquat = 10 
within_range_time1_gobletsquat = 0
within_range_time2_gobletsquat = 0

# gen feedback success
general_feedback_left_gobletsquat = ""
general_feedback_right_gobletsquat = ""

# gen feedback unsuccess
dir_gen_feedback_gobletsquat = 0
dir_gen_feedback_unsuccessful_gobletsquat = 0

cooldown_timer_gobletsquat = 0
cooldown_duration_gobletsquat = 5

rest_goblet_squat_start_time = time.time()

# ------------- END FOR GOBLET SQUAT -----------------

# ------------- FOR GOBLET SQUAT SET 2 ---------------------
detector_gobletsquat = pm_gs.poseDetectorGobletSquat()

dir_left_gobletsquat_set2 = 0
dir_right_gobletsquat_set2 = 0

repetition_time_gobletsquat_set2 = 60  # Repetition time

# Display info
display_info_gobletsquat_set2 = True

per_right_gobletsquat_set2 = 0
per_left_gobletsquat_set2 = 0
bar_left_gobletsquat_set2 = 0
bar_right_gobletsquat_set2 = 0 


color_right_gobletsquat_set2 = (0, 0, 255)
color_left_gobletsquat_set2 = (0, 0, 255)

feedback_left_gobletsquat_set2 = ""
feedback_right_gobletsquat_set2 = ""

success_threshold_gobletsquat_set2 = 100

atrest_value_gobletsquat_set2 = 0

unsuccessful_reps_count_left_gobletsquat_set2 = 0
successful_reps_count_left_gobletsquat_set2 = 0

unsuccessful_reps_count_right_gobletsquat_set2 = 0
successful_reps_count_right_gobletsquat_set2 = 0

dir_left_unsuccessful_gobletsquat_set2 = 0
dir_right_unsuccessful_gobletsquat_set2 = 0

total_reps_count_gobletsquat_set2 = 0

total_reps_count_left_gobletsquat_set2 = 0
total_reps_count_right_gobletsquat_set2 = 0

start_time1_gobletsquat_set2 = time.time()
start_time2_gobletsquat_set2 = time.time()
start_time3_gobletsquat_set2 = time.time()
time_threshold_gobletsquat_set2 = 10 
within_range_time1_gobletsquat_set2 = 0
within_range_time2_gobletsquat_set2 = 0

# gen feedback success
general_feedback_left_gobletsquat_set2 = ""
general_feedback_right_gobletsquat_set2 = ""

# gen feedback unsuccess
dir_gen_feedback_gobletsquat_set2 = 0
dir_gen_feedback_unsuccessful_gobletsquat_set2 = 0

cooldown_timer_gobletsquat_set2 = 0
cooldown_duration_gobletsquat_set2 = 5
rest_goblet_squat_start_time_set2 = time.time()

# ------------- END FOR GOBLET SQUAT SET 2 -----------------

# ------------- FOR GOBLET SQUAT SET 3---------------------
detector_gobletsquat = pm_gs.poseDetectorGobletSquat()

dir_left_gobletsquat_set3 = 0
dir_right_gobletsquat_set3 = 0

repetition_time_gobletsquat_set3 = 60  # Repetition time

# Display info
display_info_gobletsquat_set3 = True

per_right_gobletsquat_set3 = 0
per_left_gobletsquat_set3 = 0
bar_left_gobletsquat_set3 = 0
bar_right_gobletsquat_set3 = 0 


color_right_gobletsquat_set3 = (0, 0, 255)
color_left_gobletsquat_set3 = (0, 0, 255)

feedback_left_gobletsquat_set3 = ""
feedback_right_gobletsquat_set3 = ""

success_threshold_gobletsquat_set3 = 100

atrest_value_gobletsquat_set3 = 0

unsuccessful_reps_count_left_gobletsquat_set3 = 0
successful_reps_count_left_gobletsquat_set3 = 0

unsuccessful_reps_count_right_gobletsquat_set3 = 0
successful_reps_count_right_gobletsquat_set3 = 0

dir_left_unsuccessful_gobletsquat_set3 = 0
dir_right_unsuccessful_gobletsquat_set3 = 0

total_reps_count_gobletsquat_set3 = 0

total_reps_count_left_gobletsquat_set3 = 0
total_reps_count_right_gobletsquat_set3 = 0

start_time1_gobletsquat_set3 = time.time()
start_time2_gobletsquat_set3 = time.time()
start_time3_gobletsquat_set3 = time.time()
time_threshold_gobletsquat_set3 = 10 
within_range_time1_gobletsquat_set3 = 0
within_range_time2_gobletsquat_set3 = 0

# gen feedback success
general_feedback_left_gobletsquat_set3 = ""
general_feedback_right_gobletsquat_set3 = ""

# gen feedback unsuccess
dir_gen_feedback_gobletsquat_set3 = 0
dir_gen_feedback_unsuccessful_gobletsquat_set3 = 0

cooldown_timer_gobletsquat_set3 = 0
cooldown_duration_gobletsquat_set3 = 5
rest_goblet_squat_start_time_set3 = time.time()

# ------------- END FOR GOBLET SQUAT SET 3-----------------

# ------------- FOR HIGH KNEE TAP --------------------
detector_highkneetap = pm_hkt.poseDetectorHighKneeTap()

dir_left_highkneetap = 0
dir_right_highkneetap = 0

repetition_time_highkneetap = 60  # Repetition time

# Display info
display_info_highkneetap = True

per_right_highkneetap = 0
per_left_highkneetap = 0
bar_left_highkneetap = 0
bar_right_highkneetap = 0 


color_right_highkneetap = (0, 0, 255)
color_left_highkneetap = (0, 0, 255)

feedback_left_highkneetap = ""
feedback_right_highkneetap = ""

success_threshold_highkneetap = 100

atrest_value_highkneetap = 0

unsuccessful_reps_count_left_highkneetap = 0
successful_reps_count_left_highkneetap = 0

unsuccessful_reps_count_right_highkneetap = 0
successful_reps_count_right_highkneetap = 0

dir_left_unsuccessful_highkneetap = 0
dir_right_unsuccessful_highkneetap = 0

total_reps_count_highkneetap = 0

total_reps_count_left_highkneetap = 0
total_reps_count_right_highkneetap = 0

start_time1_highkneetap = time.time()
start_time2_highkneetap = time.time()
start_time3_highkneetap = time.time()
time_threshold_highkneetap = 1 # Specify the time threshold in seconds # can be changed for testing but default should be 1, 0.2 is for testing
within_range_time1_highkneetap = 0
within_range_time2_highkneetap = 0

# gen feedback success
general_feedback_left_highkneetap = ""
general_feedback_right_highkneetap = ""

# gen feedback unsuccess
dir_gen_feedback_highkneetap = 0
dir_gen_feedback_unsuccessful_highkneetap = 0

cooldown_timer_highkneetap = 0
cooldown_duration_highkneetap = 5

leftleg_highkneetap = 0
rightleg_highkneetap = 0
rest_hkt_start_time = time.time()
# ------------- FOR HIGH KNEE TAP --------------------

# ------------- FOR HIGH KNEE TAP SET 2 --------------------

dir_left_highkneetap_set2 = 0
dir_right_highkneetap_set2 = 0

repetition_time_highkneetap_set2 = 60  # Repetition time

# Display info
display_info_highkneetap_set2 = True

per_right_highkneetap_set2 = 0
per_left_highkneetap_set2 = 0
bar_left_highkneetap_set2 = 0
bar_right_highkneetap_set2 = 0 


color_right_highkneetap_set2 = (0, 0, 255)
color_left_highkneetap_set2 = (0, 0, 255)

feedback_left_highkneetap_set2 = ""
feedback_right_highkneetap_set2 = ""

success_threshold_highkneetap_set2 = 100

atrest_value_highkneetap_set2 = 0

unsuccessful_reps_count_left_highkneetap_set2 = 0
successful_reps_count_left_highkneetap_set2 = 0

unsuccessful_reps_count_right_highkneetap_set2 = 0
successful_reps_count_right_highkneetap_set2 = 0

dir_left_unsuccessful_highkneetap_set2 = 0
dir_right_unsuccessful_highkneetap_set2 = 0

total_reps_count_highkneetap_set2 = 0

total_reps_count_left_highkneetap_set2 = 0
total_reps_count_right_highkneetap_set2 = 0

start_time1_highkneetap_set2 = time.time()
start_time2_highkneetap_set2 = time.time()
start_time3_highkneetap_set2 = time.time()
time_threshold_highkneetap_set2 = 1 
within_range_time1_highkneetap_set2 = 0
within_range_time2_highkneetap_set2 = 0

# gen feedback success
general_feedback_left_highkneetap_set2 = ""
general_feedback_right_highkneetap_set2 = ""

# gen feedback unsuccess
dir_gen_feedback_highkneetap_set2 = 0
dir_gen_feedback_unsuccessful_highkneetap_set2 = 0

cooldown_timer_highkneetap_set2 = 0
cooldown_duration_highkneetap_set2 = 5

leftleg_highkneetap_set2 = 0
rightleg_highkneetap_set2 = 0
rest_hkt_start_time_set2 = time.time()
# ------------- FOR HIGH KNEE TAP SET 2 --------------------

# ------------- FOR HIGH KNEE TAP SET 3 --------------------

dir_left_highkneetap_set3 = 0
dir_right_highkneetap_set3 = 0

repetition_time_highkneetap_set3 = 60  # Repetition time

# Display info
display_info_highkneetap_set3 = True

per_right_highkneetap_set3 = 0
per_left_highkneetap_set3 = 0
bar_left_highkneetap_set3 = 0
bar_right_highkneetap_set3 = 0 


color_right_highkneetap_set3 = (0, 0, 255)
color_left_highkneetap_set3 = (0, 0, 255)

feedback_left_highkneetap_set3 = ""
feedback_right_highkneetap_set3 = ""

success_threshold_highkneetap_set3= 100

atrest_value_highkneetap_set3 = 0

unsuccessful_reps_count_left_highkneetap_set3 = 0
successful_reps_count_left_highkneetap_set3 = 0

unsuccessful_reps_count_right_highkneetap_set3 = 0
successful_reps_count_right_highkneetap_set3 = 0

dir_left_unsuccessful_highkneetap_set3 = 0
dir_right_unsuccessful_highkneetap_set3 = 0

total_reps_count_highkneetap_set3 = 0

total_reps_count_left_highkneetap_set3 = 0
total_reps_count_right_highkneetap_set3 = 0

start_time1_highkneetap_set3 = time.time()
start_time2_highkneetap_set3 = time.time()
start_time3_highkneetap_set3 = time.time()
time_threshold_highkneetap_set3 = 1
within_range_time1_highkneetap_set3 = 0
within_range_time2_highkneetap_set3 = 0

# gen feedback success
general_feedback_left_highkneetap_set3 = ""
general_feedback_right_highkneetap_set3 = ""

# gen feedback unsuccess
dir_gen_feedback_highkneetap_set3 = 0
dir_gen_feedback_unsuccessful_highkneetap_set3 = 0

cooldown_timer_highkneetap_set3 = 0
cooldown_duration_highkneetap_set3 = 5

leftleg_highkneetap_set3 = 0
rightleg_highkneetap_set3 = 0
rest_hkt_start_time_set3 = time.time()
# ------------- FOR HIGH KNEE TAP SET 3 --------------------

# ------------- FOR DUMBBELL HIP HINGE ---------------------
detector_dumbbellhiphinge = pm_dhh.poseDetectordumbbellhiphinge()

# Initialize variables
dir_left_dumbbellhiphinge = 0
dir_right_dumbbellhiphinge = 0

repetition_time_dumbbellhiphinge = 60  # Repetition time

# Display info
display_info_dumbbellhiphinge = True


per_right_dumbbellhiphinge = 0
per_left_dumbbellhiphinge = 0
bar_left_dumbbellhiphinge = 0
bar_right_dumbbellhiphinge = 0 


color_right_dumbbellhiphinge = (0, 0, 255)
color_left_dumbbellhiphinge = (0, 0, 255)

feedback_left_dumbbellhiphinge = ""
feedback_right_dumbbellhiphinge = ""

success_threshold_dumbbellhiphinge = 100

atrest_value_dumbbellhiphinge = 0

unsuccessful_reps_count_left_dumbbellhiphinge = 0
successful_reps_count_left_dumbbellhiphinge = 0

unsuccessful_reps_count_right_dumbbellhiphinge = 0
successful_reps_count_right_dumbbellhiphinge = 0

dir_left_unsuccessful_dumbbellhiphinge = 0
dir_right_unsuccessful_dumbbellhiphinge = 0

total_reps_count_dumbbellhiphinge = 0

total_reps_count_left_dumbbellhiphinge = 0
total_reps_count_right_dumbbellhiphinge = 0

start_time1_dumbbellhiphinge = time.time()
start_time2_dumbbellhiphinge = time.time()
start_time3_dumbbellhiphinge = time.time()
time_threshold_dumbbellhiphinge = 10 
within_range_time1_dumbbellhiphinge = 0
within_range_time2_dumbbellhiphinge = 0

# gen feedback success
general_feedback_left_dumbbellhiphinge = ""
general_feedback_right_dumbbellhiphinge = ""

# gen feedback unsuccess
dir_gen_feedback_dumbbellhiphinge = 0
dir_gen_feedback_unsuccessful_dumbbellhiphinge = 0

cooldown_timer_dumbbellhiphinge = 0
cooldown_duration_dumbbellhiphinge = 5

leftbody_dumbbellhiphinge = 0
rightbody_dumbbellhiphinge = 0
rest_dhh_start_time = time.time()
# ------------- END FOR DUMBBELL HIP HINGE ---------------------

# ------------- FOR DUMBBELL HIP HINGE SET 2---------------------

dir_left_dumbbellhiphinge_set2 = 0
dir_right_dumbbellhiphinge_set2 = 0

repetition_time_dumbbellhiphinge_set2 = 60  # Repetition time

# Display info
display_info_dumbbellhiphinge_set2 = True


per_right_dumbbellhiphinge_set2 = 0
per_left_dumbbellhiphinge_set2 = 0
bar_left_dumbbellhiphinge_set2 = 0
bar_right_dumbbellhiphinge_set2 = 0 


color_right_dumbbellhiphinge_set2 = (0, 0, 255)
color_left_dumbbellhiphinge_set2 = (0, 0, 255)

feedback_left_dumbbellhiphinge_set2 = ""
feedback_right_dumbbellhiphinge_set2 = ""

success_threshold_dumbbellhiphinge_set2 = 100

atrest_value_dumbbellhiphinge_set2 = 0

unsuccessful_reps_count_left_dumbbellhiphinge_set2 = 0
successful_reps_count_left_dumbbellhiphinge_set2 = 0

unsuccessful_reps_count_right_dumbbellhiphinge_set2 = 0
successful_reps_count_right_dumbbellhiphinge_set2 = 0

dir_left_unsuccessful_dumbbellhiphinge_set2 = 0
dir_right_unsuccessful_dumbbellhiphinge_set2 = 0

total_reps_count_dumbbellhiphinge_set2 = 0

total_reps_count_left_dumbbellhiphinge_set2 = 0
total_reps_count_right_dumbbellhiphinge_set2 = 0

start_time1_dumbbellhiphinge_set2 = time.time()
start_time2_dumbbellhiphinge_set2 = time.time()
start_time3_dumbbellhiphinge_set2 = time.time()
time_threshold_dumbbellhiphinge_set2 = 10 
within_range_time1_dumbbellhiphinge_set2 = 0
within_range_time2_dumbbellhiphinge_set2 = 0

# gen feedback success
general_feedback_left_dumbbellhiphinge_set2 = ""
general_feedback_right_dumbbellhiphinge_set2 = ""

# gen feedback unsuccess
dir_gen_feedback_dumbbellhiphinge_set2 = 0
dir_gen_feedback_unsuccessful_dumbbellhiphinge_set2 = 0

cooldown_timer_dumbbellhiphinge_set2 = 0
cooldown_duration_dumbbellhiphinge_set2 = 5

leftbody_dumbbellhiphinge_set2 = 0
rightbody_dumbbellhiphinge_set2 = 0
rest_dhh_start_time_set2 = time.time()
# ------------- END FOR DUMBBELL HIP HINGE SET 2 ---------------------

# ------------- FOR DUMBBELL HIP HINGE SET 3 ---------------------

dir_left_dumbbellhiphinge_set3 = 0
dir_right_dumbbellhiphinge_set3 = 0

repetition_time_dumbbellhiphinge_set3 = 60  # Repetition time

# Display info
display_info_dumbbellhiphinge_set3 = True


per_right_dumbbellhiphinge_set3 = 0
per_left_dumbbellhiphinge_set3 = 0
bar_left_dumbbellhiphinge_set3 = 0
bar_right_dumbbellhiphinge_set3 = 0 


color_right_dumbbellhiphinge_set3 = (0, 0, 255)
color_left_dumbbellhiphinge_set3 = (0, 0, 255)

feedback_left_dumbbellhiphinge_set3 = ""
feedback_right_dumbbellhiphinge_set3 = ""

success_threshold_dumbbellhiphinge_set3 = 100

atrest_value_dumbbellhiphinge_set3 = 0

unsuccessful_reps_count_left_dumbbellhiphinge_set3 = 0
successful_reps_count_left_dumbbellhiphinge_set3 = 0

unsuccessful_reps_count_right_dumbbellhiphinge_set3 = 0
successful_reps_count_right_dumbbellhiphinge_set3 = 0

dir_left_unsuccessful_dumbbellhiphinge = 0
dir_right_unsuccessful_dumbbellhiphinge_set3 = 0

total_reps_count_dumbbellhiphinge_set3 = 0

total_reps_count_left_dumbbellhiphinge_set3 = 0
total_reps_count_right_dumbbellhiphinge_set3 = 0

start_time1_dumbbellhiphinge_set3 = time.time()
start_time2_dumbbellhiphinge_set3 = time.time()
start_time3_dumbbellhiphinge_set3 = time.time()
time_threshold_dumbbellhiphinge_set3 = 10
within_range_time1_dumbbellhiphinge_set3 = 0
within_range_time2_dumbbellhiphinge_set3 = 0

# gen feedback success
general_feedback_left_dumbbellhiphinge_set3 = ""
general_feedback_right_dumbbellhiphinge_set3 = ""

# gen feedback unsuccess
dir_gen_feedback_dumbbellhiphinge_set3 = 0
dir_gen_feedback_unsuccessful_dumbbellhiphinge_set3 = 0

cooldown_timer_dumbbellhiphinge_set3 = 0
cooldown_duration_dumbbellhiphinge_set3 = 5

leftbody_dumbbellhiphinge_set3 = 0
rightbody_dumbbellhiphinge_set3 = 0
rest_dhh_start_time_set3 = time.time()
# ------------- END FOR DUMBBELL HIP HINGE SET 3 ---------------------


@muscleGain.route('/muscleGain')
@muscleGain.route('/')
def home():
    #username = session.get('username')
    if 'username' in session and session['exercise'] == "muscle_gain":
        bicep_curl = session.get('bicep_curl')
        push_up = session.get('push_up')
        shoulder_tap = session.get('shoulder_tap')
        dumbbell_frontraise = session.get('dumbbell_frontraise')
        chest_press = session.get('chest_press')
        alternatingleglunges = session.get('alternatingleglunges')
        bodyweightsquat = session.get('bodyweightsquat')
        dumbbellhiphinge = session.get('dumbbellhiphinge')
        gobletsquat = session.get('gobletsquat')
        highkneetap = session.get('highkneetap')

        return render_template('gainingMuscle.html', bicep_curl = bicep_curl, push_up = push_up, shoulder_tap = shoulder_tap, dumbbell_frontraise = dumbbell_frontraise, chest_press = chest_press, alternatingleglunges = alternatingleglunges, bodyweightsquat = bodyweightsquat, dumbbellhiphinge = dumbbellhiphinge, gobletsquat = gobletsquat, highkneetap = highkneetap)
    else:
        return render_template('home.html')
    
exercise_mode = "push_up"


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
            if exercise_mode == "rest_shouldertap_set2":
                img_with_faces = rest_shouldertap_set2(img)
            if exercise_mode == "shoulder_tap_set3":
                img_with_faces = detect_shouldertap_set3(img)
            if exercise_mode == "rest_shouldertap_set3":
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

            ret, buffer = cv2.imencode('.jpg', img_with_faces)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@muscleGain.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@muscleGain.route('/start_timer', methods=['POST'])
def start_timer():
    global start_time_bicep, countdown_before_exercise
    countdown_before_exercise = time.time()
    start_time_bicep = time.time()  # Start the timer
    return jsonify({'message': 'Timer started'}), 200

@muscleGain.route('/exercise_mode')
def get_exercise_mode():
    global exercise_mode
    return jsonify({'exercise_mode': exercise_mode})


def detect_bicep_curls(img):
    global countdown_before_exercise, countdown_repetition_time, count_bicep_left, count_bicep_right, dir_bicep_left, dir_bicep_right, start_time_bicep, repetition_time_bicep, display_info_bicep, rest_bicep_start_time, bar_left_bicep, bar_right_bicep, angle_left_bicep, angle_right_bicep, color_right_bicep, color_left_bicep, feedback_left_bicep, feedback_right_bicep, min_threshold_bicep, max_threshold_bicep, success_threshold_bicep, peak_value_bicep, atrest_value_bicep, reps_count_bicep, unsuccessful_reps_count_left_bicep, successful_reps_count_left_bicep, unsuccessful_reps_count_right_bicep, successful_reps_count_right_bicep, dir_bicep_left_unsuccessful_bicep, dir_bicep_right_unsuccessful_bicep, total_reps_count_bicep, total_reps_count_left_bicep, total_reps_count_right_bicep, start_time1_bicep, start_time2_bicep, general_feedback_left_bicep, general_feedback_right_bicep, dir_gen_feedback_bicep, dir_gen_feedback_unsuccessful_bicep, exercise_mode, per_left_bicep, per_right_bicep, within_range_time1_bicep, within_range_time2_bicep, start_time3_bicep

    img = cv2.resize(img, (1280, 720))


    countdown_elapsed_time = time.time() - countdown_before_exercise
    countdown_remaining_time = max(0, 10 - countdown_elapsed_time)
    if countdown_remaining_time <= 0:
        display_info_bicep = True

    # Timer - starts timer based on set duration
    elapsed_time_bicep = time.time() - start_time_bicep
    remaining_time_bicep = max(0, 70 - elapsed_time_bicep) #repetition_time

    # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Starting: {int(countdown_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if display_info_bicep:  # Check if to display counter, bar, and percentage
        img = detector_bicep.findPose(img, False) # initializes img as variable for findpose function
        lmList_bicep = detector_bicep.findPosition(img, False) # initializes lmList_bicep as variable for findPosition function

        # Define hand angles outside the if statement
        if len(lmList_bicep) != 0:

            angle_left_bicep = detector_bicep.BicepCurl(img, 11 ,13, 15, True)
            angle_right_bicep = detector_bicep.BicepCurl(img, 12, 14 ,16, True)

            per_left_bicep = np.interp(angle_left_bicep, (30, 130), (100, 0)) 
            bar_left_bicep = np.interp(angle_left_bicep, (30, 140), (200, 400)) 

            per_right_bicep = np.interp(angle_right_bicep, (200, 340), (0, 100)) 
            bar_right_bicep = np.interp(angle_right_bicep, (200, 340), (400, 200)) 

            # color changer for the bar
            if int(per_left_bicep) == 100:
                color_left_bicep = (0, 255, 0)  # Change color of left leg bar to green
            elif int(per_right_bicep) == 100:
                color_right_bicep = (0, 255, 0)
            else:
                color_left_bicep = (0, 0, 255)  # Keep color of left leg bar as red
                color_right_bicep = (0, 0, 255)

            #left
            if 40 <= per_left_bicep <= 90:
                # Increment the time within range
                within_range_time1_bicep += time.time() - start_time2_bicep

                # Check if peak value has been within range for the specified time
                if within_range_time1_bicep >= time_threshold_bicep:
                    if dir_bicep_left_unsuccessful_bicep == 0:
                        unsuccessful_reps_count_left_bicep += 0.5
                        dir_bicep_left_unsuccessful_bicep = 1

            else:
                within_range_time1_bicep = 0
                # Update the start time to the current time
                start_time2_bicep = time.time()

            if 1 <= per_left_bicep <= 10:
                if dir_bicep_left_unsuccessful_bicep == 1:
                    unsuccessful_reps_count_left_bicep += 0.5
                    dir_bicep_left_unsuccessful_bicep = 0

            if per_left_bicep == success_threshold_bicep:
                if dir_bicep_left == 0:
                    successful_reps_count_left_bicep += 0.5
                    dir_bicep_left = 1
                
            elif per_left_bicep == atrest_value_bicep:
                if dir_bicep_left == 1:
                    successful_reps_count_left_bicep += 0.5
                    dir_bicep_left = 0

            # right
            if 40 <= per_right_bicep <= 90:
                # Increment the time within range
                within_range_time2_bicep += time.time() - start_time3_bicep

                # Check if peak value has been within range for the specified time
                if within_range_time2_bicep >= time_threshold_bicep:
                    if dir_bicep_right_unsuccessful_bicep == 0:
                        unsuccessful_reps_count_right_bicep += 0.5
                        dir_bicep_right_unsuccessful_bicep = 1
                        print("right", unsuccessful_reps_count_right_bicep)

            else:
                within_range_time2_bicep = 0
                # Update the start time to the current time
                start_time3_bicep = time.time()

            if 1 <= per_right_bicep <= 10:
                #print("left down val: ", per_left)
                if dir_bicep_right_unsuccessful_bicep == 1:
                    unsuccessful_reps_count_right_bicep += 0.5
                    dir_bicep_right_unsuccessful_bicep = 0
                    print("right", unsuccessful_reps_count_right_bicep)

            if per_right_bicep == success_threshold_bicep:
                if dir_bicep_right == 0:
                    successful_reps_count_right_bicep += 0.5
                    dir_bicep_right = 1
                
            elif per_right_bicep == atrest_value_bicep:
                if dir_bicep_right == 1:
                    successful_reps_count_right_bicep += 0.5
                    dir_bicep_right = 0

            # feedback for left hand  # TO BE FETCHED 
            feedback_left_bicep = detector_bicep.feedback_bicep(per_left_bicep)

            detector_bicep.update_next_per_left(per_left_bicep)

            # feedback for right hand  # TO BE FETCHED 
            feedback_right_bicep = detector_bicep.feedback_bicep(per_right_bicep)

            detector_bicep.update_next_per_left(per_right_bicep)

        # label
        cvzone.putTextRect(img, 'Front Facing Bicep Curl', [440, 30], thickness=2, border=2, scale=1.5) 

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time_bicep)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # bar
        cv2.putText(img, f"R {int(per_right_bicep)}%" , (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (255, 255, 255), 5)
        cv2.rectangle(img, (8, int(bar_right_bicep)), (50, 400), color_right_bicep, -1)

        cv2.putText(img, f"L {int(per_left_bicep)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (255, 255, 255), 5)
        cv2.rectangle(img, (952, int(bar_left_bicep)), (995, 400), color_left_bicep, -1)

    #counter in display
    cv2.rectangle(img, (20, 20), (200, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(successful_reps_count_right_bicep)}/10", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (210, 20), (390, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(successful_reps_count_left_bicep)}/10", (220, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    # To check if time is still running
    if remaining_time_bicep <= 0:
        cvzone.putTextRect(img, "Time's Up", [420, 30], thickness=2, border=2, scale=2.5)
        display_info_bicep = False
        exercise_mode = "rest_bicep"
        rest_bicep_start_time = time.time()

    #total counts
    total_reps_count_left = successful_reps_count_left_bicep + unsuccessful_reps_count_left_bicep
    total_reps_count_right = successful_reps_count_right_bicep + unsuccessful_reps_count_right_bicep  


    if successful_reps_count_right_bicep >= 10 and successful_reps_count_left_bicep >= 10:
        cvzone.putTextRect(img, 'All Repetitions Completed', [420, 30], thickness=2, border=2, scale=2.5)
        display_info_bicep = False
        # General feedback after finishing the exercise # TO BE FETCHED
        if dir_gen_feedback_bicep == 0:
            general_feedback_left_bicep = detector_bicep.left_arm_feedback(total_reps_count_left)
            general_feedback_right_bicep = detector_bicep.right_arm_feedback(total_reps_count_right)
            dir_gen_feedback_bicep = 1
            print(f"{general_feedback_right_bicep} \n{general_feedback_left_bicep}")
            exercise_mode = "rest_bicep"
            rest_bicep_start_time = time.time()
        
    # To check for unsuccessful arm rep counter # CHANGED
    if unsuccessful_reps_count_left_bicep == 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for left arm. Please retry again', [420, 30], thickness=2, border=2, scale=1)
        display_info_bicep = False

        if dir_gen_feedback_unsuccessful_bicep == 0:
            general_feedback_left_bicep = detector_bicep.left_arm_unsuccessful_feedback(total_reps_count_left)
            dir_gen_feedback_unsuccessful_bicep = 1
            exercise_mode = "rest_bicep"
            rest_bicep_start_time = time.time()

    if unsuccessful_reps_count_right_bicep == 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for right arm. Please retry again', [420, 30], thickness=2, border=2, scale=1)
        display_info_bicep = False

        if dir_gen_feedback_unsuccessful_bicep == 0:
            general_feedback_right_bicep = detector_bicep.right_arm_unsuccessful_feedback(total_reps_count_right)
            dir_gen_feedback_unsuccessful_bicep == 1
            exercise_mode = "rest_bicep"
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
    global count_bicep_left_set2, count_bicep_right_set2, dir_bicep_left_set2, dir_bicep_right_set2, start_time_bicep_set2, display_info_bicep_set2, rest_bicep_start_time_set2, bar_left_bicep_set2, bar_right_bicep_set2, angle_left_bicep_set2, angle_right_bicep_set2, color_right_bicep_set2, color_left_bicep_set2, feedback_left_bicep_set2, feedback_right_bicep_set2, min_threshold_bicep_set2, max_threshold_bicep_set2, success_threshold_bicep_set2, peak_value_bicep_set2, atrest_value_bicep_set2, reps_count_bicep_set2, unsuccessful_reps_count_left_bicep_set2, successful_reps_count_left_bicep_set2, unsuccessful_reps_count_right_bicep_set2, successful_reps_count_right_bicep_set2, dir_bicep_left_unsuccessful_bicep_set2, dir_bicep_right_unsuccessful_bicep_set2, total_reps_count_bicep_set2, total_reps_count_left_bicep_set2, total_reps_count_right_bicep_set2, start_time1_bicep_set2, start_time2_bicep_set2, general_feedback_left_bicep_set2, general_feedback_right_bicep_set2, dir_gen_feedback_bicep_set2, dir_gen_feedback_unsuccessful_bicep_set2, exercise_mode, per_left_bicep_set2, per_right_bicep_set2, within_range_time1_bicep_set2, within_range_time2_bicep_set2, start_time3_bicep_set2

    img = cv2.resize(img, (1280, 720))

    elapsed_time_bicep = time.time() - start_time_bicep_set2
    remaining_time_bicep = max(0, 60 - elapsed_time_bicep) #repetition_time_bicep_set2


    if display_info_bicep_set2:  # Check if to display counter, bar, and percentage
        img = detector_bicep.findPose(img, False) # initializes img as variable for findpose function
        lmList_bicep = detector_bicep.findPosition(img, False) # initializes lmList_bicep as variable for findPosition function

        # Define hand angles outside the if statement
        if len(lmList_bicep) != 0:

            angle_left_bicep_set2 = detector_bicep.BicepCurl(img, 11 ,13, 15, True)
            angle_right_bicep_set2 = detector_bicep.BicepCurl(img, 12, 14 ,16, True)

            per_left_bicep_set2 = np.interp(angle_left_bicep_set2, (30, 130), (100, 0)) 
            bar_left_bicep_set2 = np.interp(angle_left_bicep_set2, (30, 140), (200, 400)) 

            per_right_bicep_set2 = np.interp(angle_right_bicep_set2, (200, 340), (0, 100)) 
            bar_right_bicep_set2 = np.interp(angle_right_bicep_set2, (200, 340), (400, 200)) 

            # color changer for the bar
            if int(per_left_bicep_set2) == 100:
                color_left_bicep_set2 = (0, 255, 0)  # Change color of left leg bar to green
            elif int(per_right_bicep_set2) == 100:
                color_right_bicep_set2 = (0, 255, 0)
            else:
                color_left_bicep_set2 = (0, 0, 255)  # Keep color of left leg bar as red
                color_right_bicep_set2 = (0, 0, 255)

            #left
            if 40 <= per_left_bicep_set2 <= 90:
                # Increment the time within range
                within_range_time1_bicep_set2 += time.time() - start_time2_bicep_set2

                # Check if peak value has been within range for the specified time
                if within_range_time1_bicep_set2 >= time_threshold_bicep_set2:
                    if dir_bicep_left_unsuccessful_bicep_set2 == 0:
                        unsuccessful_reps_count_left_bicep_set2 += 0.5
                        dir_bicep_left_unsuccessful_bicep_set2 = 1

            else:
                within_range_time1_bicep_set2 = 0
                # Update the start time to the current time
                start_time2_bicep_set2 = time.time()

            if 1 <= per_left_bicep_set2 <= 10:
                if dir_bicep_left_unsuccessful_bicep_set2 == 1:
                    unsuccessful_reps_count_left_bicep_set2 += 0.5
                    dir_bicep_left_unsuccessful_bicep_set2 = 0

            if per_left_bicep_set2 == success_threshold_bicep_set2:
                if dir_bicep_left_set2 == 0:
                    successful_reps_count_left_bicep_set2 += 0.5
                    dir_bicep_left_set2 = 1
                
            elif per_left_bicep_set2 == atrest_value_bicep_set2:
                if dir_bicep_left_set2 == 1:
                    successful_reps_count_left_bicep_set2 += 0.5
                    dir_bicep_left_set2 = 0

            # right
            if 40 <= per_right_bicep_set2 <= 90:
                # Increment the time within range
                within_range_time2_bicep_set2 += time.time() - start_time3_bicep_set2

                # Check if peak value has been within range for the specified time
                if within_range_time2_bicep_set2 >= time_threshold_bicep_set2:
                    if dir_bicep_right_unsuccessful_bicep_set2 == 0:
                        unsuccessful_reps_count_right_bicep_set2 += 0.5
                        dir_bicep_right_unsuccessful_bicep_set2 = 1
                        print("right", unsuccessful_reps_count_right_bicep_set2)

            else:
                within_range_time2_bicep_set2 = 0
                # Update the start time to the current time
                start_time3_bicep_set2 = time.time()

            if 1 <= per_right_bicep_set2 <= 10:
                #print("left down val: ", per_left)
                if dir_bicep_right_unsuccessful_bicep_set2 == 1:
                    unsuccessful_reps_count_right_bicep_set2 += 0.5
                    dir_bicep_right_unsuccessful_bicep_set2 = 0
                    print("right", unsuccessful_reps_count_right_bicep_set2)

            if per_right_bicep_set2 == success_threshold_bicep_set2:
                if dir_bicep_right_set2 == 0:
                    successful_reps_count_right_bicep_set2 += 0.5
                    dir_bicep_right_set2 = 1
                
            elif per_right_bicep_set2 == atrest_value_bicep_set2:
                if dir_bicep_right_set2 == 1:
                    successful_reps_count_right_bicep_set2 += 0.5
                    dir_bicep_right_set2 = 0

            # feedback for left hand  # TO BE FETCHED 
            feedback_left_bicep_set2 = detector_bicep.feedback_bicep(per_left_bicep_set2)

            detector_bicep.update_next_per_left(per_left_bicep_set2)

            # feedback for right hand  # TO BE FETCHED 
            feedback_right_bicep_set2 = detector_bicep.feedback_bicep(per_right_bicep_set2)

            detector_bicep.update_next_per_left(per_right_bicep_set2)

        # label
        cvzone.putTextRect(img, 'Front Facing Bicep Curl SET 2', [440, 30], thickness=2, border=2, scale=1.5) 

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time_bicep)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # bar
        cv2.putText(img, f"R {int(per_right_bicep_set2)}%" , (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (255, 255, 255), 5)
        cv2.rectangle(img, (8, int(bar_right_bicep_set2)), (50, 400), color_right_bicep_set2, -1)

        cv2.putText(img, f"L {int(per_left_bicep_set2)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (255, 255, 255), 5)
        cv2.rectangle(img, (952, int(bar_left_bicep_set2)), (995, 400), color_left_bicep_set2, -1)

    #counter in display
    cv2.rectangle(img, (20, 20), (200, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(successful_reps_count_right_bicep_set2)}/10", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (210, 20), (390, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(successful_reps_count_left_bicep_set2)}/10", (220, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    # To check if time is still running
    if remaining_time_bicep <= 0:
        cvzone.putTextRect(img, "Time's Up", [420, 30], thickness=2, border=2, scale=2.5)
        display_info_bicep_set2 = False
        exercise_mode = "rest_bicep_set2"
        rest_bicep_start_time_set2 = time.time()

    #total counts
    total_reps_count_left_set2 = successful_reps_count_left_bicep_set2 + unsuccessful_reps_count_left_bicep_set2
    total_reps_count_right_set2 = successful_reps_count_right_bicep_set2 + unsuccessful_reps_count_right_bicep_set2  


    if successful_reps_count_right_bicep_set2 >= 10 and successful_reps_count_left_bicep_set2 >= 10:
        cvzone.putTextRect(img, 'All Repetitions Completed', [420, 30], thickness=2, border=2, scale=2.5)
        display_info_bicep_set2 = False
        # General feedback after finishing the exercise # TO BE FETCHED
        if dir_gen_feedback_bicep_set2 == 0:
            general_feedback_left_bicep_set2 = detector_bicep.left_arm_feedback(total_reps_count_left_set2)
            general_feedback_right_bicep_set2 = detector_bicep.right_arm_feedback(total_reps_count_right_set2)
            dir_gen_feedback_bicep_set2 = 1
            exercise_mode = "rest_bicep_set2"
            rest_bicep_start_time_set2 = time.time()
    # To check for unsuccessful arm rep counter # CHANGED
    if unsuccessful_reps_count_left_bicep_set2 == 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for left arm. Please retry again', [420, 30], thickness=2, border=2, scale=1)
        display_info_bicep_set2 = False

        if dir_gen_feedback_unsuccessful_bicep_set2 == 0:
            general_feedback_left_bicep_set2 = detector_bicep.left_arm_unsuccessful_feedback(total_reps_count_left_set2)
            dir_gen_feedback_unsuccessful_bicep_set2 = 1
            exercise_mode = "rest_bicep_set2"
            rest_bicep_start_time_set2 = time.time()

    if unsuccessful_reps_count_right_bicep_set2 == 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for right arm. Please retry again', [420, 30], thickness=2, border=2, scale=1)
        display_info_bicep_set2 = False

        if dir_gen_feedback_unsuccessful_bicep_set2 == 0:
            general_feedback_right_bicep_set2 = detector_bicep.right_arm_unsuccessful_feedback(total_reps_count_right_set2)
            dir_gen_feedback_unsuccessful_bicep_set2 == 1
            exercise_mode = "rest_bicep_set2"
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
    global count_bicep_left_set3, count_bicep_right_set3, dir_bicep_left_set3, dir_bicep_right_set3, start_time_bicep_set3, display_info_bicep_set3, rest_bicep_start_time_set3, bar_left_bicep_set3, bar_right_bicep_set3, angle_left_bicep_set3, angle_right_bicep_set3, color_right_bicep_set3, color_left_bicep_set3, feedback_left_bicep_set3, feedback_right_bicep_set3, min_threshold_bicep_set3, max_threshold_bicep_set3, success_threshold_bicep_set3, peak_value_bicep_set3, atrest_value_bicep_set3, reps_count_bicep_set3, unsuccessful_reps_count_left_bicep_set3, successful_reps_count_left_bicep_set3, unsuccessful_reps_count_right_bicep_set3, successful_reps_count_right_bicep_set3, dir_bicep_left_unsuccessful_bicep_set3, dir_bicep_right_unsuccessful_bicep_set3, total_reps_count_bicep_set3, total_reps_count_left_bicep_set3, total_reps_count_right_bicep_set3, start_time1_bicep_set3, start_time2_bicep_set3, general_feedback_left_bicep_set3, general_feedback_right_bicep_set3, dir_gen_feedback_bicep_set3, dir_gen_feedback_unsuccessful_bicep_set3, exercise_mode, per_left_bicep_set3, per_right_bicep_set3, within_range_time1_bicep_set3, within_range_time2_bicep_set3, start_time3_bicep_set3

    img = cv2.resize(img, (1280, 720))

    elapsed_time = time.time() - start_time_bicep_set3
    remaining_time_bicep = max(0, 60 - elapsed_time) #repetition_time_bicep_set2

    if display_info_bicep_set3:  # Check if to display counter, bar, and percentage
        img = detector_bicep.findPose(img, False) # initializes img as variable for findpose function
        lmList_bicep = detector_bicep.findPosition(img, False) # initializes lmList_bicep as variable for findPosition function

        # Define hand angles outside the if statement
        if len(lmList_bicep) != 0:

            angle_left_bicep_set3 = detector_bicep.BicepCurl(img, 11 ,13, 15, True)
            angle_right_bicep_set3 = detector_bicep.BicepCurl(img, 12, 14 ,16, True)

            per_left_bicep_set3 = np.interp(angle_left_bicep_set3, (30, 130), (100, 0)) 
            bar_left_bicep_set3 = np.interp(angle_left_bicep_set3, (30, 140), (200, 400)) 

            per_right_bicep_set3 = np.interp(angle_right_bicep_set3, (200, 340), (0, 100)) 
            bar_right_bicep_set3 = np.interp(angle_right_bicep_set3, (200, 340), (400, 200)) 

            # color changer for the bar
            if int(per_left_bicep_set3) == 100:
                color_left_bicep_set3 = (0, 255, 0)  # Change color of left leg bar to green
            elif int(per_right_bicep_set3) == 100:
                color_right_bicep_set3 = (0, 255, 0)
            else:
                color_left_bicep_set3 = (0, 0, 255)  # Keep color of left leg bar as red
                color_right_bicep_set3 = (0, 0, 255)

            #left
            if 40 <= per_left_bicep_set3 <= 90:
                # Increment the time within range
                within_range_time1_bicep_set3 += time.time() - start_time2_bicep

                # Check if peak value has been within range for the specified time
                if within_range_time1_bicep_set3 >= time_threshold_bicep_set3:
                    if dir_bicep_left_unsuccessful_bicep_set3 == 0:
                        unsuccessful_reps_count_left_bicep_set3 += 0.5
                        dir_bicep_left_unsuccessful_bicep_set3 = 1

            else:
                within_range_time1_bicep_set3 = 0
                # Update the start time to the current time
                start_time2_bicep_set3 = time.time()

            if 1 <= per_left_bicep_set3 <= 10:
                if dir_bicep_left_unsuccessful_bicep_set3 == 1:
                    unsuccessful_reps_count_left_bicep_set3 += 0.5
                    dir_bicep_left_unsuccessful_bicep_set3 = 0

            if per_left_bicep_set3 == success_threshold_bicep_set3:
                if dir_bicep_left_set3 == 0:
                    successful_reps_count_left_bicep_set3 += 0.5
                    dir_bicep_left_set3 = 1
                
            elif per_left_bicep_set3 == atrest_value_bicep_set3:
                if dir_bicep_left_set3 == 1:
                    successful_reps_count_left_bicep_set3 += 0.5
                    dir_bicep_left_set3 = 0

            # right
            if 40 <= per_right_bicep_set3 <= 90:
                # Increment the time within range
                within_range_time2_bicep_set3 += time.time() - start_time3_bicep_set3

                # Check if peak value has been within range for the specified time
                if within_range_time2_bicep_set3 >= time_threshold_bicep_set3:
                    if dir_bicep_right_unsuccessful_bicep_set3 == 0:
                        unsuccessful_reps_count_right_bicep_set3 += 0.5
                        dir_bicep_right_unsuccessful_bicep_set3 = 1
                        print("right", unsuccessful_reps_count_right_bicep_set3)

            else:
                within_range_time2_bicep_set3 = 0
                # Update the start time to the current time
                start_time3_bicep_set3 = time.time()

            if 1 <= per_right_bicep_set3 <= 10:
                #print("left down val: ", per_left)
                if dir_bicep_right_unsuccessful_bicep_set3 == 1:
                    unsuccessful_reps_count_right_bicep_set3 += 0.5
                    dir_bicep_right_unsuccessful_bicep_set3 = 0
                    print("right", unsuccessful_reps_count_right_bicep_set3)

            if per_right_bicep_set3 == success_threshold_bicep_set3:
                if dir_bicep_right_set3 == 0:
                    successful_reps_count_right_bicep_set3 += 0.5
                    dir_bicep_right_set3 = 1
                
            elif per_right_bicep_set3 == atrest_value_bicep_set3:
                if dir_bicep_right_set3 == 1:
                    successful_reps_count_right_bicep_set3 += 0.5
                    dir_bicep_right_set3 = 0

            # feedback for left hand  # TO BE FETCHED 
            feedback_left_bicep_set3 = detector_bicep.feedback_bicep(per_left_bicep_set3)

            detector_bicep.update_next_per_left(per_left_bicep_set3)

            # feedback for right hand  # TO BE FETCHED 
            feedback_right_bicep_set3 = detector_bicep.feedback_bicep(per_right_bicep_set3)

            detector_bicep.update_next_per_left(per_right_bicep_set3)

        # label
        cvzone.putTextRect(img, 'Front Facing Bicep Curl SET 3', [440, 30], thickness=2, border=2, scale=1.5) 

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time_bicep)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # bar
        cv2.putText(img, f"R {int(per_right_bicep_set3)}%" , (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (255, 255, 255), 5)
        cv2.rectangle(img, (8, int(bar_right_bicep_set3)), (50, 400), color_right_bicep_set3, -1)

        cv2.putText(img, f"L {int(per_left_bicep_set3)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (255, 255, 255), 5)
        cv2.rectangle(img, (952, int(bar_left_bicep_set3)), (995, 400), color_left_bicep_set3, -1)

    #counter in display
    cv2.rectangle(img, (20, 20), (200, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(successful_reps_count_right_bicep_set3)}/10", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (210, 20), (390, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(successful_reps_count_left_bicep_set3)}/10", (220, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    # To check if time is still running
    if remaining_time_bicep <= 0:
        cvzone.putTextRect(img, "Time's Up", [420, 30], thickness=2, border=2, scale=2.5)
        display_info_bicep_set3 = False
        exercise_mode = "rest_bicep_set3"
        rest_bicep_start_time_set3 = time.time()

    #total counts
    total_reps_count_left_set3 = successful_reps_count_left_bicep_set3 + unsuccessful_reps_count_left_bicep_set3
    total_reps_count_right_set3 = successful_reps_count_right_bicep_set3 + unsuccessful_reps_count_right_bicep_set3  


    if successful_reps_count_right_bicep_set3 >= 10 and successful_reps_count_left_bicep_set3 >= 10:
        cvzone.putTextRect(img, 'All Repetitions Completed', [420, 30], thickness=2, border=2, scale=2.5)
        display_info_bicep_set3 = False
        # General feedback after finishing the exercise # TO BE FETCHED
        if dir_gen_feedback_bicep_set3 == 0:
            general_feedback_left_bicep_set3 = detector_bicep.left_arm_feedback(total_reps_count_left_set3)
            general_feedback_right_bicep_set3 = detector_bicep.right_arm_feedback(total_reps_count_right_set3)
            dir_gen_feedback_bicep_set3 = 1
            exercise_mode = "rest_bicep_set3"
            rest_bicep_start_time_set3 = time.time()
        
    # To check for unsuccessful arm rep counter # CHANGED
    if unsuccessful_reps_count_left_bicep_set3 == 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for left arm. Please retry again', [420, 30], thickness=2, border=2, scale=1)
        display_info_bicep_set3 = False

        if dir_gen_feedback_unsuccessful_bicep_set3 == 0:
            general_feedback_left_bicep_set3 = detector_bicep.left_arm_unsuccessful_feedback(total_reps_count_left_set3)
            dir_gen_feedback_unsuccessful_bicep_set3 = 1
            exercise_mode = "rest_bicep_set3"
            rest_bicep_start_time_set3 = time.time()

    if unsuccessful_reps_count_right_bicep_set3 == 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for right arm. Please retry again', [420, 30], thickness=2, border=2, scale=1)
        display_info_bicep_set3 = False

        if dir_gen_feedback_unsuccessful_bicep_set3 == 0:
            general_feedback_right_bicep_set3 = detector_bicep.right_arm_unsuccessful_feedback(total_reps_count_right_set3)
            dir_gen_feedback_unsuccessful_bicep_set3 == 1
            exercise_mode = "rest_bicep_set3"
            rest_bicep_start_time_set3 = time.time()

    return img 

def rest_bicep_set3(img):
    global exercise_mode, rest_bicep_start_time_set3, start_time1_pushup
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
        start_time1_pushup = time.time()

    return img




# Function to detect push-ups
def detect_push_up(img):
    global exercise_mode, display_info_pushup, per_right_pushup, per_left_pushup, bar_left_pushup, bar_right_pushup, leftangle_pushup, rightangle_pushup, color_right_pushup, color_left_pushup, feedback_left_pushup, feedback_right_pushup, success_threshold_pushup, peak_value_pushup, atrest_value_pushup, unsuccessful_reps_count_left_pushup, successful_reps_count_left_pushup, unsuccessful_reps_count_right_pushup, successful_reps_count_right_pushup, dir_left_unsuccessful_pushup, dir_right_unsuccessful_pushup, total_reps_count_pushup, total_reps_count_left_pushup, total_reps_count_right_pushup, start_time1_pushup, start_time2_pushup, start_time3_pushup, time_threshold_pushup, within_range_time1_pushup, general_feedback_left_pushup, general_feedback_right_pushup, dir_gen_feedback_pushup, dir_gen_feedback_unsuccessful_pushup, rest_pushup_start_time, dir_left_pushup, dir_right_pushup, within_range_time2_pushup

    img = cv2.resize(img, (1280, 720))

    elapsed_time_pushup = time.time() - start_time1_pushup
    remaining_time_pushup = max(0, 60 - elapsed_time_pushup)

    if display_info_pushup:  # Check if to display counter, bar, and percentage

        img = detector_pushup.findPose(img, False) # initializes img as variable for findpose function
        lmList = detector_pushup.findPosition(img, False) # initializes lmList_pushup as variable for findPosition function

        # Define hand angles outside the if statement
        if len(lmList) != 0:
            # Check if the person is in a proper push-up posture
            leftangle_pushup, rightangle_pushup = detector_pushup.findPushupAngle(img, 11, 13, 15, 12, 14, 16, drawpoints=True)  # defines left  and right arm landmark keypoints 

            #Interpolate angles to percentage and position on screen
            per_left_pushup = np.interp(leftangle_pushup, (190, 300), (100, 0)) # first parenthesis, the value threshold of the angle. Second, represents the interp value
            bar_left_pushup = np.interp(leftangle_pushup, (190, 300), (200, 400))

            per_right_pushup = np.interp(rightangle_pushup, (45, 160), (0, 100))
            bar_right_pushup = np.interp(rightangle_pushup, (45, 160), (400, 200))

            if detector_pushup.isPushUpPosture(lmList):
                if int(per_left_pushup) == 100:
                    color_left_pushup = (0, 255, 0)  # Change color of left leg bar to green
                else:
                    color_left_pushup = (0, 0, 255)
                
                if int(per_right_pushup) == 100:
                    color_right_pushup = (0, 255, 0)
                else:
                    color_right_pushup = (0, 0, 255)

                #left
                if 40 <= per_left_pushup <= 90:
                    # Increment the time within range
                    within_range_time1_pushup += time.time() - start_time2_pushup

                    # Check if peak value has been within range for the specified time
                    if within_range_time1_pushup >= time_threshold_pushup:
                        if dir_left_unsuccessful_pushup == 0:
                            unsuccessful_reps_count_left_pushup += 0.5
                            print("left", unsuccessful_reps_count_right_pushup)
                            dir_left_unsuccessful_pushup = 1

                else:
                    within_range_time1_pushup = 0
                    # Update the start time to the current time
                    start_time2_pushup = time.time()

                if 1 <= per_left_pushup <= 10:
                    if dir_left_unsuccessful_pushup == 1:
                        unsuccessful_reps_count_left_pushup += 0.5
                        print("left", unsuccessful_reps_count_right_pushup)
                        dir_left_unsuccessful_pushup = 0

                if per_left_pushup == success_threshold_pushup:
                    if dir_left_pushup == 0:
                        successful_reps_count_left_pushup += 0.5
                        dir_left_pushup = 1
                    
                elif per_left_pushup == atrest_value_pushup:
                    if dir_left_pushup == 1:
                        successful_reps_count_left_pushup += 0.5
                        dir_left_pushup = 0

                # right
                if 40 <= per_right_pushup <= 90:
                    # Increment the time within range
                    within_range_time2_pushup += time.time() - start_time3_pushup

                    # Check if peak value has been within range for the specified time
                    if within_range_time2_pushup >= time_threshold_pushup:
                        if dir_right_unsuccessful_pushup == 0:
                            unsuccessful_reps_count_right_pushup += 0.5
                            dir_right_unsuccessful_pushup = 1
                            print("right", unsuccessful_reps_count_right_pushup)

                else:
                    within_range_time2_pushup = 0
                    # Update the start time to the current time
                    start_time3_pushup = time.time()

                if 1 <= per_right_pushup <= 10:
                    #print("left down val: ", per_left)
                    if dir_right_unsuccessful_pushup == 1:
                        unsuccessful_reps_count_right_pushup += 0.5
                        dir_right_unsuccessful_pushup = 0
                        print("right", unsuccessful_reps_count_right_pushup)

                if per_right_pushup == success_threshold_pushup:
                    if dir_right_pushup == 0:
                        successful_reps_count_right_pushup += 0.5
                        dir_right_pushup = 1
                    
                elif per_right_pushup == atrest_value_pushup:
                    if dir_right_pushup == 1:
                        successful_reps_count_right_pushup += 0.5
                        dir_right_pushup = 0

                # feedback for left hand  # TO BE FETCHED 
                feedback_left_pushup = detector_pushup.feedback_pushup(per_left_pushup)

                detector_pushup.update_next_per_left(per_left_pushup)

                # feedback for right hand  # TO BE FETCHED 
                feedback_right_pushup = detector_pushup.feedback_pushup(per_right_pushup)

                detector_pushup.update_next_per_left(per_right_pushup)

        cvzone.putTextRect(img, 'Front Facing Push-Up', [430, 30], thickness=2, border=2, scale=1.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time_pushup)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # Draw bars for left and right angles
        cv2.putText(img, f"R {int(per_right_pushup)}%", (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_pushup)), (50, 400), color_right_pushup, -1)

        cv2.putText(img, f"L {int(per_left_pushup)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_pushup)), (995, 400), color_left_pushup, -1)

    cv2.rectangle(img, (20, 20), (200, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(successful_reps_count_right_pushup)}/5", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (210, 20), (390, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(successful_reps_count_left_pushup)}/5", (220, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    if remaining_time_pushup <= 0:
        cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
        display_info_pushup = False
        exercise_mode = "rest_pushup"
        rest_pushup_start_time = time.time() 


    total_reps_count_left_pushup = successful_reps_count_left_pushup + unsuccessful_reps_count_left_pushup
    total_reps_count_right_pushup = successful_reps_count_right_pushup + unsuccessful_reps_count_right_pushup  

    

    if successful_reps_count_right_pushup >= 10 and successful_reps_count_left_pushup >= 10:
        cvzone.putTextRect(img, 'All Repetitions Completed', [420, 30], thickness=2, border=2, scale=2.5)
        display_info_pushup = False
        # General feedback after finishing the exercise # TO BE FETCHED
        if dir_gen_feedback_pushup == 0:
            general_feedback_left_pushup = detector_pushup.left_arm_feedback(total_reps_count_left_pushup)
            general_feedback_right_pushup = detector_pushup.right_arm_feedback(total_reps_count_right_pushup)
            dir_gen_feedback_pushup = 1
            exercise_mode = "rest_pushup"
            rest_pushup_start_time = time.time() 
            print(f"{general_feedback_left_pushup} {general_feedback_right_pushup}")
        
    # To check for unsuccessful arm rep counter # CHANGED
    if unsuccessful_reps_count_left_pushup >= 3 and unsuccessful_reps_count_right_pushup >= 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for both arms. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_pushup = False

        if dir_gen_feedback_unsuccessful_pushup == 0:
            general_feedback_left_pushup = detector_pushup.left_arm_unsuccessful_feedback(total_reps_count_left_pushup)
            dir_gen_feedback_unsuccessful_pushup = 1
            exercise_mode = "rest_pushup"
            rest_pushup_start_time = time.time() 

    elif unsuccessful_reps_count_left_pushup >= 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for left arm. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_pushup = False

        if dir_gen_feedback_unsuccessful_pushup == 0:
            general_feedback_left_pushup = detector_pushup.left_arm_unsuccessful_feedback(total_reps_count_left_pushup)
            dir_gen_feedback_unsuccessful_pushup = 1
            exercise_mode = "rest_pushup"
            rest_pushup_start_time = time.time() 

    elif unsuccessful_reps_count_right_pushup >= 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for right arm. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_pushup = False

        if dir_gen_feedback_unsuccessful_pushup == 0:
            general_feedback_right_pushup = detector_pushup.right_arm_unsuccessful_feedback(total_reps_count_right_pushup)
            dir_gen_feedback_unsuccessful_pushup == 1
            exercise_mode = "rest_pushup"
            rest_pushup_start_time = time.time() 

    return img

def rest_pushup(img):
    global exercise_mode, rest_pushup_start_time, start_time1_pushup_set2
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_pushup_start_time
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "push_up_set2"
        start_time1_pushup_set2 = time.time()
    return img


def detect_push_up_set2(img):
    global display_info_pushup_set2, per_right_pushup_set2, per_left_pushup_set2, bar_left_pushup_set2, bar_right_pushup_set2, leftangle_pushup_set2, rightangle_pushup_set2, color_right_pushup_set2, color_left_pushup_set2, feedback_left_pushup_set2, feedback_right_pushup_set2, success_threshold_pushup_set2, peak_value_pushup_set2, atrest_value_pushup_set2, unsuccessful_reps_count_left_pushup_set2, successful_reps_count_left_pushup_set2, unsuccessful_reps_count_right_pushup_set2, successful_reps_count_right_pushup_set2, dir_left_unsuccessful_pushup_set2, dir_right_unsuccessful_pushup_set2, total_reps_count_pushup_set2, total_reps_count_left_pushup_set2, total_reps_count_right_pushup_set2, start_time1_pushup_set2, start_time2_pushup_set2, start_time3_pushup_set2, time_threshold_pushup, within_range_time1_pushup_set2, general_feedback_left_pushup_set2, general_feedback_right_pushup_set2, dir_gen_feedback_pushup_set2, dir_gen_feedback_unsuccessful_pushup_set2, rest_pushup_start_time_set2, exercise_mode, dir_left_pushup_set2, dir_right_pushup_set2, within_range_time2_pushup_set2

    img = cv2.resize(img, (1280, 720))

    elapsed_time_pushup = time.time() - start_time1_pushup_set2
    remaining_time_pushup = max(0, 60 - elapsed_time_pushup)

    if display_info_pushup_set2:  # Check if to display counter, bar, and percentage

        img = detector_pushup.findPose(img, False) # initializes img as variable for findpose function
        lmList = detector_pushup.findPosition(img, False) # initializes lmList_pushup as variable for findPosition function

        # Define hand angles outside the if statement
        if len(lmList) != 0:
            # Check if the person is in a proper push-up posture
            leftangle_pushup_set2, rightangle_pushup_set2 = detector_pushup.findPushupAngle(img, 11, 13, 15, 12, 14, 16, drawpoints=True)  # defines left  and right arm landmark keypoints 

            #Interpolate angles to percentage and position on screen
            per_left_pushup_set2 = np.interp(leftangle_pushup_set2, (190, 300), (100, 0)) # first parenthesis, the value threshold of the angle. Second, represents the interp value
            bar_left_pushup_set2 = np.interp(leftangle_pushup_set2, (190, 300), (200, 400))

            per_right_pushup_set2 = np.interp(rightangle_pushup_set2, (45, 160), (0, 100))
            bar_right_pushup_set2 = np.interp(rightangle_pushup_set2, (45, 160), (400, 200))

            if detector_pushup.isPushUpPosture(lmList):
                if int(per_left_pushup_set2) == 100:
                    color_left_pushup_set2 = (0, 255, 0)  # Change color of left leg bar to green
                else:
                    color_left_pushup_set2 = (0, 0, 255)
                
                if int(per_right_pushup_set2) == 100:
                    color_right_pushup_set2 = (0, 255, 0)
                else:
                    color_right_pushup_set2 = (0, 0, 255)

                #left
                if 40 <= per_left_pushup_set2 <= 90:
                    # Increment the time within range
                    within_range_time1_pushup_set2 += time.time() - start_time2_pushup_set2

                    # Check if peak value has been within range for the specified time
                    if within_range_time1_pushup_set2 >= time_threshold_pushup_set2:
                        if dir_left_unsuccessful_pushup_set2 == 0:
                            unsuccessful_reps_count_left_pushup_set2 += 0.5
                            print("left", unsuccessful_reps_count_right_pushup_set2)
                            dir_left_unsuccessful_pushup_set2 = 1

                else:
                    within_range_time1_pushup_set2 = 0
                    # Update the start time to the current time
                    start_time2_pushup_set2 = time.time()

                if 1 <= per_left_pushup_set2 <= 10:
                    if dir_left_unsuccessful_pushup_set2 == 1:
                        unsuccessful_reps_count_left_pushup_set2 += 0.5
                        print("left", unsuccessful_reps_count_right_pushup_set2)
                        dir_left_unsuccessful_pushup_set2 = 0

                if per_left_pushup_set2 == success_threshold_pushup_set2:
                    if dir_left_pushup_set2 == 0:
                        successful_reps_count_left_pushup_set2 += 0.5
                        dir_left_pushup_set2 = 1
                    
                elif per_left_pushup_set2 == atrest_value_pushup_set2:
                    if dir_left_pushup_set2 == 1:
                        successful_reps_count_left_pushup_set2 += 0.5
                        dir_left_pushup_set2 = 0

                # right
                if 40 <= per_right_pushup_set2 <= 90:
                    # Increment the time within range
                    within_range_time2_pushup_set2 += time.time() - start_time3_pushup_set2

                    # Check if peak value has been within range for the specified time
                    if within_range_time2_pushup_set2 >= time_threshold_pushup_set2:
                        if dir_right_unsuccessful_pushup_set2 == 0:
                            unsuccessful_reps_count_right_pushup_set2 += 0.5
                            dir_right_unsuccessful_pushup_set2 = 1
                            print("right", unsuccessful_reps_count_right_pushup_set2)

                else:
                    within_range_time2_pushup_set2 = 0
                    # Update the start time to the current time
                    start_time3_pushup_set2 = time.time()

                if 1 <= per_right_pushup_set2 <= 10:
                    #print("left down val: ", per_left)
                    if dir_right_unsuccessful_pushup_set2 == 1:
                        unsuccessful_reps_count_right_pushup_set2 += 0.5
                        dir_right_unsuccessful_pushup_set2 = 0
                        print("right", unsuccessful_reps_count_right_pushup_set2)

                if per_right_pushup_set2 == success_threshold_pushup_set2:
                    if dir_right_pushup_set2 == 0:
                        successful_reps_count_right_pushup_set2 += 0.5
                        dir_right_pushup_set2 = 1
                    
                elif per_right_pushup_set2 == atrest_value_pushup_set2:
                    if dir_right_pushup_set2 == 1:
                        successful_reps_count_right_pushup_set2 += 0.5
                        dir_right_pushup_set2 = 0

                # feedback for left hand  # TO BE FETCHED 
                feedback_left_pushup_set2 = detector_pushup.feedback_pushup(per_left_pushup_set2)

                detector_pushup.update_next_per_left(per_left_pushup_set2)

                # feedback for right hand  # TO BE FETCHED 
                feedback_right_pushup_set2 = detector_pushup.feedback_pushup(per_right_pushup_set2)

                detector_pushup.update_next_per_left(per_right_pushup_set2)

        cvzone.putTextRect(img, 'Front Facing Push-Up SET 2', [430, 30], thickness=2, border=2, scale=1.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time_pushup)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # Draw bars for left and right angles
        cv2.putText(img, f"R {int(per_right_pushup_set2)}%", (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_pushup_set2)), (50, 400), color_right_pushup_set2, -1)

        cv2.putText(img, f"L {int(per_left_pushup_set2)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_pushup_set2)), (995, 400), color_left_pushup_set2, -1)

    cv2.rectangle(img, (20, 20), (200, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(successful_reps_count_right_pushup_set2)}/10", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (210, 20), (390, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(successful_reps_count_left_pushup_set2)}/10", (220, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    if remaining_time_pushup <= 0:
        cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
        display_info_pushup_set2 = False
        exercise_mode = "rest_pushup_set2"
        rest_pushup_start_time_set2 = time.time() 


    total_reps_count_left_pushup_set2 = successful_reps_count_left_pushup_set2 + unsuccessful_reps_count_left_pushup_set2
    total_reps_count_right_pushup_set2 = successful_reps_count_right_pushup_set2 + unsuccessful_reps_count_right_pushup_set2  

    if successful_reps_count_right_pushup_set2 >= 10 and successful_reps_count_left_pushup_set2 >= 10:
        cvzone.putTextRect(img, 'All Repetitions Completed', [420, 30], thickness=2, border=2, scale=2.5)
        display_info_pushup_set2 = False
        # General feedback after finishing the exercise # TO BE FETCHED
        if dir_gen_feedback_pushup_set2 == 0:
            general_feedback_left_pushup_set2 = detector_pushup.left_arm_feedback(total_reps_count_left_pushup_set2)
            general_feedback_right_pushup_set2 = detector_pushup.right_arm_feedback(total_reps_count_right_pushup_set2)
            dir_gen_feedback_pushup_set2 = 1
            exercise_mode = "rest_pushup_set2"
            rest_pushup_start_time_set2 = time.time() 
            print(f"{general_feedback_left_pushup_set2} {general_feedback_right_pushup_set2}")
        
    # To check for unsuccessful arm rep counter # CHANGED
    if unsuccessful_reps_count_left_pushup_set2 >= 3 and unsuccessful_reps_count_right_pushup_set2 >= 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for both arms. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_pushup_set2 = False

        if dir_gen_feedback_unsuccessful_pushup_set2 == 0:
            general_feedback_left_pushup_set2 = detector_pushup.left_arm_unsuccessful_feedback(total_reps_count_left_pushup_set2)
            dir_gen_feedback_unsuccessful_pushup_set2 = 1
            exercise_mode = "rest_pushup_set2"
            rest_pushup_start_time_set2 = time.time() 

    elif unsuccessful_reps_count_left_pushup_set2 >= 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for left arm. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_pushup_set2 = False

        if dir_gen_feedback_unsuccessful_pushup_set2 == 0:
            general_feedback_left_pushup_set2 = detector_pushup.left_arm_unsuccessful_feedback(total_reps_count_left_pushup_set2)
            dir_gen_feedback_unsuccessful_pushup_set2 = 1
            exercise_mode = "rest_pushup_set2"
            rest_pushup_start_time_set2 = time.time() 

    elif unsuccessful_reps_count_right_pushup_set2 >= 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for right arm. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_pushup_set2 = False

        if dir_gen_feedback_unsuccessful_pushup_set2 == 0:
            general_feedback_right_pushup_set2 = detector_pushup.right_arm_unsuccessful_feedback(total_reps_count_right_pushup_set2)
            dir_gen_feedback_unsuccessful_pushup_set2 == 1
            exercise_mode = "rest_pushup_set2"
            rest_pushup_start_time_set2 = time.time() 
    return img

def rest_pushup_set2(img):
    global exercise_mode, rest_pushup_start_time_set2, start_time1_pushup_set3
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_pushup_start_time_set2
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "push_up_set3"
        start_time1_pushup_set3 = time.time()

    return img

def detect_push_up_set3(img):
    global exercise_mode, display_info_pushup_set3, per_right_pushup_set3, per_left_pushup_set3, bar_left_pushup_set3, bar_right_pushup_set3, leftangle_pushup_set3, rightangle_pushup_set3, color_right_pushup_set3, color_left_pushup_set3, feedback_left_pushup_set3, feedback_right_pushup_set3, success_threshold_pushup_set3, peak_value_pushup_set3, atrest_value_pushup_set3, unsuccessful_reps_count_left_pushup_set3, successful_reps_count_left_pushup_set3, unsuccessful_reps_count_right_pushup_set3, successful_reps_count_right_pushup_set3, dir_left_unsuccessful_pushup_set3, dir_right_unsuccessful_pushup_set3, total_reps_count_pushup_set3, total_reps_count_left_pushup_set3, total_reps_count_right_pushup_set3, start_time1_pushup_set3, start_time2_pushup_set3, start_time3_pushup_set3, time_threshold_pushup_set3, within_range_time1_pushup_set3, general_feedback_left_pushup_set3, general_feedback_right_pushup_set3, dir_gen_feedback_pushup_set3, dir_gen_feedback_unsuccessful_pushup_set3, rest_pushup_start_time_set3, dir_left_pushup_set3, dir_right_pushup_set3, within_range_time2_pushup_set3

    img = cv2.resize(img, (1280, 720))

    elapsed_time_pushup = time.time() - start_time1_pushup_set3
    remaining_time_pushup = max(0, 60 - elapsed_time_pushup)

    if display_info_pushup_set3:  # Check if to display counter, bar, and percentage

        img = detector_pushup.findPose(img, False) # initializes img as variable for findpose function
        lmList = detector_pushup.findPosition(img, False) # initializes lmList_pushup as variable for findPosition function

        # Define hand angles outside the if statement
        if len(lmList) != 0:
            # Check if the person is in a proper push-up posture
            leftangle_pushup_set3, rightangle_pushup_set3 = detector_pushup.findPushupAngle(img, 11, 13, 15, 12, 14, 16, drawpoints=True)  # defines left  and right arm landmark keypoints 

            #Interpolate angles to percentage and position on screen
            per_left_pushup_set3 = np.interp(leftangle_pushup_set3, (190, 300), (100, 0)) # first parenthesis, the value threshold of the angle. Second, represents the interp value
            bar_left_pushup_set3 = np.interp(leftangle_pushup_set3, (190, 300), (200, 400))

            per_right_pushup_set3 = np.interp(rightangle_pushup_set3, (45, 160), (0, 100))
            bar_right_pushup_set3 = np.interp(rightangle_pushup_set3, (45, 160), (400, 200))

            if detector_pushup.isPushUpPosture(lmList):
                if int(per_left_pushup_set3) == 100:
                    color_left_pushup_set3 = (0, 255, 0)  # Change color of left leg bar to green
                else:
                    color_left_pushup_set3 = (0, 0, 255)
                
                if int(per_right_pushup_set3) == 100:
                    color_right_pushup_set3 = (0, 255, 0)
                else:
                    color_right_pushup_set3 = (0, 0, 255)

                #left
                if 40 <= per_left_pushup_set3 <= 90:
                    # Increment the time within range
                    within_range_time1_pushup_set3 += time.time() - start_time2_pushup_set3

                    # Check if peak value has been within range for the specified time
                    if within_range_time1_pushup_set3 >= time_threshold_pushup_set3:
                        if dir_left_unsuccessful_pushup_set3 == 0:
                            unsuccessful_reps_count_left_pushup_set3 += 0.5
                            print("left", unsuccessful_reps_count_right_pushup_set3)
                            dir_left_unsuccessful_pushup_set3 = 1

                else:
                    within_range_time1_pushup_set3 = 0
                    # Update the start time to the current time
                    start_time2_pushup_set3 = time.time()

                if 1 <= per_left_pushup_set3 <= 10:
                    if dir_left_unsuccessful_pushup_set3 == 1:
                        unsuccessful_reps_count_left_pushup_set3 += 0.5
                        print("left", unsuccessful_reps_count_right_pushup_set3)
                        dir_left_unsuccessful_pushup_set3 = 0

                if per_left_pushup_set3 == success_threshold_pushup_set3:
                    if dir_left_pushup_set3 == 0:
                        successful_reps_count_left_pushup_set3 += 0.5
                        dir_left_pushup_set3 = 1
                    
                elif per_left_pushup_set3 == atrest_value_pushup_set3:
                    if dir_left_pushup_set3 == 1:
                        successful_reps_count_left_pushup_set3 += 0.5
                        dir_left_pushup_set3 = 0

                # right
                if 40 <= per_right_pushup_set3 <= 90:
                    # Increment the time within range
                    within_range_time2_pushup_set3 += time.time() - start_time3_pushup_set3

                    # Check if peak value has been within range for the specified time
                    if within_range_time2_pushup_set3 >= time_threshold_pushup_set3:
                        if dir_right_unsuccessful_pushup_set3 == 0:
                            unsuccessful_reps_count_right_pushup_set3 += 0.5
                            dir_right_unsuccessful_pushup_set3 = 1
                            print("right", unsuccessful_reps_count_right_pushup_set3)

                else:
                    within_range_time2_pushup_set3 = 0
                    # Update the start time to the current time
                    start_time3_pushup_set3 = time.time()

                if 1 <= per_right_pushup_set3 <= 10:
                    #print("left down val: ", per_left)
                    if dir_right_unsuccessful_pushup_set3 == 1:
                        unsuccessful_reps_count_right_pushup_set3 += 0.5
                        dir_right_unsuccessful_pushup_set3 = 0
                        print("right", unsuccessful_reps_count_right_pushup_set3)

                if per_right_pushup_set3 == success_threshold_pushup_set3:
                    if dir_right_pushup_set3 == 0:
                        successful_reps_count_right_pushup_set3 += 0.5
                        dir_right_pushup_set3 = 1
                    
                elif per_right_pushup_set3 == atrest_value_pushup_set3:
                    if dir_right_pushup_set3 == 1:
                        successful_reps_count_right_pushup_set3 += 0.5
                        dir_right_pushup_set3 = 0

                # feedback for left hand  # TO BE FETCHED 
                feedback_left_pushup_set3 = detector_pushup.feedback_pushup(per_left_pushup_set3)

                detector_pushup.update_next_per_left(per_left_pushup_set3)

                # feedback for right hand  # TO BE FETCHED 
                feedback_right_pushup_set3 = detector_pushup.feedback_pushup(per_right_pushup_set3)

                detector_pushup.update_next_per_left(per_right_pushup_set3)

        cvzone.putTextRect(img, 'Front Facing Push-Up SET 3', [430, 30], thickness=2, border=2, scale=1.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time_pushup)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # Draw bars for left and right angles
        cv2.putText(img, f"R {int(per_right_pushup_set3)}%", (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_pushup_set3)), (50, 400), color_right_pushup_set3, -1)

        cv2.putText(img, f"L {int(per_left_pushup_set3)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_pushup_set3)), (995, 400), color_left_pushup_set3, -1)

    cv2.rectangle(img, (20, 20), (200, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(successful_reps_count_right_pushup_set3)}/10", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (210, 20), (390, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(successful_reps_count_left_pushup_set3)}/5", (220, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    if remaining_time_pushup <= 0:
        cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
        display_info_pushup_set3 = False
        exercise_mode = "rest_pushup_set3"
        rest_pushup_start_time_set3 = time.time() 


    total_reps_count_left_pushup_set3 = successful_reps_count_left_pushup_set3 + unsuccessful_reps_count_left_pushup_set3
    total_reps_count_right_pushup_set3 = successful_reps_count_right_pushup_set3 + unsuccessful_reps_count_right_pushup_set3  

    if successful_reps_count_right_pushup_set3 >= 10 and successful_reps_count_left_pushup_set3 >= 10:
        cvzone.putTextRect(img, 'All Repetitions Completed', [420, 30], thickness=2, border=2, scale=2.5)
        display_info_pushup_set3 = False
        # General feedback after finishing the exercise # TO BE FETCHED
        if dir_gen_feedback_pushup_set3 == 0:
            general_feedback_left_pushup_set3 = detector_pushup.left_arm_feedback(total_reps_count_left_pushup_set3)
            general_feedback_right_pushup_set3 = detector_pushup.right_arm_feedback(total_reps_count_right_pushup_set3)
            dir_gen_feedback_pushup_set3 = 1
            exercise_mode = "rest_pushup_set3"
            rest_pushup_start_time = time.time() 
            print(f"{general_feedback_left_pushup_set3} {general_feedback_right_pushup_set3}")
        
    # To check for unsuccessful arm rep counter # CHANGED
    if unsuccessful_reps_count_left_pushup_set3 >= 3 and unsuccessful_reps_count_right_pushup_set3 >= 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for both arms. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_pushup_set3 = False

        if dir_gen_feedback_unsuccessful_pushup_set3 == 0:
            general_feedback_left_pushup_set3 = detector_pushup.left_arm_unsuccessful_feedback(total_reps_count_left_pushup_set3)
            dir_gen_feedback_unsuccessful_pushup_set3 = 1
            exercise_mode = "rest_pushup_set3"
            rest_pushup_start_time_set3 = time.time() 

    elif unsuccessful_reps_count_left_pushup_set3 >= 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for left arm. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_pushup_set3 = False

        if dir_gen_feedback_unsuccessful_pushup_set3 == 0:
            general_feedback_left_pushup_set3 = detector_pushup.left_arm_unsuccessful_feedback(total_reps_count_left_pushup_set3)
            dir_gen_feedback_unsuccessful_pushup_set3 = 1
            exercise_mode = "rest_pushup_set3"
            rest_pushup_start_time_set3 = time.time() 

    elif unsuccessful_reps_count_right_pushup_set3 >= 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for right arm. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_pushup_set3 = False

        if dir_gen_feedback_unsuccessful_pushup_set3 == 0:
            general_feedback_right_pushup_set3 = detector_pushup.right_arm_unsuccessful_feedback(total_reps_count_right_pushup_set3)
            dir_gen_feedback_unsuccessful_pushup_set3 == 1
            exercise_mode = "rest_pushup_set3"
            rest_pushup_start_time_set3 = time.time() 

    return img

def rest_pushup_set3(img):
    global exercise_mode, rest_pushup_start_time_set3, start_time1_shouldertaps
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
        start_time1_shouldertaps = time.time()

    return img

def detect_shouldertap(img):
    global dir_left_shouldertaps, dir_right_shouldertaps, display_info_shouldertaps, orientation_shouldertaps, orientation2_shouldertaps, per_right_shouldertaps, per_left_shouldertaps, bar_left_shouldertaps, bar_right_shouldertaps, color_right_shouldertaps, color_left_shouldertaps, feedback_left_shouldertaps, feedback_right_shouldertaps, success_threshold_shouldertaps, atrest_value_shouldertaps, unsuccessful_reps_count_left_shouldertaps, successful_reps_count_left_shouldertaps, unsuccessful_reps_count_right_shouldertaps, successful_reps_count_right_shouldertaps, dir_left_unsuccessful_shouldertaps, dir_right_unsuccessful_shouldertaps, total_reps_count_shouldertaps, total_reps_count_left_shouldertaps, total_reps_count_right_shouldertaps, start_time1_shouldertaps, start_time2_shouldertaps, start_time3_shouldertaps, time_threshold_shouldertaps, within_range_time1_shouldertaps, within_range_time2_shouldertaps, general_feedback_left_shouldertaps, general_feedback_right_shouldertaps, dir_gen_feedback_shouldertaps, dir_gen_feedback_unsuccessful_shouldertaps, cooldown_timer_shouldertaps, cooldown_duration_shouldertaps, rest_shouldertap_start_time, exercise_mode

    img = cv2.resize(img, (1280, 720))

    elapsed_time_shouldertaps = time.time() - start_time1_shouldertaps
    remaining_time_shouldertaps = max(0, 60 - elapsed_time_shouldertaps)

    if display_info_shouldertaps:  # Check if to display counter, bar, and percentage
        img = detector_shouldertaps.findPose(img, False)
        lmList_shouldertaps = detector_shouldertaps.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_shouldertaps) != 0:

            distance1_shouldertaps, distance2_shouldertaps = detector_shouldertaps.ShoulderTap(img, 12, 14, 16, 11, 13, 15, drawpoints=True) 

            #Interpolate angle to percentage and position on screen
            per_right_shouldertaps = np.interp(distance1_shouldertaps, (180, 350), (100, 0))
            bar_right_shouldertaps = np.interp(distance1_shouldertaps, (180, 350), (200, 400))

            per_left_shouldertaps = np.interp(distance2_shouldertaps, (180, 350), (100, 0))
            bar_left_shouldertaps = np.interp(distance2_shouldertaps, (180, 350), (200, 400))


            if int(per_left_shouldertaps) == 100:
                color_left_shouldertaps = (0, 255, 0)  # Change color of left leg bar to green
            else:
                color_left_shouldertaps = (0, 0, 255)
            
            if int(per_right_shouldertaps) == 100:
                color_right_shouldertaps = (0, 255, 0)
            else:
                color_right_shouldertaps = (0, 0, 255)

            #left
            if 40 <= per_left_shouldertaps <= 90:
                # Increment the time within range
                within_range_time1_shouldertaps += time.time() - start_time2_shouldertaps

                # Check if peak value has been within range for the specified time
                if within_range_time1_shouldertaps >= time_threshold_shouldertaps:
                    if dir_left_unsuccessful_shouldertaps == 0:
                        unsuccessful_reps_count_left_shouldertaps += 0.5
                        dir_left_unsuccessful_shouldertaps = 1
            else:
                within_range_time1_shouldertaps = 0
                # Update the start time to the current time
                start_time2_shouldertaps = time.time()

            if 1 <= per_left_shouldertaps <= 10:
                if dir_left_unsuccessful_shouldertaps == 1:
                    unsuccessful_reps_count_left_shouldertaps += 0.5
                    dir_left_unsuccessful_shouldertaps = 0

            if per_left_shouldertaps == success_threshold_shouldertaps:
                if dir_left_shouldertaps == 0:
                    successful_reps_count_left_shouldertaps += 0.5
                    dir_left_shouldertaps = 1

            elif per_left_shouldertaps == atrest_value_shouldertaps:
                if dir_left_shouldertaps == 1:
                    successful_reps_count_left_shouldertaps += 0.5
                    dir_left_shouldertaps = 0

            # right
            if 40 <= per_right_shouldertaps <= 90:
                # Increment the time within range
                within_range_time2_shouldertaps += time.time() - start_time3_shouldertaps

                # Check if peak value has been within range for the specified time
                if within_range_time2_shouldertaps >= time_threshold_shouldertaps:
                    if dir_right_unsuccessful_shouldertaps == 0:
                        unsuccessful_reps_count_right_shouldertaps += 0.5
                        dir_right_unsuccessful_shouldertaps = 1
            else:
                within_range_time2_shouldertaps = 0
                # Update the start time to the current time
                start_time3_shouldertaps = time.time()

            if 1 <= per_right_shouldertaps <= 10:
                if dir_right_unsuccessful_shouldertaps == 1:
                    unsuccessful_reps_count_right_shouldertaps += 0.5
                    dir_right_unsuccessful_shouldertaps = 0

            if per_right_shouldertaps == success_threshold_shouldertaps:
                if dir_right_shouldertaps == 0:
                    successful_reps_count_right_shouldertaps += 0.5
                    dir_right_shouldertaps = 1
                    cooldown_timer_shouldertaps = cooldown_duration_shouldertaps
            elif per_right_shouldertaps == atrest_value_shouldertaps: 
                if dir_right_shouldertaps == 1:
                    successful_reps_count_right_shouldertaps += 0.5
                    dir_right_shouldertaps = 0
                    cooldown_timer_shouldertaps = cooldown_duration_shouldertaps

            # feedback for left hand  # TO BE FETCHED 
            feedback_left_shouldertaps = detector_shouldertaps.feedback_shouldertaps(per_left_shouldertaps)

            detector_shouldertaps.update_next_per_left(per_left_shouldertaps)

            # feedback for right hand  # TO BE FETCHED 
            feedback_right_shouldertaps = detector_shouldertaps.feedback_shouldertaps(per_right_shouldertaps)

            detector_shouldertaps.update_next_per_left(per_right_shouldertaps)

        cvzone.putTextRect(img, 'Front Shoulder Tap', [430, 30], thickness=2, border=2, scale=1.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color


        #Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time_shouldertaps)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # ARM RIGHT
        cv2.putText(img, f"R {int(per_right_shouldertaps)}%", (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_shouldertaps)), (50, 400), color_right_shouldertaps, -1)

        # ARM LEFT
        cv2.putText(img, f"L {int(per_left_shouldertaps)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_shouldertaps)), (995, 400), color_left_shouldertaps, -1)

    # Counter 
    cv2.rectangle(img, (20, 20), (150, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(successful_reps_count_right_shouldertaps)}/10", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (170, 20), (300, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(successful_reps_count_left_shouldertaps)}/10", (180, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    if remaining_time_shouldertaps <= 0:
        cvzone.putTextRect(img, "Time's Up", [370, 30], thickness=2, border=2, scale=2.5)
        display_info_shouldertaps = False
        exercise_mode = "rest_shouldertap"
        rest_shouldertap_start_time = time.time()
    
    total_reps_count_left_shouldertaps = successful_reps_count_left_shouldertaps + unsuccessful_reps_count_left_shouldertaps
    total_reps_count_right_shouldertaps = unsuccessful_reps_count_right_shouldertaps + unsuccessful_reps_count_right_shouldertaps

    if successful_reps_count_right_shouldertaps >= 10 and successful_reps_count_left_shouldertaps >= 10:
            cvzone.putTextRect(img, 'All Repetitions Completed', [420, 30], thickness=2, border=2, scale=2.5)
            display_info_shouldertaps = False
            # General feedback after finishing the exercise # TO BE FETCHED
            if dir_gen_feedback_shouldertaps == 0:
                general_feedback_left_shouldertaps = detector_shouldertaps.left_leg_feedback(total_reps_count_left_shouldertaps)
                general_feedback_right_shouldertaps = detector_shouldertaps.right_leg_feedback(total_reps_count_right_shouldertaps)
                dir_gen_feedback_shouldertaps = 1
                exercise_mode = "rest_shouldertap"
                rest_shouldertap_start_time = time.time()
                print(f"{general_feedback_left_shouldertaps} {general_feedback_right_shouldertaps}")

    if unsuccessful_reps_count_left_shouldertaps >= 3 and unsuccessful_reps_count_right_shouldertaps >= 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for both arms. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_shouldertaps = False

        if dir_gen_feedback_unsuccessful_shouldertaps == 0:
            general_feedback_left_shouldertaps = detector_shouldertaps.left_leg_unsuccessful_feedback(total_reps_count_left_shouldertaps)
            general_feedback_right_shouldertaps = detector_shouldertaps.right_leg_unsuccessful_feedback(total_reps_count_right_shouldertaps)
            dir_gen_feedback_unsuccessful_shouldertaps = 1
            exercise_mode = "rest_shouldertap"
            rest_shouldertap_start_time = time.time()
            
    if unsuccessful_reps_count_left_shouldertaps >= 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for left arm. Please retry again', [420, 30], thickness=2, border=2, scale=1)
        display_info_shouldertaps = False

        if dir_gen_feedback_unsuccessful_shouldertaps == 0:
            general_feedback_left_shouldertaps = detector_shouldertaps.left_leg_unsuccessful_feedback(total_reps_count_left_shouldertaps)
            dir_gen_feedback_unsuccessful_shouldertaps = 1
            exercise_mode = "rest_shouldertap"
            rest_shouldertap_start_time = time.time()

    if unsuccessful_reps_count_right_shouldertaps >= 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for right arm. Please retry again', [420, 30], thickness=2, border=2, scale=1)
        display_info_shouldertaps = False

        if dir_gen_feedback_unsuccessful_shouldertaps == 0:
            general_feedback_right_shouldertaps = detector_shouldertaps.right_leg_unsuccessful_feedback(total_reps_count_right_shouldertaps)
            dir_gen_feedback_unsuccessful_shouldertaps == 1
            exercise_mode = "rest_shouldertap"
            rest_shouldertap_start_time = time.time()

    return img

def rest_shouldertap(img):
    global exercise_mode, rest_shouldertap_start_time, start_time1_shouldertaps_set2
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_shouldertap_start_time
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "shoulder_tap_set2"
        start_time1_shouldertaps_set2 = time.time()
    return img

def detect_shouldertap_set2(img):
    global dir_left_shouldertaps_set2, dir_right_shouldertaps_set2, display_info_shouldertaps_set2, orientation_shouldertaps_set2, orientation2_shouldertaps_set2, per_right_shouldertaps_set2, per_left_shouldertaps_set2, bar_left_shouldertaps_set2, bar_right_shouldertaps_set2, color_right_shouldertaps_set2, color_left_shouldertaps_set2, feedback_left_shouldertaps_set2, feedback_right_shouldertaps_set2, success_threshold_shouldertaps_set2, atrest_value_shouldertaps_set2, unsuccessful_reps_count_left_shouldertaps_set2, successful_reps_count_left_shouldertaps_set2, unsuccessful_reps_count_right_shouldertaps_set2, successful_reps_count_right_shouldertaps_set2, dir_left_unsuccessful_shouldertaps_set2, dir_right_unsuccessful_shouldertaps_set2, total_reps_count_shouldertaps_set2, total_reps_count_left_shouldertaps_set2, total_reps_count_right_shouldertaps_set2, start_time1_shouldertaps_set2, start_time2_shouldertaps_set2, start_time3_shouldertaps_set2, time_threshold_shouldertaps_set2, within_range_time1_shouldertaps_set2, within_range_time2_shouldertaps_set2, general_feedback_left_shouldertaps_set2, general_feedback_right_shouldertaps_set2, dir_gen_feedback_shouldertaps_set2, dir_gen_feedback_unsuccessful_shouldertaps_set2, cooldown_timer_shouldertaps_set2, cooldown_duration_shouldertaps_set2, rest_shouldertap_start_time_set2, exercise_mode

    img = cv2.resize(img, (1280, 720))

    elapsed_time_shouldertaps = time.time() - start_time1_shouldertaps_set2
    remaining_time_shouldertaps = max(0, 60 - elapsed_time_shouldertaps)

    if display_info_shouldertaps_set2:  # Check if to display counter, bar, and percentage
        img = detector_shouldertaps.findPose(img, False)
        lmList_shouldertaps = detector_shouldertaps.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_shouldertaps) != 0:

            distance1_shouldertaps_set2, distance2_shouldertaps_set2 = detector_shouldertaps.ShoulderTap(img, 12, 14, 16, 11, 13, 15, drawpoints=True) 

            #Interpolate angle to percentage and position on screen
            per_right_shouldertaps_set2 = np.interp(distance1_shouldertaps_set2, (180, 350), (100, 0))
            bar_right_shouldertaps_set2 = np.interp(distance1_shouldertaps_set2, (180, 350), (200, 400))

            per_left_shouldertaps_set2 = np.interp(distance2_shouldertaps_set2, (180, 350), (100, 0))
            bar_left_shouldertaps_set2 = np.interp(distance2_shouldertaps_set2, (180, 350), (200, 400))


            if int(per_left_shouldertaps_set2) == 100:
                color_left_shouldertaps_set2 = (0, 255, 0)  # Change color of left leg bar to green
            else:
                color_left_shouldertaps_set2 = (0, 0, 255)
            
            if int(per_right_shouldertaps_set2) == 100:
                color_right_shouldertaps_set2 = (0, 255, 0)
            else:
                color_right_shouldertaps_set2 = (0, 0, 255)

            #left
            if 40 <= per_left_shouldertaps_set2 <= 90:
                # Increment the time within range
                within_range_time1_shouldertaps_set2 += time.time() - start_time2_shouldertaps_set2

                # Check if peak value has been within range for the specified time
                if within_range_time1_shouldertaps_set2 >= time_threshold_shouldertaps_set2:
                    if dir_left_unsuccessful_shouldertaps_set2 == 0:
                        unsuccessful_reps_count_left_shouldertaps_set2 += 0.5
                        dir_left_unsuccessful_shouldertaps_set2 = 1
            else:
                within_range_time1_shouldertaps_set2 = 0
                # Update the start time to the current time
                start_time2_shouldertaps_set2 = time.time()

            if 1 <= per_left_shouldertaps_set2 <= 10:
                if dir_left_unsuccessful_shouldertaps_set2 == 1:
                    unsuccessful_reps_count_left_shouldertaps_set2 += 0.5
                    dir_left_unsuccessful_shouldertaps_set2 = 0

            if per_left_shouldertaps_set2 == success_threshold_shouldertaps_set2:
                if dir_left_shouldertaps_set2 == 0:
                    successful_reps_count_left_shouldertaps_set2 += 0.5
                    dir_left_shouldertaps_set2 = 1

            elif per_left_shouldertaps_set2 == atrest_value_shouldertaps_set2:
                if dir_left_shouldertaps_set2 == 1:
                    successful_reps_count_left_shouldertaps_set2 += 0.5
                    dir_left_shouldertaps_set2 = 0

            # right
            if 40 <= per_right_shouldertaps_set2 <= 90:
                # Increment the time within range
                within_range_time2_shouldertaps_set2 += time.time() - start_time3_shouldertaps_set2

                # Check if peak value has been within range for the specified time
                if within_range_time2_shouldertaps_set2 >= time_threshold_shouldertaps_set2:
                    if dir_right_unsuccessful_shouldertaps_set2 == 0:
                        unsuccessful_reps_count_right_shouldertaps_set2 += 0.5
                        dir_right_unsuccessful_shouldertaps_set2 = 1
            else:
                within_range_time2_shouldertaps_set2 = 0
                # Update the start time to the current time
                start_time3_shouldertaps_set2 = time.time()

            if 1 <= per_right_shouldertaps_set2 <= 10:
                if dir_right_unsuccessful_shouldertaps_set2 == 1:
                    unsuccessful_reps_count_right_shouldertaps_set2 += 0.5
                    dir_right_unsuccessful_shouldertaps_set2 = 0

            if per_right_shouldertaps_set2 == success_threshold_shouldertaps_set2:
                if dir_right_shouldertaps_set2 == 0:
                    successful_reps_count_right_shouldertaps_set2 += 0.5
                    dir_right_shouldertaps_set2 = 1
                    cooldown_timer_shouldertaps_set2 = cooldown_duration_shouldertaps_set2
            elif per_right_shouldertaps_set2 == atrest_value_shouldertaps_set2: 
                if dir_right_shouldertaps_set2 == 1:
                    successful_reps_count_right_shouldertaps_set2 += 0.5
                    dir_right_shouldertaps_set2 = 0
                    cooldown_timer_shouldertaps_set2 = cooldown_duration_shouldertaps_set2

            # feedback for left hand  # TO BE FETCHED 
            feedback_left_shouldertaps_set2 = detector_shouldertaps.feedback_shouldertaps(per_left_shouldertaps_set2)

            detector_shouldertaps.update_next_per_left(per_left_shouldertaps_set2)

            # feedback for right hand  # TO BE FETCHED 
            feedback_right_shouldertaps_set2 = detector_shouldertaps.feedback_shouldertaps(per_right_shouldertaps_set2)

            detector_shouldertaps.update_next_per_left(per_right_shouldertaps_set2)


        cvzone.putTextRect(img, 'Front Shoulder Tap SET 2', [430, 30], thickness=2, border=2, scale=1.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color


        #Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time_shouldertaps)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # ARM RIGHT
        cv2.putText(img, f"R {int(per_right_shouldertaps_set2)}%", (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_shouldertaps_set2)), (50, 400), color_right_shouldertaps_set2, -1)

        # ARM LEFT
        cv2.putText(img, f"L {int(per_left_shouldertaps_set2)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_shouldertaps_set2)), (995, 400), color_left_shouldertaps_set2, -1)

    # Counter 
    cv2.rectangle(img, (20, 20), (150, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(successful_reps_count_right_shouldertaps_set2)}/10", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (170, 20), (300, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(successful_reps_count_left_shouldertaps_set2)}/10", (180, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    if remaining_time_shouldertaps <= 0:
        cvzone.putTextRect(img, "Time's Up", [370, 30], thickness=2, border=2, scale=2.5)
        display_info_shouldertaps_set2 = False
        exercise_mode = "rest_shouldertap_set2"
        rest_shouldertap_start_time_set2 = time.time()

    total_reps_count_left_shouldertaps_set2 = successful_reps_count_left_shouldertaps_set2 + unsuccessful_reps_count_left_shouldertaps_set2
    total_reps_count_right_shouldertaps_set = unsuccessful_reps_count_right_shouldertaps_set2 + unsuccessful_reps_count_right_shouldertaps_set2

    if successful_reps_count_right_shouldertaps_set2 >= 10 and successful_reps_count_left_shouldertaps_set2 >= 10:
            cvzone.putTextRect(img, 'All Repetitions Completed', [420, 30], thickness=2, border=2, scale=2.5)
            display_info_shouldertaps_set2 = False
            # General feedback after finishing the exercise # TO BE FETCHED
            if dir_gen_feedback_shouldertaps_set2 == 0:
                general_feedback_left_shouldertaps_set2 = detector_shouldertaps.left_leg_feedback(total_reps_count_left_shouldertaps_set2)
                general_feedback_right_shouldertaps_set2 = detector_shouldertaps.right_leg_feedback(total_reps_count_right_shouldertaps_set2)
                dir_gen_feedback_shouldertaps_set2 = 1
                exercise_mode = "rest_shouldertap_set2"
                rest_shouldertap_start_time_set2 = time.time()
                print(f"{general_feedback_left_shouldertaps_set2} {general_feedback_right_shouldertaps_set2}")

    if unsuccessful_reps_count_left_shouldertaps_set2 >= 3 and unsuccessful_reps_count_right_shouldertaps_set2 >= 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for both arms. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_shouldertaps_set2 = False

        if dir_gen_feedback_unsuccessful_shouldertaps_set2 == 0:
            general_feedback_left_shouldertaps_set2 = detector_shouldertaps.left_leg_unsuccessful_feedback(total_reps_count_left_shouldertaps_set2)
            general_feedback_right_shouldertaps_set2 = detector_shouldertaps.right_leg_unsuccessful_feedback(total_reps_count_right_shouldertaps_set2)
            dir_gen_feedback_unsuccessful_shouldertaps_set2 = 1
            exercise_mode = "rest_shouldertap_set2"
            rest_shouldertap_start_time_set2 = time.time()
            
    if unsuccessful_reps_count_left_shouldertaps_set2 >= 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for left arm. Please retry again', [420, 30], thickness=2, border=2, scale=1)
        display_info_shouldertaps_set2 = False

        if dir_gen_feedback_unsuccessful_shouldertaps_set2 == 0:
            general_feedback_left_shouldertaps_set2 = detector_shouldertaps.left_leg_unsuccessful_feedback(total_reps_count_left_shouldertaps_set2)
            dir_gen_feedback_unsuccessful_shouldertaps_set2 = 1
            exercise_mode = "rest_shouldertap_set2"
            rest_shouldertap_start_time_set2 = time.time()

    if unsuccessful_reps_count_right_shouldertaps_set2 >= 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for right arm. Please retry again', [420, 30], thickness=2, border=2, scale=1)
        display_info_shouldertaps_set2 = False

        if dir_gen_feedback_unsuccessful_shouldertaps_set2 == 0:
            general_feedback_right_shouldertaps_set2 = detector_shouldertaps.right_leg_unsuccessful_feedback(total_reps_count_right_shouldertaps_set2)
            dir_gen_feedback_unsuccessful_shouldertaps_set2 == 1
            exercise_mode = "rest_shouldertap_set2"
            rest_shouldertap_start_time_set2 = time.time()

    return img

def rest_shouldertap_set2(img):
    global exercise_mode, rest_shouldertap_start_time_set2, start_time1_shouldertaps_set3
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_shouldertap_start_time_set2
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "shoulder_tap_set3"
        start_time1_shouldertaps_set3 = time.time()
    return img

def detect_shouldertap_set3(img):
    global dir_left_shouldertaps_set3, dir_right_shouldertaps_set3, display_info_shouldertaps_set3, orientation_shouldertaps_set3, orientation2_shouldertaps_set3, per_right_shouldertaps_set3, per_left_shouldertaps_set3, bar_left_shouldertaps_set3, bar_right_shouldertaps_set3, color_right_shouldertaps_set3, color_left_shouldertaps_set3, feedback_left_shouldertaps_set3, feedback_right_shouldertaps_set3, success_threshold_shouldertaps_set3, atrest_value_shouldertaps_set3, unsuccessful_reps_count_left_shouldertaps_set3, successful_reps_count_left_shouldertaps_set3, unsuccessful_reps_count_right_shouldertaps_set3, successful_reps_count_right_shouldertaps_set3, dir_left_unsuccessful_shouldertaps_set3, dir_right_unsuccessful_shouldertaps_set3, total_reps_count_shouldertaps_set3, total_reps_count_left_shouldertaps_set3, total_reps_count_right_shouldertaps_set3, start_time1_shouldertaps_set3, start_time2_shouldertaps_set3, start_time3_shouldertaps_set3, time_threshold_shouldertaps_set3, within_range_time1_shouldertaps_set3, within_range_time2_shouldertaps_set3, general_feedback_left_shouldertaps_set3, general_feedback_right_shouldertaps_set3, dir_gen_feedback_shouldertaps_set3, dir_gen_feedback_unsuccessful_shouldertaps_set3, cooldown_timer_shouldertaps_set3, cooldown_duration_shouldertaps_set3, rest_shouldertap_start_time_set3, exercise_mode

    img = cv2.resize(img, (1280, 720))

    elapsed_time_shouldertaps = time.time() - start_time1_shouldertaps_set3
    remaining_time_shouldertaps = max(0, 60 - elapsed_time_shouldertaps)

    if display_info_shouldertaps_set3:  # Check if to display counter, bar, and percentage
        img = detector_shouldertaps.findPose(img, False)
        lmList_shouldertaps = detector_shouldertaps.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_shouldertaps) != 0:

            distance1_shouldertaps_set3, distance2_shouldertaps_set3 = detector_shouldertaps.ShoulderTap(img, 12, 14, 16, 11, 13, 15, drawpoints=True) 

            #Interpolate angle to percentage and position on screen
            per_right_shouldertaps_set3 = np.interp(distance1_shouldertaps_set3, (180, 350), (100, 0))
            bar_right_shouldertaps_set3 = np.interp(distance1_shouldertaps_set3, (180, 350), (200, 400))

            per_left_shouldertaps_set3 = np.interp(distance2_shouldertaps_set3, (180, 350), (100, 0))
            bar_left_shouldertaps_set3 = np.interp(distance2_shouldertaps_set3, (180, 350), (200, 400))


            if int(per_left_shouldertaps_set3) == 100:
                color_left_shouldertaps_set3 = (0, 255, 0)  # Change color of left leg bar to green
            else:
                color_left_shouldertaps_set3 = (0, 0, 255)
            
            if int(per_right_shouldertaps_set3) == 100:
                color_right_shouldertaps_set3 = (0, 255, 0)
            else:
                color_right_shouldertaps_set3 = (0, 0, 255)

            #left
            if 40 <= per_left_shouldertaps_set3 <= 90:
                # Increment the time within range
                within_range_time1_shouldertaps_set3 += time.time() - start_time2_shouldertaps_set3

                # Check if peak value has been within range for the specified time
                if within_range_time1_shouldertaps_set3 >= time_threshold_shouldertaps_set3:
                    if dir_left_unsuccessful_shouldertaps_set3 == 0:
                        unsuccessful_reps_count_left_shouldertaps_set3 += 0.5
                        dir_left_unsuccessful_shouldertaps_set3 = 1
            else:
                within_range_time1_shouldertaps_set3 = 0
                # Update the start time to the current time
                start_time2_shouldertaps_set3 = time.time()

            if 1 <= per_left_shouldertaps_set3 <= 10:
                if dir_left_unsuccessful_shouldertaps_set3 == 1:
                    unsuccessful_reps_count_left_shouldertaps_set3 += 0.5
                    dir_left_unsuccessful_shouldertaps_set3 = 0

            if per_left_shouldertaps_set3 == success_threshold_shouldertaps_set3:
                if dir_left_shouldertaps_set3 == 0:
                    successful_reps_count_left_shouldertaps_set3 += 0.5
                    dir_left_shouldertaps_set3 = 1

            elif per_left_shouldertaps_set3 == atrest_value_shouldertaps_set3:
                if dir_left_shouldertaps_set3 == 1:
                    successful_reps_count_left_shouldertaps_set3 += 0.5
                    dir_left_shouldertaps_set3 = 0

            # right
            if 40 <= per_right_shouldertaps_set3 <= 90:
                # Increment the time within range
                within_range_time2_shouldertaps_set3 += time.time() - start_time3_shouldertaps_set3

                # Check if peak value has been within range for the specified time
                if within_range_time2_shouldertaps_set3 >= time_threshold_shouldertaps_set3:
                    if dir_right_unsuccessful_shouldertaps_set3 == 0:
                        unsuccessful_reps_count_right_shouldertaps_set3 += 0.5
                        dir_right_unsuccessful_shouldertaps_set3 = 1
            else:
                within_range_time2_shouldertaps_set3 = 0
                # Update the start time to the current time
                start_time3_shouldertaps_set3 = time.time()

            if 1 <= per_right_shouldertaps_set3 <= 10:
                if dir_right_unsuccessful_shouldertaps_set3 == 1:
                    unsuccessful_reps_count_right_shouldertaps_set3 += 0.5
                    dir_right_unsuccessful_shouldertaps_set3 = 0

            if per_right_shouldertaps_set3 == success_threshold_shouldertaps_set3:
                if dir_right_shouldertaps_set3 == 0:
                    successful_reps_count_right_shouldertaps_set3 += 0.5
                    dir_right_shouldertaps_set3 = 1
                    cooldown_timer_shouldertaps_set3 = cooldown_duration_shouldertaps_set3
            elif per_right_shouldertaps_set3 == atrest_value_shouldertaps_set3: 
                if dir_right_shouldertaps_set3 == 1:
                    successful_reps_count_right_shouldertaps_set3 += 0.5
                    dir_right_shouldertaps_set3 = 0
                    cooldown_timer_shouldertaps_set3 = cooldown_duration_shouldertaps_set3

            # feedback for left hand  # TO BE FETCHED 
            feedback_left_shouldertaps_set3 = detector_shouldertaps.feedback_shouldertaps(per_left_shouldertaps_set3)

            detector_shouldertaps.update_next_per_left(per_left_shouldertaps_set3)

            # feedback for right hand  # TO BE FETCHED 
            feedback_right_shouldertaps_set3 = detector_shouldertaps.feedback_shouldertaps(per_right_shouldertaps_set3)

            detector_shouldertaps.update_next_per_left(per_right_shouldertaps_set3)


        cvzone.putTextRect(img, 'Front Shoulder Tap SET 3', [430, 30], thickness=2, border=2, scale=1.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color


        #Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time_shouldertaps)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # ARM RIGHT
        cv2.putText(img, f"R {int(per_right_shouldertaps_set3)}%", (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_shouldertaps_set3)), (50, 400), color_right_shouldertaps_set3, -1)

        # ARM LEFT
        cv2.putText(img, f"L {int(per_left_shouldertaps_set3)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_shouldertaps_set3)), (995, 400), color_left_shouldertaps_set3, -1)

    # Counter 
    cv2.rectangle(img, (20, 20), (150, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(successful_reps_count_right_shouldertaps_set3)}/10", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (170, 20), (300, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(successful_reps_count_left_shouldertaps_set3)}/10", (180, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    if remaining_time_shouldertaps <= 0:
        cvzone.putTextRect(img, "Time's Up", [370, 30], thickness=2, border=2, scale=2.5)
        display_info_shouldertaps_set3 = False
        exercise_mode = "rest_shouldertap_set3"
        rest_shouldertap_start_time_set3 = time.time()

    total_reps_count_left_shouldertaps_set3 = successful_reps_count_left_shouldertaps_set3 + unsuccessful_reps_count_left_shouldertaps_set3
    total_reps_count_right_shouldertaps_set3 = unsuccessful_reps_count_right_shouldertaps_set3 + unsuccessful_reps_count_right_shouldertaps_set3

    if successful_reps_count_right_shouldertaps_set3 >= 10 and successful_reps_count_left_shouldertaps_set3 >= 10:
            cvzone.putTextRect(img, 'All Repetitions Completed', [420, 30], thickness=2, border=2, scale=2.5)
            display_info_shouldertaps_set3 = False
            # General feedback after finishing the exercise # TO BE FETCHED
            if dir_gen_feedback_shouldertaps_set3 == 0:
                general_feedback_left_shouldertaps_set3 = detector_shouldertaps.left_leg_feedback(total_reps_count_left_shouldertaps_set3)
                general_feedback_right_shouldertaps_set3 = detector_shouldertaps.right_leg_feedback(total_reps_count_right_shouldertaps_set3)
                dir_gen_feedback_shouldertaps_set3 = 1
                exercise_mode = "rest_shouldertap_set3"
                rest_shouldertap_start_time_set3 = time.time()
                print(f"{general_feedback_left_shouldertaps_set3} {general_feedback_right_shouldertaps_set3}")

    if unsuccessful_reps_count_left_shouldertaps_set3 >= 3 and unsuccessful_reps_count_right_shouldertaps_set3 >= 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for both arms. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_shouldertaps_set3 = False

        if dir_gen_feedback_unsuccessful_shouldertaps_set3 == 0:
            general_feedback_left_shouldertaps_set3 = detector_shouldertaps.left_leg_unsuccessful_feedback(total_reps_count_left_shouldertaps_set3)
            general_feedback_right_shouldertaps_set3 = detector_shouldertaps.right_leg_unsuccessful_feedback(total_reps_count_right_shouldertaps_set3)
            dir_gen_feedback_unsuccessful_shouldertaps_set3 = 1
            exercise_mode = "rest_shouldertap_set3"
            rest_shouldertap_start_time_set3 = time.time()
            
    if unsuccessful_reps_count_left_shouldertaps_set3 >= 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for left arm. Please retry again', [420, 30], thickness=2, border=2, scale=1)
        display_info_shouldertaps_set3 = False

        if dir_gen_feedback_unsuccessful_shouldertaps_set3 == 0:
            general_feedback_left_shouldertaps_set3 = detector_shouldertaps.left_leg_unsuccessful_feedback(total_reps_count_left_shouldertaps_set3)
            dir_gen_feedback_unsuccessful_shouldertaps_set3 = 1
            exercise_mode = "rest_shouldertap_set3"
            rest_shouldertap_start_time_set3 = time.time()

    if unsuccessful_reps_count_right_shouldertaps_set3 >= 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for right arm. Please retry again', [420, 30], thickness=2, border=2, scale=1)
        display_info_shouldertaps_set3 = False

        if dir_gen_feedback_unsuccessful_shouldertaps_set3 == 0:
            general_feedback_right_shouldertaps_set3 = detector_shouldertaps.right_leg_unsuccessful_feedback(total_reps_count_right_shouldertaps_set3)
            dir_gen_feedback_unsuccessful_shouldertaps_set3 == 1
            exercise_mode = "rest_shouldertap_set3"
            rest_shouldertap_start_time_set3 = time.time()

    return img

def rest_shouldertap_set3(img):
    global exercise_mode, rest_shouldertap_start_time_set3, start_time1_chestpress
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_shouldertap_start_time_set3
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "chest_press"
        start_time1_chestpress = time.time()
    return img

def detect_chestpress(img):
    global dir_left_chestpress, dir_right_chestpress, display_info_chestpress, orientation_chestpress, orientation2_chestpress, per_right_chestpress, per_left_chestpress, bar_left_chestpress, bar_right_chestpress, color_right_chestpress, color_left_chestpress, feedback_left_chestpress, feedback_right_chestpress, success_threshold_chestpress, atrest_value_chestpress, unsuccessful_reps_count_left_chestpress, successful_reps_count_left_chestpress, unsuccessful_reps_count_right_chestpress, successful_reps_count_right_chestpress, dir_left_unsuccessful_chestpress, dir_right_unsuccessful_chestpress, total_reps_count_chestpress, total_reps_count_left_chestpress, total_reps_count_right_chestpress, start_time1_chestpress, start_time2_chestpress, start_time3_chestpress, time_threshold_chestpress, within_range_time1_chestpress, within_range_time2_chestpress, general_feedback_left_chestpress, general_feedback_right_chestpress, dir_gen_feedback_chestpress, dir_gen_feedback_unsuccessful_chestpress, cooldown_timer_chestpress, cooldown_duration_chestpress, angle_left_chestpress, angle_right_chestpress, rest_chestpress_start_time, exercise_mode

    img = cv2.resize(img, (1280, 720))

    # Timer - starts timer based on set duration
    elapsed_time_chestpress = time.time() - start_time1_chestpress
    remaining_time_chestpress = max(0, 10 - elapsed_time_chestpress)


    if display_info_chestpress:  # Check if to display counter, bar, and percentage
        img = detector_chestpress.findPose(img, False) # initializes img as variable for findpose function
        lmList_chestpress = detector_chestpress.findPosition(img, False) # initializes lmList_bicep as variable for findPosition function

        # Define hand angles outside the if statement
        if len(lmList_chestpress) != 0:
            angle_left_chestpress = detector_chestpress.findAngle(img, 11, 13, 15)
            angle_right_chestpress = detector_chestpress.findAngle(img, 12, 14, 16) # defines right arm landmark keypoints
            # (refer to mediapipe landmark mapping for number equivalent)

            per_left_chestpress = np.interp(angle_left_chestpress, (60, 200), (0, 100)) # first parenthesis, the value threshold of the angle. Second, represents the interp value
            bar_left_chestpress = np.interp(angle_left_chestpress, (60, 200), (400, 200)) # 

            per_right_chestpress = np.interp(angle_right_chestpress, (150, 300), (100, 0)) # 
            bar_right_chestpress = np.interp(angle_right_chestpress, (150, 300), (200, 400)) # 


            if int(per_left_chestpress) == 100:
                color_left_chestpress = (0, 255, 0)  # Change color of left leg bar to green
            else:
                color_left_chestpress = (0, 0, 255)
            
            if int(per_right_chestpress) == 100:
                color_right_chestpress = (0, 255, 0)
            else:
                color_right_chestpress = (0, 0, 255)

            #left
            if 40 <= per_left_chestpress <= 90:
                # Increment the time within range
                within_range_time1_chestpress += time.time() - start_time2_chestpress

                # Check if peak value has been within range for the specified time
                if within_range_time1_chestpress >= time_threshold_chestpress:
                    if dir_left_unsuccessful_chestpress == 0:
                        unsuccessful_reps_count_left_chestpress += 0.5
                        dir_left_unsuccessful_chestpress = 1
                        print("UP WRONG LEFT: ", unsuccessful_reps_count_left_chestpress)

            else:
                within_range_time1_chestpress = 0
                # Update the start time to the current time
                start_time2_chestpress = time.time()

            if 1 <= per_left_chestpress <= 10:
                if dir_left_unsuccessful_chestpress == 1:
                    unsuccessful_reps_count_left_chestpress += 0.5
                    dir_left_unsuccessful_chestpress = 0
                    print("DOWN WRONG LEFT: ", unsuccessful_reps_count_left_chestpress)

            if per_left_chestpress == success_threshold_chestpress:
                if dir_left_chestpress == 0:
                    successful_reps_count_left_chestpress += 0.5
                    dir_left_chestpress = 1

            elif per_left_chestpress == atrest_value_chestpress:
                if dir_left_chestpress == 1:
                    successful_reps_count_left_chestpress += 0.5
                    dir_left_chestpress = 0

            # right
            if 40 <= per_right_chestpress <= 90:
                # Increment the time within range
                within_range_time2_chestpress += time.time() - start_time3_chestpress

                # Check if peak value has been within range for the specified time
                if within_range_time2_chestpress >= time_threshold_chestpress:
                    if dir_right_unsuccessful_chestpress == 0:
                        unsuccessful_reps_count_right_chestpress += 0.5
                        dir_right_unsuccessful_chestpress = 1
                        print("UP RIGHT WRONG", unsuccessful_reps_count_right_chestpress)
            else:
                within_range_time2_chestpress = 0
                # Update the start time to the current time
                start_time3_chestpress = time.time()

            if 1 <= per_right_chestpress <= 10:
                #print("left down val: ", per_left)
                if dir_right_unsuccessful_chestpress == 1:
                    unsuccessful_reps_count_right_chestpress += 0.5
                    dir_right_unsuccessful_chestpress = 0
                    print("DOWN RIGHT WRONG", unsuccessful_reps_count_right_chestpress)

            if per_right_chestpress == success_threshold_chestpress:
                if dir_right_chestpress == 0:
                    successful_reps_count_right_chestpress += 0.5
                    dir_right_chestpress = 1
                    cooldown_timer_chestpress = cooldown_duration_chestpress
            elif per_right_chestpress == atrest_value_chestpress: 
                if dir_right_chestpress == 1:
                    successful_reps_count_right_chestpress += 0.5
                    dir_right_chestpress = 0
                    cooldown_timer_chestpress = cooldown_duration_chestpress

            # feedback for left hand  # TO BE FETCHED 
            feedback_left_chestpress = detector_chestpress.feedback_chestpress(per_left_chestpress)

            detector_chestpress.update_next_per_left(per_left_chestpress)

            # feedback for right hand  # TO BE FETCHED 
            feedback_right_chestpress = detector_chestpress.feedback_chestpress(per_right_chestpress)

            detector_chestpress.update_next_per_left(per_right_chestpress)

        # label
        cvzone.putTextRect(img, 'Front Chest Press', [430, 30], thickness=2, border=2, scale=1.5)


        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time_chestpress)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # bar
        cv2.putText(img, f"R {int(per_right_chestpress)}%" , (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_chestpress)), (50, 400), color_right_chestpress, -1)

        cv2.putText(img, f"L {int(per_left_chestpress)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_chestpress)), (995, 400), color_left_chestpress, -1)

    #count
    cv2.rectangle(img, (20, 20), (140, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(successful_reps_count_right_chestpress)}/5", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (150, 20), (270, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(successful_reps_count_left_chestpress)}/5", (160, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255 ,255), 7)

    if remaining_time_chestpress <= 0:
        cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
        display_info_chestpress = False
        exercise_mode = "rest_chestpress"
        rest_chestpress_start_time = time.time()

    total_reps_count_left_chestpress = successful_reps_count_left_chestpress + unsuccessful_reps_count_left_chestpress
    total_reps_count_right_chestpress = successful_reps_count_right_chestpress + unsuccessful_reps_count_right_chestpress

    if successful_reps_count_right_chestpress >= 5 and successful_reps_count_left_chestpress >= 5:
        cvzone.putTextRect(img, 'All Repetitions Completed', [420, 30], thickness=2, border=2, scale=2.5)
        display_info_chestpress = False
        # General feedback after finishing the exercise # TO BE FETCHED
        if dir_gen_feedback_chestpress == 0:
            general_feedback_left_chestpress = detector_chestpress.left_arm_feedback(total_reps_count_left_chestpress)
            general_feedback_right_chestpress = detector_chestpress.right_arm_feedback(total_reps_count_right_chestpress)
            dir_gen_feedback_chestpress = 1
            display_info_chestpress = False
            exercise_mode = "rest_chestpress"
            rest_chestpress_start_time = time.time()
            print(f"{general_feedback_left_chestpress} {general_feedback_right_chestpress}")


    if unsuccessful_reps_count_left_chestpress >= 2 and unsuccessful_reps_count_right_chestpress >= 2:
        cvzone.putTextRect(img, 'You have made 2 unsuccessful tries for both arms. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_chestpress = False

        if dir_gen_feedback_unsuccessful_chestpress == 0:
            general_feedback_left_chestpress = detector_chestpress.left_arm_unsuccessful_feedback(total_reps_count_left_chestpress)
            general_feedback_right_chestpress = detector_chestpress.right_arm_unsuccessful_feedback(total_reps_count_right_chestpress)
            dir_gen_feedback_unsuccessful_chestpress = 1
            display_info_chestpress = False
            exercise_mode = "rest_chestpress"
            rest_chestpress_start_time = time.time()
    
    
    if unsuccessful_reps_count_left_chestpress >= 2:
        cvzone.putTextRect(img, 'You have made 2 unsuccessful tries for left arm. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_chestpress = False

        if dir_gen_feedback_unsuccessful_chestpress == 0:
            general_feedback_left_chestpress = detector_chestpress.left_arm_unsuccessful_feedback(total_reps_count_left_chestpress)
            dir_gen_feedback_unsuccessful_chestpress = 1
            display_info_chestpress = False
            exercise_mode = "rest_chestpress"
            rest_chestpress_start_time = time.time()

    if unsuccessful_reps_count_right_chestpress >= 2:
        cvzone.putTextRect(img, 'You have made 2 unsuccessful tries for right arm. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_chestpress = False

        if dir_gen_feedback_unsuccessful_chestpress == 0:
            general_feedback_right_chestpress = detector_chestpress.right_arm_unsuccessful_feedback(total_reps_count_right_chestpress)
            dir_gen_feedback_unsuccessful_chestpress == 1
            display_info_chestpress = False
            exercise_mode = "rest_chestpress"
            rest_chestpress_start_time = time.time()

    return img

def rest_chestpress(img):
    global exercise_mode, rest_chestpress_start_time, start_time1_chestpress_set2
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
        start_time1_chestpress_set2 = time.time()
    return img

def detect_chestpress_set2(img):
    global dir_left_chestpress_set2, dir_right_chestpress_set2, display_info_chestpress_set2, orientation_chestpress_set2, orientation2_chestpress_set2, per_right_chestpress_set2, per_left_chestpress_set2, bar_left_chestpress_set2, bar_right_chestpress_set2, color_right_chestpress_set2, color_left_chestpress_set2, feedback_left_chestpress_set2, feedback_right_chestpress_set2, success_threshold_chestpress_set2, atrest_value_chestpress_set2, unsuccessful_reps_count_left_chestpress_set2, successful_reps_count_left_chestpress_set2, unsuccessful_reps_count_right_chestpress_set2, successful_reps_count_right_chestpress_set2, dir_left_unsuccessful_chestpress_set2, dir_right_unsuccessful_chestpress_set2, total_reps_count_chestpress_set2, total_reps_count_left_chestpress_set2, total_reps_count_right_chestpress_set2, start_time1_chestpress_set2, start_time2_chestpress_set2, start_time3_chestpress_set2, time_threshold_chestpress_set2, within_range_time1_chestpress_set2, within_range_time2_chestpress_set2, general_feedback_left_chestpress_set2, general_feedback_right_chestpress_set2, dir_gen_feedback_chestpress_set2, dir_gen_feedback_unsuccessful_chestpress_set2, cooldown_timer_chestpress_set2, cooldown_duration_chestpress_set2, angle_left_chestpress_set2, angle_right_chestpress_set2, rest_chestpress_start_time_set2, exercise_mode

    img = cv2.resize(img, (1280, 720))

    # Timer - starts timer based on set duration
    elapsed_time_chestpress = time.time() - start_time1_chestpress_set2
    remaining_time_chestpress = max(0, 10 - elapsed_time_chestpress)


    if display_info_chestpress_set2:  # Check if to display counter, bar, and percentage
        img = detector_chestpress.findPose(img, False) # initializes img as variable for findpose function
        lmList_chestpress = detector_chestpress.findPosition(img, False) # initializes lmList_bicep as variable for findPosition function

        # Define hand angles outside the if statement
        if len(lmList_chestpress) != 0:
            angle_left_chestpress_set2 = detector_chestpress.findAngle(img, 11, 13, 15)
            angle_right_chestpress_set2 = detector_chestpress.findAngle(img, 12, 14, 16) # defines right arm landmark keypoints
            # (refer to mediapipe landmark mapping for number equivalent)

            per_left_chestpress_set2 = np.interp(angle_left_chestpress_set2, (60, 200), (0, 100)) # first parenthesis, the value threshold of the angle. Second, represents the interp value
            bar_left_chestpress_set2 = np.interp(angle_left_chestpress_set2, (60, 200), (400, 200)) # 

            per_right_chestpress_set2 = np.interp(angle_right_chestpress_set2, (150, 300), (100, 0)) # 
            bar_right_chestpress_set2 = np.interp(angle_right_chestpress_set2, (150, 300), (200, 400)) # 


            if int(per_left_chestpress_set2) == 100:
                color_left_chestpress_set2 = (0, 255, 0)  # Change color of left leg bar to green
            else:
                color_left_chestpress_set2 = (0, 0, 255)
            
            if int(per_right_chestpress_set2) == 100:
                color_right_chestpress_set2 = (0, 255, 0)
            else:
                color_right_chestpress_set2 = (0, 0, 255)

            #left
            if 40 <= per_left_chestpress_set2 <= 90:
                # Increment the time within range
                within_range_time1_chestpress_set2 += time.time() - start_time2_chestpress_set2

                # Check if peak value has been within range for the specified time
                if within_range_time1_chestpress_set2 >= time_threshold_chestpress_set2:
                    if dir_left_unsuccessful_chestpress_set2 == 0:
                        unsuccessful_reps_count_left_chestpress_set2 += 0.5
                        dir_left_unsuccessful_chestpress_set2 = 1
                        #print("UP WRONG LEFT: ", unsuccessful_reps_count_left_chestpress_set2)

            else:
                within_range_time1_chestpress_set2 = 0
                # Update the start time to the current time
                start_time2_chestpress_set2 = time.time()

            if 1 <= per_left_chestpress_set2 <= 10:
                if dir_left_unsuccessful_chestpress_set2 == 1:
                    unsuccessful_reps_count_left_chestpress_set2 += 0.5
                    dir_left_unsuccessful_chestpress_set2 = 0
                    #print("DOWN WRONG LEFT: ", unsuccessful_reps_count_left_chestpress_set2)

            if per_left_chestpress_set2 == success_threshold_chestpress_set2:
                if dir_left_chestpress_set2 == 0:
                    successful_reps_count_left_chestpress_set2 += 0.5
                    dir_left_chestpress_set2 = 1

            elif per_left_chestpress_set2 == atrest_value_chestpress_set2:
                if dir_left_chestpress_set2 == 1:
                    successful_reps_count_left_chestpress_set2 += 0.5
                    dir_left_chestpress_set2 = 0

            # right
            if 40 <= per_right_chestpress_set2 <= 90:
                # Increment the time within range
                within_range_time2_chestpress_set2 += time.time() - start_time3_chestpress_set2

                # Check if peak value has been within range for the specified time
                if within_range_time2_chestpress_set2 >= time_threshold_chestpress_set2:
                    if dir_right_unsuccessful_chestpress_set2 == 0:
                        unsuccessful_reps_count_right_chestpress_set2 += 0.5
                        dir_right_unsuccessful_chestpress_set2 = 1
                        #print("UP RIGHT WRONG", unsuccessful_reps_count_right_chestpress_set2)
            else:
                within_range_time2_chestpress_set2 = 0
                # Update the start time to the current time
                start_time3_chestpress_set2 = time.time()

            if 1 <= per_right_chestpress_set2 <= 10:
                #print("left down val: ", per_left)
                if dir_right_unsuccessful_chestpress_set2 == 1:
                    unsuccessful_reps_count_right_chestpress_set2 += 0.5
                    dir_right_unsuccessful_chestpress_set2 = 0
                    #print("DOWN RIGHT WRONG", unsuccessful_reps_count_right_chestpress_set2)

            if per_right_chestpress_set2 == success_threshold_chestpress_set2:
                if dir_right_chestpress_set2 == 0:
                    successful_reps_count_right_chestpress_set2 += 0.5
                    dir_right_chestpress_set2 = 1
                    cooldown_timer_chestpress_set2 = cooldown_duration_chestpress_set2
            elif per_right_chestpress_set2 == atrest_value_chestpress_set2: 
                if dir_right_chestpress_set2 == 1:
                    successful_reps_count_right_chestpress_set2 += 0.5
                    dir_right_chestpress_set2 = 0
                    cooldown_timer_chestpress_set2 = cooldown_duration_chestpress_set2

            # feedback for left hand  # TO BE FETCHED 
            feedback_left_chestpress_set2 = detector_chestpress.feedback_chestpress(per_left_chestpress_set2)

            detector_chestpress.update_next_per_left(per_left_chestpress_set2)

            # feedback for right hand  # TO BE FETCHED 
            feedback_right_chestpress_set2 = detector_chestpress.feedback_chestpress(per_right_chestpress_set2)

            detector_chestpress.update_next_per_left(per_right_chestpress_set2)

        # label
        cvzone.putTextRect(img, 'Front Chest Press SET 2', [430, 30], thickness=2, border=2, scale=1.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time_chestpress)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # bar
        cv2.putText(img, f"R {int(per_right_chestpress_set2)}%" , (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_chestpress_set2)), (50, 400), color_right_chestpress_set2, -1)

        cv2.putText(img, f"L {int(per_left_chestpress_set2)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_chestpress_set2)), (995, 400), color_left_chestpress_set2, -1)

    #count
    cv2.rectangle(img, (20, 20), (140, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(successful_reps_count_right_chestpress_set2)}/10", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (150, 20), (270, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(successful_reps_count_left_chestpress_set2)}/10", (160, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255 ,255), 7)

    if remaining_time_chestpress <= 0:
        cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
        display_info_chestpress_set2 = False
        exercise_mode = "rest_chestpress_set2"
        rest_chestpress_start_time_set2 = time.time()

    total_reps_count_left_chestpress_set2 = successful_reps_count_left_chestpress_set2 + unsuccessful_reps_count_left_chestpress_set2
    total_reps_count_right_chestpress_set2 = successful_reps_count_right_chestpress_set2 + unsuccessful_reps_count_right_chestpress_set2

    if successful_reps_count_right_chestpress_set2 >= 10 and successful_reps_count_left_chestpress_set2 >= 10:
        cvzone.putTextRect(img, 'All Repetitions Completed', [420, 30], thickness=2, border=2, scale=2.5)
        display_info_chestpress_set2 = False
        # General feedback after finishing the exercise # TO BE FETCHED
        if dir_gen_feedback_chestpress_set2 == 0:
            general_feedback_left_chestpress_set2 = detector_chestpress.left_arm_feedback(total_reps_count_left_chestpress_set2)
            general_feedback_right_chestpress_set2 = detector_chestpress.right_arm_feedback(total_reps_count_right_chestpress_set2)
            dir_gen_feedback_chestpress_set2 = 1
            display_info_chestpress_set2 = False
            exercise_mode = "rest_chestpress_set2"
            rest_chestpress_start_time_set2 = time.time()
            print(f"{general_feedback_left_chestpress_set2} {general_feedback_right_chestpress_set2}")


    if unsuccessful_reps_count_left_chestpress_set2 >= 2 and unsuccessful_reps_count_right_chestpress_set2 >= 2:
        cvzone.putTextRect(img, 'You have made 2 unsuccessful tries for both arms. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_chestpress_set2 = False

        if dir_gen_feedback_unsuccessful_chestpress_set2 == 0:
            general_feedback_left_chestpress_set2 = detector_chestpress.left_arm_unsuccessful_feedback(total_reps_count_left_chestpress_set2)
            general_feedback_right_chestpress_set2 = detector_chestpress.right_arm_unsuccessful_feedback(total_reps_count_right_chestpress_set2)
            dir_gen_feedback_unsuccessful_chestpress_set2 = 1
            display_info_chestpress_set2 = False
            exercise_mode = "rest_chestpress_set2"
            rest_chestpress_start_time_set2 = time.time()
    
    
    if unsuccessful_reps_count_left_chestpress_set2 >= 2:
        cvzone.putTextRect(img, 'You have made 2 unsuccessful tries for left arm. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_chestpress_set2 = False

        if dir_gen_feedback_unsuccessful_chestpress_set2 == 0:
            general_feedback_left_chestpress_set2 = detector_chestpress.left_arm_unsuccessful_feedback(total_reps_count_left_chestpress_set2)
            dir_gen_feedback_unsuccessful_chestpress_set2 = 1
            display_info_chestpress_set2 = False
            exercise_mode = "rest_chestpress_set2"
            rest_chestpress_start_time_set2 = time.time()

    if unsuccessful_reps_count_right_chestpress_set2 >= 2:
        cvzone.putTextRect(img, 'You have made 2 unsuccessful tries for right arm. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_chestpress_set2 = False

        if dir_gen_feedback_unsuccessful_chestpress_set2 == 0:
            general_feedback_right_chestpress_set2 = detector_chestpress.right_arm_unsuccessful_feedback(total_reps_count_right_chestpress_set2)
            dir_gen_feedback_unsuccessful_chestpress_set2 == 1
            display_info_chestpress_set2 = False
            exercise_mode = "rest_chestpress_set2"
            rest_chestpress_start_time_set2 = time.time()

    return img

def rest_chestpress_set2(img):
    global exercise_mode, rest_chestpress_start_time_set2, start_time1_chestpress_set3
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
        start_time1_chestpress_set3 = time.time()

    return img

def detect_chestpress_set3(img):

    global dir_left_chestpress_set3, dir_right_chestpress_set3, display_info_chestpress_set3, orientation_chestpress_set3, orientation2_chestpress_set3, per_right_chestpress_set3, per_left_chestpress_set3, bar_left_chestpress_set3, bar_right_chestpress_set3, color_right_chestpress_set3, color_left_chestpress_set3, feedback_left_chestpress_set3, feedback_right_chestpress_set3, success_threshold_chestpress_set3, atrest_value_chestpress_set3, unsuccessful_reps_count_left_chestpress_set3, successful_reps_count_left_chestpress_set3, unsuccessful_reps_count_right_chestpress_set3, successful_reps_count_right_chestpress_set3, dir_left_unsuccessful_chestpress_set3, dir_right_unsuccessful_chestpress_set3, total_reps_count_chestpress_set3, total_reps_count_left_chestpress_set3, total_reps_count_right_chestpress_set3, start_time1_chestpress_set3, start_time2_chestpress_set3, start_time3_chestpress_set3, time_threshold_chestpress_set3, within_range_time1_chestpress_set3, within_range_time2_chestpress_set3, general_feedback_left_chestpress_set3, general_feedback_right_chestpress_set3, dir_gen_feedback_chestpress_set3, dir_gen_feedback_unsuccessful_chestpress_set3, cooldown_timer_chestpress_set3, cooldown_duration_chestpress_set3, angle_left_chestpress_set3, angle_right_chestpress_set3, rest_chestpress_start_time_set3, exercise_mode

    img = cv2.resize(img, (1280, 720))

    # Timer - starts timer based on set duration
    elapsed_time_chestpress = time.time() - start_time1_chestpress_set3
    remaining_time_chestpress = max(0, 10 - elapsed_time_chestpress)


    if display_info_chestpress_set3:  # Check if to display counter, bar, and percentage
        img = detector_chestpress.findPose(img, False) # initializes img as variable for findpose function
        lmList_chestpress = detector_chestpress.findPosition(img, False) # initializes lmList_bicep as variable for findPosition function

        # Define hand angles outside the if statement
        if len(lmList_chestpress) != 0:
            angle_left_chestpress_set3 = detector_chestpress.findAngle(img, 11, 13, 15)
            angle_right_chestpress_set3 = detector_chestpress.findAngle(img, 12, 14, 16) # defines right arm landmark keypoints
            # (refer to mediapipe landmark mapping for number equivalent)

            per_left_chestpress_set3 = np.interp(angle_left_chestpress_set3, (60, 200), (0, 100)) # first parenthesis, the value threshold of the angle. Second, represents the interp value
            bar_left_chestpress_set3 = np.interp(angle_left_chestpress_set3, (60, 200), (400, 200)) # 

            per_right_chestpress_set3 = np.interp(angle_right_chestpress_set3, (150, 300), (100, 0)) # 
            bar_right_chestpress_set3 = np.interp(angle_right_chestpress_set3, (150, 300), (200, 400)) # 


            if int(per_left_chestpress_set3) == 100:
                color_left_chestpress_set3 = (0, 255, 0)  # Change color of left leg bar to green
            else:
                color_left_chestpress_set3 = (0, 0, 255)
            
            if int(per_right_chestpress_set3) == 100:
                color_right_chestpress_set3 = (0, 255, 0)
            else:
                color_right_chestpress_set3 = (0, 0, 255)

            #left
            if 40 <= per_left_chestpress_set3 <= 90:
                # Increment the time within range
                within_range_time1_chestpress_set3 += time.time() - start_time2_chestpress_set3

                # Check if peak value has been within range for the specified time
                if within_range_time1_chestpress_set3 >= time_threshold_chestpress_set3:
                    if dir_left_unsuccessful_chestpress_set3 == 0:
                        unsuccessful_reps_count_left_chestpress_set3 += 0.5
                        dir_left_unsuccessful_chestpress_set3 = 1
                        #print("UP WRONG LEFT: ", unsuccessful_reps_count_left_chestpress_set3)

            else:
                within_range_time1_chestpress_set3 = 0
                # Update the start time to the current time
                start_time2_chestpress_set3 = time.time()

            if 1 <= per_left_chestpress_set3 <= 10:
                if dir_left_unsuccessful_chestpress_set3 == 1:
                    unsuccessful_reps_count_left_chestpress_set3 += 0.5
                    dir_left_unsuccessful_chestpress_set3 = 0
                    #print("DOWN WRONG LEFT: ", unsuccessful_reps_count_left_chestpress_set3)

            if per_left_chestpress_set3 == success_threshold_chestpress_set3:
                if dir_left_chestpress_set3 == 0:
                    successful_reps_count_left_chestpress_set3 += 0.5
                    dir_left_chestpress_set3 = 1

            elif per_left_chestpress_set3 == atrest_value_chestpress_set3:
                if dir_left_chestpress_set3 == 1:
                    successful_reps_count_left_chestpress_set3 += 0.5
                    dir_left_chestpress_set3 = 0

            # right
            if 40 <= per_right_chestpress_set3 <= 90:
                # Increment the time within range
                within_range_time2_chestpress_set3 += time.time() - start_time3_chestpress_set3

                # Check if peak value has been within range for the specified time
                if within_range_time2_chestpress_set3 >= time_threshold_chestpress_set3:
                    if dir_right_unsuccessful_chestpress_set3 == 0:
                        unsuccessful_reps_count_right_chestpress_set3 += 0.5
                        dir_right_unsuccessful_chestpress_set3 = 1
                        #print("UP RIGHT WRONG", unsuccessful_reps_count_right_chestpress_set3)
            else:
                within_range_time2_chestpress_set3 = 0
                # Update the start time to the current time
                _set3start_time3_chestpress = time.time()

            if 1 <= per_right_chestpress_set3 <= 10:
                #print("left down val: ", per_left)
                if dir_right_unsuccessful_chestpress_set3 == 1:
                    unsuccessful_reps_count_right_chestpress_set3 += 0.5
                    dir_right_unsuccessful_chestpress_set3 = 0
                    #print("DOWN RIGHT WRONG", unsuccessful_reps_count_right_chestpress_set3)

            if per_right_chestpress_set3 == success_threshold_chestpress_set3:
                if dir_right_chestpress_set3 == 0:
                    successful_reps_count_right_chestpress_set3 += 0.5
                    dir_right_chestpress_set3 = 1
                    cooldown_timer_chestpress_set3 = cooldown_duration_chestpress_set3
            elif per_right_chestpress_set3 == atrest_value_chestpress_set3: 
                if dir_right_chestpress_set3 == 1:
                    successful_reps_count_right_chestpress_set3 += 0.5
                    dir_right_chestpress_set3 = 0
                    cooldown_timer_chestpress_set3 = cooldown_duration_chestpress_set3

            # feedback for left hand  # TO BE FETCHED 
            feedback_left_chestpress_set3 = detector_chestpress.feedback_chestpress(per_left_chestpress_set3)

            detector_chestpress.update_next_per_left(per_left_chestpress_set3)

            # feedback for right hand  # TO BE FETCHED 
            feedback_right_chestpress_set3 = detector_chestpress.feedback_chestpress(per_right_chestpress_set3)

            detector_chestpress.update_next_per_left(per_right_chestpress_set3)

        # label
        cvzone.putTextRect(img, 'Front Chest Press SET 3', [430, 30], thickness=2, border=2, scale=1.5)


        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time_chestpress)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # bar
        cv2.putText(img, f"R {int(per_right_chestpress_set3)}%" , (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_chestpress_set3)), (50, 400), color_right_chestpress_set3, -1)

        cv2.putText(img, f"L {int(per_left_chestpress_set3)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_chestpress_set3)), (995, 400), color_left_chestpress_set3, -1)

    #count
    cv2.rectangle(img, (20, 20), (140, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(successful_reps_count_right_chestpress_set3)}/10", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (150, 20), (270, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(successful_reps_count_left_chestpress_set3)}/10", (160, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255 ,255), 7)

    if remaining_time_chestpress <= 0:
        cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
        display_info_chestpress_set3 = False
        exercise_mode = "rest_chestpress_set3"
        rest_chestpress_start_time_set3 = time.time()

    total_reps_count_left_chestpress_set3 = successful_reps_count_left_chestpress_set3 + unsuccessful_reps_count_left_chestpress_set3
    total_reps_count_right_chestpress_set3 = successful_reps_count_right_chestpress_set3 + unsuccessful_reps_count_right_chestpress_set3

    if successful_reps_count_right_chestpress_set3 >= 10 and successful_reps_count_left_chestpress_set3 >= 10:
        cvzone.putTextRect(img, 'All Repetitions Completed', [420, 30], thickness=2, border=2, scale=2.5)
        display_info_chestpress_set3 = False
        # General feedback after finishing the exercise # TO BE FETCHED
        if dir_gen_feedback_chestpress_set3 == 0:
            general_feedback_left_chestpress_set3 = detector_chestpress.left_arm_feedback(total_reps_count_left_chestpress_set3)
            general_feedback_right_chestpress_set3 = detector_chestpress.right_arm_feedback(total_reps_count_right_chestpress_set3)
            dir_gen_feedback_chestpress_set3 = 1
            display_info_chestpress_set3 = False
            exercise_mode = "rest_chestpress_set3"
            rest_chestpress_start_time_set3 = time.time()
            print(f"{general_feedback_left_chestpress_set3} {general_feedback_right_chestpress_set3}")


    if unsuccessful_reps_count_left_chestpress_set3 >= 2 and unsuccessful_reps_count_right_chestpress_set3 >= 2:
        cvzone.putTextRect(img, 'You have made 2 unsuccessful tries for both arms. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_chestpress_set3 = False

        if dir_gen_feedback_unsuccessful_chestpress_set3 == 0:
            general_feedback_left_chestpress_set3 = detector_chestpress.left_arm_unsuccessful_feedback(total_reps_count_left_chestpress_set3)
            general_feedback_right_chestpress_set3 = detector_chestpress.right_arm_unsuccessful_feedback(total_reps_count_right_chestpress_set3)
            dir_gen_feedback_unsuccessful_chestpress_set3 = 1
            display_info_chestpress_set3 = False
            exercise_mode = "rest_chestpress_set3"
            rest_chestpress_start_time_set3 = time.time()
    
    
    if unsuccessful_reps_count_left_chestpress_set3 >= 2:
        cvzone.putTextRect(img, 'You have made 2 unsuccessful tries for left arm. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_chestpress_set3 = False

        if dir_gen_feedback_unsuccessful_chestpress_set3 == 0:
            general_feedback_left_chestpress_set3 = detector_chestpress.left_arm_unsuccessful_feedback(total_reps_count_left_chestpress_set3)
            dir_gen_feedback_unsuccessful_chestpress_set3 = 1
            display_info_chestpress_set3 = False
            exercise_mode = "rest_chestpress_set3"
            rest_chestpress_start_time_set3 = time.time()

    if unsuccessful_reps_count_right_chestpress_set3 >= 2:
        cvzone.putTextRect(img, 'You have made 2 unsuccessful tries for right arm. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_chestpress_set3 = False

        if dir_gen_feedback_unsuccessful_chestpress_set3 == 0:
            general_feedback_right_chestpress_set3 = detector_chestpress.right_arm_unsuccessful_feedback(total_reps_count_right_chestpress_set3)
            dir_gen_feedback_unsuccessful_chestpress_set3 == 1
            display_info_chestpress_set3 = False
            exercise_mode = "rest_chestpress_set3"
            rest_chestpress_start_time_set3 = time.time()
    return img

def rest_chestpress_set3(img):
    global exercise_mode, rest_chestpress_start_time_set3, start_time1_dumbbellfrontraise
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_chestpress_start_time_set3
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "dumbbell_frontraise"
        start_time1_dumbbellfrontraise = time.time()
    return img

def detect_dumbbellfrontraise(img):
    global dir_left_dumbbellfrontraise, dir_right_dumbbellfrontraise, display_info_dumbbellfrontraise, per_right_dumbbellfrontraise, per_left_dumbbellfrontraise, bar_left_dumbbellfrontraise, bar_right_dumbbellfrontraise, color_right_dumbbellfrontraise, color_left_dumbbellfrontraise, feedback_left_dumbbellfrontraise, feedback_right_dumbbellfrontraise, success_threshold_dumbbellfrontraise, atrest_value_dumbbellfrontraise,unsuccessful_reps_count_left_dumbbellfrontraise, successful_reps_count_left_dumbbellfrontraise, unsuccessful_reps_count_right_dumbbellfrontraise, successful_reps_count_right_dumbbellfrontraise, dir_left_unsuccessful_dumbbellfrontraise, dir_right_unsuccessful_dumbbellfrontraise, total_reps_count_dumbbellfrontraise, total_reps_count_left_dumbbellfrontraise, total_reps_count_right_dumbbellfrontraise, start_time1_dumbbellfrontraise, start_time2_dumbbellfrontraise, start_time3_dumbbellfrontraise, time_threshold_dumbbellfrontraise, within_range_time1_dumbbellfrontraise, within_range_time2_dumbbellfrontraise, general_feedback_left_dumbbellfrontraise, general_feedback_right_dumbbellfrontraise, dir_gen_feedback_dumbbellfrontraise, dir_gen_feedback_unsuccessful_dumbbellfrontraise, cooldown_timer_dumbbellfrontraise, cooldown_duration_dumbbellfrontraise, angle_left_dumbbellfrontraise, angle_right_dumbbellfrontraise, rest_dumbbellfrontraise_start_time, exercise_mode

    img = cv2.resize(img, (1280, 720))

    # Timer - starts timer based on set duration
    elapsed_time_dumbbellfrontraise = time.time() - start_time1_dumbbellfrontraise
    remaining_time_dumbbellfrontraise = max(0, 10 - elapsed_time_dumbbellfrontraise)

    if display_info_dumbbellfrontraise:  # Check if to display counter, bar, and percentage
        img = detector_dumbbellfrontraise.findPose(img, False)  # initializes img as variable for findpose function
        lmList_dumbbellfrontraise = detector_dumbbellfrontraise.findPosition(img, False)  # initializes lmList as variable for findPosition function

        # Define hand angles outside the if statement
        if len(lmList_dumbbellfrontraise) != 0:

            angle_left_dumbbellfrontraise = detector_dumbbellfrontraise.findAngle(img, 15, 11, 23, 13)
            angle_right_dumbbellfrontraise = detector_dumbbellfrontraise.findAngle2(img, 24, 12, 16, 14) 

            # # Interpolate angle to percentage and position on screen
            per_left_dumbbellfrontraise = np.interp(angle_left_dumbbellfrontraise, (20, 150), (0, 100))
            bar_left_dumbbellfrontraise = np.interp(angle_left_dumbbellfrontraise, (20, 150), (400, 200))

            per_right_dumbbellfrontraise = np.interp(angle_right_dumbbellfrontraise, (20, 150), (0, 100))
            bar_right_dumbbellfrontraise = np.interp(angle_right_dumbbellfrontraise, (20, 150), (400, 200))

            if int(per_left_dumbbellfrontraise) == 100:
                color_left_dumbbellfrontraise = (0, 255, 0)  # Change color of left leg bar to green
            else:
                color_left_dumbbellfrontraise = (0, 0, 255)
            
            if int(per_right_dumbbellfrontraise) == 100:
                color_right_dumbbellfrontraise = (0, 255, 0)
            else:
                color_right_dumbbellfrontraise = (0, 0, 255)

            #left
            if 40 <= per_left_dumbbellfrontraise <= 90:
                # Increment the time within range
                within_range_time1_dumbbellfrontraise += time.time() - start_time2_dumbbellfrontraise

                # Check if peak value has been within range for the specified time
                if within_range_time1_dumbbellfrontraise >= time_threshold_dumbbellfrontraise:
                    if dir_left_unsuccessful_dumbbellfrontraise == 0:
                        unsuccessful_reps_count_left_dumbbellfrontraise += 0.5
                        dir_left_unsuccessful_dumbbellfrontraise = 1
            else:
                within_range_time1_dumbbellfrontraise = 0
                # Update the start time to the current time
                start_time2_dumbbellfrontraise = time.time()

            if 1 <= per_left_dumbbellfrontraise <= 10:
                if dir_left_unsuccessful_dumbbellfrontraise == 1:
                    unsuccessful_reps_count_left_dumbbellfrontraise += 0.5
                    dir_left_unsuccessful_dumbbellfrontraise = 0

            if per_left_dumbbellfrontraise == success_threshold_dumbbellfrontraise:
                if dir_left_dumbbellfrontraise == 0:
                    successful_reps_count_left_dumbbellfrontraise += 0.5
                    dir_left_dumbbellfrontraise = 1

            elif per_left_dumbbellfrontraise == atrest_value_dumbbellfrontraise:
                if dir_left_dumbbellfrontraise == 1:
                    successful_reps_count_left_dumbbellfrontraise += 0.5
                    dir_left_dumbbellfrontraise = 0

            # right
            if 40 <= per_right_dumbbellfrontraise <= 90:
                # Increment the time within range
                within_range_time2_dumbbellfrontraise += time.time() - start_time3_dumbbellfrontraise

                # Check if peak value has been within range for the specified time
                if within_range_time2_dumbbellfrontraise >= time_threshold_dumbbellfrontraise:
                    if dir_right_unsuccessful_dumbbellfrontraise == 0:
                        unsuccessful_reps_count_right_dumbbellfrontraise += 0.5
                        dir_right_unsuccessful_dumbbellfrontraise = 1
            else:
                within_range_time2_dumbbellfrontraise = 0
                # Update the start time to the current time
                start_time3_dumbbellfrontraise = time.time()

            if 1 <= per_right_dumbbellfrontraise <= 10:
                #print("left down val: ", per_left)
                if dir_right_unsuccessful_dumbbellfrontraise == 1:
                    unsuccessful_reps_count_right_dumbbellfrontraise += 0.5
                    dir_right_unsuccessful_dumbbellfrontraise = 0

            if per_right_dumbbellfrontraise == success_threshold_dumbbellfrontraise:
                if dir_right_dumbbellfrontraise == 0:
                    successful_reps_count_right_dumbbellfrontraise += 0.5
                    dir_right_dumbbellfrontraise = 1
                    cooldown_timer_dumbbellfrontraise = cooldown_duration_dumbbellfrontraise
            elif per_right_dumbbellfrontraise == atrest_value_dumbbellfrontraise: 
                if dir_right_dumbbellfrontraise == 1:
                    successful_reps_count_right_dumbbellfrontraise += 0.5
                    dir_right_dumbbellfrontraise = 0
                    cooldown_timer_dumbbellfrontraise = cooldown_duration_dumbbellfrontraise

            # feedback for left hand  # TO BE FETCHED 
            feedback_left_dumbbellfrontraise = detector_dumbbellfrontraise.feedback_dumbbellfrontraise(per_left_dumbbellfrontraise)

            detector_dumbbellfrontraise.update_next_per_left(per_left_dumbbellfrontraise)

            # feedback for right hand  # TO BE FETCHED 
            feedback_right_dumbbellfrontraise = detector_dumbbellfrontraise.feedback_dumbbellfrontraise(per_right_dumbbellfrontraise)

            detector_dumbbellfrontraise.update_next_per_left(per_right_dumbbellfrontraise)

        # label
        cvzone.putTextRect(img, 'Dumbbell Raise Front', [430, 30], thickness=2, border=2, scale=1.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time_dumbbellfrontraise)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # bar
        cv2.putText(img, f"R {int(per_right_dumbbellfrontraise)}%", (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_dumbbellfrontraise)), (50, 400), color_right_dumbbellfrontraise, -1)

        cv2.putText(img, f"L {int(per_left_dumbbellfrontraise)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_dumbbellfrontraise)), (995, 400), color_left_dumbbellfrontraise, -1)

    # count
    cv2.rectangle(img, (20, 20), (140, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(successful_reps_count_right_dumbbellfrontraise)}/10", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (150, 20), (270, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(successful_reps_count_left_dumbbellfrontraise)}/10", (160, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    if remaining_time_dumbbellfrontraise <= 0:
        cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
        display_info_dumbbellfrontraise = False
        exercise_mode = "rest_dumbbellfrontraise"
        rest_dumbbellfrontraise_start_time = time.time()

    total_reps_count_left_dumbbellfrontraise = successful_reps_count_left_dumbbellfrontraise + unsuccessful_reps_count_left_dumbbellfrontraise
    total_reps_count_right_dumbbellfrontraise = successful_reps_count_right_dumbbellfrontraise + unsuccessful_reps_count_right_dumbbellfrontraise

    if successful_reps_count_right_dumbbellfrontraise >= 10 and successful_reps_count_left_dumbbellfrontraise >= 10:
        cvzone.putTextRect(img, 'All Repetitions Completed', [420, 30], thickness=2, border=2, scale=2.5)
        display_info_dumbbellfrontraise = False
        # General feedback after finishing the exercise # TO BE FETCHED
        if dir_gen_feedback_dumbbellfrontraise == 0:
            general_feedback_left_dumbbellfrontraise = detector_dumbbellfrontraise.left_arm_feedback(total_reps_count_left_dumbbellfrontraise)
            general_feedback_right_dumbbellfrontraise = detector_dumbbellfrontraise.right_arm_feedback(total_reps_count_right_dumbbellfrontraise)
            dir_gen_feedback_dumbbellfrontraise = 1
            exercise_mode = "rest_dumbbellfrontraise"
            rest_dumbbellfrontraise_start_time = time.time()

    if unsuccessful_reps_count_left_dumbbellfrontraise >= 2 and unsuccessful_reps_count_right_dumbbellfrontraise >= 2:
        cvzone.putTextRect(img, 'You have made 2 unsuccessful tries for both arms. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_dumbbellfrontraise = False

        if dir_gen_feedback_unsuccessful_dumbbellfrontraise == 0:
            general_feedback_left_dumbbellfrontraise = detector_dumbbellfrontraise.left_arm_unsuccessful_feedback(total_reps_count_left_dumbbellfrontraise)
            general_feedback_right_dumbbellfrontraise = detector_dumbbellfrontraise.right_arm_unsuccessful_feedback(total_reps_count_right_dumbbellfrontraise)
            dir_gen_feedback_unsuccessful_dumbbellfrontraise = 1
            exercise_mode = "rest_dumbbellfrontraise"
            rest_dumbbellfrontraise_start_time = time.time()
    
    if unsuccessful_reps_count_left_dumbbellfrontraise >= 2:
        cvzone.putTextRect(img, 'You have made 2 unsuccessful tries for left arm. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_dumbbellfrontraise = False

        if dir_gen_feedback_unsuccessful_dumbbellfrontraise == 0:
            general_feedback_left_dumbbellfrontraise = detector_dumbbellfrontraise.left_arm_unsuccessful_feedback(total_reps_count_left_dumbbellfrontraise)
            dir_gen_feedback_unsuccessful_dumbbellfrontraise = 1
            exercise_mode = "rest_dumbbellfrontraise"
            rest_dumbbellfrontraise_start_time = time.time()

    if unsuccessful_reps_count_right_dumbbellfrontraise >= 2:
        cvzone.putTextRect(img, 'You have made 2 unsuccessful tries for right arm. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_dumbbellfrontraise = False

        if dir_gen_feedback_unsuccessful_dumbbellfrontraise == 0:
            general_feedback_right_dumbbellfrontraise = detector_dumbbellfrontraise.right_arm_unsuccessful_feedback(total_reps_count_right_dumbbellfrontraise)
            dir_gen_feedback_unsuccessful_dumbbellfrontraise == 1
            exercise_mode = "rest_dumbbellfrontraise"
            rest_dumbbellfrontraise_start_time = time.time()

    return img

def rest_dumbbellfrontraise(img):
    global exercise_mode, rest_dumbbellfrontraise_start_time, start_time1_dumbbellfrontraise_set2
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
        start_time1_dumbbellfrontraise_set2 = time.time()

    return img

def detect_dumbbellfrontraise_set2(img):
    global dir_left_dumbbellfrontraise_set2, dir_right_dumbbellfrontraise_set2, display_info_dumbbellfrontraise_set2, per_right_dumbbellfrontraise_set2, per_left_dumbbellfrontraise_set2, bar_left_dumbbellfrontraise_set2, bar_right_dumbbellfrontraise_set2, color_right_dumbbellfrontraise_set2, color_left_dumbbellfrontraise_set2, feedback_left_dumbbellfrontraise_set2, feedback_right_dumbbellfrontraise_set2, success_threshold_dumbbellfrontraise_set2, atrest_value_dumbbellfrontraise_set2,unsuccessful_reps_count_left_dumbbellfrontraise_set2, successful_reps_count_left_dumbbellfrontraise_set2, unsuccessful_reps_count_right_dumbbellfrontraise_set2, successful_reps_count_right_dumbbellfrontraise_set2, dir_left_unsuccessful_dumbbellfrontraise_set2, dir_right_unsuccessful_dumbbellfrontraise_set2, total_reps_count_dumbbellfrontraise_set2, total_reps_count_left_dumbbellfrontraise_set2, total_reps_count_right_dumbbellfrontraise_set2, start_time1_dumbbellfrontraise_set2, start_time2_dumbbellfrontraise_set2, start_time3_dumbbellfrontraise_set2, time_threshold_dumbbellfrontraise_set2, within_range_time1_dumbbellfrontraise_set2, within_range_time2_dumbbellfrontraise_set2, general_feedback_left_dumbbellfrontraise_set2, general_feedback_right_dumbbellfrontraise_set2, dir_gen_feedback_dumbbellfrontraise_set2, dir_gen_feedback_unsuccessful_dumbbellfrontraise_set2, cooldown_timer_dumbbellfrontraise_set2, cooldown_duration_dumbbellfrontraise_set2, angle_left_dumbbellfrontraise_set2, angle_right_dumbbellfrontraise_set2, rest_dumbbellfrontraise_start_time_set2, exercise_mode

    img = cv2.resize(img, (1280, 720))

    # Timer - starts timer based on set duration
    elapsed_time_dumbbellfrontraise = time.time() - start_time1_dumbbellfrontraise_set2
    remaining_time_dumbbellfrontraise = max(0, 10 - elapsed_time_dumbbellfrontraise)

    if display_info_dumbbellfrontraise_set2:  # Check if to display counter, bar, and percentage
        img = detector_dumbbellfrontraise.findPose(img, False)  # initializes img as variable for findpose function
        lmList_dumbbellfrontraise = detector_dumbbellfrontraise.findPosition(img, False)  # initializes lmList as variable for findPosition function

        # Define hand angles outside the if statement
        if len(lmList_dumbbellfrontraise) != 0:

            angle_left_dumbbellfrontraise_set2 = detector_dumbbellfrontraise.findAngle(img, 15, 11, 23, 13)
            angle_right_dumbbellfrontraise_set2 = detector_dumbbellfrontraise.findAngle2(img, 24, 12, 16, 14) 

            # # Interpolate angle to percentage and position on screen
            per_left_dumbbellfrontraise_set2 = np.interp(angle_left_dumbbellfrontraise_set2, (20, 150), (0, 100))
            bar_left_dumbbellfrontraise_set2 = np.interp(angle_left_dumbbellfrontraise_set2, (20, 150), (400, 200))

            per_right_dumbbellfrontraise_set2 = np.interp(angle_right_dumbbellfrontraise_set2, (20, 150), (0, 100))
            bar_right_dumbbellfrontraise_set2 = np.interp(angle_right_dumbbellfrontraise_set2, (20, 150), (400, 200))

            if int(per_left_dumbbellfrontraise_set2) == 100:
                color_left_dumbbellfrontraise_set2 = (0, 255, 0)  # Change color of left leg bar to green
            else:
                color_left_dumbbellfrontraise_set2 = (0, 0, 255)
            
            if int(per_right_dumbbellfrontraise_set2) == 100:
                color_right_dumbbellfrontraise_set2 = (0, 255, 0)
            else:
                color_right_dumbbellfrontraise_set2 = (0, 0, 255)

            #left
            if 40 <= per_left_dumbbellfrontraise_set2 <= 90:
                # Increment the time within range
                within_range_time1_dumbbellfrontraise_set2 += time.time() - start_time2_dumbbellfrontraise_set2

                # Check if peak value has been within range for the specified time
                if within_range_time1_dumbbellfrontraise_set2 >= time_threshold_dumbbellfrontraise_set2:
                    if dir_left_unsuccessful_dumbbellfrontraise_set2 == 0:
                        unsuccessful_reps_count_left_dumbbellfrontraise_set2 += 0.5
                        dir_left_unsuccessful_dumbbellfrontraise_set2 = 1
            else:
                within_range_time1_dumbbellfrontraise_set2 = 0
                # Update the start time to the current time
                start_time2_dumbbellfrontraise_set2 = time.time()

            if 1 <= per_left_dumbbellfrontraise_set2 <= 10:
                if dir_left_unsuccessful_dumbbellfrontraise_set2 == 1:
                    unsuccessful_reps_count_left_dumbbellfrontraise_set2 += 0.5
                    dir_left_unsuccessful_dumbbellfrontraise_set2 = 0

            if per_left_dumbbellfrontraise_set2 == success_threshold_dumbbellfrontraise_set2:
                if dir_left_dumbbellfrontraise_set2 == 0:
                    successful_reps_count_left_dumbbellfrontraise_set2 += 0.5
                    dir_left_dumbbellfrontraise_set2 = 1

            elif per_left_dumbbellfrontraise_set2 == atrest_value_dumbbellfrontraise_set2:
                if dir_left_dumbbellfrontraise_set2 == 1:
                    successful_reps_count_left_dumbbellfrontraise_set2 += 0.5
                    dir_left_dumbbellfrontraise_set2 = 0

            # right
            if 40 <= per_right_dumbbellfrontraise_set2 <= 90:
                # Increment the time within range
                within_range_time2_dumbbellfrontraise_set2 += time.time() - start_time3_dumbbellfrontraise_set2

                # Check if peak value has been within range for the specified time
                if within_range_time2_dumbbellfrontraise_set2 >= time_threshold_dumbbellfrontraise_set2:
                    if dir_right_unsuccessful_dumbbellfrontraise_set2 == 0:
                        unsuccessful_reps_count_right_dumbbellfrontraise_set2 += 0.5
                        dir_right_unsuccessful_dumbbellfrontraise_set2 = 1
            else:
                within_range_time2_dumbbellfrontraise_set2 = 0
                # Update the start time to the current time
                start_time3_dumbbellfrontraise_set2 = time.time()

            if 1 <= per_right_dumbbellfrontraise_set2 <= 10:
                #print("left down val: ", per_left)
                if dir_right_unsuccessful_dumbbellfrontraise_set2 == 1:
                    unsuccessful_reps_count_right_dumbbellfrontraise_set2 += 0.5
                    dir_right_unsuccessful_dumbbellfrontraise_set2 = 0

            if per_right_dumbbellfrontraise_set2 == success_threshold_dumbbellfrontraise_set2:
                if dir_right_dumbbellfrontraise_set2 == 0:
                    successful_reps_count_right_dumbbellfrontraise_set2 += 0.5
                    dir_right_dumbbellfrontraise_set2 = 1
                    cooldown_timer_dumbbellfrontraise_set2 = cooldown_duration_dumbbellfrontraise_set2
            elif per_right_dumbbellfrontraise_set2 == atrest_value_dumbbellfrontraise_set2: 
                if dir_right_dumbbellfrontraise_set2 == 1:
                    successful_reps_count_right_dumbbellfrontraise_set2 += 0.5
                    dir_right_dumbbellfrontraise_set2 = 0
                    cooldown_timer_dumbbellfrontraise_set2 = cooldown_duration_dumbbellfrontraise_set2

            # feedback for left hand  # TO BE FETCHED 
            feedback_left_dumbbellfrontraise_set2 = detector_dumbbellfrontraise.feedback_dumbbellfrontraise(per_left_dumbbellfrontraise_set2)

            detector_dumbbellfrontraise.update_next_per_left(per_left_dumbbellfrontraise_set2)

            # feedback for right hand  # TO BE FETCHED 
            feedback_right_dumbbellfrontraise_set2 = detector_dumbbellfrontraise.feedback_dumbbellfrontraise(per_right_dumbbellfrontraise_set2)

            detector_dumbbellfrontraise.update_next_per_left(per_right_dumbbellfrontraise_set2)

        # label
        cvzone.putTextRect(img, 'Dumbbell Raise Front SET 2', [430, 30], thickness=2, border=2, scale=1.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time_dumbbellfrontraise)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # bar
        cv2.putText(img, f"R {int(per_right_dumbbellfrontraise_set2)}%", (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_dumbbellfrontraise_set2)), (50, 400), color_right_dumbbellfrontraise_set2, -1)

        cv2.putText(img, f"L {int(per_left_dumbbellfrontraise_set2)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_dumbbellfrontraise_set2)), (995, 400), color_left_dumbbellfrontraise_set2, -1)

    # count
    cv2.rectangle(img, (20, 20), (140, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(successful_reps_count_right_dumbbellfrontraise_set2)}/10", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (150, 20), (270, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(successful_reps_count_left_dumbbellfrontraise_set2)}/10", (160, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    if remaining_time_dumbbellfrontraise <= 0:
        cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
        display_info_dumbbellfrontraise_set2 = False
        exercise_mode = "rest_dumbbellfrontraise_set2"
        rest_dumbbellfrontraise_start_time_set2 = time.time()

    total_reps_count_left_dumbbellfrontraise_set2 = successful_reps_count_left_dumbbellfrontraise_set2 + unsuccessful_reps_count_left_dumbbellfrontraise_set2
    total_reps_count_right_dumbbellfrontraise_set2 = successful_reps_count_right_dumbbellfrontraise_set2 + unsuccessful_reps_count_right_dumbbellfrontraise_set2

    if successful_reps_count_right_dumbbellfrontraise_set2 >= 10 and successful_reps_count_left_dumbbellfrontraise_set2 >= 10:
        cvzone.putTextRect(img, 'All Repetitions Completed', [420, 30], thickness=2, border=2, scale=2.5)
        display_info_dumbbellfrontraise_set2 = False
        # General feedback after finishing the exercise # TO BE FETCHED
        if dir_gen_feedback_dumbbellfrontraise_set2 == 0:
            general_feedback_left_dumbbellfrontraise_set2 = detector_dumbbellfrontraise.left_arm_feedback(total_reps_count_left_dumbbellfrontraise_set2)
            general_feedback_right_dumbbellfrontraise_set2 = detector_dumbbellfrontraise.right_arm_feedback(total_reps_count_right_dumbbellfrontraise_set2)
            dir_gen_feedback_dumbbellfrontraise_set2 = 1
            exercise_mode = "rest_dumbbellfrontraise_set2"
            rest_dumbbellfrontraise_start_time_set2 = time.time()

    if unsuccessful_reps_count_left_dumbbellfrontraise_set2 >= 2 and unsuccessful_reps_count_right_dumbbellfrontraise_set2 >= 2:
        cvzone.putTextRect(img, 'You have made 2 unsuccessful tries for both arms. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_dumbbellfrontraise_set2 = False

        if dir_gen_feedback_unsuccessful_dumbbellfrontraise_set2 == 0:
            general_feedback_left_dumbbellfrontraise_set2 = detector_dumbbellfrontraise.left_arm_unsuccessful_feedback(total_reps_count_left_dumbbellfrontraise_set2)
            general_feedback_right_dumbbellfrontraise_set2 = detector_dumbbellfrontraise.right_arm_unsuccessful_feedback(total_reps_count_right_dumbbellfrontraise_set2)
            dir_gen_feedback_unsuccessful_dumbbellfrontraise_set2 = 1
            exercise_mode = "rest_dumbbellfrontraise_set2"
            rest_dumbbellfrontraise_start_time_set2 = time.time()
    
    if unsuccessful_reps_count_left_dumbbellfrontraise_set2 >= 2:
        cvzone.putTextRect(img, 'You have made 2 unsuccessful tries for left arm. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_dumbbellfrontraise_set2 = False

        if dir_gen_feedback_unsuccessful_dumbbellfrontraise_set2 == 0:
            general_feedback_left_dumbbellfrontraise_set2 = detector_dumbbellfrontraise.left_arm_unsuccessful_feedback(total_reps_count_left_dumbbellfrontraise_set2)
            dir_gen_feedback_unsuccessful_dumbbellfrontraise_set2 = 1
            exercise_mode = "rest_dumbbellfrontraise_set2"
            rest_dumbbellfrontraise_start_time_set2 = time.time()

    if unsuccessful_reps_count_right_dumbbellfrontraise_set2 >= 2:
        cvzone.putTextRect(img, 'You have made 2 unsuccessful tries for right arm. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_dumbbellfrontraise_set2 = False

        if dir_gen_feedback_unsuccessful_dumbbellfrontraise_set2 == 0:
            general_feedback_right_dumbbellfrontraise_set2 = detector_dumbbellfrontraise.right_arm_unsuccessful_feedback(total_reps_count_right_dumbbellfrontraise_set2)
            dir_gen_feedback_unsuccessful_dumbbellfrontraise == 1
            exercise_mode = "rest_dumbbellfrontraise_set2"
            rest_dumbbellfrontraise_start_time_set2 = time.time()
    return img

def rest_dumbbellfrontraise_set2(img):
    global exercise_mode, rest_dumbbellfrontraise_start_time_set2, start_time1_dumbbellfrontraise_set3
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
        start_time1_dumbbellfrontraise_set3 = time.time()
    return img

def detect_dumbbellfrontraise_set3(img):
    global dir_left_dumbbellfrontraise_set3, dir_right_dumbbellfrontraise_set3, display_info_dumbbellfrontraise_set3, per_right_dumbbellfrontraise_set3, per_left_dumbbellfrontraise_set3, bar_left_dumbbellfrontraise_set3, bar_right_dumbbellfrontraise_set3, color_right_dumbbellfrontraise_set3, color_left_dumbbellfrontraise_set3, feedback_left_dumbbellfrontraise_set3, feedback_right_dumbbellfrontraise_set3, success_threshold_dumbbellfrontraise_set3, atrest_value_dumbbellfrontraise_set3,unsuccessful_reps_count_left_dumbbellfrontraise_set3, successful_reps_count_left_dumbbellfrontraise_set3, unsuccessful_reps_count_right_dumbbellfrontraise_set3, successful_reps_count_right_dumbbellfrontraise_set3, dir_left_unsuccessful_dumbbellfrontraise_set3, dir_right_unsuccessful_dumbbellfrontraise_set3, total_reps_count_dumbbellfrontraise_set3, total_reps_count_left_dumbbellfrontraise_set3, total_reps_count_right_dumbbellfrontraise_set3, start_time1_dumbbellfrontraise_set3, start_time2_dumbbellfrontraise_set3, start_time3_dumbbellfrontraise_set3, time_threshold_dumbbellfrontraise_set3, within_range_time1_dumbbellfrontraise_set3, within_range_time2_dumbbellfrontraise_set3, general_feedback_left_dumbbellfrontraise_set3, general_feedback_right_dumbbellfrontraise_set3, dir_gen_feedback_dumbbellfrontraise_set3, dir_gen_feedback_unsuccessful_dumbbellfrontraise_set3, cooldown_timer_dumbbellfrontraise_set3, cooldown_duration_dumbbellfrontraise_set3, angle_left_dumbbellfrontraise_set3, angle_right_dumbbellfrontraise_set3, rest_dumbbellfrontraise_start_time_set3, exercise_mode

    img = cv2.resize(img, (1280, 720))

    # Timer - starts timer based on set duration
    elapsed_time_dumbbellfrontraise = time.time() - start_time1_dumbbellfrontraise_set3
    remaining_time_dumbbellfrontraise = max(0, 10 - elapsed_time_dumbbellfrontraise)

    if display_info_dumbbellfrontraise_set3:  # Check if to display counter, bar, and percentage
        img = detector_dumbbellfrontraise.findPose(img, False)  # initializes img as variable for findpose function
        lmList_dumbbellfrontraise = detector_dumbbellfrontraise.findPosition(img, False)  # initializes lmList as variable for findPosition function

        # Define hand angles outside the if statement
        if len(lmList_dumbbellfrontraise) != 0:

            angle_left_dumbbellfrontraise_set3 = detector_dumbbellfrontraise.findAngle(img, 15, 11, 23, 13)
            angle_right_dumbbellfrontraise_set3 = detector_dumbbellfrontraise.findAngle2(img, 24, 12, 16, 14) 

            # # Interpolate angle to percentage and position on screen
            per_left_dumbbellfrontraise_set3 = np.interp(angle_left_dumbbellfrontraise_set3, (20, 150), (0, 100))
            bar_left_dumbbellfrontraise_set3 = np.interp(angle_left_dumbbellfrontraise_set3, (20, 150), (400, 200))

            per_right_dumbbellfrontraise_set3 = np.interp(angle_right_dumbbellfrontraise_set3, (20, 150), (0, 100))
            bar_right_dumbbellfrontraise_set3 = np.interp(angle_right_dumbbellfrontraise_set3, (20, 150), (400, 200))

            if int(per_left_dumbbellfrontraise_set3) == 100:
                color_left_dumbbellfrontraise_set3 = (0, 255, 0)  # Change color of left leg bar to green
            else:
                color_left_dumbbellfrontraise_set3 = (0, 0, 255)
            
            if int(per_right_dumbbellfrontraise_set3) == 100:
                color_right_dumbbellfrontraise_set3 = (0, 255, 0)
            else:
                color_right_dumbbellfrontraise_set3 = (0, 0, 255)

            #left
            if 40 <= per_left_dumbbellfrontraise_set3 <= 90:
                # Increment the time within range
                within_range_time1_dumbbellfrontraise_set3 += time.time() - start_time2_dumbbellfrontraise_set3

                # Check if peak value has been within range for the specified time
                if within_range_time1_dumbbellfrontraise_set3 >= time_threshold_dumbbellfrontraise_set3:
                    if dir_left_unsuccessful_dumbbellfrontraise_set3 == 0:
                        unsuccessful_reps_count_left_dumbbellfrontraise_set3 += 0.5
                        dir_left_unsuccessful_dumbbellfrontraise_set3 = 1
            else:
                within_range_time1_dumbbellfrontraise_set3 = 0
                # Update the start time to the current time
                start_time2_dumbbellfrontraise_set3 = time.time()

            if 1 <= per_left_dumbbellfrontraise_set3 <= 10:
                if dir_left_unsuccessful_dumbbellfrontraise_set3 == 1:
                    unsuccessful_reps_count_left_dumbbellfrontraise_set3 += 0.5
                    dir_left_unsuccessful_dumbbellfrontraise_set3 = 0

            if per_left_dumbbellfrontraise_set3 == success_threshold_dumbbellfrontraise_set3:
                if dir_left_dumbbellfrontraise_set3 == 0:
                    successful_reps_count_left_dumbbellfrontraise_set3 += 0.5
                    dir_left_dumbbellfrontraise_set3 = 1

            elif per_left_dumbbellfrontraise_set3 == atrest_value_dumbbellfrontraise_set3:
                if dir_left_dumbbellfrontraise_set3 == 1:
                    successful_reps_count_left_dumbbellfrontraise_set3 += 0.5
                    dir_left_dumbbellfrontraise_set3 = 0

            # right
            if 40 <= per_right_dumbbellfrontraise_set3 <= 90:
                # Increment the time within range
                within_range_time2_dumbbellfrontraise_set3 += time.time() - start_time3_dumbbellfrontraise_set3

                # Check if peak value has been within range for the specified time
                if within_range_time2_dumbbellfrontraise_set3 >= time_threshold_dumbbellfrontraise_set3:
                    if dir_right_unsuccessful_dumbbellfrontraise_set3 == 0:
                        unsuccessful_reps_count_right_dumbbellfrontraise_set3 += 0.5
                        dir_right_unsuccessful_dumbbellfrontraise_set3 = 1
            else:
                within_range_time2_dumbbellfrontraise_set3 = 0
                # Update the start time to the current time
                start_time3_dumbbellfrontraise_set3 = time.time()

            if 1 <= per_right_dumbbellfrontraise_set3 <= 10:
                #print("left down val: ", per_left)
                if dir_right_unsuccessful_dumbbellfrontraise_set3 == 1:
                    unsuccessful_reps_count_right_dumbbellfrontraise_set3 += 0.5
                    dir_right_unsuccessful_dumbbellfrontraise_set3 = 0

            if per_right_dumbbellfrontraise_set3 == success_threshold_dumbbellfrontraise_set3:
                if dir_right_dumbbellfrontraise_set3 == 0:
                    successful_reps_count_right_dumbbellfrontraise_set3 += 0.5
                    dir_right_dumbbellfrontraise_set3 = 1
                    cooldown_timer_dumbbellfrontraise_set3 = cooldown_duration_dumbbellfrontraise_set3
            elif per_right_dumbbellfrontraise_set3 == atrest_value_dumbbellfrontraise_set3: 
                if dir_right_dumbbellfrontraise_set3 == 1:
                    successful_reps_count_right_dumbbellfrontraise_set3 += 0.5
                    dir_right_dumbbellfrontraise_set3 = 0
                    cooldown_timer_dumbbellfrontraise_set3 = cooldown_duration_dumbbellfrontraise_set3

            # feedback for left hand  # TO BE FETCHED 
            feedback_left_dumbbellfrontraise_set3 = detector_dumbbellfrontraise.feedback_dumbbellfrontraise(per_left_dumbbellfrontraise_set3)

            detector_dumbbellfrontraise.update_next_per_left(per_left_dumbbellfrontraise_set3)

            # feedback for right hand  # TO BE FETCHED 
            feedback_right_dumbbellfrontraise_set3 = detector_dumbbellfrontraise.feedback_dumbbellfrontraise(per_right_dumbbellfrontraise_set3)

            detector_dumbbellfrontraise.update_next_per_left(per_right_dumbbellfrontraise_set3)

        # label
        cvzone.putTextRect(img, 'Dumbbell Raise Front SET 3', [430, 30], thickness=2, border=2, scale=1.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time_dumbbellfrontraise)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # bar
        cv2.putText(img, f"R {int(per_right_dumbbellfrontraise_set3)}%", (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_dumbbellfrontraise_set3)), (50, 400), color_right_dumbbellfrontraise_set3, -1)

        cv2.putText(img, f"L {int(per_left_dumbbellfrontraise_set3)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_dumbbellfrontraise_set3)), (995, 400), color_left_dumbbellfrontraise_set3, -1)

    # count
    cv2.rectangle(img, (20, 20), (140, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(successful_reps_count_right_dumbbellfrontraise_set3)}/10", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (150, 20), (270, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(successful_reps_count_left_dumbbellfrontraise_set3)}/10", (160, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    if remaining_time_dumbbellfrontraise <= 0:
        cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
        display_info_dumbbellfrontraise_set3 = False
        exercise_mode = "rest_dumbbellfrontraise_set3"
        rest_dumbbellfrontraise_start_time_set3 = time.time()

    total_reps_count_left_dumbbellfrontraise_set3 = successful_reps_count_left_dumbbellfrontraise_set3 + unsuccessful_reps_count_left_dumbbellfrontraise_set3
    total_reps_count_right_dumbbellfrontraise_set3 = successful_reps_count_right_dumbbellfrontraise_set3 + unsuccessful_reps_count_right_dumbbellfrontraise_set3

    if successful_reps_count_right_dumbbellfrontraise_set3 >= 10 and successful_reps_count_left_dumbbellfrontraise_set3 >= 10:
        cvzone.putTextRect(img, 'All Repetitions Completed', [420, 30], thickness=2, border=2, scale=2.5)
        display_info_dumbbellfrontraise_set3 = False
        # General feedback after finishing the exercise # TO BE FETCHED
        if dir_gen_feedback_dumbbellfrontraise_set3 == 0:
            general_feedback_left_dumbbellfrontraise_set3 = detector_dumbbellfrontraise.left_arm_feedback(total_reps_count_left_dumbbellfrontraise_set3)
            general_feedback_right_dumbbellfrontraise_set3 = detector_dumbbellfrontraise.right_arm_feedback(total_reps_count_right_dumbbellfrontraise_set3)
            dir_gen_feedback_dumbbellfrontraise_set3 = 1
            exercise_mode = "rest_dumbbellfrontraise_set3"
            rest_dumbbellfrontraise_start_time_set3 = time.time()

    if unsuccessful_reps_count_left_dumbbellfrontraise_set3 >= 2 and unsuccessful_reps_count_right_dumbbellfrontraise_set3 >= 2:
        cvzone.putTextRect(img, 'You have made 2 unsuccessful tries for both arms. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_dumbbellfrontraise_set3 = False

        if dir_gen_feedback_unsuccessful_dumbbellfrontraise_set3 == 0:
            general_feedback_left_dumbbellfrontraise_set3 = detector_dumbbellfrontraise.left_arm_unsuccessful_feedback(total_reps_count_left_dumbbellfrontraise_set3)
            general_feedback_right_dumbbellfrontraise_set3 = detector_dumbbellfrontraise.right_arm_unsuccessful_feedback(total_reps_count_right_dumbbellfrontraise_set3)
            dir_gen_feedback_unsuccessful_dumbbellfrontraise_set3 = 1
            exercise_mode = "rest_dumbbellfrontraise_set3"
            rest_dumbbellfrontraise_start_time_set3 = time.time()
    
    if unsuccessful_reps_count_left_dumbbellfrontraise_set3 >= 2:
        cvzone.putTextRect(img, 'You have made 2 unsuccessful tries for left arm. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_dumbbellfrontraise_set3 = False

        if dir_gen_feedback_unsuccessful_dumbbellfrontraise_set3 == 0:
            general_feedback_left_dumbbellfrontraise_set3 = detector_dumbbellfrontraise.left_arm_unsuccessful_feedback(total_reps_count_left_dumbbellfrontraise_set3)
            dir_gen_feedback_unsuccessful_dumbbellfrontraise = 1
            exercise_mode = "rest_dumbbellfrontraise_set3"
            rest_dumbbellfrontraise_start_time_set3 = time.time()

    if unsuccessful_reps_count_right_dumbbellfrontraise_set3 >= 2:
        cvzone.putTextRect(img, 'You have made 2 unsuccessful tries for right arm. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_dumbbellfrontraise_set3 = False

        if dir_gen_feedback_unsuccessful_dumbbellfrontraise_set3 == 0:
            general_feedback_right_dumbbellfrontraise_set3 = detector_dumbbellfrontraise.right_arm_unsuccessful_feedback(total_reps_count_right_dumbbellfrontraise_set3)
            dir_gen_feedback_unsuccessful_dumbbellfrontraise_set3 == 1
            exercise_mode = "rest_dumbbellfrontraise_set3"
            rest_dumbbellfrontraise_start_time_set3 = time.time()

    return img

def rest_dumbbellfrontraise_set3(img):
    global exercise_mode, rest_dumbbellfrontraise_start_time_set3, start_time1_leglunge
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_dumbbellfrontraise_start_time_set3
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "alternating_lunge"
        start_time1_leglunge = time.time()
    return img

def detect_alternatinglunge(img):
    global dir_left_leglunge, dir_right_leglunge, display_info_leglunge, per_right_leglunge, per_left_leglunge, bar_left_leglunge, bar_right_leglunge, leftangle_leglunge, rightangle_leglunge, color_right_leglunge, color_left_leglunge, feedback_left_leglunge, feedback_right_leglunge, success_threshold_leglunge, peak_value_leglunge, atrest_value_leglunge, unsuccessful_reps_count_left_leglunge, successful_reps_count_left_leglunge, unsuccessful_reps_count_right_leglunge, successful_reps_count_right_leglunge, dir_left_unsuccessful_leglunge, dir_right_unsuccessful_leglunge, total_reps_count_leglunge, total_reps_count_left_leglunge, total_reps_count_right_leglunge, start_time1_leglunge, start_time2_leglunge, start_time3_leglunge, time_threshold_leglunge, within_range_time1_leglunge, within_range_time2_leglunge, general_feedback_left_leglunge, general_feedback_right_leglunge, dir_gen_feedback_leglunge, dir_gen_feedback_unsuccessful_leglunge, cooldown_timer_leglunge, cooldown_duration_leglunge, rest_alternatinglunge_start_time, exercise_mode

    img = cv2.resize(img, (1280, 720))

    elapsed_time_leglunge = time.time() - start_time1_leglunge
    remaining_time_leglunge = max(0, 60 - elapsed_time_leglunge)

    if display_info_leglunge:  # Check if to display counter, bar, and percentage
        img = detector_leglunge.findPose(img, False)
        lmList_leglunge = detector_leglunge.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_leglunge) != 0:

            # Right and Left keypoints
            rightleg_leglunge = detector_leglunge.AlternatingLunge(img, 24, 26, 28, True)
            leftleg_leglunge = detector_leglunge.AlternatingLunge(img, 23, 25, 27, True)

            if cooldown_timer_leglunge > 0:
                cooldown_timer_leglunge -= 1

            per_right_leglunge = np.interp(rightleg_leglunge, (150, 200), (100, 0))
            bar_right_leglunge = np.interp(rightleg_leglunge, (150, 200), (480, 680))

            per_left_leglunge = np.interp(leftleg_leglunge, (150, 200), (100, 0))
            bar_left_leglunge = np.interp(leftleg_leglunge, (150, 200), (480, 680))

            if int(per_left_leglunge) == 100:
                color_left_leglunge = (0, 255, 0)  # Change color of left leg bar to green
            else:
                color_left_leglunge = (0, 0, 255)
            
            if int(per_right_leglunge) == 100:
                color_right_leglunge = (0, 255, 0)
            else:
                color_right_leglunge = (0, 0, 255)

            #left
            if 40 <= per_left_leglunge <= 90:
                # Increment the time within range
                within_range_time1_leglunge += time.time() - start_time2_leglunge

                # Check if peak value has been within range for the specified time
                if within_range_time1_leglunge >= time_threshold_leglunge:
                    if dir_left_unsuccessful_leglunge == 0:
                        unsuccessful_reps_count_left_leglunge += 0.5
                        dir_left_unsuccessful_leglunge = 1
                        print("UP LEFT: ", unsuccessful_reps_count_left_leglunge)


            else:
                within_range_time1_leglunge = 0
                # Update the start time to the current time
                start_time2_leglunge = time.time()

            if 1 <= per_left_leglunge <= 10:
                if dir_left_unsuccessful_leglunge == 1:
                    unsuccessful_reps_count_left_leglunge += 0.5
                    dir_left_unsuccessful_leglunge = 0
                    print("UP DOWN: ", unsuccessful_reps_count_left_leglunge)


            if rightleg_leglunge <= 100 and leftleg_leglunge <= 150:
                if dir_left_leglunge == 0:
                    successful_reps_count_left_leglunge += 0.5
                    dir_left_leglunge = 1
                    cooldown_timer_leglunge = cooldown_duration_leglunge
            else:
                if dir_left_leglunge == 1:
                    successful_reps_count_left_leglunge += 0.5
                    dir_left_leglunge = 0
                    cooldown_timer_leglunge = cooldown_duration_leglunge
    
            # right
            if 40 <= per_right_leglunge <= 90:
                # Increment the time within range
                within_range_time2_leglunge += time.time() - start_time3_leglunge

                # Check if peak value has been within range for the specified time
                if within_range_time2_leglunge >= time_threshold_leglunge:
                    if dir_right_unsuccessful_leglunge == 0:
                        unsuccessful_reps_count_right_leglunge += 0.5
                        dir_right_unsuccessful_leglunge = 1
                        print("right UP", unsuccessful_reps_count_right_leglunge)
            else:
                within_range_time2_leglunge = 0
                # Update the start time to the current time
                start_time3_leglunge = time.time()

            if 1 <= per_right_leglunge <= 10:
                #print("left down val: ", per_left)
                if dir_right_unsuccessful_leglunge == 1:
                    unsuccessful_reps_count_right_leglunge += 0.5
                    dir_right_unsuccessful_leglunge = 0
                    print("right DOWN", unsuccessful_reps_count_right_leglunge)

            if rightleg_leglunge <= 150 and leftleg_leglunge <= 100:
                if dir_right_leglunge == 0:
                    successful_reps_count_right_leglunge += 0.5
                    dir_right_leglunge = 1
                    cooldown_timer_leglunge = cooldown_duration_leglunge
            else: 
                if dir_right_leglunge == 1:
                    successful_reps_count_right_leglunge += 0.5
                    dir_right_leglunge = 0
                    cooldown_timer_leglunge = cooldown_duration_leglunge

            # feedback for left hand  # TO BE FETCHED 
            feedback_left_leglunge = detector_leglunge.feedback_leglunge(per_left_leglunge)

            detector_leglunge.update_next_per_left(per_left_leglunge)

            # feedback for right hand  # TO BE FETCHED 
            feedback_right_leglunge = detector_leglunge.feedback_leglunge(per_right_leglunge)

            detector_leglunge.update_next_per_left(per_right_leglunge)

        cvzone.putTextRect(img, 'Leg Lunge Front', [430, 30], thickness=2, border=2, scale=1.5)


        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time_leglunge)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # RIGHT LEG
        cv2.putText(img, f"R {int(per_right_leglunge)}%", (24, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 480), (50, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_leglunge)), (50, 680), color_right_leglunge, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_left_leglunge)}%", (962, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 480), (995, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_leglunge)), (995, 680), color_left_leglunge, -1)

    # Counter 
    cv2.rectangle(img, (20, 20), (140, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(successful_reps_count_right_leglunge)}/10", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (150, 20), (270, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(successful_reps_count_left_leglunge)}/10", (160, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    # Timer
    if remaining_time_leglunge <= 0:
        cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
        display_info_leglunge = False
        exercise_mode = "rest_alternatinglunge"
        rest_alternatinglunge_start_time = time.time()

    total_reps_count_left_leglunge = successful_reps_count_left_leglunge + unsuccessful_reps_count_left_leglunge
    total_reps_count_right_leglunge = successful_reps_count_right_leglunge + unsuccessful_reps_count_right_leglunge  


    if successful_reps_count_right_leglunge >= 10 and successful_reps_count_left_leglunge >= 10:
        cvzone.putTextRect(img, 'All Repetitions Completed', [420, 30], thickness=2, border=2, scale=2.5)
        display_info_leglunge = False
        # General feedback after finishing the exercise # TO BE FETCHED
        if dir_gen_feedback_leglunge == 0:
            general_feedback_left_leglunge = detector_leglunge.left_leg_feedback(total_reps_count_left_leglunge)
            general_feedback_right_leglunge = detector_leglunge.right_leg_feedback(total_reps_count_right_leglunge)
            dir_gen_feedback_leglunge = 1
            exercise_mode = "rest_alternatinglunge"
            rest_alternatinglunge_start_time = time.time()
        

    if unsuccessful_reps_count_left_leglunge >= 2:
        cvzone.putTextRect(img, 'You have made 2 unsuccessful tries for left leg. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_leglunge = False

        if dir_gen_feedback_unsuccessful_leglunge == 0:
            general_feedback_left_leglunge = detector_leglunge.left_leg_unsuccessful_feedback(total_reps_count_left_leglunge)
            dir_gen_feedback_unsuccessful_leglunge = 1
            exercise_mode = "rest_alternatinglunge"
            rest_alternatinglunge_start_time = time.time()

    if unsuccessful_reps_count_right_leglunge >= 2:
        cvzone.putTextRect(img, 'You have made 2 unsuccessful tries for right leg. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_leglunge = False

        if dir_gen_feedback_unsuccessful_leglunge == 0:
            general_feedback_right_leglunge = detector_leglunge.right_leg_unsuccessful_feedback(total_reps_count_right_leglunge)
            dir_gen_feedback_unsuccessful_leglunge == 1
            exercise_mode = "rest_alternatinglunge"
            rest_alternatinglunge_start_time = time.time()

    return img

def rest_alternatinglunge(img):
    global exercise_mode, rest_alternatinglunge_start_time, start_time1_leglunge_set2
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_alternatinglunge_start_time
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "alternating_lunge_set2"
        start_time1_leglunge_set2 = time.time()

    return img

def detect_alternatinglunge_set2(img):
    global dir_left_leglunge_set2, dir_right_leglunge_set2, display_info_leglunge_set2, per_right_leglunge_set2, per_left_leglunge_set2, bar_left_leglunge_set2, bar_right_leglunge_set2, leftangle_leglunge_set2, rightangle_leglunge_set2, color_right_leglunge_set2, color_left_leglunge_set2, feedback_left_leglunge_set2, feedback_right_leglunge_set2, success_threshold_leglunge_set2, peak_value_leglunge_set2, atrest_value_leglunge_set2, unsuccessful_reps_count_left_leglunge_set2, successful_reps_count_left_leglunge_set2, unsuccessful_reps_count_right_leglunge_set2, successful_reps_count_right_leglunge_set2, dir_left_unsuccessful_leglunge_set2, dir_right_unsuccessful_leglunge_set2, total_reps_count_leglunge_set2, total_reps_count_left_leglunge_set2, total_reps_count_right_leglunge_set2, start_time1_leglunge_set2, start_time2_leglunge_set2, start_time3_leglunge_set2, time_threshold_leglunge_set2, within_range_time1_leglunge_set2, within_range_time2_leglunge_set2, general_feedback_left_leglunge_set2, general_feedback_right_leglunge_set2, dir_gen_feedback_leglunge_set2, dir_gen_feedback_unsuccessful_leglunge_set2, cooldown_timer_leglunge_set2, cooldown_duration_leglunge_set2, rest_alternatinglunge_start_time_set2, exercise_mode

    img = cv2.resize(img, (1280, 720))

    elapsed_time_leglunge = time.time() - start_time1_leglunge_set2
    remaining_time_leglunge = max(0, 60 - elapsed_time_leglunge)

    if display_info_leglunge_set2:  # Check if to display counter, bar, and percentage
        img = detector_leglunge.findPose(img, False)
        lmList_leglunge = detector_leglunge.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_leglunge) != 0:

            # Right and Left keypoints
            rightleg_leglunge_set2 = detector_leglunge.AlternatingLunge(img, 24, 26, 28, True)
            leftleg_leglunge_set2 = detector_leglunge.AlternatingLunge(img, 23, 25, 27, True)

            if cooldown_timer_leglunge_set2 > 0:
                cooldown_timer_leglunge_set2 -= 1

            per_right_leglunge_set2 = np.interp(rightleg_leglunge_set2, (150, 200), (100, 0))
            bar_right_leglunge_set2 = np.interp(rightleg_leglunge_set2, (150, 200), (480, 680))

            per_left_leglunge_set2 = np.interp(leftleg_leglunge_set2, (150, 200), (100, 0))
            bar_left_leglunge_set2 = np.interp(leftleg_leglunge_set2, (150, 200), (480, 680))

            if int(per_left_leglunge_set2) == 100:
                color_left_leglunge_set2 = (0, 255, 0)  # Change color of left leg bar to green
            else:
                color_left_leglunge_set2 = (0, 0, 255)
            
            if int(per_right_leglunge_set2) == 100:
                color_right_leglunge_set2 = (0, 255, 0)
            else:
                color_right_leglunge_set2 = (0, 0, 255)

            #left
            if 40 <= per_left_leglunge_set2 <= 90:
                # Increment the time within range
                within_range_time1_leglunge_set2 += time.time() - start_time2_leglunge_set2

                # Check if peak value has been within range for the specified time
                if within_range_time1_leglunge_set2 >= time_threshold_leglunge_set2:
                    if dir_left_unsuccessful_leglunge_set2 == 0:
                        unsuccessful_reps_count_left_leglunge_set2 += 0.5
                        dir_left_unsuccessful_leglunge_set2 = 1
                        #print("UP LEFT: ", unsuccessful_reps_count_left_leglunge_set2)


            else:
                within_range_time1_leglunge_set2 = 0
                # Update the start time to the current time
                start_time2_leglunge_set2 = time.time()

            if 1 <= per_left_leglunge_set2 <= 10:
                if dir_left_unsuccessful_leglunge_set2 == 1:
                    unsuccessful_reps_count_left_leglunge_set2 += 0.5
                    dir_left_unsuccessful_leglunge_set2 = 0
                    #print("UP DOWN: ", unsuccessful_reps_count_left_leglunge_set2)


            if rightleg_leglunge_set2 <= 100 and leftleg_leglunge_set2 <= 150:
                if dir_left_leglunge_set2 == 0:
                    successful_reps_count_left_leglunge_set2 += 0.5
                    dir_left_leglunge_set2 = 1
                    cooldown_timer_leglunge_set2 = cooldown_duration_leglunge_set2
            else:
                if dir_left_leglunge_set2 == 1:
                    successful_reps_count_left_leglunge_set2 += 0.5
                    dir_left_leglunge_set2 = 0
                    cooldown_timer_leglunge_set2 = cooldown_duration_leglunge_set2
    
            # right
            if 40 <= per_right_leglunge_set2 <= 90:
                # Increment the time within range
                within_range_time2_leglunge_set2 += time.time() - start_time3_leglunge_set2

                # Check if peak value has been within range for the specified time
                if within_range_time2_leglunge_set2 >= time_threshold_leglunge_set2:
                    if dir_right_unsuccessful_leglunge_set2 == 0:
                        unsuccessful_reps_count_right_leglunge_set2 += 0.5
                        dir_right_unsuccessful_leglunge_set2 = 1
                        #print("right UP", unsuccessful_reps_count_right_leglunge_set2)
            else:
                within_range_time2_leglunge_set2 = 0
                # Update the start time to the current time
                start_time3_leglunge_set2 = time.time()

            if 1 <= per_right_leglunge_set2 <= 10:
                #print("left down val: ", per_left)
                if dir_right_unsuccessful_leglunge_set2 == 1:
                    unsuccessful_reps_count_right_leglunge_set2 += 0.5
                    dir_right_unsuccessful_leglunge_set2 = 0
                    #print("right DOWN", unsuccessful_reps_count_right_leglunge_set2)

            if rightleg_leglunge_set2 <= 150 and leftleg_leglunge_set2 <= 100:
                if dir_right_leglunge_set2 == 0:
                    successful_reps_count_right_leglunge_set2 += 0.5
                    dir_right_leglunge_set2 = 1
                    cooldown_timer_leglunge_set2 = cooldown_duration_leglunge_set2
            else: 
                if dir_right_leglunge_set2 == 1:
                    successful_reps_count_right_leglunge_set2 += 0.5
                    dir_right_leglunge_set2 = 0
                    cooldown_timer_leglunge_set2 = cooldown_duration_leglunge_set2

            # feedback for left hand  # TO BE FETCHED 
            feedback_left_leglunge_set2 = detector_leglunge.feedback_leglunge(per_left_leglunge_set2)

            detector_leglunge.update_next_per_left(per_left_leglunge_set2)

            # feedback for right hand  # TO BE FETCHED 
            feedback_right_leglunge_set2 = detector_leglunge.feedback_leglunge(per_right_leglunge_set2)

            detector_leglunge.update_next_per_left(per_right_leglunge_set2)

        cvzone.putTextRect(img, 'Leg Lunge Front SET 2', [430, 30], thickness=2, border=2, scale=1.5)


        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time_leglunge)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # RIGHT LEG
        cv2.putText(img, f"R {int(per_right_leglunge_set2)}%", (24, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 480), (50, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_leglunge_set2)), (50, 680), color_right_leglunge_set2, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_left_leglunge_set2)}%", (962, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 480), (995, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_leglunge_set2)), (995, 680), color_left_leglunge_set2, -1)

    # Counter 
    cv2.rectangle(img, (20, 20), (140, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(successful_reps_count_right_leglunge_set2)}/10", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (150, 20), (270, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(successful_reps_count_left_leglunge_set2)}/10", (160, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    # Timer
    if remaining_time_leglunge <= 0:
        cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
        display_info_leglunge_set2 = False
        exercise_mode = "rest_alternatinglunge_set2"
        rest_alternatinglunge_start_time_set2 = time.time()

    total_reps_count_left_leglunge_set2 = successful_reps_count_left_leglunge_set2 + unsuccessful_reps_count_left_leglunge_set2
    total_reps_count_right_leglunge_set2 = successful_reps_count_right_leglunge_set2 + unsuccessful_reps_count_right_leglunge_set2  


    if successful_reps_count_right_leglunge_set2 >= 10 and successful_reps_count_left_leglunge_set2 >= 10:
        cvzone.putTextRect(img, 'All Repetitions Completed', [420, 30], thickness=2, border=2, scale=2.5)
        display_info_leglunge_set2 = False
        # General feedback after finishing the exercise # TO BE FETCHED
        if dir_gen_feedback_leglunge_set2 == 0:
            general_feedback_left_leglunge_set2 = detector_leglunge.left_leg_feedback(total_reps_count_left_leglunge_set2)
            general_feedback_right_leglunge_set2 = detector_leglunge.right_leg_feedback(total_reps_count_right_leglunge_set2)
            dir_gen_feedback_leglunge_set2 = 1
            exercise_mode = "rest_alternatinglunge_set2"
            rest_alternatinglunge_start_time_set2 = time.time()
        

    if unsuccessful_reps_count_left_leglunge_set2 >= 2:
        cvzone.putTextRect(img, 'You have made 2 unsuccessful tries for left leg. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_leglunge_set2 = False

        if dir_gen_feedback_unsuccessful_leglunge_set2 == 0:
            general_feedback_left_leglunge_set2 = detector_leglunge.left_leg_unsuccessful_feedback(total_reps_count_left_leglunge_set2)
            dir_gen_feedback_unsuccessful_leglunge_set2 = 1
            exercise_mode = "rest_alternatinglunge_set2"
            rest_alternatinglunge_start_time_set2 = time.time()

    if unsuccessful_reps_count_right_leglunge_set2 >= 2:
        cvzone.putTextRect(img, 'You have made 2 unsuccessful tries for right leg. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_leglunge_set2 = False

        if dir_gen_feedback_unsuccessful_leglunge_set2 == 0:
            general_feedback_right_leglunge_set2 = detector_leglunge.right_leg_unsuccessful_feedback(total_reps_count_right_leglunge_set2)
            dir_gen_feedback_unsuccessful_leglunge_set2 == 1
            exercise_mode = "rest_alternatinglunge_set2"
            rest_alternatinglunge_start_time_set2 = time.time()
    return img

def rest_alternatinglunge_set2(img):
    global exercise_mode, rest_alternatinglunge_start_time_set2, start_time1_leglunge_set3
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_alternatinglunge_start_time_set2
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "alternating_lunge_set3"
        start_time1_leglunge_set3 = time.time()
    return img

def detect_alternatinglunge_set3(img):
    global dir_left_leglunge_set3, dir_right_leglunge_set3, display_info_leglunge_set3, per_right_leglunge_set3, per_left_leglunge_set3, bar_left_leglunge_set3, bar_right_leglunge_set3, leftangle_leglunge_set3, rightangle_leglunge_set3, color_right_leglunge_set3, color_left_leglunge_set3, feedback_left_leglunge_set3, feedback_right_leglunge_set3, success_threshold_leglunge_set3, peak_value_leglunge_set3, atrest_value_leglunge_set3, unsuccessful_reps_count_left_leglunge_set3, successful_reps_count_left_leglunge_set3, unsuccessful_reps_count_right_leglunge_set3, successful_reps_count_right_leglunge_set3, dir_left_unsuccessful_leglunge_set3, dir_right_unsuccessful_leglunge_set3, total_reps_count_leglunge_set3, total_reps_count_left_leglunge_set3, total_reps_count_right_leglunge_set3, start_time1_leglunge_set3, start_time2_leglunge_set3, start_time3_leglunge_set3, time_threshold_leglunge_set3, within_range_time1_leglunge_set3, within_range_time2_leglunge_set3, general_feedback_left_leglunge_set3, general_feedback_right_leglunge_set3, dir_gen_feedback_leglunge_set3, dir_gen_feedback_unsuccessful_leglunge_set3, cooldown_timer_leglunge_set3, cooldown_duration_leglunge_set3, rest_alternatinglunge_start_time_set3, exercise_mode

    img = cv2.resize(img, (1280, 720))

    elapsed_time_leglunge = time.time() - start_time1_leglunge_set3
    remaining_time_leglunge = max(0, 60 - elapsed_time_leglunge)

    if display_info_leglunge_set3:  # Check if to display counter, bar, and percentage
        img = detector_leglunge.findPose(img, False)
        lmList_leglunge = detector_leglunge.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_leglunge) != 0:

            # Right and Left keypoints
            rightleg_leglunge_set3 = detector_leglunge.AlternatingLunge(img, 24, 26, 28, True)
            leftleg_leglunge_set3 = detector_leglunge.AlternatingLunge(img, 23, 25, 27, True)

            if cooldown_timer_leglunge_set3 > 0:
                cooldown_timer_leglunge_set3 -= 1

            per_right_leglunge_set3 = np.interp(rightleg_leglunge_set3, (150, 200), (100, 0))
            bar_right_leglunge_set3 = np.interp(rightleg_leglunge_set3, (150, 200), (480, 680))

            per_left_leglunge_set3 = np.interp(leftleg_leglunge_set3, (150, 200), (100, 0))
            bar_left_leglunge_set3 = np.interp(leftleg_leglunge_set3, (150, 200), (480, 680))

            if int(per_left_leglunge_set3) == 100:
                color_left_leglunge_set3 = (0, 255, 0)  # Change color of left leg bar to green
            else:
                color_left_leglunge_set3 = (0, 0, 255)
            
            if int(per_right_leglunge_set3) == 100:
                color_right_leglunge_set3 = (0, 255, 0)
            else:
                color_right_leglunge_set3 = (0, 0, 255)

            #left
            if 40 <= per_left_leglunge_set3 <= 90:
                # Increment the time within range
                within_range_time1_leglunge_set3 += time.time() - start_time2_leglunge_set3

                # Check if peak value has been within range for the specified time
                if within_range_time1_leglunge_set3 >= time_threshold_leglunge_set3:
                    if dir_left_unsuccessful_leglunge_set3 == 0:
                        unsuccessful_reps_count_left_leglunge_set3 += 0.5
                        dir_left_unsuccessful_leglunge_set3 = 1
                        #print("UP LEFT: ", unsuccessful_reps_count_left_leglunge_set3)


            else:
                within_range_time1_leglunge_set3 = 0
                # Update the start time to the current time
                start_time2_leglunge_set3 = time.time()

            if 1 <= per_left_leglunge_set3 <= 10:
                if dir_left_unsuccessful_leglunge_set3 == 1:
                    unsuccessful_reps_count_left_leglunge_set3 += 0.5
                    dir_left_unsuccessful_leglunge_set3 = 0
                    #print("UP DOWN: ", unsuccessful_reps_count_left_leglunge_set3)


            if rightleg_leglunge_set3 <= 100 and leftleg_leglunge_set3 <= 150:
                if dir_left_leglunge_set3 == 0:
                    successful_reps_count_left_leglunge_set3 += 0.5
                    dir_left_leglunge_set3 = 1
                    cooldown_timer_leglunge_set3 = cooldown_duration_leglunge_set3
            else:
                if dir_left_leglunge_set3 == 1:
                    successful_reps_count_left_leglunge_set3 += 0.5
                    dir_left_leglunge_set3 = 0
                    cooldown_timer_leglunge_set3 = cooldown_duration_leglunge_set3
    
            # right
            if 40 <= per_right_leglunge_set3 <= 90:
                # Increment the time within range
                within_range_time2_leglunge_set3 += time.time() - start_time3_leglunge_set3

                # Check if peak value has been within range for the specified time
                if within_range_time2_leglunge_set3 >= time_threshold_leglunge_set3:
                    if dir_right_unsuccessful_leglunge_set3 == 0:
                        unsuccessful_reps_count_right_leglunge_set3 += 0.5
                        dir_right_unsuccessful_leglunge_set3 = 1
                        #print("right UP", unsuccessful_reps_count_right_leglunge_set3)
            else:
                within_range_time2_leglunge_set3 = 0
                # Update the start time to the current time
                start_time3_leglunge_set3 = time.time()

            if 1 <= per_right_leglunge_set3 <= 10:
                #print("left down val: ", per_left)
                if dir_right_unsuccessful_leglunge_set3 == 1:
                    unsuccessful_reps_count_right_leglunge_set3 += 0.5
                    dir_right_unsuccessful_leglunge_set3 = 0
                    #print("right DOWN", unsuccessful_reps_count_right_leglunge_set3)

            if rightleg_leglunge_set3 <= 150 and leftleg_leglunge_set3 <= 100:
                if dir_right_leglunge == 0:
                    successful_reps_count_right_leglunge_set3 += 0.5
                    dir_right_leglunge_set3 = 1
                    cooldown_timer_leglunge_set3 = cooldown_duration_leglunge_set3
            else: 
                if dir_right_leglunge_set3 == 1:
                    successful_reps_count_right_leglunge_set3 += 0.5
                    dir_right_leglunge_set3 = 0
                    cooldown_timer_leglunge_set3 = cooldown_duration_leglunge_set3

            # feedback for left hand  # TO BE FETCHED 
            feedback_left_leglunge_set3 = detector_leglunge.feedback_leglunge(per_left_leglunge_set3)

            detector_leglunge.update_next_per_left(per_left_leglunge_set3)

            # feedback for right hand  # TO BE FETCHED 
            feedback_right_leglunge_set3 = detector_leglunge.feedback_leglunge(per_right_leglunge_set3)

            detector_leglunge.update_next_per_left(per_right_leglunge_set3)

        cvzone.putTextRect(img, 'Leg Lunge Front SET 3', [430, 30], thickness=2, border=2, scale=1.5)


        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time_leglunge)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # RIGHT LEG
        cv2.putText(img, f"R {int(per_right_leglunge_set3)}%", (24, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 480), (50, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_leglunge_set3)), (50, 680), color_right_leglunge_set3, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_left_leglunge_set3)}%", (962, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 480), (995, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_leglunge_set3)), (995, 680), color_left_leglunge_set3, -1)

    # Counter 
    cv2.rectangle(img, (20, 20), (140, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(successful_reps_count_right_leglunge_set3)}/10", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (150, 20), (270, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(successful_reps_count_left_leglunge_set3)}/10", (160, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    # Timer
    if remaining_time_leglunge <= 0:
        cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
        display_info_leglunge_set3 = False
        exercise_mode = "rest_alternatinglunge_set3"
        rest_alternatinglunge_start_time_set3 = time.time()

    total_reps_count_left_leglunge_set3 = successful_reps_count_left_leglunge_set3 + unsuccessful_reps_count_left_leglunge_set3
    total_reps_count_right_leglunge_set3 = successful_reps_count_right_leglunge_set3 + unsuccessful_reps_count_right_leglunge_set3  


    if successful_reps_count_right_leglunge_set3 >= 10 and successful_reps_count_left_leglunge_set3 >= 10:
        cvzone.putTextRect(img, 'All Repetitions Completed', [420, 30], thickness=2, border=2, scale=2.5)
        display_info_leglunge_set3 = False
        # General feedback after finishing the exercise # TO BE FETCHED
        if dir_gen_feedback_leglunge_set3 == 0:
            general_feedback_left_leglunge_set3 = detector_leglunge.left_leg_feedback(total_reps_count_left_leglunge_set3)
            general_feedback_right_leglunge_set3 = detector_leglunge.right_leg_feedback(total_reps_count_right_leglunge_set3)
            dir_gen_feedback_leglunge_set3 = 1
            exercise_mode = "rest_alternatinglunge_set3"
            rest_alternatinglunge_start_time_set3 = time.time()
        

    if unsuccessful_reps_count_left_leglunge_set3 >= 2:
        cvzone.putTextRect(img, 'You have made 2 unsuccessful tries for left leg. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_leglunge_set3 = False

        if dir_gen_feedback_unsuccessful_leglunge_set3 == 0:
            general_feedback_left_leglunge_set3 = detector_leglunge.left_leg_unsuccessful_feedback(total_reps_count_left_leglunge_set3)
            dir_gen_feedback_unsuccessful_leglunge_set3 = 1
            exercise_mode = "rest_alternatinglunge_set3"
            rest_alternatinglunge_start_time_set3= time.time()

    if unsuccessful_reps_count_right_leglunge_set3 >= 2:
        cvzone.putTextRect(img, 'You have made 2 unsuccessful tries for right leg. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_leglunge_set3 = False

        if dir_gen_feedback_unsuccessful_leglunge_set3 == 0:
            general_feedback_right_leglunge_set3 = detector_leglunge.right_leg_unsuccessful_feedback(total_reps_count_right_leglunge_set3)
            dir_gen_feedback_unsuccessful_leglunge_set3 == 1
            exercise_mode = "rest_alternatinglunge_set3"
            rest_alternatinglunge_start_time_set3 = time.time()
    return img

def rest_alternatinglunge_set3(img):
    global exercise_mode, rest_alternatinglunge_start_time_set3, start_time1_bodyweightsquat
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_alternatinglunge_start_time_set3
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "bws"
        start_time1_bodyweightsquat = time.time()

    return img

def detect_bws(img):
    global dir_left_bodyweightsquat, dir_right_bodyweightsquat, display_info_bodyweightsquat, per_right_bodyweightsquat, per_left_bodyweightsquat, bar_left_bodyweightsquat, bar_right_bodyweightsquat, leftbody_bodyweightsquat, rightbody_bodyweightsquat, color_right_bodyweightsquat, color_left_bodyweightsquat, feedback_body_bodyweightsquat, success_threshold_bodyweightsquat, peak_value_bodyweightsquat, atrest_value_bodyweightsquat, unsuccessful_reps_count_body_bodyweightsquat, successful_reps_count_body_bodyweightsquat, dir_left_unsuccessful_bodyweightsquat, start_time1_bodyweightsquat, start_time2_bodyweightsquat, start_time3_bodyweightsquat, time_threshold_bodyweightsquat, within_range_time1_bodyweightsquat, within_range_time2_bodyweightsquat, general_feedback_left_bodyweightsquat, dir_gen_feedback_bodyweightsquat, dir_gen_feedback_unsuccessful_bodyweightsquat, cooldown_timer_bodyweightsquat, cooldown_duration_bodyweightsquat, rest_bws_start_time, exercise_mode, per_right_body_bodyweightsquat, bar_right_body_bodyweightsquat, per_left_body_bodyweightsquat, bar_left_body_bodyweightsquat

    img = cv2.resize(img, (1280, 720))

    elapsed_time_bodyweightsquat = time.time() - start_time1_bodyweightsquat
    remaining_time_bodyweightsquat = max(0, 60 - elapsed_time_bodyweightsquat)

    if display_info_bodyweightsquat:  # Check if to display counter, bar, and percentage
        img = detector_bodyweightsquat.findPose(img, False)
        lmList_bodyweightsquat = detector_bodyweightsquat.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_bodyweightsquat) != 0:
            
            leftbody_bodyweightsquat = detector_bodyweightsquat.WeightSquat(img, 12, 24, 26, True)
            rightbody_bodyweightsquat = detector_bodyweightsquat.WeightSquat(img, 11, 23, 25, True)
                     
            per_right_body_bodyweightsquat = np.interp(rightbody_bodyweightsquat, (180, 270), (100, 0))
            bar_right_body_bodyweightsquat = np.interp(rightbody_bodyweightsquat, (180, 270), (200, 400))

            per_left_body_bodyweightsquat = np.interp(leftbody_bodyweightsquat, (180, 270), (100, 0))
            bar_left_body_bodyweightsquat = np.interp(leftbody_bodyweightsquat, (180, 270), (200, 400))

            if int(per_left_body_bodyweightsquat) == 100 and int(per_right_body_bodyweightsquat) == 100:
                color_left_bodyweightsquat = (0, 255, 0)
                color_right_bodyweightsquat = (0, 255, 0)  # Change color of left leg bar to green
            else:
                color_left_bodyweightsquat = (0, 0, 255)
                color_right_bodyweightsquat = (0, 0, 255)

            #body checker for successful and unsuccessful
            if 50 <= per_left_bodyweightsquat <= 90 or 50 <= per_right_body_bodyweightsquat <= 90:
                # Increment the time within range
                within_range_time1_bodyweightsquat += time.time() - start_time2_bodyweightsquat
                #print(within_range_time1_bodyweightsquat)

                # Check if peak value has been within range for the specified time
                if within_range_time1_bodyweightsquat >= time_threshold_bodyweightsquat:
                    if dir_left_unsuccessful_bodyweightsquat == 0:
                        unsuccessful_reps_count_body_bodyweightsquat += 0.5
                        dir_left_unsuccessful_bodyweightsquat = 1
                        #print("UP LEFT: ", unsuccessful_reps_count_body_bodyweightsquat)
            else:
                within_range_time1_bodyweightsquat = 0
                # Update the start time to the current time
                start_time2_bodyweightsquat = time.time()

            if 1 <= per_left_bodyweightsquat <= 10 or 1 <= per_right_body_bodyweightsquat <= 10:
                if dir_left_unsuccessful_bodyweightsquat == 1:
                    unsuccessful_reps_count_body_bodyweightsquat += 0.5
                    dir_left_unsuccessful_bodyweightsquat = 0
                    #print("UP DOWN: ", unsuccessful_reps_count_body_bodyweightsquat)

            if rightbody_bodyweightsquat <= 180 and leftbody_bodyweightsquat <= 180: 
                if dir_left_bodyweightsquat == 0:
                    successful_reps_count_body_bodyweightsquat += 0.5
                    dir_left_bodyweightsquat = 1
            elif rightbody_bodyweightsquat >= 270 and leftbody_bodyweightsquat >= 270:
                if dir_left_bodyweightsquat == 1:
                    successful_reps_count_body_bodyweightsquat += 0.5
                    dir_left_bodyweightsquat = 0

            # feedback for right hand  # TO BE FETCHED 
            feedback_body_bodyweightsquat = detector_bodyweightsquat.feedback_bodyweightsquat(per_right_bodyweightsquat)

            detector_bodyweightsquat.update_next_per_left(per_right_bodyweightsquat)

    
        cvzone.putTextRect(img, 'Front Body Weight Squat', [420, 30], thickness=2, border=2, scale=1.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time_bodyweightsquat)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # RIGHT LEG
        cv2.putText(img, f"R {int(per_right_body_bodyweightsquat)}%", (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_body_bodyweightsquat)), (50, 400), color_right_bodyweightsquat, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_left_body_bodyweightsquat)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_body_bodyweightsquat)), (995, 400), color_left_bodyweightsquat, -1)

    cv2.rectangle(img, (20, 10), (140, 120), (255, 0, 0), -1)
    cv2.putText(img, f"{int(successful_reps_count_body_bodyweightsquat)}/10", (30, 80), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    if remaining_time_bodyweightsquat <= 0:
        cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
        display_info_bodyweightsquat = False
        exercise_mode = "rest_bws"
        rest_bws_start_time = time.time()

    total_reps_count_body_bodyweightsquat = successful_reps_count_body_bodyweightsquat + unsuccessful_reps_count_body_bodyweightsquat

    if successful_reps_count_body_bodyweightsquat >= 10:
        cvzone.putTextRect(img, 'All Repetitions Completed', [420, 30], thickness=2, border=2, scale=2.5)
        display_info_bodyweightsquat = False
        # General feedback after finishing the exercise # TO BE FETCHED
        if dir_gen_feedback_bodyweightsquat == 0:
            general_feedback_left_bodyweightsquat = detector_bodyweightsquat.body_feedback(total_reps_count_body_bodyweightsquat)
            print(general_feedback_left_bodyweightsquat)
            dir_gen_feedback_bodyweightsquat = 1
            exercise_mode = "rest_bws"
            rest_bws_start_time = time.time()
        
    if unsuccessful_reps_count_body_bodyweightsquat >= 2:
        cvzone.putTextRect(img, 'You have made 2 unsuccessful tries. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_bodyweightsquat = False

        if dir_gen_feedback_unsuccessful_bodyweightsquat == 0:
            general_feedback_left_bodyweightsquat = detector_bodyweightsquat.body_unsuccessful_feedback(total_reps_count_body_bodyweightsquat)
            dir_gen_feedback_unsuccessful_bodyweightsquat = 1
            exercise_mode = "rest_bws"
            rest_bws_start_time = time.time()
    return img

def rest_bws(img):
    global exercise_mode, rest_bws_start_time, start_time1_bodyweightsquat_set2
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_bws_start_time
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "bws_set2"
        start_time1_bodyweightsquat_set2 = time.time()
    return img

def detect_bws_set2(img):
    global dir_left_bodyweightsquat_set2, dir_right_bodyweightsquat_set2, display_info_bodyweightsquat_set2, per_right_bodyweightsquat_set2, per_left_bodyweightsquat_set2, bar_left_bodyweightsquat_set2, bar_right_bodyweightsquat_set2, leftbody_bodyweightsquat_set2, rightbody_bodyweightsquat_set2, color_right_bodyweightsquat_set2, color_left_bodyweightsquat_set2, feedback_body_bodyweightsquat_set2, success_threshold_bodyweightsquat_set2, peak_value_bodyweightsquat_set2, atrest_value_bodyweightsquat_set2, unsuccessful_reps_count_body_bodyweightsquat_set2, successful_reps_count_body_bodyweightsquat_set2, dir_left_unsuccessful_bodyweightsquat_set2, start_time1_bodyweightsquat_set2, start_time2_bodyweightsquat_set2, start_time3_bodyweightsquat_set2, time_threshold_bodyweightsquat_set2, within_range_time1_bodyweightsquat_set2, within_range_time2_bodyweightsquat_set2, general_feedback_left_bodyweightsquat_set2, dir_gen_feedback_bodyweightsquat_set2, dir_gen_feedback_unsuccessful_bodyweightsquat_set2, cooldown_timer_bodyweightsquat_set2, cooldown_duration_bodyweightsquat_set2, rest_bws_start_time_set2, exercise_mode, per_right_body_bodyweightsquat_set2, bar_right_body_bodyweightsquat_set2, per_left_body_bodyweightsquat_set2, bar_left_body_bodyweightsquat_set2

    img = cv2.resize(img, (1280, 720))

    elapsed_time_bodyweightsquat = time.time() - start_time1_bodyweightsquat_set2
    remaining_time_bodyweightsquat = max(0, 60 - elapsed_time_bodyweightsquat)

    if display_info_bodyweightsquat_set2:  # Check if to display counter, bar, and percentage
        img = detector_bodyweightsquat.findPose(img, False)
        lmList_bodyweightsquat = detector_bodyweightsquat.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_bodyweightsquat) != 0:
            
            leftbody_bodyweightsquat_set2 = detector_bodyweightsquat.WeightSquat(img, 12, 24, 26, True)
            rightbody_bodyweightsquat_set2 = detector_bodyweightsquat.WeightSquat(img, 11, 23, 25, True)
                     
            per_right_body_bodyweightsquat_set2 = np.interp(rightbody_bodyweightsquat_set2, (180, 270), (100, 0))
            bar_right_body_bodyweightsquat_set2 = np.interp(rightbody_bodyweightsquat_set2, (180, 270), (200, 400))

            per_left_body_bodyweightsquat_set2 = np.interp(leftbody_bodyweightsquat_set2, (180, 270), (100, 0))
            bar_left_body_bodyweightsquat_set2 = np.interp(leftbody_bodyweightsquat_set2, (180, 270), (200, 400))

            if int(per_left_body_bodyweightsquat_set2) == 100 and int(per_right_body_bodyweightsquat_set2) == 100:
                color_left_bodyweightsquat_set2 = (0, 255, 0)
                color_right_bodyweightsquat_set2 = (0, 255, 0)  # Change color of left leg bar to green
            else:
                color_left_bodyweightsquat_set2 = (0, 0, 255)
                color_right_bodyweightsquat_set2 = (0, 0, 255)

            #body checker for successful and unsuccessful
            if 50 <= per_left_bodyweightsquat_set2 <= 90 or 50 <= per_right_body_bodyweightsquat_set2 <= 90:
                # Increment the time within range
                within_range_time1_bodyweightsquat += time.time() - start_time2_bodyweightsquat
                #print(within_range_time1_bodyweightsquat)

                # Check if peak value has been within range for the specified time
                if within_range_time1_bodyweightsquat_set2 >= time_threshold_bodyweightsquat_set2:
                    if dir_left_unsuccessful_bodyweightsquat_set2 == 0:
                        unsuccessful_reps_count_body_bodyweightsquat_set2 += 0.5
                        dir_left_unsuccessful_bodyweightsquat_set2 = 1
                        #print("UP LEFT: ", unsuccessful_reps_count_body_bodyweightsquat)
            else:
                within_range_time1_bodyweightsquat_set2 = 0
                # Update the start time to the current time
                start_time2_bodyweightsquat_set2 = time.time()

            if 1 <= per_left_bodyweightsquat_set2 <= 10 or 1 <= per_right_body_bodyweightsquat_set2 <= 10:
                if dir_left_unsuccessful_bodyweightsquat_set2 == 1:
                    unsuccessful_reps_count_body_bodyweightsquat_set2 += 0.5
                    dir_left_unsuccessful_bodyweightsquat_set2 = 0
                    #print("UP DOWN: ", unsuccessful_reps_count_body_bodyweightsquat)

            if rightbody_bodyweightsquat_set2 <= 180 and leftbody_bodyweightsquat_set2 <= 180: 
                if dir_left_bodyweightsquat_set2 == 0:
                    successful_reps_count_body_bodyweightsquat_set2 += 0.5
                    dir_left_bodyweightsquat_set2 = 1
            elif rightbody_bodyweightsquat_set2 >= 270 and leftbody_bodyweightsquat_set2 >= 270:
                if dir_left_bodyweightsquat_set2 == 1:
                    successful_reps_count_body_bodyweightsquat_set2 += 0.5
                    dir_left_bodyweightsquat_set2 = 0

            # feedback for right hand  # TO BE FETCHED 
            feedback_body_bodyweightsquat_set2 = detector_bodyweightsquat.feedback_bodyweightsquat(per_right_bodyweightsquat_set2)

            detector_bodyweightsquat.update_next_per_left(per_right_bodyweightsquat_set2)

    
        cvzone.putTextRect(img, 'Front Body Weight Squat SET 2', [420, 30], thickness=2, border=2, scale=1.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time_bodyweightsquat)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # RIGHT LEG
        cv2.putText(img, f"R {int(per_right_body_bodyweightsquat_set2)}%", (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_body_bodyweightsquat_set2)), (50, 400), color_right_bodyweightsquat_set2, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_left_body_bodyweightsquat_set2)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_body_bodyweightsquat_set2)), (995, 400), color_left_bodyweightsquat_set2, -1)

    cv2.rectangle(img, (20, 10), (140, 120), (255, 0, 0), -1)
    cv2.putText(img, f"{int(successful_reps_count_body_bodyweightsquat_set2)}/10", (30, 80), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    if remaining_time_bodyweightsquat <= 0:
        cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
        display_info_bodyweightsquat_set2 = False
        exercise_mode = "rest_bws_set2"
        rest_bws_start_time_set2 = time.time()

    total_reps_count_body_bodyweightsquat_set2 = successful_reps_count_body_bodyweightsquat_set2 + unsuccessful_reps_count_body_bodyweightsquat_set2

    if successful_reps_count_body_bodyweightsquat >= 10:
        cvzone.putTextRect(img, 'All Repetitions Completed', [420, 30], thickness=2, border=2, scale=2.5)
        display_info_bodyweightsquat_set2 = False
        # General feedback after finishing the exercise # TO BE FETCHED
        if dir_gen_feedback_bodyweightsquat_set2 == 0:
            general_feedback_left_bodyweightsquat_set2 = detector_bodyweightsquat.body_feedback(total_reps_count_body_bodyweightsquat_set2)
            #print(general_feedback_left_bodyweightsquat_set2)
            dir_gen_feedback_bodyweightsquat_set2 = 1
            exercise_mode = "rest_bws_set2"
            rest_bws_start_time_set2 = time.time()
        
    if unsuccessful_reps_count_body_bodyweightsquat_set2 >= 2:
        cvzone.putTextRect(img, 'You have made 2 unsuccessful tries. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_bodyweightsquat_set2 = False

        if dir_gen_feedback_unsuccessful_bodyweightsquat_set2 == 0:
            general_feedback_left_bodyweightsquat_set2 = detector_bodyweightsquat.body_unsuccessful_feedback(total_reps_count_body_bodyweightsquat_set2)
            dir_gen_feedback_unsuccessful_bodyweightsquat_set2 = 1
            exercise_mode = "rest_bws_set2"
            rest_bws_start_time_set2 = time.time()
    return img

def rest_bws_set2(img):
    global exercise_mode, rest_bws_start_time_set2, start_time1_bodyweightsquat_set3
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_bws_start_time_set2
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "bws_set3"
        start_time1_bodyweightsquat_set3 = time.time()
    return img

def detect_bws_set3(img):
    global dir_left_bodyweightsquat_set3, dir_right_bodyweightsquat_set3, display_info_bodyweightsquat_set3, per_right_bodyweightsquat_set3, per_left_bodyweightsquat_set3, bar_left_bodyweightsquat_set3, bar_right_bodyweightsquat_set3, leftbody_bodyweightsquat_set3, rightbody_bodyweightsquat_set3, color_right_bodyweightsquat_set3, color_left_bodyweightsquat_set3, feedback_body_bodyweightsquat_set3, success_threshold_bodyweightsquat_set3, peak_value_bodyweightsquat_set3, atrest_value_bodyweightsquat_set3, unsuccessful_reps_count_body_bodyweightsquat_set3, successful_reps_count_body_bodyweightsquat_set3, dir_left_unsuccessful_bodyweightsquat_set3, start_time1_bodyweightsquat_set3, start_time2_bodyweightsquat_set3, start_time3_bodyweightsquat_set3, time_threshold_bodyweightsquat_set3, within_range_time1_bodyweightsquat_set3, within_range_time2_bodyweightsquat_set3, general_feedback_left_bodyweightsquat_set3, dir_gen_feedback_bodyweightsquat_set3, dir_gen_feedback_unsuccessful_bodyweightsquat_set3, cooldown_timer_bodyweightsquat_set3, cooldown_duration_bodyweightsquat_set3, rest_bws_start_time_set3, exercise_mode, per_right_body_bodyweightsquat_set3, bar_right_body_bodyweightsquat_set3, per_left_body_bodyweightsquat_set3, bar_left_body_bodyweightsquat_set3

    img = cv2.resize(img, (1280, 720))

    elapsed_time_bodyweightsquat = time.time() - start_time1_bodyweightsquat_set3
    remaining_time_bodyweightsquat = max(0, 60 - elapsed_time_bodyweightsquat)

    if display_info_bodyweightsquat_set3:  # Check if to display counter, bar, and percentage
        img = detector_bodyweightsquat.findPose(img, False)
        lmList_bodyweightsquat = detector_bodyweightsquat.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_bodyweightsquat) != 0:
            
            leftbody_bodyweightsquat_set3 = detector_bodyweightsquat.WeightSquat(img, 12, 24, 26, True)
            rightbody_bodyweightsquat_set3 = detector_bodyweightsquat.WeightSquat(img, 11, 23, 25, True)
                     
            per_right_body_bodyweightsquat_set3 = np.interp(rightbody_bodyweightsquat_set3, (180, 270), (100, 0))
            bar_right_body_bodyweightsquat_set3 = np.interp(rightbody_bodyweightsquat_set3, (180, 270), (200, 400))

            per_left_body_bodyweightsquat_set3 = np.interp(leftbody_bodyweightsquat_set3, (180, 270), (100, 0))
            bar_left_body_bodyweightsquat_set3 = np.interp(leftbody_bodyweightsquat_set3, (180, 270), (200, 400))

            if int(per_left_body_bodyweightsquat_set3) == 100 and int(per_right_body_bodyweightsquat_set3) == 100:
                color_left_bodyweightsquat_set3 = (0, 255, 0)
                color_right_bodyweightsquat_set3 = (0, 255, 0)  # Change color of left leg bar to green
            else:
                color_left_bodyweightsquat_set3 = (0, 0, 255)
                color_right_bodyweightsquat_set3 = (0, 0, 255)

            #body checker for successful and unsuccessful
            if 50 <= per_left_bodyweightsquat_set3 <= 90 or 50 <= per_right_body_bodyweightsquat_set3 <= 90:
                # Increment the time within range
                within_range_time1_bodyweightsquat_set3 += time.time() - start_time2_bodyweightsquat_set3
                #print(within_range_time1_bodyweightsquat)

                # Check if peak value has been within range for the specified time
                if within_range_time1_bodyweightsquat_set3 >= time_threshold_bodyweightsquat_set3:
                    if dir_left_unsuccessful_bodyweightsquat_set3 == 0:
                        unsuccessful_reps_count_body_bodyweightsquat_set3 += 0.5
                        dir_left_unsuccessful_bodyweightsquat_set3 = 1
                        #print("UP LEFT: ", unsuccessful_reps_count_body_bodyweightsquat)
            else:
                within_range_time1_bodyweightsquat_set3 = 0
                # Update the start time to the current time
                start_time2_bodyweightsquat_set3 = time.time()

            if 1 <= per_left_bodyweightsquat_set3 <= 10 or 1 <= per_right_body_bodyweightsquat_set3 <= 10:
                if dir_left_unsuccessful_bodyweightsquat_set3 == 1:
                    unsuccessful_reps_count_body_bodyweightsquat_set3 += 0.5
                    dir_left_unsuccessful_bodyweightsquat_set3 = 0
                    #print("UP DOWN: ", unsuccessful_reps_count_body_bodyweightsquat)

            if rightbody_bodyweightsquat_set3 <= 180 and leftbody_bodyweightsquat_set3 <= 180: 
                if dir_left_bodyweightsquat_set3 == 0:
                    successful_reps_count_body_bodyweightsquat_set3 += 0.5
                    dir_left_bodyweightsquat_set3 = 1
            elif rightbody_bodyweightsquat_set3 >= 270 and leftbody_bodyweightsquat_set3 >= 270:
                if dir_left_bodyweightsquat_set3 == 1:
                    successful_reps_count_body_bodyweightsquat_set3 += 0.5
                    dir_left_bodyweightsquat_set3 = 0

            # feedback for right hand  # TO BE FETCHED 
            feedback_body_bodyweightsquat_set3 = detector_bodyweightsquat.feedback_bodyweightsquat(per_right_bodyweightsquat_set3)

            detector_bodyweightsquat.update_next_per_left(per_right_bodyweightsquat_set3)

    
        cvzone.putTextRect(img, 'Front Body Weight Squat SET 3', [420, 30], thickness=2, border=2, scale=1.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time_bodyweightsquat)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # RIGHT LEG
        cv2.putText(img, f"R {int(per_right_body_bodyweightsquat_set3)}%", (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_body_bodyweightsquat_set3)), (50, 400), color_right_bodyweightsquat_set3, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_left_body_bodyweightsquat_set3)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_body_bodyweightsquat_set3)), (995, 400), color_left_bodyweightsquat_set3, -1)

    cv2.rectangle(img, (20, 10), (140, 120), (255, 0, 0), -1)
    cv2.putText(img, f"{int(successful_reps_count_body_bodyweightsquat_set3)}/10", (30, 80), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    if remaining_time_bodyweightsquat <= 0:
        cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
        display_info_bodyweightsquat_set3 = False
        exercise_mode = "rest_bws_set3"
        rest_bws_start_time_set3 = time.time()

    total_reps_count_body_bodyweightsquat_set3 = successful_reps_count_body_bodyweightsquat_set3 + unsuccessful_reps_count_body_bodyweightsquat_set3

    if successful_reps_count_body_bodyweightsquat_set3 >= 10:
        cvzone.putTextRect(img, 'All Repetitions Completed', [420, 30], thickness=2, border=2, scale=2.5)
        display_info_bodyweightsquat_set3 = False
        # General feedback after finishing the exercise # TO BE FETCHED
        if dir_gen_feedback_bodyweightsquat_set3 == 0:
            general_feedback_left_bodyweightsquat_set3 = detector_bodyweightsquat.body_feedback(total_reps_count_body_bodyweightsquat_set3)
            #print(general_feedback_left_bodyweightsquat_set3)
            dir_gen_feedback_bodyweightsquat_set3 = 1
            exercise_mode = "rest_bws_set3"
            rest_bws_start_time_set3 = time.time()
        
    if unsuccessful_reps_count_body_bodyweightsquat_set3 >= 2:
        cvzone.putTextRect(img, 'You have made 2 unsuccessful tries. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_bodyweightsquat_set3 = False

        if dir_gen_feedback_unsuccessful_bodyweightsquat_set3 == 0:
            general_feedback_left_bodyweightsquat_set3 = detector_bodyweightsquat.body_unsuccessful_feedback(total_reps_count_body_bodyweightsquat_set3)
            dir_gen_feedback_unsuccessful_bodyweightsquat_set3 = 1
            exercise_mode = "rest_bws_set3"
            rest_bws_start_time_set3 = time.time()
    return img

def rest_bws_set3(img):
    global exercise_mode, rest_bws_start_time_set3, start_time_goblet_squat
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_bws_start_time_set3
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

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
    global dir_left_gobletsquat, dir_right_gobletsquat, display_info_gobletsquat, per_right_gobletsquat, per_left_gobletsquat, bar_left_gobletsquat, bar_right_gobletsquat, color_right_gobletsquat, color_left_gobletsquat, feedback_left_gobletsquat, feedback_right_gobletsquat, success_threshold_gobletsquat, atrest_value_gobletsquat, unsuccessful_reps_count_left_gobletsquat, successful_reps_count_left_gobletsquat, unsuccessful_reps_count_right_gobletsquat, successful_reps_count_right_gobletsquat, dir_left_unsuccessful_gobletsquat, dir_right_unsuccessful_gobletsquat, total_reps_count_gobletsquat, total_reps_count_left_gobletsquat, total_reps_count_right_gobletsquat, start_time1_gobletsquat, start_time2_gobletsquat, start_time3_gobletsquat, time_threshold_gobletsquat, within_range_time1_gobletsquat, within_range_time2_gobletsquat, general_feedback_left_gobletsquat, general_feedback_right_gobletsquat, dir_gen_feedback_gobletsquat, dir_gen_feedback_unsuccessful_gobletsquat, cooldown_timer_gobletsquat, cooldown_duration_gobletsquat, rest_goblet_squat_start_time, exercise_mode


    img = cv2.resize(img, (1280, 720))

    elapsed_time_gobletsquat = time.time() - start_time1_gobletsquat
    remaining_time_gobletsquat = max(0, 60 - elapsed_time_gobletsquat)

    if display_info_gobletsquat:  # Check if to display counter, bar, and percentage
        img = detector_gobletsquat.findPose(img, False)
        lmList_gobletsquat = detector_gobletsquat.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_gobletsquat) != 0:

            # Right and Left keypoints
            rightleg_gobletsquat = detector_gobletsquat.GobletSquat(img, 24, 26, 28, True)
            leftleg_gobletsquat = detector_gobletsquat.GobletSquat(img, 23, 25, 27, True)

            if cooldown_timer_gobletsquat > 0:
                cooldown_timer_gobletsquat -= 1

            per_right_gobletsquat = np.interp(rightleg_gobletsquat, (160, 240), (100, 0))
            bar_right_gobletsquat = np.interp(rightleg_gobletsquat, (160, 240), (480, 680))
            per_left_gobletsquat = np.interp(leftleg_gobletsquat, (160, 240), (100, 0))
            bar_left_gobletsquat = np.interp(leftleg_gobletsquat, (160, 240), (480, 680))

            if int(per_left_gobletsquat) == 100:
                color_left_gobletsquat = (0, 255, 0)  # Change color of left leg bar to green
            else:
                color_left_gobletsquat = (0, 0, 255)
            
            if int(per_right_gobletsquat) == 100:
                color_right_gobletsquat = (0, 255, 0)
            else:
                color_right_gobletsquat = (0, 0, 255)

            #left
            if 40 <= per_left_gobletsquat <= 90:
                # Increment the time within range
                within_range_time1_gobletsquat += time.time() - start_time2_gobletsquat

                # Check if peak value has been within range for the specified time
                if within_range_time1_gobletsquat >= time_threshold_gobletsquat:
                    if dir_left_unsuccessful_gobletsquat == 0:
                        unsuccessful_reps_count_left_gobletsquat += 0.5
                        dir_left_unsuccessful_gobletsquat = 1
            else:
                within_range_time1_gobletsquat = 0
                # Update the start time to the current time
                start_time2_gobletsquat = time.time()

            if 1 <= per_left_gobletsquat <= 10:
                if dir_left_unsuccessful_gobletsquat == 1:
                    unsuccessful_reps_count_left_gobletsquat += 0.5
                    dir_left_unsuccessful_gobletsquat = 0

            if per_left_gobletsquat == success_threshold_gobletsquat:
                if dir_left_gobletsquat == 0:
                    successful_reps_count_left_gobletsquat += 0.5
                    dir_left_gobletsquat = 1

            elif per_left_gobletsquat == atrest_value_gobletsquat:
                if dir_left_gobletsquat == 1:
                    successful_reps_count_left_gobletsquat += 0.5
                    dir_left_gobletsquat = 0

            # right
            if 40 <= per_right_gobletsquat <= 90:
                # Increment the time within range
                within_range_time2_gobletsquat += time.time() - start_time3_gobletsquat

                # Check if peak value has been within range for the specified time
                if within_range_time2_gobletsquat >= time_threshold_gobletsquat:
                    if dir_right_unsuccessful_gobletsquat == 0:
                        unsuccessful_reps_count_right_gobletsquat += 0.5
                        dir_right_unsuccessful_gobletsquat = 1
            else:
                within_range_time2_gobletsquat = 0
                # Update the start time to the current time
                start_time3_gobletsquat = time.time()

            if 1 <= per_right_gobletsquat <= 10:
                if dir_right_unsuccessful_gobletsquat == 1:
                    unsuccessful_reps_count_right_gobletsquat += 0.5
                    dir_right_unsuccessful_gobletsquat = 0

            if per_right_gobletsquat == success_threshold_gobletsquat:
                if dir_right_gobletsquat == 0:
                    successful_reps_count_right_gobletsquat += 0.5
                    dir_right_gobletsquat = 1
                    cooldown_timer_gobletsquat = cooldown_duration_gobletsquat
            elif per_right_gobletsquat == atrest_value_gobletsquat: 
                if dir_right_gobletsquat == 1:
                    successful_reps_count_right_gobletsquat += 0.5
                    dir_right_gobletsquat = 0
                    cooldown_timer_gobletsquat = cooldown_duration_gobletsquat

            # feedback for left hand  # TO BE FETCHED 
            feedback_left_gobletsquat = detector_gobletsquat.feedback_gobletsquat(per_left_gobletsquat)

            detector_gobletsquat.update_next_per_left(per_left_gobletsquat)

            # feedback for right hand  # TO BE FETCHED 
            feedback_right_gobletsquat = detector_gobletsquat.feedback_gobletsquat(per_right_gobletsquat)

            detector_gobletsquat.update_next_per_left(per_right_gobletsquat)


        cvzone.putTextRect(img, 'Front Goblet Squat', [450, 30], thickness=2, border=2, scale=1.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time_gobletsquat)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)
        # RIGHT LEG
        cv2.putText(img, f"R {int(per_right_gobletsquat)}%", (24, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 480), (50, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_gobletsquat)), (50, 680), color_right_gobletsquat, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_left_gobletsquat)}%", (962, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 480), (995, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_gobletsquat)), (995, 680), color_left_gobletsquat, -1)

    # Counter 
    cv2.rectangle(img, (20, 20), (200, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(successful_reps_count_right_gobletsquat)}/10", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (210, 20), (390, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(successful_reps_count_left_gobletsquat)}/10", (220, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)



    #Timer
    if remaining_time_gobletsquat <= 0:
        cvzone.putTextRect(img, "Time's Up", [420, 30], thickness=2, border=2, scale=2.5)
        display_info_gobletsquat = False
        exercise_mode = "rest_gs"
        rest_goblet_squat_start_time = time.time()

    total_reps_count_left_gobletsquat = successful_reps_count_left_gobletsquat + unsuccessful_reps_count_left_gobletsquat
    total_reps_count_right_gobletsquat = successful_reps_count_right_gobletsquat + unsuccessful_reps_count_right_gobletsquat

    if successful_reps_count_right_gobletsquat >= 10 and successful_reps_count_left_gobletsquat >= 10:
            cvzone.putTextRect(img, 'All Repetitions Completed', [420, 30], thickness=2, border=2, scale=2.5)
            display_info_gobletsquat = False
            # General feedback after finishing the exercise # TO BE FETCHED
            if dir_gen_feedback_gobletsquat == 0:
                general_feedback_left_gobletsquat = detector_gobletsquat.left_leg_feedback(total_reps_count_left_gobletsquat)
                general_feedback_right_gobletsquat = detector_gobletsquat.right_leg_feedback(total_reps_count_right_gobletsquat)
                dir_gen_feedback_gobletsquat = 1
                exercise_mode = "rest_gs"
                rest_goblet_squat_start_time = time.time()

    if unsuccessful_reps_count_left_gobletsquat >= 3 and unsuccessful_reps_count_right_gobletsquat >= 3:
        cvzone.putTextRect(img, 'You have made 2 unsuccessful tries for both arms. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_gobletsquat = False

        if dir_gen_feedback_unsuccessful_gobletsquat == 0:
            general_feedback_left_gobletsquat = detector_gobletsquat.left_leg_unsuccessful_feedback(total_reps_count_left_gobletsquat)
            general_feedback_right_gobletsquat = detector_gobletsquat.right_leg_unsuccessful_feedback(total_reps_count_right_gobletsquat)
            dir_gen_feedback_unsuccessful_gobletsquat = 1
            exercise_mode = "rest_gs"
            rest_goblet_squat_start_time = time.time()

    if unsuccessful_reps_count_left_gobletsquat >= 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for left arm. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_gobletsquat = False

        if dir_gen_feedback_unsuccessful_gobletsquat == 0:
            general_feedback_left_gobletsquat = detector_gobletsquat.left_leg_unsuccessful_feedback(total_reps_count_left_gobletsquat)
            dir_gen_feedback_unsuccessful_gobletsquat = 1
            exercise_mode = "rest_gs"
            rest_goblet_squat_start_time = time.time()

    if unsuccessful_reps_count_right_gobletsquat >= 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for right arm. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_gobletsquat = False

        if dir_gen_feedback_unsuccessful_gobletsquat == 0:
            general_feedback_right_gobletsquat = detector_gobletsquat.right_leg_unsuccessful_feedback(total_reps_count_right_gobletsquat)
            dir_gen_feedback_unsuccessful_gobletsquat == 1
            exercise_mode = "rest_gs"
            rest_goblet_squat_start_time = time.time()

    return img

def rest_gs(img):
    global exercise_mode, rest_goblet_squat_start_time, start_time1_gobletsquat_set2
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_goblet_squat_start_time
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "goblet_squat_set2"
        start_time1_gobletsquat_set2 = time.time()
    return img

def detect_gs_set2(img):
    global dir_left_gobletsquat_set2, dir_right_gobletsquat_set2, display_info_gobletsquat_set2, per_right_gobletsquat_set2, per_left_gobletsquat_set2, bar_left_gobletsquat_set2, bar_right_gobletsquat_set2, color_right_gobletsquat_set2, color_left_gobletsquat_set2, feedback_left_gobletsquat_set2, feedback_right_gobletsquat_set2, success_threshold_gobletsquat_set2, atrest_value_gobletsquat_set2, unsuccessful_reps_count_left_gobletsquat_set2, successful_reps_count_left_gobletsquat_set2, unsuccessful_reps_count_right_gobletsquat_set2, successful_reps_count_right_gobletsquat_set2, dir_left_unsuccessful_gobletsquat_set2, dir_right_unsuccessful_gobletsquat_set2, total_reps_count_gobletsquat_set2, total_reps_count_left_gobletsquat_set2, total_reps_count_right_gobletsquat_set2, start_time1_gobletsquat_set2, start_time2_gobletsquat_set2, start_time3_gobletsquat_set2, time_threshold_gobletsquat_set2, within_range_time1_gobletsquat_set2, within_range_time2_gobletsquat_set2, general_feedback_left_gobletsquat_set2, general_feedback_right_gobletsquat_set2, dir_gen_feedback_gobletsquat_set2, dir_gen_feedback_unsuccessful_gobletsquat_set2, cooldown_timer_gobletsquat_set2, cooldown_duration_gobletsquat_set2, rest_goblet_squat_start_time_set2, exercise_mode


    img = cv2.resize(img, (1280, 720))

    elapsed_time_gobletsquat = time.time() - start_time1_gobletsquat_set2
    remaining_time_gobletsquat = max(0, 60 - elapsed_time_gobletsquat)

    if display_info_gobletsquat_set2:  # Check if to display counter, bar, and percentage
        img = detector_gobletsquat.findPose(img, False)
        lmList_gobletsquat = detector_gobletsquat.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_gobletsquat) != 0:

            # Right and Left keypoints
            rightleg_gobletsquat_set2 = detector_gobletsquat.GobletSquat(img, 24, 26, 28, True)
            leftleg_gobletsquat_set2 = detector_gobletsquat.GobletSquat(img, 23, 25, 27, True)

            if cooldown_timer_gobletsquat_set2 > 0:
                cooldown_timer_gobletsquat_set2 -= 1

            per_right_gobletsquat_set2 = np.interp(rightleg_gobletsquat_set2, (160, 240), (100, 0))
            bar_right_gobletsquat_set2 = np.interp(rightleg_gobletsquat_set2, (160, 240), (480, 680))
            per_left_gobletsquat_set2 = np.interp(leftleg_gobletsquat_set2, (160, 240), (100, 0))
            bar_left_gobletsquat_set2 = np.interp(leftleg_gobletsquat_set2, (160, 240), (480, 680))

            if int(per_left_gobletsquat_set2) == 100:
                color_left_gobletsquat_set2 = (0, 255, 0)  # Change color of left leg bar to green
            else:
                color_left_gobletsquat_set2 = (0, 0, 255)
            
            if int(per_right_gobletsquat_set2) == 100:
                color_right_gobletsquat_set2 = (0, 255, 0)
            else:
                color_right_gobletsquat_set2 = (0, 0, 255)

            #left
            if 40 <= per_left_gobletsquat_set2 <= 90:
                # Increment the time within range
                within_range_time1_gobletsquat_set2 += time.time() - start_time2_gobletsquat_set2

                # Check if peak value has been within range for the specified time
                if within_range_time1_gobletsquat_set2 >= time_threshold_gobletsquat_set2:
                    if dir_left_unsuccessful_gobletsquat_set2 == 0:
                        unsuccessful_reps_count_left_gobletsquat_set2 += 0.5
                        dir_left_unsuccessful_gobletsquat_set2 = 1
            else:
                within_range_time1_gobletsquat_set2 = 0
                # Update the start time to the current time
                start_time2_gobletsquat_set2 = time.time()

            if 1 <= per_left_gobletsquat_set2 <= 10:
                if dir_left_unsuccessful_gobletsquat_set2 == 1:
                    unsuccessful_reps_count_left_gobletsquat_set2 += 0.5
                    dir_left_unsuccessful_gobletsquat_set2 = 0

            if per_left_gobletsquat_set2 == success_threshold_gobletsquat_set2:
                if dir_left_gobletsquat_set2 == 0:
                    successful_reps_count_left_gobletsquat_set2 += 0.5
                    dir_left_gobletsquat_set2 = 1

            elif per_left_gobletsquat_set2 == atrest_value_gobletsquat_set2:
                if dir_left_gobletsquat_set2 == 1:
                    successful_reps_count_left_gobletsquat_set2 += 0.5
                    dir_left_gobletsquat_set2 = 0

            # right
            if 40 <= per_right_gobletsquat_set2 <= 90:
                # Increment the time within range
                within_range_time2_gobletsquat_set2 += time.time() - start_time3_gobletsquat_set2

                # Check if peak value has been within range for the specified time
                if within_range_time2_gobletsquat_set2 >= time_threshold_gobletsquat_set2:
                    if dir_right_unsuccessful_gobletsquat_set2 == 0:
                        unsuccessful_reps_count_right_gobletsquat_set2 += 0.5
                        dir_right_unsuccessful_gobletsquat_set2 = 1
            else:
                within_range_time2_gobletsquat_set2 = 0
                # Update the start time to the current time
                start_time3_gobletsquat_set2 = time.time()

            if 1 <= per_right_gobletsquat_set2 <= 10:
                if dir_right_unsuccessful_gobletsquat_set2 == 1:
                    unsuccessful_reps_count_right_gobletsquat_set2 += 0.5
                    dir_right_unsuccessful_gobletsquat_set2 = 0

            if per_right_gobletsquat_set2 == success_threshold_gobletsquat_set2:
                if dir_right_gobletsquat_set2 == 0:
                    successful_reps_count_right_gobletsquat_set2 += 0.5
                    dir_right_gobletsquat_set2 = 1
                    cooldown_timer_gobletsquat_set2 = cooldown_duration_gobletsquat_set2
            elif per_right_gobletsquat_set2 == atrest_value_gobletsquat_set2: 
                if dir_right_gobletsquat_set2 == 1:
                    successful_reps_count_right_gobletsquat_set2 += 0.5
                    dir_right_gobletsquat_set2 = 0
                    cooldown_timer_gobletsquat_set2 = cooldown_duration_gobletsquat_set2

            # feedback for left hand  # TO BE FETCHED 
            feedback_left_gobletsquat_set2 = detector_gobletsquat.feedback_gobletsquat(per_left_gobletsquat_set2)

            detector_gobletsquat.update_next_per_left(per_left_gobletsquat_set2)

            # feedback for right hand  # TO BE FETCHED 
            feedback_right_gobletsquat_set2 = detector_gobletsquat.feedback_gobletsquat(per_right_gobletsquat_set2)

            detector_gobletsquat.update_next_per_left(per_right_gobletsquat_set2)


        cvzone.putTextRect(img, 'Front Goblet Squat SET 2', [450, 30], thickness=2, border=2, scale=1.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time_gobletsquat)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)
        # RIGHT LEG
        cv2.putText(img, f"R {int(per_right_gobletsquat_set2)}%", (24, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 480), (50, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_gobletsquat_set2)), (50, 680), color_right_gobletsquat_set2, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_left_gobletsquat_set2)}%", (962, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 480), (995, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_gobletsquat_set2)), (995, 680), color_left_gobletsquat_set2, -1)

    # Counter 
    cv2.rectangle(img, (20, 20), (200, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(successful_reps_count_right_gobletsquat_set2)}/10", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (210, 20), (390, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(successful_reps_count_left_gobletsquat_set2)}/10", (220, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)


    #Timer
    if remaining_time_gobletsquat <= 0:
        cvzone.putTextRect(img, "Time's Up", [420, 30], thickness=2, border=2, scale=2.5)
        display_info_gobletsquat_set2 = False
        exercise_mode = "rest_gs_set2"
        rest_goblet_squat_start_time_set2 = time.time()

    total_reps_count_left_gobletsquat_set2 = successful_reps_count_left_gobletsquat_set2 + unsuccessful_reps_count_left_gobletsquat_set2
    total_reps_count_right_gobletsquat_set2 = successful_reps_count_right_gobletsquat_set2 + unsuccessful_reps_count_right_gobletsquat_set2

    if successful_reps_count_right_gobletsquat_set2 >= 10 and successful_reps_count_left_gobletsquat_set2 >= 10:
            cvzone.putTextRect(img, 'All Repetitions Completed', [420, 30], thickness=2, border=2, scale=2.5)
            display_info_gobletsquat_set2 = False
            # General feedback after finishing the exercise # TO BE FETCHED
            if dir_gen_feedback_gobletsquat_set2 == 0:
                general_feedback_left_gobletsquat_set2 = detector_gobletsquat.left_leg_feedback(total_reps_count_left_gobletsquat_set2)
                general_feedback_right_gobletsquat_set2 = detector_gobletsquat.right_leg_feedback(total_reps_count_right_gobletsquat_set2)
                dir_gen_feedback_gobletsquat_set2 = 1
                exercise_mode = "rest_gs_set2"
                rest_goblet_squat_start_time_set2 = time.time()

    if unsuccessful_reps_count_left_gobletsquat_set2 >= 3 and unsuccessful_reps_count_right_gobletsquat_set2 >= 3:
        cvzone.putTextRect(img, 'You have made 2 unsuccessful tries for both arms. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_gobletsquat_set2 = False

        if dir_gen_feedback_unsuccessful_gobletsquat_set2 == 0:
            general_feedback_left_gobletsquat_set2 = detector_gobletsquat.left_leg_unsuccessful_feedback(total_reps_count_left_gobletsquat_set2)
            general_feedback_right_gobletsquat_set2 = detector_gobletsquat.right_leg_unsuccessful_feedback(total_reps_count_right_gobletsquat_set2)
            dir_gen_feedback_unsuccessful_gobletsquat_set2 = 1
            exercise_mode = "rest_gs_set2"
            rest_goblet_squat_start_time_set2 = time.time()

    if unsuccessful_reps_count_left_gobletsquat_set2 >= 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for left arm. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_gobletsquat_set2 = False

        if dir_gen_feedback_unsuccessful_gobletsquat_set2 == 0:
            general_feedback_left_gobletsquat_set2 = detector_gobletsquat.left_leg_unsuccessful_feedback(total_reps_count_left_gobletsquat_set2)
            dir_gen_feedback_unsuccessful_gobletsquat_set2 = 1
            exercise_mode = "rest_gs_set2"
            rest_goblet_squat_start_time_set2 = time.time()

    if unsuccessful_reps_count_right_gobletsquat_set2 >= 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for right arm. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_gobletsquat_set2 = False

        if dir_gen_feedback_unsuccessful_gobletsquat_set2 == 0:
            general_feedback_right_gobletsquat_set2 = detector_gobletsquat.right_leg_unsuccessful_feedback(total_reps_count_right_gobletsquat_set2)
            dir_gen_feedback_unsuccessful_gobletsquat_set2 == 1
            exercise_mode = "rest_gs_set2"
            rest_goblet_squat_start_time_set2 = time.time()

    return img

def rest_gs_set2(img):
    global exercise_mode, rest_goblet_squat_start_time_set2, start_time1_gobletsquat_set3
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_goblet_squat_start_time_set2
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "goblet_squat_set3"
        start_time1_gobletsquat_set3 = time.time()
    return img

def detect_gs_set3(img):
    global dir_left_gobletsquat_set3, dir_right_gobletsquat_set3, display_info_gobletsquat_set3, per_right_gobletsquat_set3, per_left_gobletsquat_set3, bar_left_gobletsquat_set3, bar_right_gobletsquat_set3, color_right_gobletsquat_set3, color_left_gobletsquat_set3, feedback_left_gobletsquat_set3, feedback_right_gobletsquat_set3, success_threshold_gobletsquat_set3, atrest_value_gobletsquat_set3, unsuccessful_reps_count_left_gobletsquat_set3, successful_reps_count_left_gobletsquat_set3, unsuccessful_reps_count_right_gobletsquat_set3, successful_reps_count_right_gobletsquat_set3, dir_left_unsuccessful_gobletsquat_set3, dir_right_unsuccessful_gobletsquat_set3, total_reps_count_gobletsquat_set3, total_reps_count_left_gobletsquat_set3, total_reps_count_right_gobletsquat_set3, start_time1_gobletsquat_set3, start_time2_gobletsquat_set3, start_time3_gobletsquat_set3, time_threshold_gobletsquat_set3, within_range_time1_gobletsquat_set3, within_range_time2_gobletsquat_set3, general_feedback_left_gobletsquat_set3, general_feedback_right_gobletsquat_set3, dir_gen_feedback_gobletsquat_set3, dir_gen_feedback_unsuccessful_gobletsquat_set3, cooldown_timer_gobletsquat_set3, cooldown_duration_gobletsquat_set3, rest_goblet_squat_start_time_set3, exercise_mode


    img = cv2.resize(img, (1280, 720))

    elapsed_time_gobletsquat = time.time() - start_time1_gobletsquat_set3
    remaining_time_gobletsquat = max(0, 60 - elapsed_time_gobletsquat)

    if display_info_gobletsquat_set3:  # Check if to display counter, bar, and percentage
        img = detector_gobletsquat.findPose(img, False)
        lmList_gobletsquat = detector_gobletsquat.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_gobletsquat) != 0:

            # Right and Left keypoints
            rightleg_gobletsquat_set3 = detector_gobletsquat.GobletSquat(img, 24, 26, 28, True)
            leftleg_gobletsquat_set3 = detector_gobletsquat.GobletSquat(img, 23, 25, 27, True)

            if cooldown_timer_gobletsquat_set3 > 0:
                cooldown_timer_gobletsquat_set3 -= 1

            per_right_gobletsquat_set3 = np.interp(rightleg_gobletsquat_set3, (160, 240), (100, 0))
            bar_right_gobletsquat_set3 = np.interp(rightleg_gobletsquat_set3, (160, 240), (480, 680))
            per_left_gobletsquat_set3 = np.interp(leftleg_gobletsquat_set3, (160, 240), (100, 0))
            bar_left_gobletsquat_set3 = np.interp(leftleg_gobletsquat_set3, (160, 240), (480, 680))

            if int(per_left_gobletsquat_set3) == 100:
                color_left_gobletsquat_set3 = (0, 255, 0)  # Change color of left leg bar to green
            else:
                color_left_gobletsquat_set3 = (0, 0, 255)
            
            if int(per_right_gobletsquat_set3) == 100:
                color_right_gobletsquat_set3 = (0, 255, 0)
            else:
                color_right_gobletsquat_set3 = (0, 0, 255)

            #left
            if 40 <= per_left_gobletsquat_set3 <= 90:
                # Increment the time within range
                within_range_time1_gobletsquat_set3 += time.time() - start_time2_gobletsquat_set3

                # Check if peak value has been within range for the specified time
                if within_range_time1_gobletsquat_set3 >= time_threshold_gobletsquat_set3:
                    if dir_left_unsuccessful_gobletsquat_set3 == 0:
                        unsuccessful_reps_count_left_gobletsquat_set3 += 0.5
                        dir_left_unsuccessful_gobletsquat_set3 = 1
            else:
                within_range_time1_gobletsquat_set3 = 0
                # Update the start time to the current time
                start_time2_gobletsquat_set3 = time.time()

            if 1 <= per_left_gobletsquat_set3 <= 10:
                if dir_left_unsuccessful_gobletsquat_set3 == 1:
                    unsuccessful_reps_count_left_gobletsquat_set3 += 0.5
                    dir_left_unsuccessful_gobletsquat_set3 = 0

            if per_left_gobletsquat_set3 == success_threshold_gobletsquat_set3:
                if dir_left_gobletsquat_set3 == 0:
                    successful_reps_count_left_gobletsquat_set3 += 0.5
                    dir_left_gobletsquat_set3 = 1

            elif per_left_gobletsquat_set3 == atrest_value_gobletsquat_set3:
                if dir_left_gobletsquat_set3 == 1:
                    successful_reps_count_left_gobletsquat_set3 += 0.5
                    dir_left_gobletsquat_set3 = 0

            # right
            if 40 <= per_right_gobletsquat_set3 <= 90:
                # Increment the time within range
                within_range_time2_gobletsquat_set3 += time.time() - start_time3_gobletsquat_set3

                # Check if peak value has been within range for the specified time
                if within_range_time2_gobletsquat_set3 >= time_threshold_gobletsquat_set3:
                    if dir_right_unsuccessful_gobletsquat_set3 == 0:
                        unsuccessful_reps_count_right_gobletsquat_set3 += 0.5
                        dir_right_unsuccessful_gobletsquat_set3 = 1
            else:
                within_range_time2_gobletsquat_set3 = 0
                # Update the start time to the current time
                start_time3_gobletsquat_set3 = time.time()

            if 1 <= per_right_gobletsquat_set3 <= 10:
                if dir_right_unsuccessful_gobletsquat_set3 == 1:
                    unsuccessful_reps_count_right_gobletsquat_set3 += 0.5
                    dir_right_unsuccessful_gobletsquat_set3 = 0

            if per_right_gobletsquat_set3 == success_threshold_gobletsquat_set3:
                if dir_right_gobletsquat_set3 == 0:
                    successful_reps_count_right_gobletsquat_set3 += 0.5
                    dir_right_gobletsquat_set3 = 1
                    cooldown_timer_gobletsquat_set3 = cooldown_duration_gobletsquat_set3
            elif per_right_gobletsquat_set3 == atrest_value_gobletsquat_set3: 
                if dir_right_gobletsquat_set3 == 1:
                    successful_reps_count_right_gobletsquat_set3 += 0.5
                    dir_right_gobletsquat_set3 = 0
                    cooldown_timer_gobletsquat_set3 = cooldown_duration_gobletsquat_set3

            # feedback for left hand  # TO BE FETCHED 
            feedback_left_gobletsquat_set3 = detector_gobletsquat.feedback_gobletsquat(per_left_gobletsquat_set3)

            detector_gobletsquat.update_next_per_left(per_left_gobletsquat_set3)

            # feedback for right hand  # TO BE FETCHED 
            feedback_right_gobletsquat_set3 = detector_gobletsquat.feedback_gobletsquat(per_right_gobletsquat_set3)

            detector_gobletsquat.update_next_per_left(per_right_gobletsquat_set3)


        cvzone.putTextRect(img, 'Front Goblet Squat SET 3', [450, 30], thickness=2, border=2, scale=1.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time_gobletsquat)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)
        # RIGHT LEG
        cv2.putText(img, f"R {int(per_right_gobletsquat_set3)}%", (24, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 480), (50, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_gobletsquat_set3)), (50, 680), color_right_gobletsquat_set3, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_left_gobletsquat_set3)}%", (962, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 480), (995, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_gobletsquat_set3)), (995, 680), color_left_gobletsquat_set3, -1)

    # Counter 
    cv2.rectangle(img, (20, 20), (200, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(successful_reps_count_right_gobletsquat_set3)}/10", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (210, 20), (390, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(successful_reps_count_left_gobletsquat_set3)}/10", (220, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)


    #Timer
    if remaining_time_gobletsquat <= 0:
        cvzone.putTextRect(img, "Time's Up", [420, 30], thickness=2, border=2, scale=2.5)
        display_info_gobletsquat_set3 = False
        exercise_mode = "rest_gs_set3"
        rest_goblet_squat_start_time_set3 = time.time()

    total_reps_count_left_gobletsquat_set3 = successful_reps_count_left_gobletsquat_set3 + unsuccessful_reps_count_left_gobletsquat_set3
    total_reps_count_right_gobletsquat_set3 = successful_reps_count_right_gobletsquat_set3 + unsuccessful_reps_count_right_gobletsquat_set3

    if successful_reps_count_right_gobletsquat_set3 >= 10 and successful_reps_count_left_gobletsquat_set3 >= 10:
            cvzone.putTextRect(img, 'All Repetitions Completed', [420, 30], thickness=2, border=2, scale=2.5)
            display_info_gobletsquat_set3 = False
            # General feedback after finishing the exercise # TO BE FETCHED
            if dir_gen_feedback_gobletsquat_set3 == 0:
                general_feedback_left_gobletsquat_set3 = detector_gobletsquat.left_leg_feedback(total_reps_count_left_gobletsquat_set3)
                general_feedback_right_gobletsquat_set3 = detector_gobletsquat.right_leg_feedback(total_reps_count_right_gobletsquat_set3)
                dir_gen_feedback_gobletsquat_set3 = 1
                exercise_mode = "rest_gs_set3"
                rest_goblet_squat_start_time_set3 = time.time()

    if unsuccessful_reps_count_left_gobletsquat_set3 >= 3 and unsuccessful_reps_count_right_gobletsquat_set3 >= 3:
        cvzone.putTextRect(img, 'You have made 2 unsuccessful tries for both arms. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_gobletsquat_set3 = False

        if dir_gen_feedback_unsuccessful_gobletsquat_set3 == 0:
            general_feedback_left_gobletsquat_set3 = detector_gobletsquat.left_leg_unsuccessful_feedback(total_reps_count_left_gobletsquat_set3)
            general_feedback_right_gobletsquat_set3 = detector_gobletsquat.right_leg_unsuccessful_feedback(total_reps_count_right_gobletsquat_set3)
            dir_gen_feedback_unsuccessful_gobletsquat_set3 = 1
            exercise_mode = "rest_gs_set3"
            rest_goblet_squat_start_time_set3 = time.time()

    if unsuccessful_reps_count_left_gobletsquat_set3 >= 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for left arm. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_gobletsquat_set3 = False

        if dir_gen_feedback_unsuccessful_gobletsquat_set3 == 0:
            general_feedback_left_gobletsquat_set3 = detector_gobletsquat.left_leg_unsuccessful_feedback(total_reps_count_left_gobletsquat_set3)
            dir_gen_feedback_unsuccessful_gobletsquat_set3 = 1
            exercise_mode = "rest_gs_set3"
            rest_goblet_squat_start_time_set3 = time.time()

    if unsuccessful_reps_count_right_gobletsquat_set3 >= 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for right arm. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_gobletsquat_set3 = False

        if dir_gen_feedback_unsuccessful_gobletsquat_set3 == 0:
            general_feedback_right_gobletsquat_set3 = detector_gobletsquat.right_leg_unsuccessful_feedback(total_reps_count_right_gobletsquat_set3)
            dir_gen_feedback_unsuccessful_gobletsquat_set3 == 1
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
    global dir_left_highkneetap, dir_right_highkneetap, display_info_highkneetap, per_right_highkneetap, per_left_highkneetap, bar_left_highkneetap, bar_right_highkneetap, color_right_highkneetap, color_left_highkneetap, feedback_left_highkneetap, feedback_right_highkneetap, success_threshold_highkneetap, atrest_value_highkneetap, unsuccessful_reps_count_left_highkneetap, successful_reps_count_left_highkneetap, unsuccessful_reps_count_right_highkneetap, successful_reps_count_right_highkneetap, dir_left_unsuccessful_highkneetap, dir_right_unsuccessful_highkneetap, total_reps_count_highkneetap, total_reps_count_left_highkneetap, total_reps_count_right_highkneetap, start_time1_highkneetap, start_time2_highkneetap, start_time3_highkneetap, time_threshold_highkneetap, within_range_time1_highkneetap, within_range_time2_highkneetap, general_feedback_left_highkneetap, general_feedback_right_highkneetap, dir_gen_feedback_highkneetap, dir_gen_feedback_unsuccessful_highkneetap, cooldown_timer_highkneetap, cooldown_duration_highkneetap, leftleg_highkneetap, rightleg_highkneetap, rest_hkt_start_time, exercise_mode

    img = cv2.resize(img, (1280, 720))

    elapsed_time_highkneetap = time.time() - start_time1_highkneetap
    remaining_time_highkneetap = max(0, 10 - elapsed_time_highkneetap)

    if display_info_highkneetap:  # Check if to display counter, bar, and percentage
        img = detector_highkneetap.findPose(img, False)
        lmList_highkneetap = detector_highkneetap.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_highkneetap) != 0:

            # Right and Left keypoints
            rightleg_highkneetap = detector_highkneetap.HighKneeTap(img, 24, 26, 28, True)
            leftleg_highkneetap = detector_highkneetap.HighKneeTap(img, 23, 25, 27, True)

            if cooldown_timer_highkneetap > 0:
                cooldown_timer_highkneetap -= 1

            per_right_highkneetap = np.interp(rightleg_highkneetap, (150, 240), (100, 0))
            bar_right_highkneetap = np.interp(rightleg_highkneetap, (150, 240), (480, 680))

            per_left_highkneetap = np.interp(leftleg_highkneetap, (150, 240), (100, 0))
            bar_left_highkneetap = np.interp(leftleg_highkneetap, (150, 240), (480, 680))

            if int(per_left_highkneetap) == 100:
                color_left_highkneetap = (0, 255, 0)  # Change color of left leg bar to green
            else:
                color_left_highkneetap = (0, 0, 255)
            
            if int(per_right_highkneetap) == 100:
                color_right_highkneetap = (0, 255, 0)
            else:
                color_right_highkneetap = (0, 0, 255)

            #left
            if 40 <= per_left_highkneetap <= 90:
                # Increment the time within range
                within_range_time1_highkneetap += time.time() - start_time2_highkneetap

                # Check if peak value has been within range for the specified time
                if within_range_time1_highkneetap >= time_threshold_highkneetap:
                    if dir_left_unsuccessful_highkneetap == 0:
                        unsuccessful_reps_count_left_highkneetap += 0.5
                        dir_left_unsuccessful_highkneetap = 1
            else:
                within_range_time1_highkneetap = 0
                # Update the start time to the current time
                start_time2_highkneetap = time.time()

            if 1 <= per_left_highkneetap <= 10:
                if dir_left_unsuccessful_highkneetap == 1:
                    unsuccessful_reps_count_left_highkneetap += 0.5
                    dir_left_unsuccessful_highkneetap = 0

            if per_left_highkneetap == success_threshold_highkneetap:
                if dir_left_highkneetap == 0:
                    successful_reps_count_left_highkneetap += 0.5
                    dir_left_highkneetap = 1

            elif per_left_highkneetap == atrest_value_highkneetap:
                if dir_left_highkneetap == 1:
                    successful_reps_count_left_highkneetap += 0.5
                    dir_left_highkneetap = 0

            # right
            if 40 <= per_right_highkneetap <= 90:
                # Increment the time within range
                within_range_time2_highkneetap += time.time() - start_time3_highkneetap

                # Check if peak value has been within range for the specified time
                if within_range_time2_highkneetap >= time_threshold_highkneetap:
                    if dir_right_unsuccessful_highkneetap == 0:
                        unsuccessful_reps_count_right_highkneetap += 0.5
                        dir_right_unsuccessful_highkneetap = 1
            else:
                within_range_time2_highkneetap = 0
                # Update the start time to the current time
                start_time3_highkneetap = time.time()

            if 1 <= per_right_highkneetap <= 10:
                if dir_right_unsuccessful_highkneetap == 1:
                    unsuccessful_reps_count_right_highkneetap += 0.5
                    dir_right_unsuccessful_highkneetap = 0

            if per_right_highkneetap == success_threshold_highkneetap:
                if dir_right_highkneetap == 0:
                    successful_reps_count_right_highkneetap += 0.5
                    dir_right_highkneetap = 1
                    cooldown_timer_highkneetap = cooldown_duration_highkneetap
            elif per_right_highkneetap == atrest_value_highkneetap: 
                if dir_right_highkneetap == 1:
                    successful_reps_count_right_highkneetap += 0.5
                    dir_right_highkneetap = 0
                    cooldown_timer_highkneetap = cooldown_duration_highkneetap

            # feedback for left hand  # TO BE FETCHED 
            feedback_left_highkneetap = detector_highkneetap.feedback_highkneetap(per_left_highkneetap)

            detector_highkneetap.update_next_per_left(per_left_highkneetap)

            # feedback for right hand  # TO BE FETCHED 
            feedback_right_highkneetap = detector_highkneetap.feedback_highkneetap(per_right_highkneetap)

            detector_highkneetap.update_next_per_left(per_right_highkneetap)


        cvzone.putTextRect(img, 'Front High Knee Tap', [450, 30], thickness=2, border=2, scale=1.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time_highkneetap)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # RIGHT LEG
        cv2.putText(img, f"R {int(per_right_highkneetap)}%", (24, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 480), (50, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_highkneetap)), (50, 680), color_right_highkneetap, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_left_highkneetap)}%", (962, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 480), (995, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_highkneetap)), (995, 680), color_left_highkneetap, -1)
    
    # Counter 
    cv2.rectangle(img, (20, 20), (200, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(successful_reps_count_right_highkneetap)}/10", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (210, 20), (390, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(successful_reps_count_left_highkneetap)}/10", (220, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    #Timer
    if remaining_time_highkneetap <= 0:
        cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
        display_info_highkneetap = False
        exercise_mode = "rest_hkt"
        rest_hkt_start_time = time.time()

    total_reps_count_left_highkneetap = successful_reps_count_left_highkneetap + unsuccessful_reps_count_left_highkneetap
    total_reps_count_right_highkneetap = successful_reps_count_right_highkneetap + unsuccessful_reps_count_right_highkneetap

    if successful_reps_count_right_highkneetap >= 10 and successful_reps_count_left_highkneetap >= 10:
            cvzone.putTextRect(img, 'All Repetitions Completed', [420, 30], thickness=2, border=2, scale=2.5)
            display_info_highkneetap = False
            # General feedback after finishing the exercise # TO BE FETCHED
            if dir_gen_feedback_highkneetap == 0:
                general_feedback_left_highkneetap = detector_highkneetap.left_leg_feedback(total_reps_count_left_highkneetap)
                general_feedback_right_highkneetap = detector_highkneetap.right_leg_feedback(total_reps_count_right_highkneetap)
                dir_gen_feedback_highkneetap = 1
                exercise_mode = "rest_hkt"
                rest_hkt_start_time = time.time()

    if unsuccessful_reps_count_left_highkneetap >= 3 and unsuccessful_reps_count_right_highkneetap >= 3:
        cvzone.putTextRect(img, 'You have made 2 unsuccessful tries for both arms. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_highkneetap = False

        if dir_gen_feedback_unsuccessful_highkneetap == 0:
            general_feedback_left_highkneetap = detector_highkneetap.left_leg_unsuccessful_feedback(total_reps_count_left_highkneetap)
            general_feedback_right_highkneetap = detector_highkneetap.right_leg_unsuccessful_feedback(total_reps_count_right_highkneetap)
            dir_gen_feedback_unsuccessful_highkneetap = 1
            exercise_mode = "rest_hkt"
            rest_hkt_start_time = time.time()

    if unsuccessful_reps_count_left_highkneetap >= 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for left arm. Please retry again', [420, 30], thickness=2, border=2, scale=1)
        display_info_highkneetap = False

        if dir_gen_feedback_unsuccessful_highkneetap == 0:
            general_feedback_left_highkneetap = detector_highkneetap.left_leg_unsuccessful_feedback(total_reps_count_left_highkneetap)
            dir_gen_feedback_unsuccessful_highkneetap = 1
            exercise_mode = "rest_hkt"
            rest_hkt_start_time = time.time()

    if unsuccessful_reps_count_right_highkneetap >= 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for right arm. Please retry again', [420, 30], thickness=2, border=2, scale=1)
        display_info_highkneetap = False

        if dir_gen_feedback_unsuccessful_highkneetap == 0:
            general_feedback_right_highkneetap = detector_highkneetap.right_leg_unsuccessful_feedback(total_reps_count_right_highkneetap)
            dir_gen_feedback_unsuccessful_highkneetap == 1
            exercise_mode = "rest_hkt"
            rest_hkt_start_time = time.time()
    return img

def rest_hkt(img):
    global exercise_mode, rest_hkt_start_time, start_time1_highkneetap_set2
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
        start_time1_highkneetap_set2 = time.time()
    return img

def detect_hkt_set2(img):
    global dir_left_highkneetap_set2, dir_right_highkneetap_set2, display_info_highkneetap_set2, per_right_highkneetap_set2, per_left_highkneetap_set2, bar_left_highkneetap_set2, bar_right_highkneetap_set2, color_right_highkneetap_set2, color_left_highkneetap_set2, feedback_left_highkneetap_set2, feedback_right_highkneetap_set2, success_threshold_highkneetap_set2, atrest_value_highkneetap_set2, unsuccessful_reps_count_left_highkneetap_set2, successful_reps_count_left_highkneetap_set2, unsuccessful_reps_count_right_highkneetap_set2, successful_reps_count_right_highkneetap_set2, dir_left_unsuccessful_highkneetap_set2, dir_right_unsuccessful_highkneetap_set2, total_reps_count_highkneetap_set2, total_reps_count_left_highkneetap_set2, total_reps_count_right_highkneetap_set2, start_time1_highkneetap_set2, start_time2_highkneetap_set2, start_time3_highkneetap_set2, time_threshold_highkneetap_set2, within_range_time1_highkneetap_set2, within_range_time2_highkneetap_set2, general_feedback_left_highkneetap_set2, general_feedback_right_highkneetap_set2, dir_gen_feedback_highkneetap_set2, dir_gen_feedback_unsuccessful_highkneetap_set2, cooldown_timer_highkneetap_set2, cooldown_duration_highkneetap_set2, leftleg_highkneetap_set2, rightleg_highkneetap_set2, rest_hkt_start_time_set2, exercise_mode

    img = cv2.resize(img, (1280, 720))

    elapsed_time_highkneetap = time.time() - start_time1_highkneetap_set2
    remaining_time_highkneetap = max(0, 10 - elapsed_time_highkneetap)

    if display_info_highkneetap_set2:  # Check if to display counter, bar, and percentage
        img = detector_highkneetap.findPose(img, False)
        lmList_highkneetap = detector_highkneetap.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_highkneetap) != 0:

            # Right and Left keypoints
            rightleg_highkneetap_set2 = detector_highkneetap.HighKneeTap(img, 24, 26, 28, True)
            leftleg_highkneetap_set2 = detector_highkneetap.HighKneeTap(img, 23, 25, 27, True)

            if cooldown_timer_highkneetap_set2 > 0:
                cooldown_timer_highkneetap_set2 -= 1

            per_right_highkneetap_set2 = np.interp(rightleg_highkneetap_set2, (150, 240), (100, 0))
            bar_right_highkneetap_set2 = np.interp(rightleg_highkneetap_set2, (150, 240), (480, 680))

            per_left_highkneetap_set2 = np.interp(leftleg_highkneetap_set2, (150, 240), (100, 0))
            bar_left_highkneetap_set2 = np.interp(leftleg_highkneetap_set2, (150, 240), (480, 680))

            if int(per_left_highkneetap_set2) == 100:
                color_left_highkneetap_set2 = (0, 255, 0)  # Change color of left leg bar to green
            else:
                color_left_highkneetap_set2 = (0, 0, 255)
            
            if int(per_right_highkneetap_set2) == 100:
                color_right_highkneetap_set2 = (0, 255, 0)
            else:
                color_right_highkneetap_set2 = (0, 0, 255)

            #left
            if 40 <= per_left_highkneetap_set2 <= 90:
                # Increment the time within range
                within_range_time1_highkneetap_set2 += time.time() - start_time2_highkneetap_set2

                # Check if peak value has been within range for the specified time
                if within_range_time1_highkneetap_set2 >= time_threshold_highkneetap_set2:
                    if dir_left_unsuccessful_highkneetap_set2 == 0:
                        unsuccessful_reps_count_left_highkneetap_set2 += 0.5
                        dir_left_unsuccessful_highkneetap_set2 = 1
            else:
                within_range_time1_highkneetap_set2 = 0
                # Update the start time to the current time
                start_time2_highkneetap_set2 = time.time()

            if 1 <= per_left_highkneetap_set2 <= 10:
                if dir_left_unsuccessful_highkneetap_set2 == 1:
                    unsuccessful_reps_count_left_highkneetap_set2 += 0.5
                    dir_left_unsuccessful_highkneetap_set2 = 0

            if per_left_highkneetap_set2 == success_threshold_highkneetap_set2:
                if dir_left_highkneetap_set2 == 0:
                    successful_reps_count_left_highkneetap_set2 += 0.5
                    dir_left_highkneetap_set2 = 1

            elif per_left_highkneetap_set2 == atrest_value_highkneetap_set2:
                if dir_left_highkneetap_set2 == 1:
                    successful_reps_count_left_highkneetap_set2 += 0.5
                    dir_left_highkneetap_set2 = 0

            # right
            if 40 <= per_right_highkneetap_set2 <= 90:
                # Increment the time within range
                within_range_time2_highkneetap_set2 += time.time() - start_time3_highkneetap_set2

                # Check if peak value has been within range for the specified time
                if within_range_time2_highkneetap_set2 >= time_threshold_highkneetap_set2:
                    if dir_right_unsuccessful_highkneetap_set2 == 0:
                        unsuccessful_reps_count_right_highkneetap_set2 += 0.5
                        dir_right_unsuccessful_highkneetap_set2 = 1
            else:
                within_range_time2_highkneetap_set2 = 0
                # Update the start time to the current time
                start_time3_highkneetap_set2 = time.time()

            if 1 <= per_right_highkneetap_set2 <= 10:
                if dir_right_unsuccessful_highkneetap_set2 == 1:
                    unsuccessful_reps_count_right_highkneetap_set2 += 0.5
                    dir_right_unsuccessful_highkneetap_set2 = 0

            if per_right_highkneetap_set2 == success_threshold_highkneetap_set2:
                if dir_right_highkneetap_set2 == 0:
                    successful_reps_count_right_highkneetap_set2 += 0.5
                    dir_right_highkneetap_set2 = 1
                    cooldown_timer_highkneetap_set2 = cooldown_duration_highkneetap_set2
            elif per_right_highkneetap_set2 == atrest_value_highkneetap_set2: 
                if dir_right_highkneetap_set2 == 1:
                    successful_reps_count_right_highkneetap_set2 += 0.5
                    dir_right_highkneetap_set2 = 0
                    cooldown_timer_highkneetap_set2 = cooldown_duration_highkneetap_set2

            # feedback for left hand  # TO BE FETCHED 
            feedback_left_highkneetap_set2 = detector_highkneetap.feedback_highkneetap(per_left_highkneetap_set2)

            detector_highkneetap.update_next_per_left(per_left_highkneetap_set2)

            # feedback for right hand  # TO BE FETCHED 
            feedback_right_highkneetap_set2 = detector_highkneetap.feedback_highkneetap(per_right_highkneetap_set2)

            detector_highkneetap.update_next_per_left(per_right_highkneetap_set2)


        cvzone.putTextRect(img, 'Front High Knee Tap SET 2', [450, 30], thickness=2, border=2, scale=1.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time_highkneetap)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # RIGHT LEG
        cv2.putText(img, f"R {int(per_right_highkneetap_set2)}%", (24, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 480), (50, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_highkneetap_set2)), (50, 680), color_right_highkneetap_set2, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_left_highkneetap_set2)}%", (962, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 480), (995, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_highkneetap_set2)), (995, 680), color_left_highkneetap_set2, -1)
    
    # Counter 
    cv2.rectangle(img, (20, 20), (200, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(successful_reps_count_right_highkneetap_set2)}/10", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (210, 20), (390, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(successful_reps_count_left_highkneetap_set2)}/10", (220, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    #Timer
    if remaining_time_highkneetap <= 0:
        cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
        display_info_highkneetap_set2 = False
        exercise_mode = "rest_hkt_set2"
        rest_hkt_start_time_set2 = time.time()

    total_reps_count_left_highkneetap_set2 = successful_reps_count_left_highkneetap_set2 + unsuccessful_reps_count_left_highkneetap_set2
    total_reps_count_right_highkneetap_set2 = successful_reps_count_right_highkneetap_set2 + unsuccessful_reps_count_right_highkneetap_set2

    if successful_reps_count_right_highkneetap_set2 >= 10 and successful_reps_count_left_highkneetap_set2 >= 10:
            cvzone.putTextRect(img, 'All Repetitions Completed', [420, 30], thickness=2, border=2, scale=2.5)
            display_info_highkneetap_set2 = False
            # General feedback after finishing the exercise # TO BE FETCHED
            if dir_gen_feedback_highkneetap_set2 == 0:
                general_feedback_left_highkneetap_set2 = detector_highkneetap.left_leg_feedback(total_reps_count_left_highkneetap_set2)
                general_feedback_right_highkneetap_set2 = detector_highkneetap.right_leg_feedback(total_reps_count_right_highkneetap_set2)
                dir_gen_feedback_highkneetap_set2 = 1
                exercise_mode = "rest_hkt_set2"
                rest_hkt_start_time_set2 = time.time()

    if unsuccessful_reps_count_left_highkneetap_set2 >= 3 and unsuccessful_reps_count_right_highkneetap_set2 >= 3:
        cvzone.putTextRect(img, 'You have made 2 unsuccessful tries for both arms. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_highkneetap_set2 = False

        if dir_gen_feedback_unsuccessful_highkneetap_set2 == 0:
            general_feedback_left_highkneetap_set2 = detector_highkneetap.left_leg_unsuccessful_feedback(total_reps_count_left_highkneetap_set2)
            general_feedback_right_highkneetap_set2 = detector_highkneetap.right_leg_unsuccessful_feedback(total_reps_count_right_highkneetap_set2)
            dir_gen_feedback_unsuccessful_highkneetap_set2 = 1
            exercise_mode = "rest_hkt_set2"
            rest_hkt_start_time_set2 = time.time()

    if unsuccessful_reps_count_left_highkneetap_set2 >= 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for left arm. Please retry again', [420, 30], thickness=2, border=2, scale=1)
        display_info_highkneetap_set2 = False

        if dir_gen_feedback_unsuccessful_highkneetap_set2 == 0:
            general_feedback_left_highkneetap_set2 = detector_highkneetap.left_leg_unsuccessful_feedback(total_reps_count_left_highkneetap_set2)
            dir_gen_feedback_unsuccessful_highkneetap_set2 = 1
            exercise_mode = "rest_hkt_set2"
            rest_hkt_start_time_set2 = time.time()

    if unsuccessful_reps_count_right_highkneetap_set2 >= 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for right arm. Please retry again', [420, 30], thickness=2, border=2, scale=1)
        display_info_highkneetap_set2 = False

        if dir_gen_feedback_unsuccessful_highkneetap_set2 == 0:
            general_feedback_right_highkneetap_set2 = detector_highkneetap.right_leg_unsuccessful_feedback(total_reps_count_right_highkneetap_set2)
            dir_gen_feedback_unsuccessful_highkneetap_set2 == 1
            exercise_mode = "rest_hkt_set2"
            rest_hkt_start_time_set2 = time.time()

    return img

def rest_hkt_set2(img):
    global exercise_mode, rest_hkt_start_time_set2, start_time1_highkneetap_set3
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
        start_time1_highkneetap_set3 = time.time()

    return img

def detect_hkt_set3(img):
    global dir_left_highkneetap_set3, dir_right_highkneetap_set3, display_info_highkneetap_set3, per_right_highkneetap_set3, per_left_highkneetap_set3, bar_left_highkneetap_set3, bar_right_highkneetap_set3, color_right_highkneetap_set3, color_left_highkneetap_set3, feedback_left_highkneetap_set3, feedback_right_highkneetap_set3, success_threshold_highkneetap_set3, atrest_value_highkneetap_set3, unsuccessful_reps_count_left_highkneetap_set3, successful_reps_count_left_highkneetap_set3, unsuccessful_reps_count_right_highkneetap_set3, successful_reps_count_right_highkneetap_set3, dir_left_unsuccessful_highkneetap_set3, dir_right_unsuccessful_highkneetap_set3, total_reps_count_highkneetap_set3, total_reps_count_left_highkneetap_set3, total_reps_count_right_highkneetap_set3, start_time1_highkneetap_set3, start_time2_highkneetap_set3, start_time3_highkneetap_set3, time_threshold_highkneetap_set3, within_range_time1_highkneetap_set3, within_range_time2_highkneetap_set3, general_feedback_left_highkneetap_set3, general_feedback_right_highkneetap_set3, dir_gen_feedback_highkneetap_set3, dir_gen_feedback_unsuccessful_highkneetap_set3, cooldown_timer_highkneetap_set3, cooldown_duration_highkneetap_set3, leftleg_highkneetap_set3, rightleg_highkneetap_set3, rest_hkt_start_time_set3, exercise_mode

    img = cv2.resize(img, (1280, 720))

    elapsed_time_highkneetap = time.time() - start_time1_highkneetap_set3
    remaining_time_highkneetap = max(0, 10 - elapsed_time_highkneetap)

    if display_info_highkneetap_set3:  # Check if to display counter, bar, and percentage
        img = detector_highkneetap.findPose(img, False)
        lmList_highkneetap = detector_highkneetap.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_highkneetap) != 0:

            # Right and Left keypoints
            rightleg_highkneetap_set3 = detector_highkneetap.HighKneeTap(img, 24, 26, 28, True)
            leftleg_highkneetap_set3 = detector_highkneetap.HighKneeTap(img, 23, 25, 27, True)

            if cooldown_timer_highkneetap_set3 > 0:
                cooldown_timer_highkneetap_set3 -= 1

            per_right_highkneetap_set3 = np.interp(rightleg_highkneetap_set3, (150, 240), (100, 0))
            bar_right_highkneetap_set3 = np.interp(rightleg_highkneetap_set3, (150, 240), (480, 680))

            per_left_highkneetap_set3 = np.interp(leftleg_highkneetap_set3, (150, 240), (100, 0))
            bar_left_highkneetap_set3 = np.interp(leftleg_highkneetap_set3, (150, 240), (480, 680))

            if int(per_left_highkneetap_set3) == 100:
                color_left_highkneetap_set3 = (0, 255, 0)  # Change color of left leg bar to green
            else:
                color_left_highkneetap_set3 = (0, 0, 255)
            
            if int(per_right_highkneetap_set3) == 100:
                color_right_highkneetap_set3 = (0, 255, 0)
            else:
                color_right_highkneetap_set3 = (0, 0, 255)

            #left
            if 40 <= per_left_highkneetap <= 90:
                # Increment the time within range
                within_range_time1_highkneetap_set3 += time.time() - start_time2_highkneetap_set3

                # Check if peak value has been within range for the specified time
                if within_range_time1_highkneetap_set3 >= time_threshold_highkneetap_set3:
                    if dir_left_unsuccessful_highkneetap_set3 == 0:
                        unsuccessful_reps_count_left_highkneetap_set3 += 0.5
                        dir_left_unsuccessful_highkneetap_set3 = 1
            else:
                within_range_time1_highkneetap_set3 = 0
                # Update the start time to the current time
                start_time2_highkneetap_set3 = time.time()

            if 1 <= per_left_highkneetap_set3 <= 10:
                if dir_left_unsuccessful_highkneetap_set3 == 1:
                    unsuccessful_reps_count_left_highkneetap_set3 += 0.5
                    dir_left_unsuccessful_highkneetap_set3 = 0

            if per_left_highkneetap_set3 == success_threshold_highkneetap_set3:
                if dir_left_highkneetap_set3 == 0:
                    successful_reps_count_left_highkneetap_set3 += 0.5
                    dir_left_highkneetap_set3 = 1

            elif per_left_highkneetap_set3 == atrest_value_highkneetap_set3:
                if dir_left_highkneetap_set3 == 1:
                    successful_reps_count_left_highkneetap_set3 += 0.5
                    dir_left_highkneetap_set3 = 0

            # right
            if 40 <= per_right_highkneetap_set3 <= 90:
                # Increment the time within range
                within_range_time2_highkneetap_set3 += time.time() - start_time3_highkneetap_set3

                # Check if peak value has been within range for the specified time
                if within_range_time2_highkneetap_set3 >= time_threshold_highkneetap_set3:
                    if dir_right_unsuccessful_highkneetap_set3 == 0:
                        unsuccessful_reps_count_right_highkneetap_set3 += 0.5
                        dir_right_unsuccessful_highkneetap_set3 = 1
            else:
                within_range_time2_highkneetap_set3 = 0
                # Update the start time to the current time
                start_time3_highkneetap_set3 = time.time()

            if 1 <= per_right_highkneetap_set3 <= 10:
                if dir_right_unsuccessful_highkneetap_set3 == 1:
                    unsuccessful_reps_count_right_highkneetap_set3 += 0.5
                    dir_right_unsuccessful_highkneetap_set3 = 0

            if per_right_highkneetap_set3 == success_threshold_highkneetap_set3:
                if dir_right_highkneetap_set3 == 0:
                    successful_reps_count_right_highkneetap_set3 += 0.5
                    dir_right_highkneetap_set3 = 1
                    cooldown_timer_highkneetap_set3 = cooldown_duration_highkneetap_set3
            elif per_right_highkneetap_set3 == atrest_value_highkneetap_set3: 
                if dir_right_highkneetap_set3 == 1:
                    successful_reps_count_right_highkneetap_set3 += 0.5
                    dir_right_highkneetap_set3 = 0
                    cooldown_timer_highkneetap_set3 = cooldown_duration_highkneetap_set3

            # feedback for left hand  # TO BE FETCHED 
            feedback_left_highkneetap_set3 = detector_highkneetap.feedback_highkneetap(per_left_highkneetap_set3)

            detector_highkneetap.update_next_per_left(per_left_highkneetap_set3)

            # feedback for right hand  # TO BE FETCHED 
            feedback_right_highkneetap_set3 = detector_highkneetap.feedback_highkneetap(per_right_highkneetap_set3)

            detector_highkneetap.update_next_per_left(per_right_highkneetap_set3)


        cvzone.putTextRect(img, 'Front High Knee Tap SET 3', [450, 30], thickness=2, border=2, scale=1.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time_highkneetap)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # RIGHT LEG
        cv2.putText(img, f"R {int(per_right_highkneetap_set3)}%", (24, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 480), (50, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_highkneetap_set3)), (50, 680), color_right_highkneetap_set3, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_left_highkneetap_set3)}%", (962, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 480), (995, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_highkneetap_set3)), (995, 680), color_left_highkneetap_set3, -1)
    
    # Counter 
    cv2.rectangle(img, (20, 20), (200, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(successful_reps_count_right_highkneetap_set3)}/10", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (210, 20), (390, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(successful_reps_count_left_highkneetap_set3)}/10", (220, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    #Timer
    if remaining_time_highkneetap <= 0:
        cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
        display_info_highkneetap_set3 = False
        exercise_mode = "rest_hkt"
        rest_hkt_start_time_set3 = time.time()

    total_reps_count_left_highkneetap_set3 = successful_reps_count_left_highkneetap_set3 + unsuccessful_reps_count_left_highkneetap_set3
    total_reps_count_right_highkneetap_set3 = successful_reps_count_right_highkneetap_set3 + unsuccessful_reps_count_right_highkneetap_set3

    if successful_reps_count_right_highkneetap_set3 >= 10 and successful_reps_count_left_highkneetap_set3 >= 10:
            cvzone.putTextRect(img, 'All Repetitions Completed', [420, 30], thickness=2, border=2, scale=2.5)
            display_info_highkneetap_set3 = False
            # General feedback after finishing the exercise # TO BE FETCHED
            if dir_gen_feedback_highkneetap_set3 == 0:
                general_feedback_left_highkneetap_set3 = detector_highkneetap.left_leg_feedback(total_reps_count_left_highkneetap_set3)
                general_feedback_right_highkneetap_set3 = detector_highkneetap.right_leg_feedback(total_reps_count_right_highkneetap_set3)
                dir_gen_feedback_highkneetap_set3 = 1
                exercise_mode = "rest_hkt_set3"
                rest_hkt_start_time_set3 = time.time()

    if unsuccessful_reps_count_left_highkneetap_set3 >= 3 and unsuccessful_reps_count_right_highkneetap_set3 >= 3:
        cvzone.putTextRect(img, 'You have made 2 unsuccessful tries for both arms. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_highkneetap_set3 = False

        if dir_gen_feedback_unsuccessful_highkneetap_set3 == 0:
            general_feedback_left_highkneetap_set3 = detector_highkneetap.left_leg_unsuccessful_feedback(total_reps_count_left_highkneetap_set3)
            general_feedback_right_highkneetap_set3 = detector_highkneetap.right_leg_unsuccessful_feedback(total_reps_count_right_highkneetap_set3)
            dir_gen_feedback_unsuccessful_highkneetap_set3 = 1
            exercise_mode = "rest_hkt_set3"
            rest_hkt_start_time_set3 = time.time()

    if unsuccessful_reps_count_left_highkneetap_set3 >= 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for left arm. Please retry again', [420, 30], thickness=2, border=2, scale=1)
        display_info_highkneetap_set3 = False

        if dir_gen_feedback_unsuccessful_highkneetap_set3 == 0:
            general_feedback_left_highkneetap_set3 = detector_highkneetap.left_leg_unsuccessful_feedback(total_reps_count_left_highkneetap_set3)
            dir_gen_feedback_unsuccessful_highkneetap_set3 = 1
            exercise_mode = "rest_hkt_set3"
            rest_hkt_start_time_set3 = time.time()

    if unsuccessful_reps_count_right_highkneetap_set3 >= 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for right arm. Please retry again', [420, 30], thickness=2, border=2, scale=1)
        display_info_highkneetap_set3 = False

        if dir_gen_feedback_unsuccessful_highkneetap_set3 == 0:
            general_feedback_right_highkneetap_set3 = detector_highkneetap.right_leg_unsuccessful_feedback(total_reps_count_right_highkneetap_set3)
            dir_gen_feedback_unsuccessful_highkneetap_set3 == 1
            exercise_mode = "rest_hkt_set3"
            rest_hkt_start_time_set3 = time.time()
    return img

def rest_hkt_set3(img):
    global exercise_mode, rest_hkt_start_time_set3, start_time_hpp
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_hkt_start_time_set3
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

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
    global dir_left_dumbbellhiphinge, dir_right_dumbbellhiphinge, display_info_dumbbellhiphinge, per_right_dumbbellhiphinge, per_left_dumbbellhiphinge, bar_left_dumbbellhiphinge, bar_right_dumbbellhiphinge, color_right_dumbbellhiphinge, color_left_dumbbellhiphinge, feedback_left_dumbbellhiphinge, feedback_right_dumbbellhiphinge, success_threshold_dumbbellhiphinge, atrest_value_dumbbellhiphinge, unsuccessful_reps_count_left_dumbbellhiphinge, successful_reps_count_left_dumbbellhiphinge, unsuccessful_reps_count_right_dumbbellhiphinge, successful_reps_count_right_dumbbellhiphinge, dir_left_unsuccessful_dumbbellhiphinge, dir_right_unsuccessful_dumbbellhiphinge, total_reps_count_dumbbellhiphinge, total_reps_count_left_dumbbellhiphinge, total_reps_count_right_dumbbellhiphinge, start_time1_dumbbellhiphinge, start_time2_dumbbellhiphinge, start_time3_dumbbellhiphinge, time_threshold_dumbbellhiphinge, within_range_time1_dumbbellhiphinge, within_range_time2_dumbbellhiphinge, general_feedback_left_dumbbellhiphinge, general_feedback_right_dumbbellhiphinge, dir_gen_feedback_dumbbellhiphinge, dir_gen_feedback_unsuccessful_dumbbellhiphinge, cooldown_timer_dumbbellhiphinge, cooldown_duration_dumbbellhiphinge, leftbody_dumbbellhiphinge, rightbody_dumbbellhiphinge, rest_dhh_start_time, exercise_mode


    img = cv2.resize(img, (1280, 720))

    elapsed_time_dumbbellhiphinge = time.time() - start_time1_dumbbellhiphinge
    remaining_time_dumbbellhiphinge = max(0, 60 - elapsed_time_dumbbellhiphinge)

    if display_info_dumbbellhiphinge:
        img = detector_dumbbellhiphinge.findPose(img, False)
        lmList_hip_hinge = detector_dumbbellhiphinge.findPosition(img, False)

        if len(lmList_hip_hinge) != 0:
            leftbody_dumbbellhiphinge = detector_dumbbellhiphinge.HipHinge(img, 11, 23, 25, True)
            rightbody_dumbbellhiphinge  = detector_dumbbellhiphinge.HipHinge(img, 12, 24, 26, True)

            if leftbody_dumbbellhiphinge is not None and rightbody_dumbbellhiphinge is not None:
                per_left_dumbbellhiphinge = np.interp(int(leftbody_dumbbellhiphinge), (90, 240), (100, 0))
                bar_left_dumbbellhiphinge = np.interp(int(leftbody_dumbbellhiphinge), (90, 240), (200, 400))

                per_right_dumbbellhiphinge = np.interp(int(rightbody_dumbbellhiphinge), (90, 240), (100, 0))
                bar_right_dumbbellhiphinge= np.interp(int(rightbody_dumbbellhiphinge), (90, 240), (200, 400))

            if int(per_left_dumbbellhiphinge) == 100:
                color_left_dumbbellhiphinge = (0, 255, 0)  # Change color of left leg bar to green
            else:
                color_left_dumbbellhiphinge = (0, 0, 255)
            
            if int(per_right_dumbbellhiphinge) == 100:
                color_right_dumbbellhiphinge = (0, 255, 0)
            else:
                color_right_dumbbellhiphinge = (0, 0, 255)

            #left
            if 40 <= per_left_dumbbellhiphinge <= 90:
                # Increment the time within range
                within_range_time1_dumbbellhiphinge += time.time() - start_time2_dumbbellhiphinge

                # Check if peak value has been within range for the specified time
                if within_range_time1_dumbbellhiphinge >= time_threshold_dumbbellhiphinge:
                    if dir_left_unsuccessful_dumbbellhiphinge == 0:
                        unsuccessful_reps_count_left_dumbbellhiphinge += 0.5
                        dir_left_unsuccessful_dumbbellhiphinge = 1
            else:
                within_range_time1_dumbbellhiphinge = 0
                # Update the start time to the current time
                start_time2_dumbbellhiphinge = time.time()

            if 1 <= per_left_dumbbellhiphinge <= 10:
                if dir_left_unsuccessful_dumbbellhiphinge == 1:
                    unsuccessful_reps_count_left_dumbbellhiphinge += 0.5
                    dir_left_unsuccessful_dumbbellhiphinge = 0

            if per_left_dumbbellhiphinge == success_threshold_dumbbellhiphinge:
                if dir_left_dumbbellhiphinge == 0:
                    successful_reps_count_left_dumbbellhiphinge += 0.5
                    dir_left_dumbbellhiphinge = 1

            elif per_left_dumbbellhiphinge == atrest_value_dumbbellhiphinge:
                if dir_left_dumbbellhiphinge == 1:
                    successful_reps_count_left_dumbbellhiphinge += 0.5
                    dir_left_dumbbellhiphinge = 0

            # right
            if 40 <= per_right_dumbbellhiphinge <= 90:
                # Increment the time within range
                within_range_time2_dumbbellhiphinge += time.time() - start_time3_dumbbellhiphinge

                # Check if peak value has been within range for the specified time
                if within_range_time2_dumbbellhiphinge >= time_threshold_dumbbellhiphinge:
                    if dir_right_unsuccessful_dumbbellhiphinge == 0:
                        unsuccessful_reps_count_right_dumbbellhiphinge += 0.5
                        dir_right_unsuccessful_dumbbellhiphinge = 1
            else:
                within_range_time2_dumbbellhiphinge = 0
                # Update the start time to the current time
                start_time3_dumbbellhiphinge = time.time()

            if 1 <= per_right_dumbbellhiphinge <= 10:
                if dir_right_unsuccessful_dumbbellhiphinge == 1:
                    unsuccessful_reps_count_right_dumbbellhiphinge += 0.5
                    dir_right_unsuccessful_dumbbellhiphinge = 0

            if per_right_dumbbellhiphinge == success_threshold_dumbbellhiphinge:
                if dir_right_dumbbellhiphinge == 0:
                    successful_reps_count_right_dumbbellhiphinge += 0.5
                    dir_right_dumbbellhiphinge = 1
                    cooldown_timer_dumbbellhiphinge = cooldown_duration_dumbbellhiphinge
            elif per_right_dumbbellhiphinge == atrest_value_dumbbellhiphinge: 
                if dir_right_dumbbellhiphinge == 1:
                    successful_reps_count_right_dumbbellhiphinge += 0.5
                    dir_right_dumbbellhiphinge = 0
                    cooldown_timer_dumbbellhiphinge = cooldown_duration_dumbbellhiphinge

            # feedback for left hand  # TO BE FETCHED 
            feedback_left_dumbbellhiphinge = detector_dumbbellhiphinge.feedback_dumbbellhiphinge(per_left_dumbbellhiphinge)

            detector_dumbbellhiphinge.update_next_per_left(per_left_dumbbellhiphinge)

            # feedback for right hand  # TO BE FETCHED 
            feedback_right_dumbbellhiphinge = detector_dumbbellhiphinge.feedback_dumbbellhiphinge(per_right_dumbbellhiphinge)

            detector_dumbbellhiphinge.update_next_per_left(per_right_dumbbellhiphinge)



        cvzone.putTextRect(img, 'Front Dumbbell Hip Hinge', [370, 30], thickness=2, border=2, scale=1.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time_dumbbellhiphinge)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # Draw angle information
        cv2.putText(img, f"R: {int(per_right_dumbbellhiphinge)}", (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_dumbbellhiphinge)),(50, 400), color_right_dumbbellhiphinge, -1)

        cv2.putText(img, f"L: {int(per_left_dumbbellhiphinge)}", (924, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_dumbbellhiphinge)), (995, 400), color_left_dumbbellhiphinge,-1)

    
    # count
    cv2.rectangle(img, (20, 20), (140, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(successful_reps_count_right_dumbbellhiphinge)}/10", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (150, 20), (270, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(successful_reps_count_left_dumbbellhiphinge)}/10", (160, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    # Check if time's up
    if remaining_time_dumbbellhiphinge <= 0:
        cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
        display_info_dumbbellhiphinge = False
        exercise_mode = "rest_dhh"
        rest_dhh_start_time = time.time()

    total_reps_count_left_dumbbellhiphinge = successful_reps_count_left_dumbbellhiphinge + unsuccessful_reps_count_left_dumbbellhiphinge
    total_reps_count_right_dumbbellhiphinge = successful_reps_count_right_dumbbellhiphinge + unsuccessful_reps_count_right_dumbbellhiphinge


    if successful_reps_count_right_dumbbellhiphinge >= 10 and successful_reps_count_left_dumbbellhiphinge >= 10:
            cvzone.putTextRect(img, 'All Repetitions Completed', [420, 30], thickness=2, border=2, scale=2.5)
            display_info_dumbbellhiphinge = False
            # General feedback after finishing the exercise # TO BE FETCHED
            if dir_gen_feedback_dumbbellhiphinge == 0:
                general_feedback_left_dumbbellhiphinge = detector_dumbbellhiphinge.left_arm_feedback(total_reps_count_left_dumbbellhiphinge)
                general_feedback_right_dumbbellhiphinge = detector_dumbbellhiphinge.right_arm_feedback(total_reps_count_right_dumbbellhiphinge)
                dir_gen_feedback_dumbbellhiphinge = 1
                exercise_mode = "rest_dhh"
                rest_dhh_start_time = time.time()

    if unsuccessful_reps_count_left_dumbbellhiphinge >= 3 and unsuccessful_reps_count_right_dumbbellhiphinge >= 3:
        cvzone.putTextRect(img, 'You have made 2 unsuccessful tries for both arms. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_dumbbellhiphinge = False

        if dir_gen_feedback_unsuccessful_dumbbellhiphinge == 0:
            general_feedback_left_dumbbellhiphinge = detector_dumbbellhiphinge.left_arm_unsuccessful_feedback(total_reps_count_left_dumbbellhiphinge)
            general_feedback_right_dumbbellhiphinge = detector_dumbbellhiphinge.right_arm_unsuccessful_feedback(total_reps_count_right_dumbbellhiphinge)
            dir_gen_feedback_unsuccessful_dumbbellhiphinge = 1
            exercise_mode = "rest_dhh"
            rest_dhh_start_time = time.time()

    if unsuccessful_reps_count_left_dumbbellhiphinge >= 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for left arm. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_dumbbellhiphinge = False
    

        if dir_gen_feedback_unsuccessful_dumbbellhiphinge == 0:
            general_feedback_left_dumbbellhiphinge = detector_dumbbellhiphinge.left_arm_unsuccessful_feedback(total_reps_count_left_dumbbellhiphinge)
            dir_gen_feedback_unsuccessful_dumbbellhiphinge = 1
            exercise_mode = "rest_dhh"
            rest_dhh_start_time = time.time()

    if unsuccessful_reps_count_right_dumbbellhiphinge >= 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for right arm. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_dumbbellhiphinge = False

        if dir_gen_feedback_unsuccessful_dumbbellhiphinge == 0:
            general_feedback_right_dumbbellhiphinge = detector_dumbbellhiphinge.right_arm_unsuccessful_feedback(total_reps_count_right_dumbbellhiphinge)
            dir_gen_feedback_unsuccessful_dumbbellhiphinge == 1
            exercise_mode = "rest_dhh"
            rest_dhh_start_time = time.time()

    return img

def rest_dhh(img):
    global exercise_mode, rest_dhh_start_time, start_time1_dumbbellhiphinge_set2
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_dhh_start_time
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "dhh_set2"
        start_time1_dumbbellhiphinge_set2 = time.time()
    return img

def detect_dhh_set2(img):
    global dir_left_dumbbellhiphinge_set2, dir_right_dumbbellhiphinge_set2, display_info_dumbbellhiphinge_set2, per_right_dumbbellhiphinge_set2, per_left_dumbbellhiphinge_set2, bar_left_dumbbellhiphinge_set2, bar_right_dumbbellhiphinge_set2, color_right_dumbbellhiphinge_set2, color_left_dumbbellhiphinge_set2, feedback_left_dumbbellhiphinge_set2, feedback_right_dumbbellhiphinge_set2, success_threshold_dumbbellhiphinge_set2, atrest_value_dumbbellhiphinge_set2, unsuccessful_reps_count_left_dumbbellhiphinge_set2, successful_reps_count_left_dumbbellhiphinge_set2, unsuccessful_reps_count_right_dumbbellhiphinge_set2, successful_reps_count_right_dumbbellhiphinge_set2, dir_left_unsuccessful_dumbbellhiphinge_set2, dir_right_unsuccessful_dumbbellhiphinge_set2, total_reps_count_dumbbellhiphinge_set2, total_reps_count_left_dumbbellhiphinge_set2, total_reps_count_right_dumbbellhiphinge_set2, start_time1_dumbbellhiphinge_set2, start_time2_dumbbellhiphinge_set2, start_time3_dumbbellhiphinge_set2, time_threshold_dumbbellhiphinge_set2, within_range_time1_dumbbellhiphinge_set2, within_range_time2_dumbbellhiphinge_set2, general_feedback_left_dumbbellhiphinge_set2, general_feedback_right_dumbbellhiphinge_set2, dir_gen_feedback_dumbbellhiphinge_set2, dir_gen_feedback_unsuccessful_dumbbellhiphinge_set2, cooldown_timer_dumbbellhiphinge_set2, cooldown_duration_dumbbellhiphinge_set2, leftbody_dumbbellhiphinge_set2, rightbody_dumbbellhiphinge_set2, rest_dhh_start_time_set2, exercise_mode


    img = cv2.resize(img, (1280, 720))

    elapsed_time_dumbbellhiphinge = time.time() - start_time1_dumbbellhiphinge_set2
    remaining_time_dumbbellhiphinge = max(0, 60 - elapsed_time_dumbbellhiphinge)

    if display_info_dumbbellhiphinge_set2:
        img = detector_dumbbellhiphinge.findPose(img, False)
        lmList_hip_hinge = detector_dumbbellhiphinge.findPosition(img, False)

        if len(lmList_hip_hinge) != 0:
            leftbody_dumbbellhiphinge_set2 = detector_dumbbellhiphinge.HipHinge(img, 11, 23, 25, True)
            rightbody_dumbbellhiphinge_set2  = detector_dumbbellhiphinge.HipHinge(img, 12, 24, 26, True)

            if leftbody_dumbbellhiphinge_set2 is not None and rightbody_dumbbellhiphinge_set2 is not None:
                per_left_dumbbellhiphinge_set2 = np.interp(int(leftbody_dumbbellhiphinge_set2), (90, 240), (100, 0))
                bar_left_dumbbellhiphinge_set2 = np.interp(int(leftbody_dumbbellhiphinge_set2), (90, 240), (200, 400))

                per_right_dumbbellhiphinge_set2 = np.interp(int(rightbody_dumbbellhiphinge_set2), (90, 240), (100, 0))
                bar_right_dumbbellhiphinge_set2= np.interp(int(rightbody_dumbbellhiphinge_set2), (90, 240), (200, 400))

            if int(per_left_dumbbellhiphinge_set2) == 100:
                color_left_dumbbellhiphinge_set2 = (0, 255, 0)  # Change color of left leg bar to green
            else:
                color_left_dumbbellhiphinge_set2 = (0, 0, 255)
            
            if int(per_right_dumbbellhiphinge_set2) == 100:
                color_right_dumbbellhiphinge_set2 = (0, 255, 0)
            else:
                color_right_dumbbellhiphinge_set2 = (0, 0, 255)

            #left
            if 40 <= per_left_dumbbellhiphinge_set2 <= 90:
                # Increment the time within range
                within_range_time1_dumbbellhiphinge_set2 += time.time() - start_time2_dumbbellhiphinge_set2

                # Check if peak value has been within range for the specified time
                if within_range_time1_dumbbellhiphinge_set2 >= time_threshold_dumbbellhiphinge_set2:
                    if dir_left_unsuccessful_dumbbellhiphinge_set2 == 0:
                        unsuccessful_reps_count_left_dumbbellhiphinge_set2 += 0.5
                        dir_left_unsuccessful_dumbbellhiphinge_set2 = 1
            else:
                within_range_time1_dumbbellhiphinge_set2 = 0
                # Update the start time to the current time
                start_time2_dumbbellhiphinge_set2 = time.time()

            if 1 <= per_left_dumbbellhiphinge_set2 <= 10:
                if dir_left_unsuccessful_dumbbellhiphinge_set2 == 1:
                    unsuccessful_reps_count_left_dumbbellhiphinge_set2 += 0.5
                    dir_left_unsuccessful_dumbbellhiphinge_set2 = 0

            if per_left_dumbbellhiphinge_set2 == success_threshold_dumbbellhiphinge_set2:
                if dir_left_dumbbellhiphinge_set2 == 0:
                    successful_reps_count_left_dumbbellhiphinge_set2 += 0.5
                    dir_left_dumbbellhiphinge_set2 = 1

            elif per_left_dumbbellhiphinge_set2 == atrest_value_dumbbellhiphinge_set2:
                if dir_left_dumbbellhiphinge_set2 == 1:
                    successful_reps_count_left_dumbbellhiphinge_set2 += 0.5
                    dir_left_dumbbellhiphinge_set2 = 0

            # right
            if 40 <= per_right_dumbbellhiphinge_set2 <= 90:
                # Increment the time within range
                within_range_time2_dumbbellhiphinge_set2 += time.time() - start_time3_dumbbellhiphinge_set2

                # Check if peak value has been within range for the specified time
                if within_range_time2_dumbbellhiphinge_set2 >= time_threshold_dumbbellhiphinge_set2:
                    if dir_right_unsuccessful_dumbbellhiphinge_set2 == 0:
                        unsuccessful_reps_count_right_dumbbellhiphinge_set2 += 0.5
                        dir_right_unsuccessful_dumbbellhiphinge_set2 = 1
            else:
                within_range_time2_dumbbellhiphinge_set2 = 0
                # Update the start time to the current time
                start_time3_dumbbellhiphinge_set2 = time.time()

            if 1 <= per_right_dumbbellhiphinge_set2 <= 10:
                if dir_right_unsuccessful_dumbbellhiphinge_set2 == 1:
                    unsuccessful_reps_count_right_dumbbellhiphinge_set2 += 0.5
                    dir_right_unsuccessful_dumbbellhiphinge_set2 = 0

            if per_right_dumbbellhiphinge_set2 == success_threshold_dumbbellhiphinge_set2:
                if dir_right_dumbbellhiphinge_set2 == 0:
                    successful_reps_count_right_dumbbellhiphinge_set2 += 0.5
                    dir_right_dumbbellhiphinge_set2 = 1
                    cooldown_timer_dumbbellhiphinge_set2 = cooldown_duration_dumbbellhiphinge_set2
            elif per_right_dumbbellhiphinge_set2 == atrest_value_dumbbellhiphinge_set2: 
                if dir_right_dumbbellhiphinge_set2 == 1:
                    successful_reps_count_right_dumbbellhiphinge_set2 += 0.5
                    dir_right_dumbbellhiphinge_set2 = 0
                    cooldown_timer_dumbbellhiphinge_set2 = cooldown_duration_dumbbellhiphinge_set2

            # feedback for left hand  # TO BE FETCHED 
            feedback_left_dumbbellhiphinge_set2 = detector_dumbbellhiphinge.feedback_dumbbellhiphinge(per_left_dumbbellhiphinge_set2)

            detector_dumbbellhiphinge.update_next_per_left(per_left_dumbbellhiphinge_set2)

            # feedback for right hand  # TO BE FETCHED 
            feedback_right_dumbbellhiphinge_set2 = detector_dumbbellhiphinge.feedback_dumbbellhiphinge(per_right_dumbbellhiphinge_set2)

            detector_dumbbellhiphinge.update_next_per_left(per_right_dumbbellhiphinge_set2)



        cvzone.putTextRect(img, 'Front Dumbbell Hip Hinge SET 2', [370, 30], thickness=2, border=2, scale=1.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time_dumbbellhiphinge)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # Draw angle information
        cv2.putText(img, f"R: {int(per_right_dumbbellhiphinge_set2)}", (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_dumbbellhiphinge_set2)),(50, 400), color_right_dumbbellhiphinge_set2, -1)

        cv2.putText(img, f"L: {int(per_left_dumbbellhiphinge_set2)}", (924, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_dumbbellhiphinge_set2)), (995, 400), color_left_dumbbellhiphinge_set2,-1)

    
    # count
    cv2.rectangle(img, (20, 20), (140, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(successful_reps_count_right_dumbbellhiphinge_set2)}/10", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (150, 20), (270, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(successful_reps_count_left_dumbbellhiphinge_set2)}/10", (160, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    # Check if time's up
    if remaining_time_dumbbellhiphinge <= 0:
        cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
        display_info_dumbbellhiphinge_set2 = False
        exercise_mode = "rest_dhh_set2"
        rest_dhh_start_time_set2 = time.time()
    
    total_reps_count_left_dumbbellhiphinge_set2 = successful_reps_count_left_dumbbellhiphinge_set2 + unsuccessful_reps_count_left_dumbbellhiphinge
    total_reps_count_right_dumbbellhiphinge_set2 = successful_reps_count_right_dumbbellhiphinge_set2 + unsuccessful_reps_count_right_dumbbellhiphinge_set2


    if successful_reps_count_right_dumbbellhiphinge_set2 >= 10 and successful_reps_count_left_dumbbellhiphinge_set2 >= 10:
            cvzone.putTextRect(img, 'All Repetitions Completed', [420, 30], thickness=2, border=2, scale=2.5)
            display_info_dumbbellhiphinge_set2 = False
            # General feedback after finishing the exercise # TO BE FETCHED
            if dir_gen_feedback_dumbbellhiphinge_set2 == 0:
                general_feedback_left_dumbbellhiphinge_set2 = detector_dumbbellhiphinge.left_arm_feedback(total_reps_count_left_dumbbellhiphinge_set2)
                general_feedback_right_dumbbellhiphinge_set2 = detector_dumbbellhiphinge.right_arm_feedback(total_reps_count_right_dumbbellhiphinge_set2)
                dir_gen_feedback_dumbbellhiphinge_set2 = 1
                exercise_mode = "rest_dhh_set2"
                rest_dhh_start_time_set2 = time.time()

    if unsuccessful_reps_count_left_dumbbellhiphinge_set2 >= 3 and unsuccessful_reps_count_right_dumbbellhiphinge_set2 >= 3:
        cvzone.putTextRect(img, 'You have made 2 unsuccessful tries for both arms. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_dumbbellhiphinge_set2 = False

        if dir_gen_feedback_unsuccessful_dumbbellhiphinge_set2 == 0:
            general_feedback_left_dumbbellhiphinge_set2 = detector_dumbbellhiphinge.left_arm_unsuccessful_feedback(total_reps_count_left_dumbbellhiphinge_set2)
            general_feedback_right_dumbbellhiphinge_set2 = detector_dumbbellhiphinge.right_arm_unsuccessful_feedback(total_reps_count_right_dumbbellhiphinge_set2)
            dir_gen_feedback_unsuccessful_dumbbellhiphinge_set2 = 1
            exercise_mode = "rest_dhh_set2"
            rest_dhh_start_time_set2 = time.time()

    if unsuccessful_reps_count_left_dumbbellhiphinge_set2 >= 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for left arm. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_dumbbellhiphinge_set2 = False
    

        if dir_gen_feedback_unsuccessful_dumbbellhiphinge_set2 == 0:
            general_feedback_left_dumbbellhiphinge_set2 = detector_dumbbellhiphinge.left_arm_unsuccessful_feedback(total_reps_count_left_dumbbellhiphinge_set2)
            dir_gen_feedback_unsuccessful_dumbbellhiphinge_set2 = 1
            exercise_mode = "rest_dhh_set2"
            rest_dhh_start_time_set2 = time.time()

    if unsuccessful_reps_count_right_dumbbellhiphinge_set2 >= 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for right arm. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_dumbbellhiphinge_set2 = False

        if dir_gen_feedback_unsuccessful_dumbbellhiphinge_set2 == 0:
            general_feedback_right_dumbbellhiphinge_set2 = detector_dumbbellhiphinge.right_arm_unsuccessful_feedback(total_reps_count_right_dumbbellhiphinge_set2)
            dir_gen_feedback_unsuccessful_dumbbellhiphinge_set2 == 1
            exercise_mode = "rest_dhh_set2"
            rest_dhh_start_time_set2 = time.time()

    return img

def rest_dhh_set2(img):
    global exercise_mode, rest_dhh_start_time_set2, start_time1_dumbbellhiphinge_set3
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_dhh_start_time_set2
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "dhh_set3"
        start_time1_dumbbellhiphinge_set3 = time.time()
    return img

def detect_dhh_set3(img):
    global dir_left_dumbbellhiphinge_set3, dir_right_dumbbellhiphinge_set3, display_info_dumbbellhiphinge_set3, per_right_dumbbellhiphinge_set3, per_left_dumbbellhiphinge_set3, bar_left_dumbbellhiphinge_set3, bar_right_dumbbellhiphinge_set3, color_right_dumbbellhiphinge_set3, color_left_dumbbellhiphinge_set3, feedback_left_dumbbellhiphinge_set3, feedback_right_dumbbellhiphinge_set3, success_threshold_dumbbellhiphinge_set3, atrest_value_dumbbellhiphinge_set3, unsuccessful_reps_count_left_dumbbellhiphinge_set3, successful_reps_count_left_dumbbellhiphinge_set3, unsuccessful_reps_count_right_dumbbellhiphinge_set3, successful_reps_count_right_dumbbellhiphinge_set3, dir_left_unsuccessful_dumbbellhiphinge_set3, dir_right_unsuccessful_dumbbellhiphinge_set3, total_reps_count_dumbbellhiphinge_set3, total_reps_count_left_dumbbellhiphinge_set3, total_reps_count_right_dumbbellhiphinge_set3, start_time1_dumbbellhiphinge_set3, start_time2_dumbbellhiphinge_set3, start_time3_dumbbellhiphinge_set3, time_threshold_dumbbellhiphinge_set3, within_range_time1_dumbbellhiphinge_set3, within_range_time2_dumbbellhiphinge_set3, general_feedback_left_dumbbellhiphinge_set3, general_feedback_right_dumbbellhiphinge_set3, dir_gen_feedback_dumbbellhiphinge_set3, dir_gen_feedback_unsuccessful_dumbbellhiphinge_set3, cooldown_timer_dumbbellhiphinge_set3, cooldown_duration_dumbbellhiphinge_set3, leftbody_dumbbellhiphinge_set3, rightbody_dumbbellhiphinge_set3, rest_dhh_start_time_set3, exercise_mode


    img = cv2.resize(img, (1280, 720))

    elapsed_time_dumbbellhiphinge = time.time() - start_time1_dumbbellhiphinge_set3
    remaining_time_dumbbellhiphinge = max(0, 60 - elapsed_time_dumbbellhiphinge)

    if display_info_dumbbellhiphinge_set3:
        img = detector_dumbbellhiphinge.findPose(img, False)
        lmList_hip_hinge = detector_dumbbellhiphinge.findPosition(img, False)

        if len(lmList_hip_hinge) != 0:
            leftbody_dumbbellhiphinge_set3 = detector_dumbbellhiphinge.HipHinge(img, 11, 23, 25, True)
            rightbody_dumbbellhiphinge_set3  = detector_dumbbellhiphinge.HipHinge(img, 12, 24, 26, True)

            if leftbody_dumbbellhiphinge_set3 is not None and rightbody_dumbbellhiphinge_set3 is not None:
                per_left_dumbbellhiphinge_set3 = np.interp(int(leftbody_dumbbellhiphinge_set3), (90, 240), (100, 0))
                bar_left_dumbbellhiphinge_set3 = np.interp(int(leftbody_dumbbellhiphinge_set3), (90, 240), (200, 400))

                per_right_dumbbellhiphinge_set3 = np.interp(int(rightbody_dumbbellhiphinge_set3), (90, 240), (100, 0))
                bar_right_dumbbellhiphinge_set3= np.interp(int(rightbody_dumbbellhiphinge_set3), (90, 240), (200, 400))

            if int(per_left_dumbbellhiphinge_set3) == 100:
                color_left_dumbbellhiphinge_set3 = (0, 255, 0)  # Change color of left leg bar to green
            else:
                color_left_dumbbellhiphinge_set3 = (0, 0, 255)
            
            if int(per_right_dumbbellhiphinge_set3) == 100:
                color_right_dumbbellhiphinge_set3 = (0, 255, 0)
            else:
                color_right_dumbbellhiphinge_set3 = (0, 0, 255)

            #left
            if 40 <= per_left_dumbbellhiphinge_set3 <= 90:
                # Increment the time within range
                within_range_time1_dumbbellhiphinge_set3 += time.time() - start_time2_dumbbellhiphinge_set3

                # Check if peak value has been within range for the specified time
                if within_range_time1_dumbbellhiphinge_set3 >= time_threshold_dumbbellhiphinge_set3:
                    if dir_left_unsuccessful_dumbbellhiphinge_set3 == 0:
                        unsuccessful_reps_count_left_dumbbellhiphinge_set3 += 0.5
                        dir_left_unsuccessful_dumbbellhiphinge_set3 = 1
            else:
                within_range_time1_dumbbellhiphinge_set3 = 0
                # Update the start time to the current time
                start_time2_dumbbellhiphinge_set3 = time.time()

            if 1 <= per_left_dumbbellhiphinge_set3 <= 10:
                if dir_left_unsuccessful_dumbbellhiphinge_set3 == 1:
                    unsuccessful_reps_count_left_dumbbellhiphinge_set3 += 0.5
                    dir_left_unsuccessful_dumbbellhiphinge_set3 = 0

            if per_left_dumbbellhiphinge_set3 == success_threshold_dumbbellhiphinge_set3:
                if dir_left_dumbbellhiphinge_set3 == 0:
                    successful_reps_count_left_dumbbellhiphinge_set3 += 0.5
                    dir_left_dumbbellhiphinge_set3 = 1

            elif per_left_dumbbellhiphinge_set3 == atrest_value_dumbbellhiphinge_set3:
                if dir_left_dumbbellhiphinge_set3 == 1:
                    successful_reps_count_left_dumbbellhiphinge_set3 += 0.5
                    dir_left_dumbbellhiphinge_set3 = 0

            # right
            if 40 <= per_right_dumbbellhiphinge_set3 <= 90:
                # Increment the time within range
                within_range_time2_dumbbellhiphinge_set3 += time.time() - start_time3_dumbbellhiphinge_set3

                # Check if peak value has been within range for the specified time
                if within_range_time2_dumbbellhiphinge_set3 >= time_threshold_dumbbellhiphinge_set3:
                    if dir_right_unsuccessful_dumbbellhiphinge_set3 == 0:
                        unsuccessful_reps_count_right_dumbbellhiphinge_set3 += 0.5
                        dir_right_unsuccessful_dumbbellhiphinge_set3 = 1
            else:
                within_range_time2_dumbbellhiphinge_set3 = 0
                # Update the start time to the current time
                start_time3_dumbbellhiphinge_set3 = time.time()

            if 1 <= per_right_dumbbellhiphinge_set3 <= 10:
                if dir_right_unsuccessful_dumbbellhiphinge_set3 == 1:
                    unsuccessful_reps_count_right_dumbbellhiphinge_set3 += 0.5
                    dir_right_unsuccessful_dumbbellhiphinge_set3 = 0

            if per_right_dumbbellhiphinge_set3 == success_threshold_dumbbellhiphinge_set3:
                if dir_right_dumbbellhiphinge_set3 == 0:
                    successful_reps_count_right_dumbbellhiphinge_set3 += 0.5
                    dir_right_dumbbellhiphinge_set3 = 1
                    cooldown_timer_dumbbellhiphinge_set3 = cooldown_duration_dumbbellhiphinge_set3
            elif per_right_dumbbellhiphinge_set3 == atrest_value_dumbbellhiphinge_set3: 
                if dir_right_dumbbellhiphinge_set3 == 1:
                    successful_reps_count_right_dumbbellhiphinge_set3 += 0.5
                    dir_right_dumbbellhiphinge_set3 = 0
                    cooldown_timer_dumbbellhiphinge_set3 = cooldown_duration_dumbbellhiphinge_set3

            # feedback for left hand  # TO BE FETCHED 
            feedback_left_dumbbellhiphinge_set3 = detector_dumbbellhiphinge.feedback_dumbbellhiphinge(per_left_dumbbellhiphinge_set3)

            detector_dumbbellhiphinge.update_next_per_left(per_left_dumbbellhiphinge_set3)

            # feedback for right hand  # TO BE FETCHED 
            feedback_right_dumbbellhiphinge_set3 = detector_dumbbellhiphinge.feedback_dumbbellhiphinge(per_right_dumbbellhiphinge_set3)

            detector_dumbbellhiphinge.update_next_per_left(per_right_dumbbellhiphinge_set3)



        cvzone.putTextRect(img, 'Front Dumbbell Hip Hinge SET 3', [370, 30], thickness=2, border=2, scale=1.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time_dumbbellhiphinge)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # Draw angle information
        cv2.putText(img, f"R: {int(per_right_dumbbellhiphinge_set3)}", (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_dumbbellhiphinge_set3)),(50, 400), color_right_dumbbellhiphinge_set3, -1)

        cv2.putText(img, f"L: {int(per_left_dumbbellhiphinge_set3)}", (924, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_dumbbellhiphinge_set3)), (995, 400), color_left_dumbbellhiphinge_set3,-1)

    
    # count
    cv2.rectangle(img, (20, 20), (140, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(successful_reps_count_right_dumbbellhiphinge_set3)}/10", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (150, 20), (270, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(successful_reps_count_left_dumbbellhiphinge_set3)}/10", (160, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    # Check if time's up
    if remaining_time_dumbbellhiphinge <= 0:
        cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
        display_info_dumbbellhiphinge_set3 = False
        exercise_mode = "rest_dhh_set3"
        rest_dhh_start_time_set3 = time.time()

    total_reps_count_left_dumbbellhiphinge_set3 = successful_reps_count_left_dumbbellhiphinge_set3 + unsuccessful_reps_count_left_dumbbellhiphinge_set3
    total_reps_count_right_dumbbellhiphinge_set3 = successful_reps_count_right_dumbbellhiphinge_set3 + unsuccessful_reps_count_right_dumbbellhiphinge_set3


    if successful_reps_count_right_dumbbellhiphinge_set3 >= 10 and successful_reps_count_left_dumbbellhiphinge_set3 >= 10:
            cvzone.putTextRect(img, 'All Repetitions Completed', [420, 30], thickness=2, border=2, scale=2.5)
            display_info_dumbbellhiphinge_set3 = False
            # General feedback after finishing the exercise # TO BE FETCHED
            if dir_gen_feedback_dumbbellhiphinge_set3 == 0:
                general_feedback_left_dumbbellhiphinge_set3 = detector_dumbbellhiphinge.left_arm_feedback(total_reps_count_left_dumbbellhiphinge_set3)
                general_feedback_right_dumbbellhiphinge_set3 = detector_dumbbellhiphinge.right_arm_feedback(total_reps_count_right_dumbbellhiphinge_set3)
                dir_gen_feedback_dumbbellhiphinge_set3 = 1
                exercise_mode = "rest_dhh_set3"
                rest_dhh_start_time_set3 = time.time()

    if unsuccessful_reps_count_left_dumbbellhiphinge_set3 >= 3 and unsuccessful_reps_count_right_dumbbellhiphinge_set3 >= 3:
        cvzone.putTextRect(img, 'You have made 2 unsuccessful tries for both arms. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_dumbbellhiphinge_set3 = False

        if dir_gen_feedback_unsuccessful_dumbbellhiphinge_set3 == 0:
            general_feedback_left_dumbbellhiphinge_set3 = detector_dumbbellhiphinge.left_arm_unsuccessful_feedback(total_reps_count_left_dumbbellhiphinge_set3)
            general_feedback_right_dumbbellhiphinge_set3 = detector_dumbbellhiphinge.right_arm_unsuccessful_feedback(total_reps_count_right_dumbbellhiphinge_set3)
            dir_gen_feedback_unsuccessful_dumbbellhiphinge_set3 = 1
            exercise_mode = "rest_dhh_set3"
            rest_dhh_start_time_set3 = time.time()

    if unsuccessful_reps_count_left_dumbbellhiphinge_set3 >= 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for left arm. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_dumbbellhiphinge_set3 = False
    

        if dir_gen_feedback_unsuccessful_dumbbellhiphinge_set3 == 0:
            general_feedback_left_dumbbellhiphinge_set3 = detector_dumbbellhiphinge.left_arm_unsuccessful_feedback(total_reps_count_left_dumbbellhiphinge_set3)
            dir_gen_feedback_unsuccessful_dumbbellhiphinge_set3 = 1
            exercise_mode = "rest_dhh_set3"
            rest_dhh_start_time_set3 = time.time()

    if unsuccessful_reps_count_right_dumbbellhiphinge_set3 >= 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for right arm. Please retry again', [390, 30], thickness=2, border=2, scale=1)
        display_info_dumbbellhiphinge_set3 = False

        if dir_gen_feedback_unsuccessful_dumbbellhiphinge_set3 == 0:
            general_feedback_right_dumbbellhiphinge_set3 = detector_dumbbellhiphinge.right_arm_unsuccessful_feedback(total_reps_count_right_dumbbellhiphinge_set3)
            dir_gen_feedback_unsuccessful_dumbbellhiphinge_set3 == 1
            exercise_mode = "rest_dhh_set3"
            rest_dhh_start_time_set3 = time.time()
    return img

def rest_dhh_set3(img):
    global exercise_mode, rest_dhh_start_time_set3
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_dhh_start_time_set3
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "done exercise"
        print(exercise_mode)
    return img

@muscleGain.route('/detect_bicep_curls')
def feedback_bicep_curls():
    global general_feedback_right_bicep, general_feedback_left_bicep, general_feedback_right_bicep_set2, general_feedback_left_bicep_set2, general_feedback_right_bicep_set3, general_feedback_left_bicep_set3, general_feedback_left_pushup,general_feedback_right_pushup,general_feedback_left_pushup_set2,general_feedback_right_pushup_set2,general_feedback_left_pushup_set3,general_feedback_right_pushup_set3,general_feedback_left_shouldertaps,general_feedback_right_shouldertaps,general_feedback_left_shouldertaps_set2,general_feedback_right_shouldertaps_set2,general_feedback_left_shouldertaps_set3,general_feedback_right_shouldertaps_set3,general_feedback_left_chestpress,general_feedback_right_chestpress,general_feedback_left_chestpress_set2,general_feedback_right_chestpress_set2,general_feedback_left_chestpress_set3,general_feedback_right_chestpress_set3,general_feedback_left_dumbbellfrontraise,general_feedback_right_dumbbellfrontraise,general_feedback_left_dumbbellfrontraise_set2,general_feedback_right_dumbbellfrontraise_set2,general_feedback_left_dumbbellfrontraise_set3,general_feedback_right_dumbbellfrontraise_set3,general_feedback_right_leglunge,general_feedback_left_leglunge,general_feedback_right_leglunge_set2,general_feedback_left_leglunge_set2,general_feedback_right_leglunge_set3,general_feedback_left_leglunge_set3,general_feedback_left_bodyweightsquat,general_feedback_left_bodyweightsquat_set2,general_feedback_left_bodyweightsquat_set3,general_feedback_left_gobletsquat,general_feedback_right_gobletsquat,general_feedback_left_gobletsquat_set2,general_feedback_right_gobletsquat_set2,general_feedback_left_gobletsquat_set3,general_feedback_right_gobletsquat_set3,general_feedback_left_highkneetap,general_feedback_right_highkneetap,general_feedback_left_highkneetap_set2,general_feedback_right_highkneetap_set2,general_feedback_left_highkneetap_set3,general_feedback_right_highkneetap_set3,general_feedback_left_dumbbellhiphinge,general_feedback_right_dumbbellhiphinge,general_feedback_left_dumbbellhiphinge_set2,general_feedback_right_dumbbellhiphinge_set2,general_feedback_left_dumbbellhiphinge_set3,general_feedback_right_dumbbellhiphinge_set3



    return jsonify({'general_feedback_right_bicep': general_feedback_right_bicep},{'general_feedback_left_bicep': general_feedback_left_bicep}, {'general_feedback_right_bicep_set2': general_feedback_right_bicep_set2}, {'general_feedback_left_bicep_set2': general_feedback_left_bicep_set2}, {'general_feedback_right_bicep_set3':general_feedback_right_bicep_set3}, {'general_feedback_left_bicep_set3':general_feedback_left_bicep_set3}, {'general_feedback_left_pushup':general_feedback_left_pushup}, 
    {'general_feedback_right_pushup':general_feedback_right_pushup}, {'general_feedback_left_pushup_set2':general_feedback_left_pushup_set2}, {'general_feedback_right_pushup_set2':general_feedback_right_pushup_set2}, {'general_feedback_left_pushup_set3':general_feedback_left_pushup_set3}, {'general_feedback_right_pushup_set3':general_feedback_right_pushup_set3}, {'general_feedback_left_shouldertaps':general_feedback_left_shouldertaps}, {'general_feedback_right_shouldertaps':general_feedback_right_shouldertaps}, {'general_feedback_left_shouldertaps_set2':general_feedback_left_shouldertaps_set2}, {'general_feedback_right_shouldertaps_set2':general_feedback_right_shouldertaps_set2}, {'general_feedback_left_shouldertaps_set3':general_feedback_left_shouldertaps_set3}, {'general_feedback_right_shouldertaps_set3':general_feedback_right_shouldertaps_set3}, {'general_feedback_left_chestpress':general_feedback_left_chestpress}, {'general_feedback_right_chestpress':general_feedback_right_chestpress}, {'general_feedback_left_chestpress_set2':general_feedback_left_chestpress_set2}, {'general_feedback_right_chestpress_set2':general_feedback_right_chestpress_set2}, {'general_feedback_left_chestpress_set3':general_feedback_left_chestpress_set3}, {'general_feedback_right_chestpress_set3':general_feedback_right_chestpress_set3}, {'general_feedback_left_dumbbellfrontraise':general_feedback_left_dumbbellfrontraise}, {'general_feedback_right_dumbbellfrontraise':general_feedback_right_dumbbellfrontraise}, {'general_feedback_left_dumbbellfrontraise_set2':general_feedback_left_dumbbellfrontraise_set2}, {'general_feedback_right_dumbbellfrontraise_set2':general_feedback_right_dumbbellfrontraise_set2}, {'general_feedback_left_dumbbellfrontraise_set3':general_feedback_left_dumbbellfrontraise_set3}, {'general_feedback_right_dumbbellfrontraise_set3':general_feedback_right_dumbbellfrontraise_set3}, {'general_feedback_right_leglunge':general_feedback_right_leglunge}, {'general_feedback_left_leglunge':general_feedback_left_leglunge}, {'general_feedback_right_leglunge_set2':general_feedback_right_leglunge_set2}, {'general_feedback_left_leglunge_set2':general_feedback_left_leglunge_set2}, {'general_feedback_right_leglunge_set3':general_feedback_right_leglunge_set3}, {'general_feedback_left_leglunge_set3':general_feedback_left_leglunge_set3}, {'general_feedback_left_bodyweightsquat':general_feedback_left_bodyweightsquat}, {'general_feedback_left_bodyweightsquat_set2':general_feedback_left_bodyweightsquat_set2}, {'general_feedback_left_bodyweightsquat_set3':general_feedback_left_bodyweightsquat_set3}, {'general_feedback_left_gobletsquat':general_feedback_left_gobletsquat}, {'general_feedback_right_gobletsquat':general_feedback_right_gobletsquat}, {'general_feedback_left_gobletsquat_set2':general_feedback_left_gobletsquat_set2}, {'general_feedback_right_gobletsquat_set2':general_feedback_right_gobletsquat_set2}, {'general_feedback_left_gobletsquat_set3':general_feedback_left_gobletsquat_set3}, {'general_feedback_right_gobletsquat_set3':general_feedback_right_gobletsquat_set3}, {'general_feedback_left_highkneetap':general_feedback_left_highkneetap}, {'general_feedback_right_highkneetap':general_feedback_right_highkneetap}, {'general_feedback_left_highkneetap_set2':general_feedback_left_highkneetap_set2}, {'general_feedback_right_highkneetap_set2':general_feedback_right_highkneetap_set2}, {'general_feedback_left_highkneetap_set3':general_feedback_left_highkneetap_set3}, {'general_feedback_right_highkneetap_set3':general_feedback_right_highkneetap_set3}, {'general_feedback_left_dumbbellhiphinge':general_feedback_left_dumbbellhiphinge}, {'general_feedback_right_dumbbellhiphinge':general_feedback_right_dumbbellhiphinge}, {'general_feedback_left_dumbbellhiphinge_set2':general_feedback_left_dumbbellhiphinge_set2}, {'general_feedback_right_dumbbellhiphinge_set2':general_feedback_right_dumbbellhiphinge_set2}, {'general_feedback_left_dumbbellhiphinge_set3':general_feedback_left_dumbbellhiphinge_set3}, {'general_feedback_right_dumbbellhiphinge_set3':general_feedback_right_dumbbellhiphinge_set3})










