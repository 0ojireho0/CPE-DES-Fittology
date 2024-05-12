from flask import Blueprint, render_template ,session, Response, jsonify
import cv2
import cvzone
import time
import os
import numpy as np
import poseModules.bicepcurl_front_PoseModule as pm_bicep
import poseModules.pushup_front_PoseModule as pm_pushup
import poseModules.shouldertaps_front_PoseModule as pm_shouldertap
import poseModules.chestpress_PoseModule as pm_chestpress
import poseModules.dumbbellfrontraise_PoseModule as pm_dumbbellfrontraise
import poseModules.alternatinglunge_PoseModule as pm_alternatinglunge
import poseModules.bodyweightsquat_PoseModule as pm_bws
import poseModules.gobletsquat_PoseModule as pm_gs
import poseModules.highkneetap_PoseModule as pm_hkt
import poseModules.dumbbellhiphinge_PoseModule as pm_dhh

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
    
exercise_mode = "bicep_curl"




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
        if dir_gen_feedback_bicep == 0:
            general_feedback_left_bicep_set2 = detector_bicep.left_arm_feedback(total_reps_count_left_set2)
            general_feedback_right_bicep_set2 = detector_bicep.right_arm_feedback(total_reps_count_right_set2)
            dir_gen_feedback_bicep = 1
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
    global exercise_mode, display_info_pushup, per_right_pushup, per_left_pushup, bar_left_pushup, bar_right_pushup, leftangle_pushup, rightangle_pushup, color_right_pushup, color_left_pushup, feedback_left_pushup, feedback_right_pushup, success_threshold_pushup, peak_value_pushup, atrest_value_pushup, unsuccessful_reps_count_left_pushup, successful_reps_count_left_pushup, unsuccessful_reps_count_right_pushup, successful_reps_count_right_pushup, dir_left_unsuccessful_pushup, dir_right_unsuccessful_pushup, total_reps_count_pushup, total_reps_count_left_pushup, total_reps_count_right_pushup, start_time1_pushup, start_time2_pushup, start_time3_pushup, time_threshold_pushup, within_range_time1_pushup, general_feedback_left_pushup, general_feedback_right_pushup, dir_gen_feedback_pushup, dir_gen_feedback_unsuccessful_pushup, rest_pushup_start_time, dir_left_pushup, dir_right_pushup

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
    global display_info_pushup_set2, per_right_pushup_set2, per_left_pushup_set2, bar_left_pushup_set2, bar_right_pushup_set2, leftangle_pushup_set2, rightangle_pushup_set2, color_right_pushup_set2, color_left_pushup_set2, feedback_left_pushup_set2, feedback_right_pushup_set2, success_threshold_pushup_set2, peak_value_pushup_set2, atrest_value_pushup_set2, unsuccessful_reps_count_left_pushup_set2, successful_reps_count_left_pushup_set2, unsuccessful_reps_count_right_pushup_set2, successful_reps_count_right_pushup_set2, dir_left_unsuccessful_pushup_set2, dir_right_unsuccessful_pushup_set2, total_reps_count_pushup_set2, total_reps_count_left_pushup_set2, total_reps_count_right_pushup_set2, start_time1_pushup_set2, start_time2_pushup_set2, start_time3_pushup_set2, time_threshold_pushup, within_range_time1_pushup_set2, general_feedback_left_pushup_set2, general_feedback_right_pushup_set2, dir_gen_feedback_pushup_set2, dir_gen_feedback_unsuccessful_pushup_set2, rest_pushup_start_time_set2, exercise_mode, dir_left_pushup_set2, dir_right_pushup_set2

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
    global exercise_mode, display_info_pushup_set3, per_right_pushup_set3, per_left_pushup_set3, bar_left_pushup_set3, bar_right_pushup_set3, leftangle_pushup_set3, rightangle_pushup_set3, color_right_pushup_set3, color_left_pushup_set3, feedback_left_pushup_set3, feedback_right_pushup_set3, success_threshold_pushup_set3, peak_value_pushup_set3, atrest_value_pushup_set3, unsuccessful_reps_count_left_pushup_set3, successful_reps_count_left_pushup_set3, unsuccessful_reps_count_right_pushup_set3, successful_reps_count_right_pushup_set3, dir_left_unsuccessful_pushup_set3, dir_right_unsuccessful_pushup_set3, total_reps_count_pushup_set3, total_reps_count_left_pushup_set3, total_reps_count_right_pushup_set3, start_time1_pushup_set3, start_time2_pushup_set3, start_time3_pushup_set3, time_threshold_pushup_set3, within_range_time1_pushup_set3, general_feedback_left_pushup_set3, general_feedback_right_pushup_set3, dir_gen_feedback_pushup_set3, dir_gen_feedback_unsuccessful_pushup_set3, rest_pushup_start_time_set3, dir_left_pushup_set3, dir_right_pushup_set3

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
    global exercise_mode, rest_shouldertap_start_time_set3, start_time_chestpress
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
        start_time_chestpress = time.time()
    return img

def detect_chestpress(img):
    global count_chestpress_left, count_chestpress_right, dir_chestpress_right, dir_chestpress_left, start_time_chestpress, repetition_time_chestpress, display_info_chestpress, bar_left_chestpress, bar_right_chestpress, per_left_chestpress, per_right_chestpress, angle_left_chestpress, angle_right_chestpress, exercise_mode, rest_chestpress_start_time

    img = cv2.resize(img, (1280, 720))

    # Timer - starts timer based on set duration
    elapsed_time = time.time() - start_time_chestpress
    remaining_time = max(0, 60 - elapsed_time) #repetition_time_chestpress


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

    if count_chestpress_right >= 5 and count_chestpress_left >= 5:
        cvzone.putTextRect(img, 'All Repetitions Completed', [390, 30], thickness=2, border=2, scale=2.5)
        display_info_chestpress = False
        exercise_mode = "rest_chestpress"
        rest_chestpress_start_time = time.time()
    return img

def rest_chestpress(img):
    global exercise_mode, rest_chestpress_start_time, start_time_chestpress_set2
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_chestpress_start_time
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

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
    remaining_time = max(0, 60 - elapsed_time) #repetition_time_chestpress_set2


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

    if count_chestpress_right_set2 >= 5 and count_chestpress_left_set2 >= 5:
        cvzone.putTextRect(img, 'All Repetitions Completed', [390, 30], thickness=2, border=2, scale=2.5)
        display_info_chestpress_set2 = False
        exercise_mode = "rest_chestpress_set2"
        rest_chestpress_start_time_set2 = time.time()

    return img

def rest_chestpress_set2(img):
    global exercise_mode, rest_chestpress_start_time_set2, start_time_chestpress_set3
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_chestpress_start_time_set2
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

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
    remaining_time = max(0, 60 - elapsed_time) #repetition_time_chestpress_set3


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

    if count_chestpress_right_set3 >= 5 and count_chestpress_left_set3 >= 5:
        cvzone.putTextRect(img, 'All Repetitions Completed', [390, 30], thickness=2, border=2, scale=2.5)
        display_info_chestpress_set3 = False
        exercise_mode = "rest_chestpress_set3"
        rest_chestpress_start_time_set3 = time.time()
    return img

def rest_chestpress_set3(img):
    global exercise_mode, rest_chestpress_start_time_set3, start_time_dumbbellfrontraise
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
        start_time_dumbbellfrontraise = time.time()
    return img

def detect_dumbbellfrontraise(img):
    global count_left_dumbbellfrontraise, count_right_dumbbellfrontraise, dir_left_dumbbellfrontraise, dir_right_dumbbellfrontraise, start_time_dumbbellfrontraise, repetition_time_dumbbellfrontraise, display_info_dumbbellfrontraise, bar_left_dumbbellfrontraise, bar_right_dumbbellfrontraise, per_left_dumbbellfrontraise, per_right_dumbbellfrontraise, angle_left_dumbbellfrontraise, angle_right_dumbbellfrontraise, rest_dumbbellfrontraise_start_time, exercise_mode

    img = cv2.resize(img, (1280, 720))

    # Timer - starts timer based on set duration
    elapsed_time = time.time() - start_time_dumbbellfrontraise
    remaining_time = max(0, 60 - elapsed_time) #repetition_time_dumbbellfrontraise

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

    if count_right_dumbbellfrontraise >= 5 and count_left_dumbbellfrontraise >= 5:
        cvzone.putTextRect(img, 'All Repetitions Completed', [390, 30], thickness=2, border=2, scale=2.5)
        display_info_dumbbellfrontraise = False
        exercise_mode = "rest_dumbbellfrontraise"
        rest_dumbbellfrontraise_start_time = time.time()
    return img

def rest_dumbbellfrontraise(img):
    global exercise_mode, rest_dumbbellfrontraise_start_time, start_time_dumbbellfrontraise_set2
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_dumbbellfrontraise_start_time
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

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
    remaining_time = max(0, 60 - elapsed_time) #repetition_time_dumbbellfrontraise_set2

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

    if count_right_dumbbellfrontraise >= 5 and count_left_dumbbellfrontraise >= 5:
        cvzone.putTextRect(img, 'All Repetitions Completed', [390, 30], thickness=2, border=2, scale=2.5)
        display_info_dumbbellfrontraise_set2 = False
        exercise_mode = "rest_dumbbellfrontraise_set2"
        rest_dumbbellfrontraise_start_time_set2 = time.time()
    return img

def rest_dumbbellfrontraise_set2(img):
    global exercise_mode, rest_dumbbellfrontraise_start_time_set2, start_time_dumbbellfrontraise_set3
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_dumbbellfrontraise_start_time_set2
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

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
    remaining_time = max(0, 60 - elapsed_time) #repetition_time_dumbbellfrontraise_set3

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
                    count_left_dumbbellfrontraise_set3 += 0.5
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

    if count_right_dumbbellfrontraise_set3 >= 5 and count_left_dumbbellfrontraise_set3 >= 5:
        cvzone.putTextRect(img, 'All Repetitions Completed', [390, 30], thickness=2, border=2, scale=2.5)
        display_info_dumbbellfrontraise_set3 = False
        exercise_mode = "rest_dumbbellfrontraise_set3"
        rest_dumbbellfrontraise_start_time_set3 = time.time()

    return img

def rest_dumbbellfrontraise_set3(img):
    global exercise_mode, rest_dumbbellfrontraise_start_time_set3, start_time_alternatinglunge
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
        start_time_alternatinglunge = time.time()
    return img

def detect_alternatinglunge(img):
    global count_alternating_left_lunge, count_alternating_right_lunge, dir_alternating_left_lunge, dir_alternating_right_lunge, start_time_alternatinglunge, repetition_time_alternatinglunge, per_left_leg_alternatinglunge, per_right_leg_alternatinglunge, display_info_alternatinglunge, bar_left_leg_alternatinglunge, bar_right_leg_alternatinglunge, leftleg_alternatinglunge, rightleg_alternatinglunge, cooldown_duration_alternatinglunge, cooldown_timer_alternatinglunge, color_right_leg_alternatinglunge, color_left_leg_alternatinglunge, exercise_mode, rest_alternatinglunge_start_time, orientation, orientation2

    img = cv2.resize(img, (1280, 720))

    elapsed_time = time.time() - start_time_alternatinglunge
    remaining_time = max(0, 60 - elapsed_time) #repetition_time_alternatinglunge

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
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

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
    remaining_time = max(0, 60 - elapsed_time) #repetition_time_alternatinglunge_set2

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
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

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
    remaining_time = max(0, 60 - elapsed_time) #repetition_time_alternatinglunge_set3

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
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

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
    remaining_time = max(0, 60 - elapsed_time) #repetition_time_bws

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
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

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
    remaining_time = max(0, 60 - elapsed_time) #repetition_time_bws_set2

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
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

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
    remaining_time = max(0, 60 - elapsed_time) #repetition_time_bws_set3

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
    global count_goblet_squat, dir_goblet_squat, start_time_goblet_squat, repetition_time_goblet_squat, display_info_goblet_squat, cooldown_timer_goblet_squat, cooldown_duration_goblet_squat, color_left_leg_goblet_squat, color_right_leg_goblet_squat, rest_goblet_squat_start_time, orientation, orientation2, exercise_mode, per_right_leg, per_left_leg, bar_right_leg, bar_left_leg, color_left_leg, color_right_leg

    img = cv2.resize(img, (1280, 720))

    elapsed_time = time.time() - start_time_goblet_squat
    remaining_time = max(0, 60 - elapsed_time) #repetition_time_goblet_squat

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
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

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
    remaining_time = max(0, 60 - elapsed_time) #repetition_time_goblet_squat_set2

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
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

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
    remaining_time = max(0, 60 - elapsed_time) #repetition_time_goblet_squat_set3

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
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

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
    remaining_time = max(0, 60 - elapsed_time) #repetition_time_hkt

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
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

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
    remaining_time = max(0, 60 - elapsed_time) #repetition_time_hkt_set2

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
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

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
    remaining_time = max(0, 60 - elapsed_time) #repetition_time_hkt_set3

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
    global count_hip_hinge, dir_hip_hinge, start_time_hpp, repetition_time_hpp, display_info_hpp, per_left_hip_angle, bar_left_hip_angle, per_right_hip_angle, bar_right_hip_angle, leftbody_hpp, rightbody_hpp, color_hip, rest_dhh_start_time, orientation, orientation2, exercise_mode


    img = cv2.resize(img, (1280, 720))


    elapsed_time = time.time() - start_time_hpp
    remaining_time = max(0, 60 - elapsed_time) #repetition_time_hpp

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
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

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
    remaining_time = max(0, 60 - elapsed_time) #repetition_time_hpp_set2

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
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

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
    remaining_time = max(0, 60 - elapsed_time) #repetition_time_hpp_set3

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