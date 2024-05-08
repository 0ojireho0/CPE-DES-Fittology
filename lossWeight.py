from flask import Blueprint, render_template, session, Response, jsonify
import cv2
import time
import cvzone
import numpy as np

import poseModules.jogginginplace_PoseModule as pm_jip
import poseModules.JumpingJack_PoseModule as pm_jumpingjacks
import poseModules.buttkick_PoseModule as pm_buttkick
import poseModules.SideLegRaises_PoseModule as pm_slr
import poseModules.SquatJack_PoseModule as pm_squatjacks
import poseModules.squatjump_PoseModule as pm_squatjump
import poseModules.squatsidekick_PoseModule as pm_squatsidekick
import poseModules.jumpinglunge_PoseModule as pm_jumpinglunge
import poseModules.plankjacks_PoseModule as pm_plankjacks
import poseModules.PlankToeTaps_PoseModule as pm_ptt

lossWeight = Blueprint("lossWeight", __name__,static_folder="static", template_folder="templates")

# --------------- FOR JOG IN PLACE -------------------
detector_jip = pm_jip.PoseDetector()

left_foot_lift_off_count_jip = 0
right_foot_lift_off_count_jip = 0
counter_left_jip = 0
counter_right_jip = 0

per_down_right_jip = 0
bar_down_right_jip = 0

per_down_left_jip = 0
bar_down_left_jip = 0
countdown_before_jip = None


dir_left_jip = 0
dir_right_jip = 0

start_time_jip = time.time()
repetition_time_jip = 70
display_info_jip = False

color_leg_jip = (0, 0, 255)
rest_jip_start_time = time.time()
drawings = None
drawings2 = None
# --------------- END FOR JOG IN PLACE --------------

# --------------- FOR JOG IN PLACE SET 2 -------------------
detector_jip = pm_jip.PoseDetector()

left_foot_lift_off_count_jip_set2 = 0
right_foot_lift_off_count_jip_set2 = 0
counter_left_jip_set2 = 0
counter_right_jip_set2 = 0

per_down_right_jip_set2 = 0
bar_down_right_jip_set2 = 0

per_down_left_jip_set2 = 0
bar_down_left_jip_set2 = 0


dir_left_jip_set2 = 0
dir_right_jip_set2 = 0

start_time_jip_set2 = time.time()
repetition_time_jip_set2 = 60
display_info_jip_set2 = True

color_leg_jip_set2 = (0, 0, 255)
rest_jip_start_time_set2 = time.time()
# --------------- END FOR JOG IN PLACE SET 2 --------------


# --------------- FOR JOG IN PLACE SET 3 -------------------
detector_jip = pm_jip.PoseDetector()

left_foot_lift_off_count_jip_set3 = 0
right_foot_lift_off_count_jip_set3 = 0
counter_left_jip_set3 = 0
counter_right_jip_set3 = 0

per_down_right_jip_set3 = 0
bar_down_right_jip_set3 = 0

per_down_left_jip_set3 = 0
bar_down_left_jip_set3 = 0


dir_left_jip_set3 = 0
dir_right_jip_set3 = 0

start_time_jip_set3 = time.time()
repetition_time_jip_set3 = 70
display_info_jip_set3 = True

color_leg_jip_set3 = (0, 0, 255)
rest_jip_start_time_set3 = time.time()
# --------------- END FOR JOG IN PLACE SET 3 --------------

# --------------- FOR JUMPING JACK ------------------
detector_JumpingJack = pm_jumpingjacks.poseDetectorJumpingJack()

count_jumping_jacks = 0
dir_jumping_jacks = 0

start_time_jumpingjacks = time.time()
repetition_time_jumpingjacks = 60
display_info_jumpingjacks = True

per_left_arm_jumpingjacks = 0
bar_left_arm_jumpingjacks = 0

per_right_arm_jumpingjacks = 0
bar_right_arm_jumpingjacks = 0

per_down_left_jumpingjacks = 0
per_down_right_jumpingjacks = 0

bar_down_left_jumpingjacks = 0
bar_down_right_jumpingjacks = 0

leftwholearm_jumpingjacks = 0
rightwholearm_jumpingjacks = 0
distance_jumpingjacks = 0
rest_jumpingjack_start_time = time.time()
# --------------- END FOR JUMPING JACK -------------

# --------------- FOR JUMPING JACK SET 2 ------------------
detector_JumpingJack = pm_jumpingjacks.poseDetectorJumpingJack()

count_jumping_jacks_set2 = 0
dir_jumping_jacks_set2 = 0

start_time_jumpingjacks_set2 = time.time()
repetition_time_jumpingjacks_set2 = 60
display_info_jumpingjacks_set2 = True

per_left_arm_jumpingjacks_set2 = 0
bar_left_arm_jumpingjacks_set2 = 0

per_right_arm_jumpingjacks_set2 = 0
bar_right_arm_jumpingjacks_set2 = 0

per_down_left_jumpingjacks_set2 = 0
per_down_right_jumpingjacks_set2 = 0

bar_down_left_jumpingjacks_set2 = 0
bar_down_right_jumpingjacks_set2 = 0

leftwholearm_jumpingjacks_set2 = 0
rightwholearm_jumpingjacks_set2 = 0
distance_jumpingjacks_set2 = 0
rest_jumpingjack_start_time_set2 = time.time()
# --------------- END FOR JUMPING JACK SET 2 -------------

# --------------- FOR JUMPING JACK SET SET 3 ------------------
detector_JumpingJack = pm_jumpingjacks.poseDetectorJumpingJack()

count_jumping_jacks_set3 = 0
dir_jumping_jacks_set3 = 0

start_time_jumpingjacks_set3 = time.time()
repetition_time_jumpingjacks_set3 = 60
display_info_jumpingjacks_set3 = True

per_left_arm_jumpingjacks_set3 = 0
bar_left_arm_jumpingjacks_set3 = 0

per_right_arm_jumpingjacks_set3 = 0
bar_right_arm_jumpingjacks_set3 = 0

per_down_left_jumpingjacks_set3 = 0
per_down_right_jumpingjacks_set3 = 0

bar_down_left_jumpingjacks_set3 = 0
bar_down_right_jumpingjacks_set3 = 0

leftwholearm_jumpingjacks_set3 = 0
rightwholearm_jumpingjacks_set3 = 0
distance_jumpingjacks_set3 = 0
rest_jumpingjack_start_time_set3 = time.time()
# --------------- END FOR JUMPING JACK SET 3 -------------

# ---------------- FOR BUTTKICK -----------------------
detector_buttkick = pm_buttkick.poseDetectorButtKick()

count_alternating_right_lunge_buttkick = 0
count_alternating_left_lunge_buttkick = 0

dir_alternating_left_lunge_buttkick = 0
dir_alternating_right_lunge_buttkick = 0


start_time_buttkick = time.time()
repetition_time_buttkick = 60
display_info_buttkick = True

per_left_leg_buttkick = 0
bar_left_leg_buttkick = 0

per_right_leg_buttkick = 0
bar_right_leg_buttkick = 0

leftleg_buttkick= 0
rightleg_buttkick = 0

right_buttkick = 0
left_buttkick = 0


cooldown_duration_buttkick = 5
cooldown_timer_buttkick = 0

color_left_leg_buttkick = (0, 0, 255)
color_right_leg_buttkick = (0, 0, 255)
rest_buttkick_start_time = time.time()
# ---------------- END FOR BUTTKICK ------------------

# ---------------- FOR BUTTKICK SET 2 -----------------------
detector_buttkick = pm_buttkick.poseDetectorButtKick()

count_alternating_right_lunge_buttkick_set2 = 0
count_alternating_left_lunge_buttkick_set2 = 0

dir_alternating_left_lunge_buttkick_set2 = 0
dir_alternating_right_lunge_buttkick_set2 = 0


start_time_buttkick_set2 = time.time()
repetition_time_buttkick_set2 = 60
display_info_buttkick_set2 = True

per_left_leg_buttkick_set2 = 0
bar_left_leg_buttkick_set2 = 0

per_right_leg_buttkick_set2 = 0
bar_right_leg_buttkick_set2 = 0

leftleg_buttkick_set2= 0
rightleg_buttkick_set2 = 0

right_buttkick_set2 = 0
left_buttkick_set2 = 0


cooldown_duration_buttkick_set2 = 5
cooldown_timer_buttkick_set2 = 0

color_left_leg_buttkick_set2 = (0, 0, 255)
color_right_leg_buttkick_set2 = (0, 0, 255)
rest_buttkick_start_time_set2 = time.time()
# ---------------- END FOR BUTTKICK SET 2 ------------------

# ---------------- FOR BUTTKICK -----------------------
detector_buttkick = pm_buttkick.poseDetectorButtKick()

count_alternating_right_lunge_buttkick_set3 = 0
count_alternating_left_lunge_buttkick_set3 = 0

dir_alternating_left_lunge_buttkick_set3 = 0
dir_alternating_right_lunge_buttkick_set3 = 0


start_time_buttkick_set3 = time.time()
repetition_time_buttkick_set3 = 60
display_info_buttkick_set3 = True

per_left_leg_buttkick_set3 = 0
bar_left_leg_buttkick_set3 = 0

per_right_leg_buttkick_set3 = 0
bar_right_leg_buttkick_set3 = 0

leftleg_buttkick_set3 = 0
rightleg_buttkick_set3 = 0

right_buttkick_set3 = 0
left_buttkick_set3 = 0


cooldown_duration_buttkick_set3 = 5
cooldown_timer_buttkick_set3 = 0

color_left_leg_buttkick_set3 = (0, 0, 255)
color_right_leg_buttkick_set3 = (0, 0, 255)
rest_buttkick_start_time_set3 = time.time()
# ---------------- END FOR BUTTKICK ------------------

# --------------- FOR SIDE LEG RAISES ---------------
detector_SideLegRaises = pm_slr.poseDetectorSideLegRaises()

#Initialize Variables
count_sidelegraise_left = 0
count_sidelegraise_right = 0

dir_sidelegraises_left = 0
dir_sidelegraises_right = 0

start_time_slr = time.time() # starts time
repetition_time_slr = 60 # duration time
display_info_slr = True # display features

bar_left_slr = 0
bar_right_slr = 0
per_left_slr = 0
per_right_slr = 0
angle_left_slr = 0

color_left_leg_slr = (0, 0, 255)
color_right_leg_slr = (0, 0, 255)

left_leg_slr = 0
right_leg_slr = 0
rest_slr_start_time = time.time()
# --------------- END FOR SIDE LEG RAISES ------------

# --------------- FOR SIDE LEG RAISES SET 2 ---------------
detector_SideLegRaises = pm_slr.poseDetectorSideLegRaises()

#Initialize Variables
count_sidelegraise_left_set2 = 0
count_sidelegraise_right_set2 = 0

dir_sidelegraises_left_set2 = 0
dir_sidelegraises_right_set2 = 0

start_time_slr_set2 = time.time() # starts time
repetition_time_slr_set2 = 60 # duration time
display_info_slr_set2 = True # display features

bar_left_slr_set2 = 0
bar_right_slr_set2 = 0
per_left_slr_set2 = 0
per_right_slr_set2 = 0
angle_left_slr_set2 = 0

color_left_leg_slr_set2 = (0, 0, 255)
color_right_leg_slr_set2 = (0, 0, 255)

left_leg_slr_set2 = 0
right_leg_slr_set2 = 0
rest_slr_start_time_set2 = time.time()
# --------------- END FOR SIDE LEG RAISES SET 2 ------------

# --------------- FOR SIDE LEG RAISES SET 3 ---------------
detector_SideLegRaises = pm_slr.poseDetectorSideLegRaises()

#Initialize Variables
count_sidelegraise_left_set3 = 0
count_sidelegraise_right_set3 = 0

dir_sidelegraises_left_set3 = 0
dir_sidelegraises_right_set3 = 0

start_time_slr_set3 = time.time() # starts time
repetition_time_slr_set3 = 60 # duration time
display_info_slr_set3 = True # display features

bar_left_slr_set3 = 0
bar_right_slr_set3 = 0
per_left_slr_set3 = 0
per_right_slr_set3 = 0
angle_left_slr_set3 = 0

color_left_leg_slr_set3 = (0, 0, 255)
color_right_leg_slr_set3 = (0, 0, 255)

left_leg_slr_set3 = 0
right_leg_slr_set3 = 0
rest_slr_start_time_set3 = time.time()
# --------------- END FOR SIDE LEG RAISES SET 3 ------------

# --------------- FOR SQUAT JACKS --------------------
detector_squatjack = pm_squatjacks.poseDetectorSquatJack()

# Initialize Variables
count_squatjack = 0
dir_squatjack = 0
start_time_squatjack = time.time()  # starts time
repetition_time_squatjack = 60  # duration time
display_info_squatjack = True  # display features
rest_squatjacks_start_time = time.time()

per_down_squatjacks = 0 
bar_down_squatjacks = 0 
distance_squatjacks = 0 
# --------------- END FOR SQUAT JACKS ----------------

# --------------- FOR SQUAT JACKS SET 2--------------------
detector_squatjack = pm_squatjacks.poseDetectorSquatJack()

# Initialize Variables
count_squatjack_set2 = 0
dir_squatjack_set2 = 0
start_time_squatjack_set2 = time.time()  # starts time
repetition_time_squatjack_set2 = 60  # duration time
display_info_squatjack_set2 = True  # display features
rest_squatjacks_start_time_set2 = time.time()

per_down_squatjacks_set2 = 0 
bar_down_squatjacks_set2 = 0 
distance_squatjacks_set2 = 0 
# --------------- END FOR SQUAT JACKS SET 2 ----------------

# --------------- FOR SQUAT JACKS SET 3--------------------
detector_squatjack = pm_squatjacks.poseDetectorSquatJack()

# Initialize Variables
count_squatjack_set3 = 0
dir_squatjack_set3 = 0
start_time_squatjack_set3 = time.time()  # starts time
repetition_time_squatjack_set3 = 60  # duration time
display_info_squatjack_set3 = True  # display features
rest_squatjacks_start_time_set3 = time.time()

per_down_squatjacks_set3 = 0 
bar_down_squatjacks_set3 = 0 
distance_squatjacks_set3 = 0 
# --------------- END FOR SQUAT JACKS SET 3----------------

# --------------- FOR SQUAT JUMP --------------------
detector_squatjump = pm_squatjump.poseDetectorsquatjump()

count_squat_jump = 0
dir_squat_jump = 0

start_time_squatjump = time.time()
repetition_time_squatjump = 60
display_info_squatjump = True

per_left_leg_squatjump = 0
bar_left_leg_squatjump = 0

per_right_leg_squatjump = 0
bar_right_leg_squatjump = 0

leftleg_squatjump = 0
rightleg_squatjump = 0


cooldown_duration_squatjump = 5
cooldown_timer_squatjump = 0

color_left_leg_squatjump = (0, 0, 255)
color_right_leg_squatjump = (0, 0, 255)
rest_squatjump_start_time = time.time()
# --------------- END FOR SQUAT JUMP ---------------

# --------------- FOR SQUAT JUMP SET 2 --------------------
detector_squatjump = pm_squatjump.poseDetectorsquatjump()

count_squat_jump_set2 = 0
dir_squat_jump_set2 = 0

start_time_squatjump_set2 = time.time()
repetition_time_squatjump_set2 = 60
display_info_squatjump_set2 = True

per_left_leg_squatjump_set2 = 0
bar_left_leg_squatjump_set2 = 0

per_right_leg_squatjump_set2 = 0
bar_right_leg_squatjump_set2 = 0

leftleg_squatjump_set2 = 0
rightleg_squatjump_set2 = 0


cooldown_duration_squatjump_set2 = 5
cooldown_timer_squatjump_set2 = 0

color_left_leg_squatjump_set2 = (0, 0, 255)
color_right_leg_squatjump_set2 = (0, 0, 255)
rest_squatjump_start_time_set2 = time.time()
# --------------- END FOR SQUAT JUMP SET 2 ---------------

# --------------- FOR SQUAT JUMP SET 3 --------------------
detector_squatjump = pm_squatjump.poseDetectorsquatjump()

count_squat_jump_set3 = 0
dir_squat_jump_set3 = 0

start_time_squatjump_set3 = time.time()
repetition_time_squatjump_set3 = 60
display_info_squatjump_set3 = True

per_left_leg_squatjump_set3 = 0
bar_left_leg_squatjump_set3 = 0

per_right_leg_squatjump_set3 = 0
bar_right_leg_squatjump_set3 = 0

leftleg_squatjump_set3 = 0
rightleg_squatjump_set3 = 0


cooldown_duration_squatjump_set3 = 5
cooldown_timer_squatjump_set3 = 0

color_left_leg_squatjump_set3 = (0, 0, 255)
color_right_leg_squatjump_set3 = (0, 0, 255)
rest_squatjump_start_time_set3 = time.time()
# --------------- END FOR SQUAT JUMP SET 3 ---------------

# --------------- FOR SQUAT SIDE KICK -----------------
detector_SquatSideKick = pm_squatsidekick.poseDetectorSquatSideKick()

count_squatsidekick = 0
dir_squatsidekick = 0

count_left_kick_squatsidekick = 0
dir_kick_left_squatsidekick = 0

count_right_kick_squatsidekick = 0
dir_kick_right_squatsidekick = 0


start_time_squatsidekick = time.time()
repetition_time_squatsidekick = 60
display_info_squatsidekick = True

per_left_leg_squatsidekick = 0
bar_left_leg_squatsidekick = 0
per_left_leg_left_kick_squatsidekick = 0
bar_left_leg_left_kick_squatsidekick = 0

per_right_leg_squatsidekick = 0
bar_right_leg_squatsidekick = 0
per_right_leg_right_kick_squatsidekick = 0
bar_right_leg_right_kick_squatsidekick = 0

cooldown_duration_squatsidekick = 5
cooldown_timer_squatsidekick = 0

color_left_leg_squatsidekick = (0, 0, 255)
color_right_leg_squatsidekick = (0, 0, 255)

color_left_leg_left_kick_squatsidekick = (0, 0, 255)
color_right_leg_right_kick_squatsidekick = (0, 0, 255)

rightleg_squatsidekick = 0
leftleg_squatsidekick = 0
kickleft_squatsidekick = 0
kickright_squatsidekick = 0


squat_completed_squatsidekick = False
performing_squat_squatsidekick = True
rest_squatsidekick_start_time = time.time()
# --------------- END FOR SQUAT SIDE KICK ------------

# --------------- FOR SQUAT SIDE KICK SET 2 -----------------
detector_SquatSideKick = pm_squatsidekick.poseDetectorSquatSideKick()

count_squatsidekick_set2 = 0
dir_squatsidekick_set2 = 0

count_left_kick_squatsidekick_set2 = 0
dir_kick_left_squatsidekick_set2 = 0

count_right_kick_squatsidekick_set2 = 0
dir_kick_right_squatsidekick_set2 = 0


start_time_squatsidekick_set2 = time.time()
repetition_time_squatsidekick_set2 = 60
display_info_squatsidekick_set2 = True

per_left_leg_squatsidekick_set2 = 0
bar_left_leg_squatsidekick_set2 = 0
per_left_leg_left_kick_squatsidekick_set2 = 0
bar_left_leg_left_kick_squatsidekick_set2 = 0

per_right_leg_squatsidekick_set2 = 0
bar_right_leg_squatsidekick_set2 = 0
per_right_leg_right_kick_squatsidekick_set2 = 0
bar_right_leg_right_kick_squatsidekick_set2 = 0

cooldown_duration_squatsidekick_set2 = 5
cooldown_timer_squatsidekick_set2 = 0

color_left_leg_squatsidekick_set2 = (0, 0, 255)
color_right_leg_squatsidekick_set2 = (0, 0, 255)

color_left_leg_left_kick_squatsidekick_set2 = (0, 0, 255)
color_right_leg_right_kick_squatsidekick_set2 = (0, 0, 255)

rightleg_squatsidekick_set2 = 0
leftleg_squatsidekick_set2 = 0
kickleft_squatsidekick_set2 = 0
kickright_squatsidekick_set2 = 0


squat_completed_squatsidekick_set2 = False
performing_squat_squatsidekick_set2 = True
rest_squatsidekick_start_time_set2 = time.time()
# --------------- END FOR SQUAT SIDE KICK SET 2 ------------

# --------------- FOR SQUAT SIDE KICK SET 3 -----------------
detector_SquatSideKick = pm_squatsidekick.poseDetectorSquatSideKick()

count_squatsidekick_set3 = 0
dir_squatsidekick_set3 = 0

count_left_kick_squatsidekick_set3 = 0
dir_kick_left_squatsidekick_set3 = 0

count_right_kick_squatsidekick_set3 = 0
dir_kick_right_squatsidekick_set3 = 0


start_time_squatsidekick_set3 = time.time()
repetition_time_squatsidekick_set3 = 60
display_info_squatsidekick_set3 = True

per_left_leg_squatsidekick_set3 = 0
bar_left_leg_squatsidekick_set3 = 0
per_left_leg_left_kick_squatsidekick_set3 = 0
bar_left_leg_left_kick_squatsidekick_set3 = 0

per_right_leg_squatsidekick_set3 = 0
bar_right_leg_squatsidekick_set3 = 0
per_right_leg_right_kick_squatsidekick_set3 = 0
bar_right_leg_right_kick_squatsidekick_set3 = 0

cooldown_duration_squatsidekick_set3 = 5
cooldown_timer_squatsidekick_set3 = 0

color_left_leg_squatsidekick_set3 = (0, 0, 255)
color_right_leg_squatsidekick_set3 = (0, 0, 255)

color_left_leg_left_kick_squatsidekick_set3 = (0, 0, 255)
color_right_leg_right_kick_squatsidekick_set3 = (0, 0, 255)

rightleg_squatsidekick_set3 = 0
leftleg_squatsidekick_set3 = 0
kickleft_squatsidekick_set3 = 0
kickright_squatsidekick_set3 = 0


squat_completed_squatsidekick_set3 = False
performing_squat_squatsidekick_set3 = True
rest_squatsidekick_start_time_set3 = time.time()
# --------------- END FOR SQUAT SIDE KICK SET 3 ------------

# ---------------- FOR JUMPING LUNGE -------------------
detector_jumpinglunge = pm_jumpinglunge.poseDetectorJumpingLunge()

count_alternating_right_lunge_jumpinglunge = 0
count_alternating_left_lunge_jumpinglunge = 0

dir_alternating_left_lunge_jumpinglunge = 0
dir_alternating_right_lunge_jumpinglunge = 0

start_time_jumpinglunge = time.time()
repetition_time_jumpinglunge = 60
display_info_jumpinglunge = True

per_left_leg_jumpinglunge = 0
bar_left_leg_jumpinglunge = 0

per_right_leg_jumpinglunge = 0
bar_right_leg_jumpinglunge = 0


cooldown_duration_jumpinglunge = 5
cooldown_timer_jumpinglunge = 0

color_left_leg_jumpinglunge = (0, 0, 255)
color_right_leg_jumpinglunge = (0, 0, 255)

rest_jumpinglunge_start_time = time.time()
# ---------------- END FOR JUMPING LUNGE ---------------

# ---------------- FOR JUMPING LUNGE SET 2 -------------------
detector_jumpinglunge = pm_jumpinglunge.poseDetectorJumpingLunge()

count_alternating_right_lunge_jumpinglunge_set2 = 0
count_alternating_left_lunge_jumpinglunge_set2 = 0

dir_alternating_left_lunge_jumpinglunge_set2 = 0
dir_alternating_right_lunge_jumpinglunge_set2 = 0

start_time_jumpinglunge_set2 = time.time()
repetition_time_jumpinglunge_set2 = 60
display_info_jumpinglunge_set2 = True

per_left_leg_jumpinglunge_set2 = 0
bar_left_leg_jumpinglunge_set2 = 0

per_right_leg_jumpinglunge_set2 = 0
bar_right_leg_jumpinglunge_set2 = 0


cooldown_duration_jumpinglunge_set2 = 5
cooldown_timer_jumpinglunge_set2 = 0

color_left_leg_jumpinglunge_set2 = (0, 0, 255)
color_right_leg_jumpinglunge_set2 = (0, 0, 255)

rest_jumpinglunge_start_time_set2 = time.time()
# ---------------- END FOR JUMPING LUNGE SET 2 ---------------

# ---------------- FOR JUMPING LUNGE SET 3 -------------------
detector_jumpinglunge = pm_jumpinglunge.poseDetectorJumpingLunge()

count_alternating_right_lunge_jumpinglunge_set3 = 0
count_alternating_left_lunge_jumpinglunge_set3 = 0

dir_alternating_left_lunge_jumpinglunge_set3 = 0
dir_alternating_right_lunge_jumpinglunge_set3 = 0

start_time_jumpinglunge_set3 = time.time()
repetition_time_jumpinglunge_set3 = 60
display_info_jumpinglunge_set3 = True

per_left_leg_jumpinglunge_set3 = 0
bar_left_leg_jumpinglunge_set3 = 0

per_right_leg_jumpinglunge_set3 = 0
bar_right_leg_jumpinglunge_set3 = 0


cooldown_duration_jumpinglunge_set3 = 5
cooldown_timer_jumpinglunge_set3 = 0

color_left_leg_jumpinglunge_set3 = (0, 0, 255)
color_right_leg_jumpinglunge_set3 = (0, 0, 255)

rest_jumpinglunge_start_time_set3 = time.time()
# ---------------- END FOR JUMPING LUNGE SET 3 ---------------

# --------------- FOR PLANK JACKS --------------------------
detector_PlankJacks = pm_plankjacks.poseDetectorPlankJacks()

count_Plank_Jacks = 0
dir_Plank_Jacks = 0

start_time_plankjacks = time.time()
repetition_time_plankjacks = 60
display_info_plankjacks = True

per_right_leg_plankjacks = 0
per_left_leg_plankjacks = 0
bar_right_leg_plankjacks = 0
bar_left_leg_plankjacks = 0


cooldown_duration_plankjacks = 5
cooldown_timer_plankjacks = 0

color_left_leg_plankjacks = (0, 0, 255)
color_right_leg_plankjacks = (0, 0, 255)
rest_plankjacks_start_time = time.time()
# ---------------- FOR PLANK JACKS -----------------------

# --------------- FOR PLANK JACKS SET 2 --------------------------
detector_PlankJacks = pm_plankjacks.poseDetectorPlankJacks()

count_Plank_Jacks_set2 = 0
dir_Plank_Jacks_set2 = 0

start_time_plankjacks_set2 = time.time()
repetition_time_plankjacks_set2 = 60
display_info_plankjacks_set2 = True

per_right_leg_plankjacks_set2 = 0
bar_left_leg_plankjacks_set2 = 0
per_left_leg_plankjacks_set2 = 0
bar_right_leg_plankjacks_set2 = 0


cooldown_duration_plankjacks_set2 = 5
cooldown_timer_plankjacks_set2 = 0

color_left_leg_plankjacks_set2 = (0, 0, 255)
color_right_leg_plankjacks_set2 = (0, 0, 255)
rest_plankjacks_start_time_set2 = time.time()
# ---------------- FOR PLANK JACKS SET 2 -----------------------

# --------------- FOR PLANK JACKS SET 3 --------------------------
detector_PlankJacks = pm_plankjacks.poseDetectorPlankJacks()

count_Plank_Jacks_set3 = 0
dir_Plank_Jacks_set3 = 0

start_time_plankjacks_set3 = time.time()
repetition_time_plankjacks_set3 = 60
display_info_plankjacks_set3 = True

per_right_leg_plankjacks_set3 = 0
bar_left_leg_plankjacks_set3 = 0
per_left_leg_plankjacks_set3 = 0
bar_right_leg_plankjacks_set3 = 0


cooldown_duration_plankjacks_set3 = 5
cooldown_timer_plankjacks_set3 = 0

color_left_leg_plankjacks_set3 = (0, 0, 255)
color_right_leg_plankjacks_set3 = (0, 0, 255)
rest_plankjacks_start_time_set3 = time.time()
# ---------------- FOR PLANK JACKS SET 3 -----------------------

# ---------------- FOR PLANK TOE TAPS -------------------------
detector_PlankToeTaps = pm_ptt.poseDetectorPlankToeTaps()

count_plank_toe_taps_right = 0
count_plank_toe_taps_left = 0


dir_plank_toe_taps_right = 0
dir_plank_toe_taps_left = 0


start_time_ptt = time.time()
repetition_time_ptt = 60
display_info_ptt = True

per_left_leg_ptt = 0
bar_left_leg_ptt = 0

per_right_leg_ptt = 0
bar_right_leg_ptt = 0

cooldown_duration_ptt = 5
cooldown_timer_ptt = 0

color_left_leg_ptt = (0, 0, 255)
color_right_leg_ptt = (0, 0, 255)

rest_ptt_start_time = time.time()
# ---------------- END FOR PLANK TOE TAPS ---------------------

# ---------------- FOR PLANK TOE TAPS SET 2 -------------------------
detector_PlankToeTaps = pm_ptt.poseDetectorPlankToeTaps()

count_plank_toe_taps_right_set2 = 0
count_plank_toe_taps_left_set2 = 0


dir_plank_toe_taps_right_set2 = 0
dir_plank_toe_taps_left_set2 = 0


start_time_ptt_set2 = time.time()
repetition_time_ptt_set2 = 60
display_info_ptt_set2 = True

per_left_leg_ptt_set2 = 0
bar_left_leg_ptt_set2 = 0

per_right_leg_ptt_set2 = 0
bar_right_leg_ptt_set2 = 0

cooldown_duration_ptt_set2 = 5
cooldown_timer_ptt_set2 = 0

color_left_leg_ptt_set2 = (0, 0, 255)
color_right_leg_ptt_set2 = (0, 0, 255)

rest_ptt_start_time_set2 = time.time()
# ---------------- END FOR PLANK TOE TAPS SET 2 ---------------------

# ---------------- FOR PLANK TOE TAPS SET 3 -------------------------
detector_PlankToeTaps = pm_ptt.poseDetectorPlankToeTaps()

count_plank_toe_taps_right_set3 = 0
count_plank_toe_taps_left_set3 = 0


dir_plank_toe_taps_right_set3 = 0
dir_plank_toe_taps_left_set3 = 0


start_time_ptt_set3 = time.time()
repetition_time_ptt_set3 = 60
display_info_ptt_set3 = True

per_left_leg_ptt_set3 = 0
bar_left_leg_ptt_set3 = 0

per_right_leg_ptt_set3 = 0
bar_right_leg_ptt_set3 = 0

cooldown_duration_ptt_set3 = 5
cooldown_timer_ptt_set3 = 0

color_left_leg_ptt_set3 = (0, 0, 255)
color_right_leg_ptt_set3 = (0, 0, 255)

rest_ptt_start_time_set3 = time.time()

orientation = ''
orientation2 = ''
# ---------------- END FOR PLANK TOE TAPS SET 3 ---------------------



@lossWeight.route('/lossWeight')
@lossWeight.route('/')
def home():
    #username = session.get('username')
    if 'username' in session and session['exercise'] == "loss_weight":
        buttkicks = session.get('buttkicks')
        joginplace = session.get('joginplace')
        jumpingjacks = session.get('jumpingjacks')
        jumpinglunges = session.get('jumpinglunges')
        plankjacks = session.get('plankjacks')
        planktoetaps = session.get('planktoetaps')
        sidelegraise = session.get('sidelegraise')
        squatjacks = session.get('squatjacks')
        squatjump = session.get('squatjump')
        squatsidekick = session.get('squatsidekick')
        return render_template('lossWeight.html', buttkicks = buttkicks, joginplace = joginplace, jumpingjacks = jumpingjacks, jumpinglunges = jumpinglunges, plankjacks = plankjacks, planktoetaps = planktoetaps, sidelegraise = sidelegraise, squatjacks = squatjacks, squatjump = squatjump, squatsidekick = squatsidekick  )
    else:
        return render_template('home.html')

exercise_mode = "joginplace"
    
def gen_frames():
    cap = cv2.VideoCapture(0)
    while True:
        success, img = cap.read()
        if not success:
            break
        else:
            if exercise_mode == "joginplace":
                img_with_faces = detect_jip(img)
            if exercise_mode == "rest_jip":
                img_with_faces = rest_jip(img)
            if exercise_mode == "joginplace_set2":
                img_with_faces = detect_jip_set2(img)
            if exercise_mode == "rest_jip_set2":
                img_with_faces = rest_jip_set2(img)
            if exercise_mode == "joginplace_set3":
                img_with_faces = detect_jip_set3(img)
            if exercise_mode == "rest_jip_set3":
                img_with_faces = rest_jip_set3(img)
            if exercise_mode == "jumpingjacks":
                img_with_faces = detect_jumpingjacks(img)
            if exercise_mode == "rest_jumpingjacks":
                img_with_faces = rest_jumpingjacks(img)
            if exercise_mode == "jumpingjacks_set2":
                img_with_faces = detect_jumpingjacks_set2(img)
            if exercise_mode == "rest_jumpingjacks_set2":
                img_with_faces = rest_jumpingjacks_set2(img)
            if exercise_mode == "jumpingjacks_set3":
                img_with_faces = detect_jumpingjacks_set3(img)
            if exercise_mode == "rest_jumpingjacks_set3":
                img_with_faces = rest_jumpingjacks_set3(img)
            if exercise_mode == "buttkick":
                img_with_faces = detect_buttkick(img)
            if exercise_mode == "rest_buttkick":
                img_with_faces = rest_buttkick(img)
            if exercise_mode == "buttkick_set2":
                img_with_faces = detect_buttkick_set2(img)
            if exercise_mode == "rest_buttkick_set2":
                img_with_faces = rest_buttkick_set2(img)
            if exercise_mode == "buttkick_set3":
                img_with_faces = detect_buttkick_set3(img)
            if exercise_mode == "rest_buttkick_set3":
                img_with_faces = rest_buttkick_set3(img)
            if exercise_mode == "slr":
                img_with_faces = detect_slr(img)
            if exercise_mode == "rest_slr":
                img_with_faces = rest_slr(img)
            if exercise_mode == "slr_set2":
                img_with_faces = detect_slr_set2(img)
            if exercise_mode == "rest_slr_set2":
                img_with_faces = rest_slr_set2(img)
            if exercise_mode == "slr_set3":
                img_with_faces = detect_slr_set3(img)
            if exercise_mode == "rest_slr_set3":
                img_with_faces = rest_slr_set3(img)
            if exercise_mode == "squatjacks":
                img_with_faces = detect_squatjacks(img)
            if exercise_mode == "rest_squatjacks":
                img_with_faces = rest_squatjacks(img)
            if exercise_mode == "squatjacks_set2":
                img_with_faces = detect_squatjacks_set2(img)
            if exercise_mode == "rest_squatjacks_set2":
                img_with_faces = rest_squatjacks_set2(img)
            if exercise_mode == "squatjacks_set3":
                img_with_faces = detect_squatjacks_set3(img)
            if exercise_mode == "rest_squatjacks_set3":
                img_with_faces = rest_squatjacks_set3(img)
            if exercise_mode == "squatjump":
                img_with_faces = detect_squatjump(img)
            if exercise_mode == "rest_squatjump":
                img_with_faces = rest_squatjump(img)
            if exercise_mode == "squatjump_set2":
                img_with_faces = detect_squatjump_set2(img)
            if exercise_mode == "rest_squatjump_set2":
                img_with_faces = rest_squatjump_set2(img)
            if exercise_mode == "squatjump_set3":
                img_with_faces = detect_squatjump_set3(img)
            if exercise_mode == "rest_squatjump_set3":
                img_with_faces = rest_squatjump_set3(img)
            if exercise_mode == "squatsidekick":
                img_with_faces = detect_squatsidekick(img)
            if exercise_mode == "rest_squatsidekick":
                img_with_faces = rest_squatsidekick(img)
            if exercise_mode == "squatsidekick_set2":
                img_with_faces = detect_squatsidekick_set2(img)
            if exercise_mode == "rest_squatsidekick_set2":
                img_with_faces = rest_squatsidekick_set2(img)
            if exercise_mode == "squatsidekick_set3":
                img_with_faces = detect_squatsidekick_set3(img)
            if exercise_mode == "rest_squatsidekick_set3":
                img_with_faces = rest_squatsidekick_set3(img)
            if exercise_mode == "jumpinglunge":
                img_with_faces = detect_jumpinglunge(img)
            if exercise_mode == "rest_jumpinglunge":
                img_with_faces = rest_jumpinglunge(img)
            if exercise_mode == "jumpinglunge_set2":
                img_with_faces = detect_jumpinglunge_set2(img)
            if exercise_mode == "rest_jumpinglunge_set2":
                img_with_faces = rest_jumpinglunge_set2(img)
            if exercise_mode == "jumpinglunge_set3":
                img_with_faces = detect_jumpinglunge_set3(img)
            if exercise_mode == "rest_jumpinglunge_set3":
                img_with_faces = rest_jumpinglunge_set3(img)
            if exercise_mode == "plankjacks":
                img_with_faces = detect_plankjacks(img)
            if exercise_mode == "rest_plankjacks":
                img_with_faces = rest_plankjacks(img)
            if exercise_mode == "plankjacks_set2":
                img_with_faces = detect_plankjacks_set2(img)
            if exercise_mode == "rest_plankjacks_set2":
                img_with_faces = rest_plankjacks_set2(img)
            if exercise_mode == "plankjacks_set3":
                img_with_faces = detect_plankjacks_set3(img)
            if exercise_mode == "rest_plankjacks_set3":
                img_with_faces = rest_plankjacks_set3(img)
            if exercise_mode == "ptt":
                img_with_faces = detect_ptt(img)
            if exercise_mode == "rest_ptt":
                img_with_faces = rest_ptt(img)
            if exercise_mode == "ptt_set2":
                img_with_faces = detect_ptt_set2(img)
            if exercise_mode == "rest_ptt_set2":
                img_with_faces = rest_ptt_set2(img)
            if exercise_mode == "ptt_set3":
                img_with_faces = detect_ptt_set3(img)
            if exercise_mode == "rest_ptt_set3":
                img_with_faces = rest_ptt_set3(img)

            ret, buffer = cv2.imencode('.jpg', img_with_faces)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    return 
    
@lossWeight.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@lossWeight.route('/start_timer_lossWeight', methods=['POST'])
def start_timer_lossWeight():
    global start_time_jip, countdown_before_jip
    countdown_before_jip = time.time()
    start_time_jip = time.time()  # Start the timer
    return jsonify({'message': 'Timer started'}), 200

@lossWeight.route('/exercise_mode')
def get_exercise_mode():
    global exercise_mode
    return jsonify({'exercise_mode': exercise_mode})

def detect_jip(img):
    global left_foot_lift_off_count_jip, right_foot_lift_off_count_jip, counter_left_jip, counter_right_jip, per_down_right_jip, bar_down_right_jip, per_down_left_jip, bar_down_left_jip, dir_left_jip, dir_right_jip, start_time_jip, repetition_time_jip, display_info_jip, color_leg_jip, rest_jip_start_time, countdown_before_jip, drawings, drawings2, exercise_mode
    
    img = cv2.resize(img, (1280, 720))

    countdown_elapsed_time = time.time() - countdown_before_jip
    countdown_remaining_time = max(0, 10 - countdown_elapsed_time)

    if countdown_remaining_time <= 0:
        display_info_jip = True

    elapsed_time = time.time() - start_time_jip
    remaining_time = max(0, 70 - elapsed_time) #repetition_time_jip

    # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Starting: {int(countdown_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)
    if display_info_jip:
        img = detector_jip.find_Pose(img, False)
        pose_landmarks = detector_jip.get_pose_landmarks()
        drawings = detector_jip.pose_landmarks_drawings(img, pose_landmarks,  32, 28, 30, 26, 24, True)
        drawings2 = detector_jip.pose_landmarks_drawings(img, pose_landmarks, 31, 27, 29, 25, 23, True)

        if pose_landmarks:
            left_foot_lift_off_count_jip, right_foot_lift_off_count_jip = detector_jip.detect_feet_lift_off(pose_landmarks, threshold=0.80)

            per_down_left_jip = np.interp(left_foot_lift_off_count_jip, (0, 1), (100, 0))
            bar_down_left_jip = np.interp(left_foot_lift_off_count_jip, (0, 1), (480, 680))

            per_down_right_jip= np.interp(right_foot_lift_off_count_jip, (0, 1), (100, 0))
            bar_down_right_jip= np.interp(right_foot_lift_off_count_jip, (0, 1), (480, 680))


            if per_down_left_jip == 100 or per_down_right_jip == 100:
                color_leg_jip = (0, 255, 0)
     
            if left_foot_lift_off_count_jip == 1:
                if dir_left_jip == 0 and counter_left_jip <= 60:
                    counter_left_jip += 1
                    if counter_left_jip == 60:
                        dir_left_jip = 0
                    else:
                        dir_left_jip = 1
            else: 
                if dir_left_jip == 1:
                    dir_left_jip = 0

            if right_foot_lift_off_count_jip == 1:
                if dir_right_jip == 0 and counter_right_jip <= 60:
                    counter_right_jip += 1
                    if counter_right_jip == 60:
                        dir_right_jip = 0
                    else:
                        dir_right_jip = 1
            else: 
                if dir_right_jip == 1:
                    dir_right_jip = 0

        # label
        cvzone.putTextRect(img, 'Jogging in Place', [450, 30], thickness=2, border=2, scale=2) 

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # RIGHT LEG
        cv2.putText(img, f"R {int(per_down_right_jip)}%", (24, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 480), (50, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_down_right_jip)), (50, 680), color_leg_jip, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_down_left_jip)}%", (962, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 480), (995, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_down_left_jip)), (995, 680), color_leg_jip, -1)

    # Counter for the right foot
    cv2.rectangle(img, (20, 20), (200, 130), (0, 0, 255), -1)  # Adjusted rectangle shape
    cv2.putText(img, f"{int(counter_right_jip)}/60", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    # Counter for the left foot
    cv2.rectangle(img, (210, 20), (390, 130), (255, 0, 0), -1)  # Adjusted rectangle shape and coordinates
    cv2.putText(img, f"{int(counter_left_jip)}/60", (220, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [345, 30], thickness=2, border=2, scale=2.5)
        display_info_jip = False
        exercise_mode = "rest_jip"
        rest_jip_start_time = time.time()
        

    if counter_right_jip == 60 and counter_left_jip == 60:
        cvzone.putTextRect(img, 'All Repetitions Completed', [345, 30], thickness=2, border=2, scale=2.5)
        display_info_jip = False
        exercise_mode = "rest_jip"
        rest_jip_start_time = time.time()
    return img


def rest_jip(img):
    global exercise_mode, rest_jip_start_time, start_time_jip_set2
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_jip_start_time
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "joginplace_set2"
        start_time_jip_set2 = time.time()
    return img

def detect_jip_set2(img):
    global left_foot_lift_off_count_jip_set2, right_foot_lift_off_count_jip_set2, counter_left_jip_set2, counter_right_jip_set2, per_down_right_jip_set2, bar_down_right_jip_set2, per_down_left_jip_set2, bar_down_left_jip_set2, dir_left_jip_set2, dir_right_jip_set2, start_time_jip_set2, repetition_time_jip_set2, display_info_jip_set2, color_leg_jip_set2, rest_jip_start_time_set2, drawings, drawings2, exercise_mode

    img = cv2.resize(img, (1280, 720))
    elapsed_time = time.time() - start_time_jip_set2
    remaining_time = max(0, 60 - elapsed_time) #repetition_time_jip

    if display_info_jip_set2:
        img = detector_jip.find_Pose(img, False)
        pose_landmarks = detector_jip.get_pose_landmarks()
        drawings = detector_jip.pose_landmarks_drawings(img, pose_landmarks,  32, 28, 30, 26, 24, True)
        drawings2 = detector_jip.pose_landmarks_drawings(img, pose_landmarks, 31, 27, 29, 25, 23, True)

        if pose_landmarks:
            left_foot_lift_off_count_jip_set2, right_foot_lift_off_count_jip_set2 = detector_jip.detect_feet_lift_off(pose_landmarks, threshold=0.80)

            per_down_left_jip_set2 = np.interp(left_foot_lift_off_count_jip_set2, (0, 1), (100, 0))
            bar_down_left_jip_set2 = np.interp(left_foot_lift_off_count_jip_set2, (0, 1), (480, 680))

            per_down_right_jip_set2= np.interp(right_foot_lift_off_count_jip_set2, (0, 1), (100, 0))
            bar_down_right_jip_set2= np.interp(right_foot_lift_off_count_jip_set2, (0, 1), (480, 680))


            if per_down_left_jip_set2 == 100 or per_down_right_jip_set2 == 100:
                color_leg_jip_set2 = (0, 255, 0)
     
            if left_foot_lift_off_count_jip_set2 == 1:
                if dir_left_jip_set2 == 0 and counter_left_jip_set2 <= 60:
                    counter_left_jip_set2 += 1
                    if counter_left_jip_set2 == 60:
                        dir_left_jip_set2 = 0
                    else:
                        dir_left_jip_set2 = 1
            else: 
                if dir_left_jip_set2 == 1:
                    dir_left_jip_set2 = 0

            if right_foot_lift_off_count_jip_set2 == 1:
                if dir_right_jip_set2 == 0 and counter_right_jip_set2 <= 60:
                    counter_right_jip_set2 += 1
                    if counter_right_jip_set2 == 60:
                        dir_right_jip_set2 = 0
                    else:
                        dir_right_jip_set2 = 1
            else: 
                if dir_right_jip_set2 == 1:
                    dir_right_jip_set2 = 0

        # label
        cvzone.putTextRect(img, 'Jogging in Place SET 2', [450, 30], thickness=2, border=2, scale=2) 

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # RIGHT LEG
        cv2.putText(img, f"R {int(per_down_right_jip_set2)}%", (24, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 480), (50, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_down_right_jip_set2)), (50, 680), color_leg_jip_set2, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_down_left_jip_set2)}%", (962, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 480), (995, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_down_left_jip_set2)), (995, 680), color_leg_jip_set2, -1)

    # Counter for the right foot
    cv2.rectangle(img, (20, 20), (200, 130), (0, 0, 255), -1)  # Adjusted rectangle shape
    cv2.putText(img, f"{int(counter_right_jip_set2)}/60", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    # Counter for the left foot
    cv2.rectangle(img, (210, 20), (390, 130), (255, 0, 0), -1)  # Adjusted rectangle shape and coordinates
    cv2.putText(img, f"{int(counter_left_jip_set2)}/60", (220, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [345, 30], thickness=2, border=2, scale=2.5)
        display_info_jip_set2 = False
        exercise_mode = "rest_jip_set2"
        rest_jip_start_time_set2 = time.time()

    if counter_right_jip_set2 == 60 and counter_left_jip_set2 == 60:
        cvzone.putTextRect(img, 'All Repetitions Completed', [345, 30], thickness=2, border=2, scale=2.5)
        display_info_jip_set2 = False
        exercise_mode = "rest_jip_set2"
        rest_jip_start_time_set2 = time.time()
    return img

def rest_jip_set2(img):
    global exercise_mode, rest_jip_start_time_set2, start_time_jip_set3
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_jip_start_time_set2
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "joginplace_set3"
        start_time_jip_set3 = time.time()
    return img 

def detect_jip_set3(img):
    global left_foot_lift_off_count_jip_set3, right_foot_lift_off_count_jip_set3, counter_left_jip_set3, counter_right_jip_set3, per_down_right_jip_set3, bar_down_right_jip_set3, per_down_left_jip_set3, bar_down_left_jip_set3, dir_left_jip_set3, dir_right_jip_set3, start_time_jip_set3, repetition_time_jip_set3, display_info_jip_set3, color_leg_jip_set3, rest_jip_start_time_set3, drawings, drawings2, exercise_mode

    img = cv2.resize(img, (1280, 720))
    elapsed_time = time.time() - start_time_jip_set3
    remaining_time = max(0, 60 - elapsed_time) #repetition_time_jip

    if display_info_jip_set3:
        img = detector_jip.find_Pose(img, False)
        pose_landmarks = detector_jip.get_pose_landmarks()
        drawings = detector_jip.pose_landmarks_drawings(img, pose_landmarks,  32, 28, 30, 26, 24, True)
        drawings2 = detector_jip.pose_landmarks_drawings(img, pose_landmarks, 31, 27, 29, 25, 23, True)

        if pose_landmarks:
            left_foot_lift_off_count_jip_set3, right_foot_lift_off_count_jip_set3 = detector_jip.detect_feet_lift_off(pose_landmarks, threshold=0.80)

            per_down_left_jip_set3 = np.interp(left_foot_lift_off_count_jip_set3, (0, 1), (100, 0))
            bar_down_left_jip_set3 = np.interp(left_foot_lift_off_count_jip_set3, (0, 1), (480, 680))

            per_down_right_jip_set3= np.interp(right_foot_lift_off_count_jip_set3, (0, 1), (100, 0))
            bar_down_right_jip_set3= np.interp(right_foot_lift_off_count_jip_set3, (0, 1), (480, 680))


            if per_down_left_jip_set3 == 100 or per_down_right_jip_set3 == 100:
                color_leg_jip_set3 = (0, 255, 0)
     
            if left_foot_lift_off_count_jip_set3 == 1:
                if dir_left_jip_set3 == 0 and counter_left_jip_set3 <= 60:
                    counter_left_jip_set3 += 1
                    if counter_left_jip_set3 == 60:
                        dir_left_jip_set3 = 0
                    else:
                        dir_left_jip_set3 = 1
            else: 
                if dir_left_jip_set3 == 1:
                    dir_left_jip_set3 = 0

            if right_foot_lift_off_count_jip_set3 == 1:
                if dir_right_jip_set3 == 0 and counter_right_jip_set3 <= 60:
                    counter_right_jip_set3 += 1
                    if counter_right_jip_set3 == 60:
                        dir_right_jip_set3 = 0
                    else:
                        dir_right_jip_set3 = 1
            else: 
                if dir_right_jip_set3 == 1:
                    dir_right_jip_set3 = 0

        # label
        cvzone.putTextRect(img, 'Jogging in Place SET 3', [450, 30], thickness=2, border=2, scale=2) 

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # RIGHT LEG
        cv2.putText(img, f"R {int(per_down_right_jip_set3)}%", (24, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 480), (50, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_down_right_jip_set3)), (50, 680), color_leg_jip_set3, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_down_left_jip_set3)}%", (962, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 480), (995, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_down_left_jip_set3)), (995, 680), color_leg_jip_set3, -1)

    # Counter for the right foot
    cv2.rectangle(img, (20, 20), (200, 130), (0, 0, 255), -1)  # Adjusted rectangle shape
    cv2.putText(img, f"{int(counter_right_jip_set3)}/60", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    # Counter for the left foot
    cv2.rectangle(img, (210, 20), (390, 130), (255, 0, 0), -1)  # Adjusted rectangle shape and coordinates
    cv2.putText(img, f"{int(counter_left_jip_set3)}/60", (220, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [345, 30], thickness=2, border=2, scale=2.5)
        display_info_jip_set3 = False
        exercise_mode = "rest_jip_set3"
        rest_jip_start_time_set3 = time.time()

    if counter_right_jip_set3 == 60 and counter_left_jip_set3 == 60:
        cvzone.putTextRect(img, 'All Repetitions Completed', [345, 30], thickness=2, border=2, scale=2.5)
        display_info_jip_set3 = False
        exercise_mode = "rest_jip_set3"
        rest_jip_start_time_set3 = time.time()
    return img 

def rest_jip_set3(img):
    global exercise_mode, rest_jip_start_time_set3, start_time_jumpingjacks
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_jip_start_time_set3
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "jumpingjacks"
        start_time_jumpingjacks = time.time()
    return img

def detect_jumpingjacks(img):
    global count_jumping_jacks, dir_jumping_jacks, start_time_jumpingjacks, repetition_time_jumpingjacks, display_info_jumpingjacks, per_left_arm_jumpingjacks, bar_left_arm_jumpingjacks, per_right_arm_jumpingjacks, bar_right_arm_jumpingjacks, per_down_left_jumpingjacks, per_down_right_jumpingjacks, bar_down_left_jumpingjacks, bar_down_right_jumpingjacks, leftwholearm_jumpingjacks, rightwholearm_jumpingjacks, distance_jumpingjacks, rest_jumpingjack_start_time, exercise_mode

    img = cv2.resize(img, (1280, 720))

    elapsed_time = time.time() - start_time_jumpingjacks
    remaining_time = max(0, 60 - elapsed_time)

    if display_info_jumpingjacks:  # Check if to display counter, bar, and percentage
        img = detector_JumpingJack.findPose(img, False)
        lmList_jumping_jacks = detector_JumpingJack.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_jumping_jacks) != 0:

            leftwholearm_jumpingjacks, rightwholearm_jumpingjacks, = detector_JumpingJack.UpperBodySwing(
                img, 23, 11, 13, 14, 12, 24, 15, 16, drawpoints= True)
            distance_jumpingjacks = detector_JumpingJack.findJumpingJack(img, 24, 26, 28, 23, 25, 27, drawpoints=True)  # Define landmark keypoints

            #Interpolate angle to percentage and position on screen
            per_left_arm_jumpingjacks = np.interp(leftwholearm_jumpingjacks, (200, 270), (100, 0))
            bar_left_arm_jumpingjacks = np.interp(leftwholearm_jumpingjacks, (210, 280), (200, 400))

            per_right_arm_jumpingjacks = np.interp(rightwholearm_jumpingjacks, (200, 270), (100, 0))
            bar_right_arm_jumpingjacks = np.interp(rightwholearm_jumpingjacks, (210, 280), (200, 400))


            per_down_left_jumpingjacks = np.interp(distance_jumpingjacks, (35, 180), (0, 100))
            bar_down_left_jumpingjacks = np.interp(distance_jumpingjacks, (35, 190), (680, 480))

            per_down_right_jumpingjacks= np.interp(distance_jumpingjacks, (35, 180), (0, 100))
            bar_down_right_jumpingjacks= np.interp(distance_jumpingjacks, (35, 190), (680, 480))


            if leftwholearm_jumpingjacks <= 220 and rightwholearm_jumpingjacks  <= 220 and distance_jumpingjacks >= 180:
                if dir_jumping_jacks == 0:
                    count_jumping_jacks += 0.5
                    dir_jumping_jacks = 1 
                    
            elif leftwholearm_jumpingjacks >= 270 and rightwholearm_jumpingjacks >= 270 and distance_jumpingjacks <= 35:
                if dir_jumping_jacks == 1:
                    count_jumping_jacks += 0.5
                    dir_jumping_jacks = 0  



        cvzone.putTextRect(img, 'Ai Jumping Jack', [345, 30], thickness=2, border=2, scale=2.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color


        #Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # ARM RIGHT
        cv2.putText(img, f"R {int(per_right_arm_jumpingjacks)}%", (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_arm_jumpingjacks)), (50, 400), (0, 0, 255), -1)

        # ARM LEFT
        cv2.putText(img, f"L {int(per_left_arm_jumpingjacks)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_arm_jumpingjacks)), (995, 400), (0, 0, 255), -1)

        # RIGHT LEG
        cv2.putText(img, f"R {int(per_down_right_jumpingjacks)}%", (24, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 480), (50, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_down_right_jumpingjacks)), (50, 680), (0, 0, 255), -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_down_left_jumpingjacks)}%", (962, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 480), (995, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_down_left_jumpingjacks)), (995, 680), (0, 0, 255), -1)

        if leftwholearm_jumpingjacks <= 210:
            cv2.rectangle(img, (952, int(bar_left_arm_jumpingjacks)), (995, 400), (0, 255, 0), -1)

        if rightwholearm_jumpingjacks <= 210:
            cv2.rectangle(img, (8, int(bar_right_arm_jumpingjacks)), (50, 400), (0, 255, 0), -1)

        if distance_jumpingjacks >= 180:
            cv2.rectangle(img, (952, int(bar_down_left_jumpingjacks)), (995, 680), (0, 255, 0), -1)
        
        if distance_jumpingjacks >= 180:
            cv2.rectangle(img, (8, int(bar_down_right_jumpingjacks)), (50, 680), (0, 255, 0), -1)

    cv2.rectangle(img, (20, 10), (140, 120), (255, 0, 0), -1)
    cv2.putText(img, f"{int(count_jumping_jacks)}/5", (30, 80), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [370, 30], thickness=2, border=2, scale=2.5)
        display_info_jumpingjacks = False
        exercise_mode = "rest_jumpingjacks"
        rest_jumpingjack_start_time = time.time()

    if count_jumping_jacks >= 5:  # Assuming 10 jumping jacks for demonstration
        cvzone.putTextRect(img, 'Exercise Complete', [370, 30], thickness=2, border=2, scale=2.5)
        display_info_jumpingjacks = False
        exercise_mode = "rest_jumpingjacks"
        rest_jumpingjack_start_time = time.time()
    return img

def rest_jumpingjacks(img):
    global exercise_mode, rest_jumpingjack_start_time, start_time_jumpingjacks_set2
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_jumpingjack_start_time
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "jumpingjacks_set2"
        start_time_jumpingjacks_set2 = time.time()
    return img 

def detect_jumpingjacks_set2(img):
    global count_jumping_jacks_set2, dir_jumping_jacks_set2, start_time_jumpingjacks_set2, repetition_time_jumpingjacks_set2, display_info_jumpingjacks_set2, per_left_arm_jumpingjacks_set2, bar_left_arm_jumpingjacks_set2, per_right_arm_jumpingjacks_set2, bar_right_arm_jumpingjacks_set2, per_down_left_jumpingjacks_set2, per_down_right_jumpingjacks_set2, bar_down_left_jumpingjacks_set2, bar_down_right_jumpingjacks_set2, leftwholearm_jumpingjacks_set2, rightwholearm_jumpingjacks_set2, distance_jumpingjacks_set2, rest_jumpingjack_start_time_set2, exercise_mode

    img = cv2.resize(img, (1280, 720))

    elapsed_time = time.time() - start_time_jumpingjacks_set2
    remaining_time = max(0, 60 - elapsed_time)

    if display_info_jumpingjacks_set2:  # Check if to display counter, bar, and percentage
        img = detector_JumpingJack.findPose(img, False)
        lmList_jumping_jacks = detector_JumpingJack.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_jumping_jacks) != 0:

            leftwholearm_jumpingjacks_set2, rightwholearm_jumpingjacks_set2, = detector_JumpingJack.UpperBodySwing(
                img, 23, 11, 13, 14, 12, 24, 15, 16, drawpoints= True)
            distance_jumpingjacks_set2 = detector_JumpingJack.findJumpingJack(img, 24, 26, 28, 23, 25, 27, drawpoints=True)  # Define landmark keypoints

            #Interpolate angle to percentage and position on screen
            per_left_arm_jumpingjacks_set2 = np.interp(leftwholearm_jumpingjacks_set2, (200, 270), (100, 0))
            bar_left_arm_jumpingjacks_set2 = np.interp(leftwholearm_jumpingjacks_set2, (210, 280), (200, 400))

            per_right_arm_jumpingjacks_set2 = np.interp(rightwholearm_jumpingjacks_set2, (200, 270), (100, 0))
            bar_right_arm_jumpingjacks_set2 = np.interp(rightwholearm_jumpingjacks_set2, (210, 280), (200, 400))


            per_down_left_jumpingjacks_set2 = np.interp(distance_jumpingjacks_set2, (35, 180), (0, 100))
            bar_down_left_jumpingjacks_set2 = np.interp(distance_jumpingjacks_set2, (35, 190), (680, 480))

            per_down_right_jumpingjacks_set2= np.interp(distance_jumpingjacks_set2, (35, 180), (0, 100))
            bar_down_right_jumpingjacks_set2= np.interp(distance_jumpingjacks_set2, (35, 190), (680, 480))


            if leftwholearm_jumpingjacks_set2 <= 220 and rightwholearm_jumpingjacks_set2  <= 220 and distance_jumpingjacks_set2 >= 180:
                if dir_jumping_jacks_set2 == 0:
                    count_jumping_jacks_set2 += 0.5
                    dir_jumping_jacks_set2 = 1 
                    
            elif leftwholearm_jumpingjacks_set2 >= 270 and rightwholearm_jumpingjacks_set2 >= 270 and distance_jumpingjacks_set2 <= 35:
                if dir_jumping_jacks_set2 == 1:
                    count_jumping_jacks_set2 += 0.5
                    dir_jumping_jacks_set2 = 0  



        cvzone.putTextRect(img, 'Ai Jumping Jack SET 2', [345, 30], thickness=2, border=2, scale=2.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color


        #Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # ARM RIGHT
        cv2.putText(img, f"R {int(per_right_arm_jumpingjacks_set2)}%", (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_arm_jumpingjacks_set2)), (50, 400), (0, 0, 255), -1)

        # ARM LEFT
        cv2.putText(img, f"L {int(per_left_arm_jumpingjacks_set2)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_arm_jumpingjacks_set2)), (995, 400), (0, 0, 255), -1)

        # RIGHT LEG
        cv2.putText(img, f"R {int(per_down_right_jumpingjacks_set2)}%", (24, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 480), (50, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_down_right_jumpingjacks_set2)), (50, 680), (0, 0, 255), -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_down_left_jumpingjacks_set2)}%", (962, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 480), (995, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_down_left_jumpingjacks_set2)), (995, 680), (0, 0, 255), -1)

        if leftwholearm_jumpingjacks_set2 <= 210:
            cv2.rectangle(img, (952, int(bar_left_arm_jumpingjacks_set2)), (995, 400), (0, 255, 0), -1)

        if rightwholearm_jumpingjacks_set2 <= 210:
            cv2.rectangle(img, (8, int(bar_right_arm_jumpingjacks_set2)), (50, 400), (0, 255, 0), -1)

        if distance_jumpingjacks_set2 >= 180:
            cv2.rectangle(img, (952, int(bar_down_left_jumpingjacks_set2)), (995, 680), (0, 255, 0), -1)
        
        if distance_jumpingjacks_set2 >= 180:
            cv2.rectangle(img, (8, int(bar_down_right_jumpingjacks_set2)), (50, 680), (0, 255, 0), -1)

    cv2.rectangle(img, (20, 10), (140, 120), (255, 0, 0), -1)
    cv2.putText(img, f"{int(count_jumping_jacks_set2)}/5", (30, 80), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [370, 30], thickness=2, border=2, scale=2.5)
        display_info_jumpingjacks_set2 = False
        exercise_mode = "rest_jumpingjacks_set2"
        rest_jumpingjack_start_time_set2 = time.time()

    if count_jumping_jacks_set2 >= 5:  # Assuming 10 jumping jacks for demonstration
        cvzone.putTextRect(img, 'Exercise Complete', [370, 30], thickness=2, border=2, scale=2.5)
        display_info_jumpingjacks_set2 = False
        exercise_mode = "rest_jumpingjacks_set2"
        rest_jumpingjack_start_time_set2 = time.time()
    return img

def rest_jumpingjacks_set2(img):
    global exercise_mode, rest_jumpingjack_start_time_set2, start_time_jumpingjacks_set3
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_jumpingjack_start_time_set2
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "jumpingjacks_set3"
        start_time_jumpingjacks_set3 = time.time()
    return img

def detect_jumpingjacks_set3(img):
    global count_jumping_jacks_set3, dir_jumping_jacks_set3, start_time_jumpingjacks_set3, repetition_time_jumpingjacks_set3, display_info_jumpingjacks_set3, per_left_arm_jumpingjacks_set3, bar_left_arm_jumpingjacks_set3, per_right_arm_jumpingjacks_set3, bar_right_arm_jumpingjacks_set3, per_down_left_jumpingjacks_set3, per_down_right_jumpingjacks_set3, bar_down_left_jumpingjacks_set3, bar_down_right_jumpingjacks_set3, leftwholearm_jumpingjacks_set3, rightwholearm_jumpingjacks_set3, distance_jumpingjacks_set3, rest_jumpingjack_start_time_set3, exercise_mode

    img = cv2.resize(img, (1280, 720))

    elapsed_time = time.time() - start_time_jumpingjacks_set3
    remaining_time = max(0, 60 - elapsed_time)

    if display_info_jumpingjacks_set3:  # Check if to display counter, bar, and percentage
        img = detector_JumpingJack.findPose(img, False)
        lmList_jumping_jacks = detector_JumpingJack.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_jumping_jacks) != 0:

            leftwholearm_jumpingjacks_set3, rightwholearm_jumpingjacks_set3, = detector_JumpingJack.UpperBodySwing(
                img, 23, 11, 13, 14, 12, 24, 15, 16, drawpoints= True)
            distance_jumpingjacks_set3 = detector_JumpingJack.findJumpingJack(img, 24, 26, 28, 23, 25, 27, drawpoints=True)  # Define landmark keypoints

            #Interpolate angle to percentage and position on screen
            per_left_arm_jumpingjacks_set3 = np.interp(leftwholearm_jumpingjacks_set3, (200, 270), (100, 0))
            bar_left_arm_jumpingjacks_set3 = np.interp(leftwholearm_jumpingjacks_set3, (210, 280), (200, 400))

            per_right_arm_jumpingjacks_set3 = np.interp(rightwholearm_jumpingjacks_set3, (200, 270), (100, 0))
            bar_right_arm_jumpingjacks_set3 = np.interp(rightwholearm_jumpingjacks_set3, (210, 280), (200, 400))


            per_down_left_jumpingjacks_set3 = np.interp(distance_jumpingjacks_set3, (35, 180), (0, 100))
            bar_down_left_jumpingjacks_set3 = np.interp(distance_jumpingjacks_set3, (35, 190), (680, 480))

            per_down_right_jumpingjacks_set3= np.interp(distance_jumpingjacks_set3, (35, 180), (0, 100))
            bar_down_right_jumpingjacks_set3= np.interp(distance_jumpingjacks_set3, (35, 190), (680, 480))


            if leftwholearm_jumpingjacks_set3 <= 220 and rightwholearm_jumpingjacks_set3  <= 220 and distance_jumpingjacks_set3 >= 180:
                if dir_jumping_jacks_set3 == 0:
                    count_jumping_jacks_set3 += 0.5
                    dir_jumping_jacks_set3 = 1 
                    
            elif leftwholearm_jumpingjacks_set3 >= 270 and rightwholearm_jumpingjacks_set3 >= 270 and distance_jumpingjacks_set3 <= 35:
                if dir_jumping_jacks_set3 == 1:
                    count_jumping_jacks_set3 += 0.5
                    dir_jumping_jacks_set3 = 0  



        cvzone.putTextRect(img, 'Ai Jumping Jack SET 3', [345, 30], thickness=2, border=2, scale=2.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color


        #Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # ARM RIGHT
        cv2.putText(img, f"R {int(per_right_arm_jumpingjacks_set3)}%", (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_arm_jumpingjacks_set3)), (50, 400), (0, 0, 255), -1)

        # ARM LEFT
        cv2.putText(img, f"L {int(per_left_arm_jumpingjacks_set3)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_arm_jumpingjacks_set3)), (995, 400), (0, 0, 255), -1)

        # RIGHT LEG
        cv2.putText(img, f"R {int(per_down_right_jumpingjacks_set3)}%", (24, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 480), (50, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_down_right_jumpingjacks_set3)), (50, 680), (0, 0, 255), -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_down_left_jumpingjacks_set3)}%", (962, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 480), (995, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_down_left_jumpingjacks_set3)), (995, 680), (0, 0, 255), -1)

        if leftwholearm_jumpingjacks_set3 <= 210:
            cv2.rectangle(img, (952, int(bar_left_arm_jumpingjacks_set3)), (995, 400), (0, 255, 0), -1)

        if rightwholearm_jumpingjacks_set3 <= 210:
            cv2.rectangle(img, (8, int(bar_right_arm_jumpingjacks_set3)), (50, 400), (0, 255, 0), -1)

        if distance_jumpingjacks_set3 >= 180:
            cv2.rectangle(img, (952, int(bar_down_left_jumpingjacks_set3)), (995, 680), (0, 255, 0), -1)
        
        if distance_jumpingjacks_set3 >= 180:
            cv2.rectangle(img, (8, int(bar_down_right_jumpingjacks_set3)), (50, 680), (0, 255, 0), -1)

    cv2.rectangle(img, (20, 10), (140, 120), (255, 0, 0), -1)
    cv2.putText(img, f"{int(count_jumping_jacks_set3)}/5", (30, 80), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [370, 30], thickness=2, border=2, scale=2.5)
        display_info_jumpingjacks_set3 = False
        exercise_mode = "rest_jumpingjacks_set3"
        rest_jumpingjack_start_time_set3 = time.time()

    if count_jumping_jacks_set3 >= 5:  # Assuming 10 jumping jacks for demonstration
        cvzone.putTextRect(img, 'Exercise Complete', [370, 30], thickness=2, border=2, scale=2.5)
        display_info_jumpingjacks_set3 = False
        exercise_mode = "rest_jumpingjacks_set3"
        rest_jumpingjack_start_time_set3 = time.time()
    return img

def rest_jumpingjacks_set3(img):
    global exercise_mode, rest_jumpingjack_start_time_set3, start_time_buttkick
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_jumpingjack_start_time_set3
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "buttkick"
        start_time_buttkick = time.time()
    return img

def detect_buttkick(img):
    global count_alternating_right_lunge_buttkick, count_alternating_left_lunge_buttkick, dir_alternating_left_lunge_buttkick, dir_alternating_right_lunge_buttkick, start_time_buttkick, repetition_time_buttkick, display_info_buttkick, per_left_leg_buttkick, bar_left_leg_buttkick, per_right_leg_buttkick, bar_right_leg_buttkick, leftleg_buttkick, rightleg_buttkick, right_buttkick, left_buttkick, cooldown_duration_buttkick, cooldown_timer_buttkick, color_left_leg_buttkick, color_right_leg_buttkick, rest_buttkick_start_time, orientation, orientation2, exercise_mode

    img = cv2.resize(img, (1280, 720))

    elapsed_time = time.time() - start_time_buttkick
    remaining_time = max(0, 60 - elapsed_time)

    if display_info_buttkick:  # Check if to display counter, bar, and percentage
        img = detector_buttkick.findPose(img, False)
        lmList_jumping_jacks = detector_buttkick.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_jumping_jacks) != 0:

            # Right and Left keypoints
            rightleg_buttkick, orientation = detector_buttkick.ButtKick(img, 24, 26, 28, True)
            leftleg_buttkick, orientation2 = detector_buttkick.ButtKick(img, 23, 25, 27, True)

            if cooldown_timer_buttkick > 0:
                cooldown_timer_buttkick -= 1

            
           

            #print(orientation, orientation2)
            if orientation == 'right' and orientation2 == 'right':
                    
                    per_right_leg_buttkick = np.interp(rightleg_buttkick, (90, 170), (100, 0))
                    bar_right_leg_buttkick = np.interp(rightleg_buttkick, (90, 170), (480, 680))
                    per_left_leg_buttkick = np.interp(leftleg_buttkick, (90, 170), (100, 0))
                    bar_left_leg_buttkick = np.interp(leftleg_buttkick, (90, 170), (480, 680))

                    if int(per_left_leg_buttkick) == 100:
                        color_left_leg_buttkick = (0, 255, 0)  # Change color of left leg bar to green
                    elif int(per_right_leg_buttkick) == 100:
                        color_right_leg_buttkick = (0, 255, 0)
                    else:
                        color_left_leg_buttkick = (0, 0, 255)  # Keep color of left leg bar as red
                        color_right_leg_buttkick = (0, 0, 255)

                    if rightleg_buttkick <= 90:
                        if dir_alternating_right_lunge_buttkick == 0 and count_alternating_right_lunge_buttkick <= 25:
                            count_alternating_right_lunge_buttkick += 0.5
                            if count_alternating_right_lunge_buttkick == 25:
                                dir_alternating_right_lunge_buttkick = 0
                            else:
                                dir_alternating_right_lunge_buttkick = 1
                                cooldown_timer_buttkick = cooldown_duration_buttkick
                    elif rightleg_buttkick >= 150:
                        if dir_alternating_right_lunge_buttkick == 1 and count_alternating_right_lunge_buttkick <= 25:
                            count_alternating_right_lunge_buttkick += 0.5
                            if count_alternating_right_lunge_buttkick == 25:
                                dir_alternating_right_lunge_buttkick = 1
                            else:
                                dir_alternating_right_lunge_buttkick = 0
                                cooldown_timer_buttkick = cooldown_duration_buttkick
                    
                    if leftleg_buttkick <= 90:
                        if dir_alternating_left_lunge_buttkick == 0 and count_alternating_left_lunge_buttkick <= 25:
                            count_alternating_left_lunge_buttkick += 0.5
                            if count_alternating_left_lunge_buttkick == 25:
                                dir_alternating_left_lunge_buttkick = 0
                            else:
                                dir_alternating_left_lunge_buttkick = 1
                                cooldown_timer_buttkick = cooldown_duration_buttkick
                    elif leftleg_buttkick >= 150:
                        if dir_alternating_left_lunge_buttkick == 1 and count_alternating_left_lunge_buttkick <= 25:
                            count_alternating_left_lunge_buttkick += 0.5
                            if count_alternating_left_lunge_buttkick == 25:
                                dir_alternating_left_lunge_buttkick = 1
                            else:
                                dir_alternating_left_lunge_buttkick = 0
                                cooldown_timer_buttkick = cooldown_duration_buttkick


            elif orientation =='left' and orientation2 == 'left':
                if leftleg_buttkick is not None and rightleg_buttkick is not None:
                    per_right_leg_buttkick = np.interp(rightleg_buttkick, (190, 270), (0, 100))
                    bar_right_leg_buttkick = np.interp(rightleg_buttkick, (190, 270), (680, 480))
                    per_left_leg_buttkick = np.interp(leftleg_buttkick, (190, 270), (0, 100))
                    bar_left_leg_buttkick = np.interp(leftleg_buttkick, (190, 270), (680, 480))

                    #print("R: ", rightleg) #"L: ", leftleg
                    if int(per_left_leg_buttkick) == 100:
                        color_left_leg_buttkick = (0, 255, 0)  # Change color of left leg bar to green
                    elif int(per_right_leg_buttkick) == 100:
                        color_right_leg_buttkick = (0, 255, 0)
                    else:
                        color_left_leg_buttkick = (0, 0, 255)  # Keep color of left leg bar as red
                        color_right_leg_buttkick = (0, 0, 255)
              
                    if rightleg_buttkick >= 270:
                        if dir_alternating_right_lunge_buttkick == 0 and count_alternating_right_lunge_buttkick <= 25:
                            count_alternating_right_lunge_buttkick += 0.5
                            if count_alternating_right_lunge_buttkick == 25:
                                dir_alternating_right_lunge_buttkick = 0
                            else:
                                dir_alternating_right_lunge_buttkick = 1
                                cooldown_timer_buttkick = cooldown_duration_buttkick
                    elif rightleg_buttkick <= 200:
                        if dir_alternating_right_lunge_buttkick == 1 and count_alternating_right_lunge_buttkick <= 25:
                            count_alternating_right_lunge_buttkick += 0.5
                            if count_alternating_right_lunge_buttkick == 25:
                                dir_alternating_right_lunge_buttkick = 1
                            else:
                                dir_alternating_right_lunge_buttkick = 0
                                cooldown_timer_buttkick = cooldown_duration_buttkick

                    if leftleg_buttkick >= 270:
                        
                        if dir_alternating_left_lunge_buttkick == 0 and count_alternating_left_lunge_buttkick <= 25:
                            count_alternating_left_lunge_buttkick += 0.5
                            if count_alternating_left_lunge_buttkick == 25:
                                dir_alternating_left_lunge_buttkick = 0
                            else:
                                dir_alternating_left_lunge_buttkick = 1
                                cooldown_timer_buttkick = cooldown_duration_buttkick
                    elif leftleg_buttkick <= 200:
                        if dir_alternating_left_lunge_buttkick == 1 and count_alternating_left_lunge_buttkick <= 25:
                            count_alternating_left_lunge_buttkick += 0.5
                            if count_alternating_left_lunge_buttkick == 25:
                                dir_alternating_left_lunge_buttkick = 1
                            else:
                                dir_alternating_left_lunge_buttkick = 0
                                cooldown_timer_buttkick = cooldown_duration_buttkick

            elif orientation == 'front' and orientation2 == 'front':
                    
                    per_right_leg_buttkick = np.interp(rightleg_buttkick, (100, 200), (100, 0))
                    bar_right_leg_buttkick = np.interp(rightleg_buttkick, (100, 200), (480, 680))
                    per_left_leg_buttkick = np.interp(leftleg_buttkick, (100, 200), (100, 0))
                    bar_left_leg_buttkick = np.interp(leftleg_buttkick, (100, 200), (480, 680))

                    if int(per_left_leg_buttkick) == 100:
                        color_left_leg_buttkick = (0, 255, 0)  # Change color of left leg bar to green
                    elif int(per_right_leg_buttkick) == 100:
                        color_right_leg_buttkick = (0, 255, 0)
                    else:
                        color_left_leg_buttkick = (0, 0, 255)  # Keep color of left leg bar as red
                        color_right_leg_buttkick = (0, 0, 255)  # Keep color of right leg bar as red

                    if rightleg_buttkick <= 90:
                        if dir_alternating_right_lunge_buttkick == 0 and count_alternating_right_lunge_buttkick <= 25:
                            count_alternating_right_lunge_buttkick += 0.5
                            if count_alternating_right_lunge_buttkick == 25:
                                dir_alternating_right_lunge_buttkick = 0
                            else:
                                dir_alternating_right_lunge_buttkick = 1
                                cooldown_timer_buttkick = cooldown_duration_buttkick
                    else: 
                        if dir_alternating_right_lunge_buttkick == 1 and count_alternating_right_lunge_buttkick <= 25:
                            count_alternating_right_lunge_buttkick += 0.5
                            if count_alternating_right_lunge_buttkick == 25:
                                dir_alternating_right_lunge_buttkick = 1
                            else:
                                dir_alternating_right_lunge_buttkick = 0
                                cooldown_timer_buttkick = cooldown_duration_buttkick

                    if leftleg_buttkick <= 90:
                        if dir_alternating_left_lunge_buttkick == 0 and count_alternating_left_lunge_buttkick <= 25:
                            count_alternating_left_lunge_buttkick += 0.5
                            if count_alternating_left_lunge_buttkick == 25:
                                dir_alternating_left_lunge_buttkick = 0
                            else:
                                dir_alternating_left_lunge_buttkick = 1
                                cooldown_timer_buttkick = cooldown_duration_buttkick
                    else:
                        if dir_alternating_left_lunge_buttkick == 1 and count_alternating_left_lunge_buttkick <= 25:
                            count_alternating_left_lunge_buttkick += 0.5
                            if count_alternating_left_lunge_buttkick == 25:
                                dir_alternating_left_lunge_buttkick = 1
                            else:
                                dir_alternating_left_lunge_buttkick = 0
                                cooldown_timer_buttkick = cooldown_duration_buttkick

        cvzone.putTextRect(img, 'Buttkick Tracker', [470, 30], thickness=2, border=2, scale=2.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)
       
        # Orientation
        cv2.rectangle(img, (890, 100), (1180, 160), (0, 0, 255), -2)
        cv2.putText(img, f"Orientation: {orientation}", (900, 140), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)

        # RIGHT LEG
        cv2.putText(img, f"R {int(per_right_leg_buttkick)}%", (24, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 480), (50, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_leg_buttkick)), (50, 680), color_right_leg_buttkick, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_left_leg_buttkick)}%", (962, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 480), (995, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_leg_buttkick)), (995, 680), color_left_leg_buttkick, -1)

    # Counter 
    cv2.rectangle(img, (20, 20), (200, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(count_alternating_right_lunge_buttkick)}/25", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (210, 20), (390, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(count_alternating_left_lunge_buttkick)}/25", (220, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    # Timer
    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [345, 30], thickness=2, border=2, scale=2.5)
        display_info_buttkick = False
        exercise_mode = "rest_buttkick"
        rest_buttkick_start_time = time.time()

    # Repetition
    if count_alternating_left_lunge_buttkick >= 25:  # Assuming 10 jumping jacks for demonstration
        cvzone.putTextRect(img, 'Exercise Complete', [345, 30], thickness=2, border=2, scale=2.5)
        display_info_buttkick = False
        exercise_mode = "rest_buttkick"
        rest_buttkick_start_time = time.time()
    return img 

def rest_buttkick(img):
    global exercise_mode, rest_buttkick_start_time, start_time_buttkick_set2
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_buttkick_start_time
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "buttkick_set2"
        start_time_buttkick_set2 = time.time()
    return img

def detect_buttkick_set2(img):
    global count_alternating_right_lunge_buttkick_set2, count_alternating_left_lunge_buttkick_set2, dir_alternating_left_lunge_buttkick_set2, dir_alternating_right_lunge_buttkick_set2, start_time_buttkick_set2, repetition_time_buttkick_set2, display_info_buttkick_set2, per_left_leg_buttkick_set2, bar_left_leg_buttkick_set2, per_right_leg_buttkick_set2, bar_right_leg_buttkick_set2, leftleg_buttkick_set2, rightleg_buttkick_set2, right_buttkick_set2, left_buttkick_set2, cooldown_duration_buttkick_set2, cooldown_timer_buttkick_set2, color_left_leg_buttkick_set2, color_right_leg_buttkick_set2, rest_buttkick_start_time_set2, orientation, orientation2, exercise_mode

    img = cv2.resize(img, (1280, 720))

    elapsed_time = time.time() - start_time_buttkick_set2
    remaining_time = max(0, 60 - elapsed_time)

    if display_info_buttkick_set2:  # Check if to display counter, bar, and percentage
        img = detector_buttkick.findPose(img, False)
        lmList_jumping_jacks = detector_buttkick.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_jumping_jacks) != 0:

            # Right and Left keypoints
            rightleg_buttkick_set2, orientation = detector_buttkick.ButtKick(img, 24, 26, 28, True)
            leftleg_buttkick_set2, orientation2 = detector_buttkick.ButtKick(img, 23, 25, 27, True)

            if cooldown_timer_buttkick_set2 > 0:
                cooldown_timer_buttkick_set2 -= 1

            
           

            #print(orientation, orientation2)
            if orientation == 'right' and orientation2 == 'right':
                    
                    per_right_leg_buttkick_set2 = np.interp(rightleg_buttkick_set2, (90, 170), (100, 0))
                    bar_right_leg_buttkick_set2 = np.interp(rightleg_buttkick_set2, (90, 170), (480, 680))
                    per_left_leg_buttkick_set2 = np.interp(leftleg_buttkick_set2, (90, 170), (100, 0))
                    bar_left_leg_buttkick_set2 = np.interp(leftleg_buttkick_set2, (90, 170), (480, 680))

                    if int(per_left_leg_buttkick_set2) == 100:
                        color_left_leg_buttkick_set2 = (0, 255, 0)  # Change color of left leg bar to green
                    elif int(per_right_leg_buttkick_set2) == 100:
                        color_right_leg_buttkick_set2 = (0, 255, 0)
                    else:
                        color_left_leg_buttkick_set2 = (0, 0, 255)  # Keep color of left leg bar as red
                        color_right_leg_buttkick_set2 = (0, 0, 255)

                    if rightleg_buttkick_set2 <= 90:
                        if dir_alternating_right_lunge_buttkick_set2 == 0 and count_alternating_right_lunge_buttkick_set2 <= 25:
                            count_alternating_right_lunge_buttkick_set2 += 0.5
                            if count_alternating_right_lunge_buttkick_set2 == 25:
                                dir_alternating_right_lunge_buttkick_set2 = 0
                            else:
                                dir_alternating_right_lunge_buttkick_set2 = 1
                                cooldown_timer_buttkick_set2 = cooldown_duration_buttkick_set2
                    elif rightleg_buttkick_set2 >= 150:
                        if dir_alternating_right_lunge_buttkick_set2 == 1 and count_alternating_right_lunge_buttkick_set2 <= 25:
                            count_alternating_right_lunge_buttkick_set2 += 0.5
                            if count_alternating_right_lunge_buttkick_set2 == 25:
                                dir_alternating_right_lunge_buttkick_set2 = 1
                            else:
                                dir_alternating_right_lunge_buttkick_set2 = 0
                                cooldown_timer_buttkick_set2 = cooldown_duration_buttkick_set2
                    
                    if leftleg_buttkick_set2 <= 90:
                        if dir_alternating_left_lunge_buttkick_set2 == 0 and count_alternating_left_lunge_buttkick_set2 <= 25:
                            count_alternating_left_lunge_buttkick_set2 += 0.5
                            if count_alternating_left_lunge_buttkick_set2 == 25:
                                dir_alternating_left_lunge_buttkick_set2 = 0
                            else:
                                dir_alternating_left_lunge_buttkick_set2 = 1
                                cooldown_timer_buttkick_set2 = cooldown_duration_buttkick_set2
                    elif leftleg_buttkick_set2 >= 150:
                        if dir_alternating_left_lunge_buttkick_set2 == 1 and count_alternating_left_lunge_buttkick_set2 <= 25:
                            count_alternating_left_lunge_buttkick_set2 += 0.5
                            if count_alternating_left_lunge_buttkick_set2 == 25:
                                dir_alternating_left_lunge_buttkick_set2 = 1
                            else:
                                dir_alternating_left_lunge_buttkick_set2 = 0
                                cooldown_timer_buttkick_set2 = cooldown_duration_buttkick_set2


            elif orientation =='left' and orientation2 == 'left':
                if leftleg_buttkick_set2 is not None and rightleg_buttkick_set2 is not None:
                    per_right_leg_buttkick_set2 = np.interp(rightleg_buttkick_set2, (190, 270), (0, 100))
                    bar_right_leg_buttkick_set2 = np.interp(rightleg_buttkick_set2, (190, 270), (680, 480))
                    per_left_leg_buttkick_set2 = np.interp(leftleg_buttkick_set2, (190, 270), (0, 100))
                    bar_left_leg_buttkick_set2 = np.interp(leftleg_buttkick_set2, (190, 270), (680, 480))

                    #print("R: ", rightleg) #"L: ", leftleg
                    if int(per_left_leg_buttkick_set2) == 100:
                        color_left_leg_buttkick_set2 = (0, 255, 0)  # Change color of left leg bar to green
                    elif int(per_right_leg_buttkick_set2) == 100:
                        color_right_leg_buttkick_set2 = (0, 255, 0)
                    else:
                        color_left_leg_buttkick_set2 = (0, 0, 255)  # Keep color of left leg bar as red
                        color_right_leg_buttkick_set2 = (0, 0, 255)
              
                    if rightleg_buttkick_set2 >= 270:
                        if dir_alternating_right_lunge_buttkick_set2 == 0 and count_alternating_right_lunge_buttkick_set2 <= 25:
                            count_alternating_right_lunge_buttkick_set2 += 0.5
                            if count_alternating_right_lunge_buttkick_set2 == 25:
                                dir_alternating_right_lunge_buttkick_set2 = 0
                            else:
                                dir_alternating_right_lunge_buttkick_set2 = 1
                                cooldown_timer_buttkick_set2 = cooldown_duration_buttkick_set2
                    elif rightleg_buttkick_set2 <= 200:
                        if dir_alternating_right_lunge_buttkick_set2 == 1 and count_alternating_right_lunge_buttkick_set2 <= 25:
                            count_alternating_right_lunge_buttkick_set2 += 0.5
                            if count_alternating_right_lunge_buttkick_set2 == 25:
                                dir_alternating_right_lunge_buttkick_set2 = 1
                            else:
                                dir_alternating_right_lunge_buttkick_set2 = 0
                                cooldown_timer_buttkick_set2 = cooldown_duration_buttkick_set2

                    if leftleg_buttkick_set2 >= 270:
                        
                        if dir_alternating_left_lunge_buttkick_set2 == 0 and count_alternating_left_lunge_buttkick_set2 <= 25:
                            count_alternating_left_lunge_buttkick_set2 += 0.5
                            if count_alternating_left_lunge_buttkick_set2 == 25:
                                dir_alternating_left_lunge_buttkick_set2 = 0
                            else:
                                dir_alternating_left_lunge_buttkick_set2 = 1
                                cooldown_timer_buttkick_set2 = cooldown_duration_buttkick_set2
                    elif leftleg_buttkick_set2 <= 200:
                        if dir_alternating_left_lunge_buttkick_set2 == 1 and count_alternating_left_lunge_buttkick_set2 <= 25:
                            count_alternating_left_lunge_buttkick_set2 += 0.5
                            if count_alternating_left_lunge_buttkick_set2 == 25:
                                dir_alternating_left_lunge_buttkick_set2 = 1
                            else:
                                dir_alternating_left_lunge_buttkick_set2 = 0
                                cooldown_timer_buttkick_set2 = cooldown_duration_buttkick_set2

            elif orientation == 'front' and orientation2 == 'front':
                    
                    per_right_leg_buttkick_set2 = np.interp(rightleg_buttkick_set2, (100, 200), (100, 0))
                    bar_right_leg_buttkick_set2 = np.interp(rightleg_buttkick_set2, (100, 200), (480, 680))
                    per_left_leg_buttkick_set2 = np.interp(leftleg_buttkick_set2, (100, 200), (100, 0))
                    bar_left_leg_buttkick_set2 = np.interp(leftleg_buttkick_set2, (100, 200), (480, 680))

                    if int(per_left_leg_buttkick_set2) == 100:
                        color_left_leg_buttkick_set2 = (0, 255, 0)  # Change color of left leg bar to green
                    elif int(per_right_leg_buttkick_set2) == 100:
                        color_right_leg_buttkick_set2 = (0, 255, 0)
                    else:
                        color_left_leg_buttkick_set2 = (0, 0, 255)  # Keep color of left leg bar as red
                        color_right_leg_buttkick_set2 = (0, 0, 255)  # Keep color of right leg bar as red

                    if rightleg_buttkick_set2 <= 90:
                        if dir_alternating_right_lunge_buttkick_set2 == 0 and count_alternating_right_lunge_buttkick_set2 <= 25:
                            count_alternating_right_lunge_buttkick_set2 += 0.5
                            if count_alternating_right_lunge_buttkick_set2 == 25:
                                dir_alternating_right_lunge_buttkick_set2 = 0
                            else:
                                dir_alternating_right_lunge_buttkick_set2 = 1
                                cooldown_timer_buttkick_set2 = cooldown_duration_buttkick_set2
                    else: 
                        if dir_alternating_right_lunge_buttkick_set2 == 1 and count_alternating_right_lunge_buttkick_set2 <= 25:
                            count_alternating_right_lunge_buttkick_set2 += 0.5
                            if count_alternating_right_lunge_buttkick_set2 == 25:
                                dir_alternating_right_lunge_buttkick_set2 = 1
                            else:
                                dir_alternating_right_lunge_buttkick_set2 = 0
                                cooldown_timer_buttkick_set2 = cooldown_duration_buttkick_set2

                    if leftleg_buttkick_set2 <= 90:
                        if dir_alternating_left_lunge_buttkick_set2 == 0 and count_alternating_left_lunge_buttkick_set2 <= 25:
                            count_alternating_left_lunge_buttkick_set2 += 0.5
                            if count_alternating_left_lunge_buttkick_set2 == 25:
                                dir_alternating_left_lunge_buttkick_set2 = 0
                            else:
                                dir_alternating_left_lunge_buttkick_set2 = 1
                                cooldown_timer_buttkick_set2 = cooldown_duration_buttkick_set2
                    else:
                        if dir_alternating_left_lunge_buttkick_set2 == 1 and count_alternating_left_lunge_buttkick_set2 <= 25:
                            count_alternating_left_lunge_buttkick_set2 += 0.5
                            if count_alternating_left_lunge_buttkick_set2 == 25:
                                dir_alternating_left_lunge_buttkick_set2 = 1
                            else:
                                dir_alternating_left_lunge_buttkick_set2 = 0
                                cooldown_timer_buttkick_set2 = cooldown_duration_buttkick_set2

        cvzone.putTextRect(img, 'Buttkick SET 2', [470, 30], thickness=2, border=2, scale=2.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)
       
        # Orientation
        cv2.rectangle(img, (890, 100), (1180, 160), (0, 0, 255), -2)
        cv2.putText(img, f"Orientation: {orientation}", (900, 140), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)

        # RIGHT LEG
        cv2.putText(img, f"R {int(per_right_leg_buttkick_set2)}%", (24, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 480), (50, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_leg_buttkick_set2)), (50, 680), color_right_leg_buttkick_set2, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_left_leg_buttkick_set2)}%", (962, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 480), (995, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_leg_buttkick_set2)), (995, 680), color_left_leg_buttkick_set2, -1)

    # Counter 
    cv2.rectangle(img, (20, 20), (200, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(count_alternating_right_lunge_buttkick_set2)}/25", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (210, 20), (390, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(count_alternating_left_lunge_buttkick_set2)}/25", (220, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    # Timer
    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [345, 30], thickness=2, border=2, scale=2.5)
        display_info_buttkick_set2 = False
        exercise_mode = "rest_buttkick_set2"
        rest_buttkick_start_time_set2 = time.time()

    # Repetition
    if count_alternating_left_lunge_buttkick_set2 >= 25:  # Assuming 10 jumping jacks for demonstration
        cvzone.putTextRect(img, 'Exercise Complete', [345, 30], thickness=2, border=2, scale=2.5)
        display_info_buttkick_set2 = False
        exercise_mode = "rest_buttkick_set2"
        rest_buttkick_start_time_set2 = time.time()
    return img

def rest_buttkick_set2(img):
    global exercise_mode, rest_buttkick_start_time_set2, start_time_buttkick_set3
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_buttkick_start_time_set2
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "buttkick_set3"
        start_time_buttkick_set3 = time.time()
    return img

def detect_buttkick_set3(img):
    global count_alternating_right_lunge_buttkick_set3, count_alternating_left_lunge_buttkick_set3, dir_alternating_left_lunge_buttkick_set3, dir_alternating_right_lunge_buttkick_set3, start_time_buttkick_set3, repetition_time_buttkick_set3, display_info_buttkick_set3, per_left_leg_buttkick_set3, bar_left_leg_buttkick_set3, per_right_leg_buttkick_set3, bar_right_leg_buttkick_set3, leftleg_buttkick_set3, rightleg_buttkick,_set3, right_buttkick_set3, left_buttkick_set3, cooldown_duration_buttkick_set3, cooldown_timer_buttkick_set3, color_left_leg_buttkick_set3, color_right_leg_buttkick_set3, rest_buttkick_start_time_set3, orientation, orientation2, exercise_mode

    img = cv2.resize(img, (1280, 720))

    elapsed_time = time.time() - start_time_buttkick_set3
    remaining_time = max(0, 60 - elapsed_time)

    if display_info_buttkick_set3:  # Check if to display counter, bar, and percentage
        img = detector_buttkick.findPose(img, False)
        lmList_jumping_jacks = detector_buttkick.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_jumping_jacks) != 0:

            # Right and Left keypoints
            rightleg_buttkick_set3, orientation = detector_buttkick.ButtKick(img, 24, 26, 28, True)
            leftleg_buttkick_set3, orientation2 = detector_buttkick.ButtKick(img, 23, 25, 27, True)

            if cooldown_timer_buttkick_set3 > 0:
                cooldown_timer_buttkick_set3 -= 1

            
           

            #print(orientation, orientation2)
            if orientation == 'right' and orientation2 == 'right':
                    
                    per_right_leg_buttkick_set3 = np.interp(rightleg_buttkick_set3, (90, 170), (100, 0))
                    bar_right_leg_buttkick_set3 = np.interp(rightleg_buttkick_set3, (90, 170), (480, 680))
                    per_left_leg_buttkick_set3 = np.interp(leftleg_buttkick_set3, (90, 170), (100, 0))
                    bar_left_leg_buttkick_set3 = np.interp(leftleg_buttkick_set3, (90, 170), (480, 680))

                    if int(per_left_leg_buttkick_set3) == 100:
                        color_left_leg_buttkick_set3 = (0, 255, 0)  # Change color of left leg bar to green
                    elif int(per_right_leg_buttkick_set3) == 100:
                        color_right_leg_buttkick_set3 = (0, 255, 0)
                    else:
                        color_left_leg_buttkick_set3 = (0, 0, 255)  # Keep color of left leg bar as red
                        color_right_leg_buttkick_set3 = (0, 0, 255)

                    if rightleg_buttkick_set3 <= 90:
                        if dir_alternating_right_lunge_buttkick_set3 == 0 and count_alternating_right_lunge_buttkick_set3 <= 25:
                            count_alternating_right_lunge_buttkick_set3 += 0.5
                            if count_alternating_right_lunge_buttkick_set3 == 25:
                                dir_alternating_right_lunge_buttkick_set3
                            else:
                                dir_alternating_right_lunge_buttkick_set3 = 1
                                cooldown_timer_buttkick_set3 = cooldown_duration_buttkick_set3
                    elif rightleg_buttkick_set3 >= 150:
                        if dir_alternating_right_lunge_buttkick_set3 == 1 and count_alternating_right_lunge_buttkick_set3 <= 25:
                            count_alternating_right_lunge_buttkick_set3 += 0.5
                            if count_alternating_right_lunge_buttkick_set3 == 25:
                                dir_alternating_right_lunge_buttkick_set3 = 1
                            else:
                                dir_alternating_right_lunge_buttkick_set3 = 0
                                cooldown_timer_buttkick_set3 = cooldown_duration_buttkick_set3
                    
                    if leftleg_buttkick_set3 <= 90:
                        if dir_alternating_left_lunge_buttkick_set3 == 0 and count_alternating_left_lunge_buttkick_set3 <= 25:
                            count_alternating_left_lunge_buttkick_set3 += 0.5
                            if count_alternating_left_lunge_buttkick_set3 == 25:
                                dir_alternating_left_lunge_buttkick_set3 = 0
                            else:
                                dir_alternating_left_lunge_buttkick_set3 = 1
                                cooldown_timer_buttkick_set3 = cooldown_duration_buttkick_set3
                    elif leftleg_buttkick_set3 >= 150:
                        if dir_alternating_left_lunge_buttkick_set3 == 1 and count_alternating_left_lunge_buttkick_set3 <= 25:
                            count_alternating_left_lunge_buttkick_set3 += 0.5
                            if count_alternating_left_lunge_buttkick_set3 == 25:
                                dir_alternating_left_lunge_buttkick_set3 = 1
                            else:
                                dir_alternating_left_lunge_buttkick_set3 = 0
                                cooldown_timer_buttkick_set3 = cooldown_duration_buttkick_set3


            elif orientation =='left' and orientation2 == 'left':
                if leftleg_buttkick_set3 is not None and rightleg_buttkick_set3 is not None:
                    per_right_leg_buttkick_set3 = np.interp(rightleg_buttkick_set3, (190, 270), (0, 100))
                    bar_right_leg_buttkick_set3 = np.interp(rightleg_buttkick_set3, (190, 270), (680, 480))
                    per_left_leg_buttkick_set3 = np.interp(leftleg_buttkick_set3, (190, 270), (0, 100))
                    bar_left_leg_buttkick_set3 = np.interp(leftleg_buttkick_set3, (190, 270), (680, 480))

                    #print("R: ", rightleg) #"L: ", leftleg
                    if int(per_left_leg_buttkick_set3) == 100:
                        color_left_leg_buttkick_set3 = (0, 255, 0)  # Change color of left leg bar to green
                    elif int(per_right_leg_buttkick_set3) == 100:
                        color_right_leg_buttkick_set3 = (0, 255, 0)
                    else:
                        color_left_leg_buttkick_set3 = (0, 0, 255)  # Keep color of left leg bar as red
                        color_right_leg_buttkick_set3 = (0, 0, 255)
              
                    if rightleg_buttkick_set3 >= 270:
                        if dir_alternating_right_lunge_buttkick_set3 == 0 and count_alternating_right_lunge_buttkick_set3 <= 25:
                            count_alternating_right_lunge_buttkick_set3 += 0.5
                            if count_alternating_right_lunge_buttkick_set3 == 25:
                                dir_alternating_right_lunge_buttkick_set3 = 0
                            else:
                                dir_alternating_right_lunge_buttkick_set3 = 1
                                cooldown_timer_buttkick_set3 = cooldown_duration_buttkick_set3
                    elif rightleg_buttkick_set3 <= 200:
                        if dir_alternating_right_lunge_buttkick_set3 == 1 and count_alternating_right_lunge_buttkick_set3 <= 25:
                            count_alternating_right_lunge_buttkick_set3 += 0.5
                            if count_alternating_right_lunge_buttkick_set3 == 25:
                                dir_alternating_right_lunge_buttkick_set3 = 1
                            else:
                                dir_alternating_right_lunge_buttkick_set3 = 0
                                cooldown_timer_buttkick_set3 = cooldown_duration_buttkick_set3

                    if leftleg_buttkick_set3 >= 270:
                        
                        if dir_alternating_left_lunge_buttkick_set3 == 0 and count_alternating_left_lunge_buttkick_set3 <= 25:
                            count_alternating_left_lunge_buttkick_set3 += 0.5
                            if count_alternating_left_lunge_buttkick_set3 == 25:
                                dir_alternating_left_lunge_buttkick_set3 = 0
                            else:
                                dir_alternating_left_lunge_buttkick_set3 = 1
                                cooldown_timer_buttkick_set3 = cooldown_duration_buttkick_set3
                    elif leftleg_buttkick_set3 <= 200:
                        if dir_alternating_left_lunge_buttkick_set3 == 1 and count_alternating_left_lunge_buttkick_set3 <= 25:
                            count_alternating_left_lunge_buttkick_set3 += 0.5
                            if count_alternating_left_lunge_buttkick_set3 == 25:
                                dir_alternating_left_lunge_buttkick_set3 = 1
                            else:
                                dir_alternating_left_lunge_buttkick_set3 = 0
                                cooldown_timer_buttkick_set3 = cooldown_duration_buttkick_set3

            elif orientation == 'front' and orientation2 == 'front':
                    
                    per_right_leg_buttkick_set3 = np.interp(rightleg_buttkick_set3, (100, 200), (100, 0))
                    bar_right_leg_buttkick_set3 = np.interp(rightleg_buttkick_set3, (100, 200), (480, 680))
                    per_left_leg_buttkick_set3 = np.interp(leftleg_buttkick_set3, (100, 200), (100, 0))
                    bar_left_leg_buttkick_set3 = np.interp(leftleg_buttkick_set3, (100, 200), (480, 680))

                    if int(per_left_leg_buttkick_set3) == 100:
                        color_left_leg_buttkick_set3 = (0, 255, 0)  # Change color of left leg bar to green
                    elif int(per_right_leg_buttkick_set3) == 100:
                        color_right_leg_buttkick_set3 = (0, 255, 0)
                    else:
                        color_left_leg_buttkick_set3 = (0, 0, 255)  # Keep color of left leg bar as red
                        color_right_leg_buttkick_set3 = (0, 0, 255)  # Keep color of right leg bar as red

                    if rightleg_buttkick_set3 <= 90:
                        if dir_alternating_right_lunge_buttkick_set3 == 0 and count_alternating_right_lunge_buttkick_set3 <= 25:
                            count_alternating_right_lunge_buttkick_set3 += 0.5
                            if count_alternating_right_lunge_buttkick_set3 == 25:
                                dir_alternating_right_lunge_buttkick_set3 = 0
                            else:
                                dir_alternating_right_lunge_buttkick_set3 = 1
                                cooldown_timer_buttkick_set3 = cooldown_duration_buttkick_set3
                    else: 
                        if dir_alternating_right_lunge_buttkick_set3 == 1 and count_alternating_right_lunge_buttkick_set3 <= 25:
                            count_alternating_right_lunge_buttkick_set3 += 0.5
                            if count_alternating_right_lunge_buttkick_set3 == 25:
                                dir_alternating_right_lunge_buttkick_set3 = 1 
                            else: 
                                dir_alternating_right_lunge_buttkick_set3 = 0
                                cooldown_timer_buttkick_set3 = cooldown_duration_buttkick_set3

                    if leftleg_buttkick_set3 <= 90:
                        if dir_alternating_left_lunge_buttkick_set3 == 0 and count_alternating_left_lunge_buttkick_set3 <= 25:
                            count_alternating_left_lunge_buttkick_set3 += 0.5
                            if count_alternating_left_lunge_buttkick_set3 == 25:
                                dir_alternating_left_lunge_buttkick_set3 = 0
                            else:
                                dir_alternating_left_lunge_buttkick_set3 = 1
                                cooldown_timer_buttkick_set3 = cooldown_duration_buttkick_set3
                    else:
                        if dir_alternating_left_lunge_buttkick_set3 == 1 and count_alternating_left_lunge_buttkick_set3 <= 25:
                            count_alternating_left_lunge_buttkick_set3 += 0.5
                            if count_alternating_left_lunge_buttkick_set3 == 25:
                                dir_alternating_left_lunge_buttkick_set3 = 1
                            else:
                                dir_alternating_left_lunge_buttkick_set3 = 0
                                cooldown_timer_buttkick_set3 = cooldown_duration_buttkick_set3

        cvzone.putTextRect(img, 'Buttkick SET 3', [470, 30], thickness=2, border=2, scale=2.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)
       
        # Orientation
        cv2.rectangle(img, (890, 100), (1180, 160), (0, 0, 255), -2)
        cv2.putText(img, f"Orientation: {orientation}", (900, 140), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)

        # RIGHT LEG
        cv2.putText(img, f"R {int(per_right_leg_buttkick_set3)}%", (24, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 480), (50, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_leg_buttkick_set3)), (50, 680), color_right_leg_buttkick_set3, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_left_leg_buttkick_set3)}%", (962, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 480), (995, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_leg_buttkick_set3)), (995, 680), color_left_leg_buttkick_set3, -1)

    # Counter 
    cv2.rectangle(img, (20, 20), (200, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(count_alternating_right_lunge_buttkick_set3)}/25", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (210, 20), (390, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(count_alternating_left_lunge_buttkick_set3)}/25", (220, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    # Timer
    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [345, 30], thickness=2, border=2, scale=2.5)
        display_info_buttkick_set3 = False
        exercise_mode = "rest_buttkick_set3"
        rest_buttkick_start_time_set3 = time.time()

    # Repetition
    if count_alternating_left_lunge_buttkick_set3 >= 25:  # Assuming 10 jumping jacks for demonstration
        cvzone.putTextRect(img, 'Exercise Complete', [345, 30], thickness=2, border=2, scale=2.5)
        display_info_buttkick_set3 = False
        exercise_mode = "rest_buttkick_set3"
        rest_buttkick_start_time_set3 = time.time()
    return img

def rest_buttkick_set3(img):
    global exercise_mode, rest_buttkick_start_time_set3, start_time_slr
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_buttkick_start_time_set3
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "slr"
        start_time_slr = time.time()
    return img

def detect_slr(img):
    global count_sidelegraise_left, count_sidelegraise_right, dir_sidelegraises_left, dir_sidelegraises_right, start_time_slr, repetition_time_slr, bar_left_slr, bar_right_slr, per_left_slr, per_right_slr, angle_left_slr, color_left_leg_slr, color_right_leg_slr, left_leg_slr, right_leg_slr, rest_slr_start_time, exercise_mode, display_info_slr
    img = cv2.resize(img, (1280, 720))

    # Timer - starts timer based on set duration
    elapsed_time = time.time() - start_time_slr
    remaining_time = max(0, 60 - elapsed_time)


    if display_info_slr:  # Check if to display counter, bar, and percentage
        img = detector_SideLegRaises.findPose(img, False) # initializes img as variable for findpose function
        lmList_bicep = detector_SideLegRaises.findPosition(img, False) # initializes lmList_bicep as variable for findPosition function

        # Define hand angles outside the if statement
        if len(lmList_bicep) != 0:
            right_leg_slr = detector_SideLegRaises.SideLegRight(img, 12, 24, 26, 28, True)
            left_leg_slr = detector_SideLegRaises.SideLegLeft(img, 11, 23, 25, 27, True) # defines right arm landmark keypoints

            per_right_slr = np.interp(right_leg_slr, (180, 260), (0, 100)) 
            bar_right_slr = np.interp(right_leg_slr, (180, 260), (400, 200)) 

            per_left_slr = np.interp(left_leg_slr, (100, 170), (100, 0)) 
            bar_left_slr = np.interp(left_leg_slr, (100, 170), (200, 400)) 

            if int(per_left_slr) == 100 :
                color_left_leg_slr = (0, 255, 0) 
            elif int(per_right_slr) == 100:
                color_right_leg_slr = (0, 255, 0)
            else:
                color_left_leg_slr = (0, 0, 255)  
                color_right_leg_slr = (0, 0, 255)

            if right_leg_slr >= 260:
                if dir_sidelegraises_right == 0 and count_sidelegraise_right <= 5:
                    count_sidelegraise_right += 0.5
                    if count_sidelegraise_right == 5:
                        dir_sidelegraises_right = 0
                    else:
                        dir_sidelegraises_right = 1
            if right_leg_slr <= 180:
                if dir_sidelegraises_right == 1 and count_sidelegraise_right <= 5:
                    count_sidelegraise_right += 0.5
                    if count_sidelegraise_right == 5:
                        dir_sidelegraises_right = 1
                    else:
                        dir_sidelegraises_right = 0
            
            if left_leg_slr <= 100:
                if dir_sidelegraises_left == 0 and count_sidelegraise_left <= 5:
                    count_sidelegraise_left += 0.5
                    if count_sidelegraise_left == 5:
                        dir_sidelegraises_left = 0
                    else:
                        dir_sidelegraises_left = 1
            elif left_leg_slr >= 170:
                if dir_sidelegraises_left == 1 and count_sidelegraise_left <= 5:
                    count_sidelegraise_left += 0.5
                    if count_sidelegraise_left == 5:
                        dir_sidelegraises_left = 1
                    else:
                        dir_sidelegraises_left = 0

        # label
        cvzone.putTextRect(img, 'Side Leg Raise', [345, 30], thickness=2, border=2, scale=2.5) 

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # bar
        cv2.putText(img, f"R {int(per_right_slr)}%" , (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_slr)), (50, 400), color_right_leg_slr, -1)

        cv2.putText(img, f"L {int(per_left_slr)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_slr)), (995, 400), color_left_leg_slr, -1)
        

    #count
    cv2.rectangle(img, (20, 20), (140, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(count_sidelegraise_right)}/5", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (150, 20), (270, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(count_sidelegraise_left)}/5", (160, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [345, 30], thickness=2, border=2, scale=2.5)
        display_info_slr = False
        exercise_mode = "rest_slr"
        rest_slr_start_time = time.time()

    if count_sidelegraise_right == 5 and count_sidelegraise_left == 5:
        cvzone.putTextRect(img, 'All Repetitions Completed', [345, 30], thickness=2, border=2, scale=2.5)
        display_info_slr = False
        exercise_mode = "rest_slr"
        rest_slr_start_time = time.time()
    return img

def rest_slr(img):
    global exercise_mode, rest_slr_start_time, start_time_slr_set2
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_slr_start_time
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "slr_set2"
        start_time_slr_set2 = time.time()
    return img

def detect_slr_set2(img):
    global count_sidelegraise_left_set2, count_sidelegraise_right_set2, dir_sidelegraises_left_set2, dir_sidelegraises_right_set2, start_time_slr_set2, repetition_time_slr_set2, bar_left_slr_set2, bar_right_slr_set2, per_left_slr_set2, per_right_slr_set2, angle_left_slr_set2, color_left_leg_slr_set2, color_right_leg_slr_set2, left_leg_slr_set2, right_leg_slr_set2, rest_slr_start_time_set2, exercise_mode, display_info_slr_set2

    img = cv2.resize(img, (1280, 720))

    # Timer - starts timer based on set duration
    elapsed_time = time.time() - start_time_slr_set2
    remaining_time = max(0, 60 - elapsed_time)


    if display_info_slr_set2:  # Check if to display counter, bar, and percentage
        img = detector_SideLegRaises.findPose(img, False) # initializes img as variable for findpose function
        lmList_bicep = detector_SideLegRaises.findPosition(img, False) # initializes lmList_bicep as variable for findPosition function

        # Define hand angles outside the if statement
        if len(lmList_bicep) != 0:
            right_leg_slr_set2 = detector_SideLegRaises.SideLegRight(img, 12, 24, 26, 28, True)
            left_leg_slr_set2 = detector_SideLegRaises.SideLegLeft(img, 11, 23, 25, 27, True) # defines right arm landmark keypoints

            per_right_slr_set2 = np.interp(right_leg_slr_set2, (180, 260), (0, 100)) 
            bar_right_slr_set2 = np.interp(right_leg_slr_set2, (180, 260), (400, 200)) 

            per_left_slr_set2 = np.interp(left_leg_slr_set2, (100, 170), (100, 0)) 
            bar_left_slr_set2 = np.interp(left_leg_slr_set2, (100, 170), (200, 400)) 

            if int(per_left_slr_set2) == 100 :
                color_left_leg_slr_set2 = (0, 255, 0) 
            elif int(per_right_slr_set2) == 100:
                color_right_leg_slr_set2 = (0, 255, 0)
            else:
                color_left_leg_slr_set2 = (0, 0, 255)  
                color_right_leg_slr_set2 = (0, 0, 255)

            if right_leg_slr_set2 >= 260:
                if dir_sidelegraises_right_set2 == 0 and count_sidelegraise_right_set2 <= 5:
                    count_sidelegraise_right_set2 += 0.5
                    if count_sidelegraise_right_set2 == 5:
                        dir_sidelegraises_right_set2 = 0
                    else:
                        dir_sidelegraises_right_set2 = 1
            if right_leg_slr_set2 <= 180:
                if dir_sidelegraises_right_set2 == 1 and count_sidelegraise_right_set2 <= 5:
                    count_sidelegraise_right_set2 += 0.5
                    if count_sidelegraise_right_set2 == 5:
                        dir_sidelegraises_right_set2 = 1
                    else:
                        dir_sidelegraises_right_set2 = 0
            
            if left_leg_slr_set2 <= 100:
                if dir_sidelegraises_left_set2 == 0 and count_sidelegraise_left_set2 <= 5:
                    count_sidelegraise_left_set2 += 0.5
                    if count_sidelegraise_left_set2 == 5:
                        dir_sidelegraises_left_set2 = 0
                    else:
                        dir_sidelegraises_left_set2 = 1
            elif left_leg_slr >= 170:
                if dir_sidelegraises_left_set2 == 1 and count_sidelegraise_left_set2 <= 5:
                    count_sidelegraise_left_set2 += 0.5
                    if count_sidelegraise_left_set2 == 5:
                        dir_sidelegraises_left_set2 = 1
                    else:
                        dir_sidelegraises_left_set2 = 0

        # label
        cvzone.putTextRect(img, 'Side Leg Raise SET 2', [345, 30], thickness=2, border=2, scale=2.5) 

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # bar
        cv2.putText(img, f"R {int(per_right_slr_set2)}%" , (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_slr_set2)), (50, 400), color_right_leg_slr_set2, -1)

        cv2.putText(img, f"L {int(per_left_slr_set2)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_slr_set2)), (995, 400), color_left_leg_slr_set2, -1)
        

    #count
    cv2.rectangle(img, (20, 20), (140, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(count_sidelegraise_right_set2)}/5", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (150, 20), (270, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(count_sidelegraise_left_set2)}/5", (160, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [345, 30], thickness=2, border=2, scale=2.5)
        display_info_slr_set2 = False
        exercise_mode = "rest_slr_set2"
        rest_slr_start_time_set2 = time.time()

    if count_sidelegraise_right_set2 == 5 and count_sidelegraise_left_set2 == 5:
        cvzone.putTextRect(img, 'All Repetitions Completed', [345, 30], thickness=2, border=2, scale=2.5)
        display_info_slr_set2 = False
        exercise_mode = "rest_slr_set2"
        rest_slr_start_time_set2 = time.time()
    return img 

def rest_slr_set2(img):
    global exercise_mode, rest_slr_start_time_set2, start_time_slr_set3
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_slr_start_time_set2
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "slr_set3"
        start_time_slr_set3 = time.time()
    return img 

def detect_slr_set3(img):
    global count_sidelegraise_left_set3, count_sidelegraise_right_set3, dir_sidelegraises_left_set3, dir_sidelegraises_right_set3, start_time_slr_set3, repetition_time_slr_set3, bar_left_slr_set3, bar_right_slr_set3, per_left_slr_set3, per_right_slr_set3, angle_left_slr_set3, color_left_leg_slr_set3, color_right_leg_slr_set3, left_leg_slr_set3, right_leg_slr_set3, rest_slr_start_time_set3, exercise_mode, display_info_slr_set3

    img = cv2.resize(img, (1280, 720))

    # Timer - starts timer based on set duration
    elapsed_time = time.time() - start_time_slr_set3
    remaining_time = max(0, 60 - elapsed_time)


    if display_info_slr_set3:  # Check if to display counter, bar, and percentage
        img = detector_SideLegRaises.findPose(img, False) # initializes img as variable for findpose function
        lmList_bicep = detector_SideLegRaises.findPosition(img, False) # initializes lmList_bicep as variable for findPosition function

        # Define hand angles outside the if statement
        if len(lmList_bicep) != 0:
            right_leg_slr_set3 = detector_SideLegRaises.SideLegRight(img, 12, 24, 26, 28, True)
            left_leg_slr_set3 = detector_SideLegRaises.SideLegLeft(img, 11, 23, 25, 27, True) # defines right arm landmark keypoints

            per_right_slr_set3 = np.interp(right_leg_slr_set3, (180, 260), (0, 100)) 
            bar_right_slr_set3 = np.interp(right_leg_slr_set3, (180, 260), (400, 200)) 

            per_left_slr_set3 = np.interp(left_leg_slr_set3, (100, 170), (100, 0)) 
            bar_left_slr_set3 = np.interp(left_leg_slr_set3, (100, 170), (200, 400)) 

            if int(per_left_slr_set3) == 100 :
                color_left_leg_slr_set3 = (0, 255, 0) 
            elif int(per_right_slr_set3) == 100:
                color_right_leg_slr_set3 = (0, 255, 0)
            else:
                color_left_leg_slr_set3 = (0, 0, 255)  
                color_right_leg_slr_set3 = (0, 0, 255)

            if right_leg_slr_set3 >= 260:
                if dir_sidelegraises_right_set3 == 0 and count_sidelegraise_right_set3 <= 5:
                    count_sidelegraise_right_set3 += 0.5
                    if count_sidelegraise_right_set3 == 5:
                        dir_sidelegraises_right_set3 = 0
                    else:
                        dir_sidelegraises_right_set3 = 1
            if right_leg_slr_set3 <= 180:
                if dir_sidelegraises_right_set3 == 1 and count_sidelegraise_right_set3 <= 5:
                    count_sidelegraise_right_set3 += 0.5
                    if count_sidelegraise_right_set3 == 5:
                        dir_sidelegraises_right_set3 = 1
                    else:
                        dir_sidelegraises_right_set3 = 0
            
            if left_leg_slr_set3 <= 100:
                if dir_sidelegraises_left_set3 == 0 and count_sidelegraise_left_set3 <= 5:
                    count_sidelegraise_left_set3 += 0.5
                    if count_sidelegraise_left_set3 == 5:
                        dir_sidelegraises_left_set3 = 0
                    else:
                        dir_sidelegraises_left_set3 = 1
            elif left_leg_slr_set3 >= 170:
                if dir_sidelegraises_left_set3 == 1 and count_sidelegraise_left_set3 <= 5:
                    count_sidelegraise_left_set3 += 0.5
                    if count_sidelegraise_left_set3 == 5:
                        dir_sidelegraises_left_set3 = 1
                    else:
                        dir_sidelegraises_left_set3 = 0

        # label
        cvzone.putTextRect(img, 'Side Leg Raise SET 3', [345, 30], thickness=2, border=2, scale=2.5) 

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # bar
        cv2.putText(img, f"R {int(per_right_slr_set3)}%" , (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_slr_set3)), (50, 400), color_right_leg_slr_set3, -1)

        cv2.putText(img, f"L {int(per_left_slr_set3)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_slr_set3)), (995, 400), color_left_leg_slr_set3, -1)
        

    #count
    cv2.rectangle(img, (20, 20), (140, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(count_sidelegraise_right_set3)}/5", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (150, 20), (270, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(count_sidelegraise_left_set3)}/5", (160, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [345, 30], thickness=2, border=2, scale=2.5)
        display_info_slr_set3 = False
        exercise_mode = "rest_slr_set3"
        rest_slr_start_time_set3 = time.time()

    if count_sidelegraise_right_set3 == 5 and count_sidelegraise_left_set3 == 5:
        cvzone.putTextRect(img, 'All Repetitions Completed', [345, 30], thickness=2, border=2, scale=2.5)
        display_info_slr_set3 = False
        exercise_mode = "rest_slr_set3"
        rest_slr_start_time_set3 = time.time()



    return img

def rest_slr_set3(img):
    global exercise_mode, rest_slr_start_time_set3, start_time_squatjacks
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_slr_start_time_set3
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "squatjacks"
        start_time_squatjacks = time.time()
    return img

def detect_squatjacks(img):
    global  count_squatjack, dir_squatjack , start_time_squatjacks ,repetition_time_squatjack, display_info_squatjack, per_down_squatjacks, distance_squatjacks, bar_down_squatjacks, exercise_mode, rest_squatjacks_start_time

    img = cv2.resize(img, (1280, 720))

    # Timer - starts timer based on set duration
    elapsed_time = time.time() - start_time_squatjacks
    remaining_time = max(0, 60 - elapsed_time)

    if display_info_squatjack:  # Check if to display counter, bar, and percentage
        img = detector_squatjack.findPose(img, False)  # initializes img as variable for findpose function
        lmList_squatjack = detector_squatjack.findPosition(img, False)  # initializes lmList_squatjack as variable for findPosition function

        # Define leg angles outside the if statement
        if len(lmList_squatjack) != 0:
            distance_squatjacks = detector_squatjack.findSquatJack(img, 24, 26, 28, 23, 25, 27, drawpoints=True)  # Define landmark keypoints
            leftangle, rightangle = detector_squatjack.CheckUpperBody(img, 11, 13, 15, 12, 14, 16, drawpoints=True)

            #Interpolate the distance between the two ankle  to percentage and position on screen
            per_down_squatjacks = np.interp(distance_squatjacks, (60, 240), (0, 100))
            bar_down_squatjacks = np.interp(distance_squatjacks, (60, 250), (400, 200))


            if distance_squatjacks >= 240:
                if dir_squatjack == 0:
                    count_squatjack += 0.5
                    dir_squatjack = 1
            elif distance_squatjacks <= 60:
                if dir_squatjack == 1:
                    count_squatjack +=0.5
                    dir_squatjack = 0


        # Label
        cvzone.putTextRect(img, 'Squat Jack', [345, 30], thickness=2, border=2, scale=2.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        cv2.putText(img, f"R {int(per_down_squatjacks)}%", (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_down_squatjacks)), (50, 400), (0, 0, 255), -1)

        cv2.putText(img, f"L {int(per_down_squatjacks)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_down_squatjacks)), (995, 400), (0, 0, 255), -1)

        if distance_squatjacks >= 240:
            cv2.rectangle(img, (952, int(bar_down_squatjacks)), (995, 400), (0, 255, 0), -1)
            cv2.rectangle(img, (8, int(bar_down_squatjacks)), (50, 400), (0, 255, 0), -1)

    # Count
    cv2.rectangle(img, (20, 10), (140, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(count_squatjack)}/5", (30, 80), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
        display_info_squatjack = False
        exercise_mode = "rest_squatjacks"
        rest_squatjacks_start_time = time.time()

    if count_squatjack == 5:
        cvzone.putTextRect(img, 'All Repetitions Completed', [390, 30], thickness=2, border=2, scale=2.5)
        display_info_squatjack = False
        exercise_mode = "rest_squatjacks"
        rest_squatjacks_start_time = time.time()
    return img
 
def rest_squatjacks(img):
    global exercise_mode, rest_squatjacks_start_time, start_time_squatjacks_set2
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_squatjacks_start_time
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "squatjacks_set2"
        start_time_squatjacks_set2 = time.time()
    return img

def detect_squatjacks_set2(img):
    global  count_squatjack_set2, dir_squatjack_set2, start_time_squatjacks_set2, repetition_time_squatjack_set2, display_info_squatjack_set2, per_down_squatjacks_set2, distance_squatjacks_set2, bar_down_squatjacks_set2, exercise_mode, rest_squatjacks_start_time_set2

    img = cv2.resize(img, (1280, 720))

    # Timer - starts timer based on set duration
    elapsed_time = time.time() - start_time_squatjacks_set2
    remaining_time = max(0, 60 - elapsed_time)

    if display_info_squatjack_set2:  # Check if to display counter, bar, and percentage
        img = detector_squatjack.findPose(img, False)  # initializes img as variable for findpose function
        lmList_squatjack = detector_squatjack.findPosition(img, False)  # initializes lmList_squatjack as variable for findPosition function

        # Define leg angles outside the if statement
        if len(lmList_squatjack) != 0:
            distance_squatjacks_set2 = detector_squatjack.findSquatJack(img, 24, 26, 28, 23, 25, 27, drawpoints=True)  # Define landmark keypoints
            leftangle, rightangle = detector_squatjack.CheckUpperBody(img, 11, 13, 15, 12, 14, 16, drawpoints=True)

            #Interpolate the distance between the two ankle  to percentage and position on screen
            per_down_squatjacks_set2 = np.interp(distance_squatjacks_set2, (60, 240), (0, 100))
            bar_down_squatjacks_set2 = np.interp(distance_squatjacks_set2, (60, 250), (400, 200))


            if distance_squatjacks_set2 >= 240:
                if dir_squatjack_set2 == 0:
                    count_squatjack_set2 += 0.5
                    dir_squatjack_set2 = 1
            elif distance_squatjacks_set2 <= 60:
                if dir_squatjack_set2 == 1:
                    count_squatjack_set2 +=0.5
                    dir_squatjack_set2 = 0


        # Label
        cvzone.putTextRect(img, 'Squat Jack SET 2', [345, 30], thickness=2, border=2, scale=2.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        cv2.putText(img, f"R {int(per_down_squatjacks_set2)}%", (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_down_squatjacks)), (50, 400), (0, 0, 255), -1)

        cv2.putText(img, f"L {int(per_down_squatjacks_set2)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_down_squatjacks_set2)), (995, 400), (0, 0, 255), -1)

        if distance_squatjacks >= 240:
            cv2.rectangle(img, (952, int(bar_down_squatjacks_set2)), (995, 400), (0, 255, 0), -1)
            cv2.rectangle(img, (8, int(bar_down_squatjacks_set2)), (50, 400), (0, 255, 0), -1)

    # Count
    cv2.rectangle(img, (20, 10), (140, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(count_squatjack_set2)}/5", (30, 80), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
        display_info_squatjack_set2 = False
        exercise_mode = "rest_squatjacks_set2"
        rest_squatjacks_start_time_set2 = time.time()

    if count_squatjack_set2 == 5:
        cvzone.putTextRect(img, 'All Repetitions Completed', [390, 30], thickness=2, border=2, scale=2.5)
        display_info_squatjack_set2 = False
        exercise_mode = "rest_squatjacks_set2"
        rest_squatjacks_start_time_set2 = time.time()
    return img

def rest_squatjacks_set2(img):
    global exercise_mode, rest_squatjacks_start_time_set2, start_time_squatjacks_set3
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_squatjacks_start_time_set2
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "squatjacks_set3"
        start_time_squatjacks_set3 = time.time()
    return img

def detect_squatjacks_set3(img):
    global  count_squatjack_set3, dir_squatjack_set3, start_time_squatjacks_set3, repetition_time_squatjack_set3, display_info_squatjack_set3, per_down_squatjacks_set3, distance_squatjacks_set3, bar_down_squatjacks_set3, exercise_mode, rest_squatjacks_start_time_set3

    img = cv2.resize(img, (1280, 720))

    # Timer - starts timer based on set duration
    elapsed_time = time.time() - start_time_squatjacks_set3
    remaining_time = max(0, 60 - elapsed_time)

    if display_info_squatjack_set3:  # Check if to display counter, bar, and percentage
        img = detector_squatjack.findPose(img, False)  # initializes img as variable for findpose function
        lmList_squatjack = detector_squatjack.findPosition(img, False)  # initializes lmList_squatjack as variable for findPosition function

        # Define leg angles outside the if statement
        if len(lmList_squatjack) != 0:
            distance_squatjacks_set3 = detector_squatjack.findSquatJack(img, 24, 26, 28, 23, 25, 27, drawpoints=True)  # Define landmark keypoints
            leftangle, rightangle = detector_squatjack.CheckUpperBody(img, 11, 13, 15, 12, 14, 16, drawpoints=True)

            #Interpolate the distance between the two ankle  to percentage and position on screen
            per_down_squatjacks_set3 = np.interp(distance_squatjacks_set3, (60, 240), (0, 100))
            bar_down_squatjacks_set3 = np.interp(distance_squatjacks_set3, (60, 250), (400, 200))


            if distance_squatjacks_set3 >= 240:
                if dir_squatjack_set3 == 0:
                    count_squatjack_set3 += 0.5
                    dir_squatjack_set3 = 1
            elif distance_squatjacks_set3 <= 60:
                if dir_squatjack_set3 == 1:
                    count_squatjack_set3 +=0.5
                    dir_squatjack_set3 = 0


        # Label
        cvzone.putTextRect(img, 'Squat Jack SET 3', [345, 30], thickness=2, border=2, scale=2.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        cv2.putText(img, f"R {int(per_down_squatjacks_set3)}%", (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_down_squatjacks_set3)), (50, 400), (0, 0, 255), -1)

        cv2.putText(img, f"L {int(per_down_squatjacks_set3)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_down_squatjacks_set3)), (995, 400), (0, 0, 255), -1)

        if distance_squatjacks_set3 >= 240:
            cv2.rectangle(img, (952, int(bar_down_squatjacks_set3)), (995, 400), (0, 255, 0), -1)
            cv2.rectangle(img, (8, int(bar_down_squatjacks_set3)), (50, 400), (0, 255, 0), -1)

    # Count
    cv2.rectangle(img, (20, 10), (140, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(count_squatjack_set3)}/5", (30, 80), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
        display_info_squatjack_set3 = False
        exercise_mode = "rest_squatjacks_set3"
        rest_squatjacks_start_time_set3 = time.time()

    if count_squatjack == 5:
        cvzone.putTextRect(img, 'All Repetitions Completed', [390, 30], thickness=2, border=2, scale=2.5)
        display_info_squatjack_set3 = False
        exercise_mode = "rest_squatjacks_set3"
        rest_squatjacks_start_time_set3 = time.time()
    return img 

def rest_squatjacks_set3(img):
    global exercise_mode, rest_squatjacks_start_time_set3, start_time_squatjump
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_squatjacks_start_time_set3
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "squatjump"
        start_time_squatjump = time.time()
    return img

def detect_squatjump(img):
    global count_squat_jump, dir_squat_jump, start_time_squatjump, repetition_time_squatjump, display_info_squatjump, per_left_leg_squatjump, bar_left_leg_squatjump, per_right_leg_squatjump, bar_right_leg_squatjump, leftleg_squatjump, rightleg_squatjump, cooldown_duration_squatjump, cooldown_timer_squatjump, color_left_leg_squatjump, color_right_leg_squatjump, rest_squatjump_start_time, orientation, orientation2, exercise_mode

    img = cv2.resize(img, (1280, 720))

    elapsed_time = time.time() - start_time_squatjump
    remaining_time = max(0, 60 - elapsed_time)

    if display_info_squatjump:  # Check if to display counter, bar, and percentage
        img = detector_squatjump.findPose(img, False)
        lmList_squat_jump = detector_squatjump.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_squat_jump) != 0:

            # Right and Left keypoints
            rightleg_squatjump, orientation, lift_off = detector_squatjump.SquatJump(img, 12, 24, 26, True)
            leftleg_squatjump, orientation2, lift_off = detector_squatjump.SquatJump(img, 11, 23, 25, True)

            if cooldown_timer_squatjump > 0:
                cooldown_timer_squatjump -= 1

            if orientation == 'right' and orientation2 == 'right':
                    
                    per_right_leg_squatjump = np.interp(rightleg_squatjump, (190, 290), (0, 100))
                    bar_right_leg_squatjump = np.interp(rightleg_squatjump, (190, 290), (680, 480))
                    per_left_leg_squatjump = np.interp(leftleg_squatjump, (190, 290), (0, 100))
                    bar_left_leg_squatjump = np.interp(leftleg_squatjump, (190, 290), (680, 480))

                    if int(per_left_leg_squatjump) == 100 and int(per_right_leg_squatjump) == 100:
                        color_left_leg_squatjump = (0, 255, 0)
                        color_right_leg_squatjump = (0, 255, 0)  # Change color of left leg bar to green
                    else:
                        color_left_leg_squatjump = (0, 0, 255)  # Keep color of left leg bar as red
                        color_right_leg_squatjump = (0, 0, 255)

                    if rightleg_squatjump >= 290:
                        if dir_squat_jump == 0:
                            count_squat_jump += 0.5
                            dir_squat_jump = 1
                            cooldown_timer_squatjump = cooldown_duration_squatjump
                    elif rightleg_squatjump <= 190:
                        if dir_squat_jump == 1:
                            count_squat_jump += 0.5
                            dir_squat_jump = 0
                            cooldown_timer_squatjump = cooldown_duration_squatjump
                    
                    if leftleg_squatjump >= 290:
                        if dir_squat_jump == 0:
                            count_squat_jump += 0.5
                            dir_squat_jump = 1
                            cooldown_timer_squatjump = cooldown_duration_squatjump
                    elif leftleg_squatjump <= 190:
                        if dir_squat_jump == 1:
                            count_squat_jump += 0.5
                            dir_squat_jump = 0
                            cooldown_timer_squatjump = cooldown_duration_squatjump


            elif orientation =='left' and orientation2 == 'left':
                if leftleg_squatjump is not None and rightleg_squatjump is not None:
                    per_right_leg_squatjump = np.interp(rightleg_squatjump, (70, 150), (100, 0))
                    bar_right_leg_squatjump = np.interp(rightleg_squatjump, (70, 150), (480, 680))
                    per_left_leg_squatjump = np.interp(leftleg_squatjump, (70, 150), (100 ,0))
                    bar_left_leg_squatjump = np.interp(leftleg_squatjump, (70, 150), (480, 680))

                    if int(per_left_leg_squatjump) == 100 and int(per_right_leg_squatjump) == 100:
                        color_left_leg_squatjump = (0, 255, 0)
                        color_right_leg_squatjump = (0, 255, 0)  # Change color of left leg bar to green
                    else:
                        color_left_leg_squatjump = (0, 0, 255)  # Keep color of left leg bar as red
                        color_right_leg_squatjump = (0, 0, 255)
              
                    if rightleg_squatjump <= 70:
                        if dir_squat_jump == 0:
                            count_squat_jump += 0.5
                            dir_squat_jump = 1
                            cooldown_timer_squatjump = cooldown_duration_squatjump
                    elif rightleg_squatjump >= 150:
                        if dir_squat_jump == 1:
                            count_squat_jump += 0.5
                            dir_squat_jump = 0
                            cooldown_timer_squatjump = cooldown_duration_squatjump

                    if leftleg_squatjump <= 70:
                        if dir_squat_jump == 0:
                            count_squat_jump += 0.5
                            dir_squat_jump = 1
                            cooldown_timer_squatjump = cooldown_duration_squatjump
                    elif leftleg_squatjump >= 150:
                        if dir_squat_jump == 1:
                            count_squat_jump += 0.5
                            dir_squat_jump = 0
                            cooldown_timer_squatjump = cooldown_duration_squatjump

            elif orientation == 'front' and orientation2 == 'front':
                    
                    per_right_leg_squatjump = np.interp(rightleg_squatjump, (170, 280), (100, 0))
                    bar_right_leg_squatjump = np.interp(rightleg_squatjump, (170, 280), (480, 680))
                    per_left_leg_squatjump = np.interp(leftleg_squatjump, (170, 280), (100, 0))
                    bar_left_leg_squatjump = np.interp(leftleg_squatjump, (170, 280), (480, 680))

                    if int(per_left_leg_squatjump) == 100 and int(per_right_leg_squatjump) == 100:
                        color_left_leg_squatjump = (0, 255, 0)
                        color_right_leg_squatjump = (0, 255, 0)  # Change color of left leg bar to green
                    else:
                        color_left_leg_squatjump = (0, 0, 255)  # Keep color of left leg bar as red
                        color_right_leg_squatjump = (0, 0, 255)  # Keep color of right leg bar as red

                    if rightleg_squatjump <= 170:
                        if dir_squat_jump == 0:
                            count_squat_jump += 0.5
                            dir_squat_jump = 1
                            cooldown_timer_squatjump = cooldown_duration_squatjump
                    elif rightleg_squatjump >= 280: 
                        if dir_squat_jump == 1:
                            count_squat_jump += 0.5
                            dir_squat_jump = 0
                            cooldown_timer_squatjump = cooldown_duration_squatjump
                    if leftleg_squatjump <= 170:
                        if dir_squat_jump == 0:
                            count_squat_jump += 0.5
                            dir_squat_jump = 1
                            cooldown_timer = cooldown_duration_squatjump
                    elif leftleg_squatjump >= 280:
                        if dir_squat_jump == 1:
                            count_squat_jump += 0.5
                            dir_squat_jump = 0
                            cooldown_timer_squatjump = cooldown_duration_squatjump

        cvzone.putTextRect(img, 'Squat Jump Tracker', [420, 30], thickness=2, border=2, scale=2.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)
       
        # Orientation
        cv2.rectangle(img, (890, 100), (1180, 160), (0, 0, 255), -2)
        cv2.putText(img, f"Orientation: {orientation}", (900, 140), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)

        # RIGHT LEG
        cv2.putText(img, f"R {int(per_right_leg_squatjump)}%", (24, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 480), (50, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_leg_squatjump)), (50, 680), color_right_leg_squatjump, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_left_leg_squatjump)}%", (962, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 480), (995, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_leg_squatjump)), (995, 680), color_left_leg_squatjump, -1)

    # Counter 
    cv2.rectangle(img, (20, 20), (200, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(count_squat_jump)}/5", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    # Timer
    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
        display_info_squatjump = False
        exercise_mode = "rest_squatjump"
        rest_squatjump_start_time = time.time()

    # Repetition
    if count_squat_jump == 5:  # Assuming 10 jumping jacks for demonstration
        cvzone.putTextRect(img, 'Exercise Complete', [390, 30], thickness=2, border=2, scale=2.5)
        display_info_squatjump = False
        exercise_mode = "rest_squatjump"
        rest_squatjump_start_time = time.time()
    return img

def rest_squatjump(img):
    global exercise_mode, rest_squatjump_start_time, start_time_squatjump_set2
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_squatjump_start_time
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "squatjump_set2"
        start_time_squatjump_set2 = time.time()
    return img

def detect_squatjump_set2(img):
    global count_squat_jump_set2, dir_squat_jump_set2, start_time_squatjump_set2, repetition_time_squatjump_set2, display_info_squatjump_set2, per_left_leg_squatjump_set2, bar_left_leg_squatjump_set2, per_right_leg_squatjump_set2, bar_right_leg_squatjump_set2, leftleg_squatjump_set2, rightleg_squatjump_set2, cooldown_duration_squatjump_set2, cooldown_timer_squatjump_set2, color_left_leg_squatjump_set2, color_right_leg_squatjump_set2, rest_squatjump_start_time_set2, orientation, orientation2, exercise_mode

    img = cv2.resize(img, (1280, 720))

    elapsed_time = time.time() - start_time_squatjump_set2
    remaining_time = max(0, 60 - elapsed_time)

    if display_info_squatjump_set2:  # Check if to display counter, bar, and percentage
        img = detector_squatjump.findPose(img, False)
        lmList_squat_jump = detector_squatjump.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_squat_jump) != 0:

            # Right and Left keypoints
            rightleg_squatjump_set2, orientation, lift_off = detector_squatjump.SquatJump(img, 12, 24, 26, True)
            leftleg_squatjump_set2, orientation2, lift_off = detector_squatjump.SquatJump(img, 11, 23, 25, True)

            if cooldown_timer_squatjump_set2 > 0:
                cooldown_timer_squatjump_set2 -= 1

            if orientation == 'right' and orientation2 == 'right':
                    
                    per_right_leg_squatjump_set2 = np.interp(rightleg_squatjump_set2, (190, 290), (0, 100))
                    bar_right_leg_squatjump_set2 = np.interp(rightleg_squatjump_set2, (190, 290), (680, 480))
                    per_left_leg_squatjump_set2 = np.interp(leftleg_squatjump_set2, (190, 290), (0, 100))
                    bar_left_leg_squatjump_set2 = np.interp(leftleg_squatjump_set2, (190, 290), (680, 480))

                    if int(per_left_leg_squatjump_set2) == 100 and int(per_right_leg_squatjump_set2) == 100:
                        color_left_leg_squatjump_set2 = (0, 255, 0)
                        color_right_leg_squatjump_set2 = (0, 255, 0)  # Change color of left leg bar to green
                    else:
                        color_left_leg_squatjump_set2 = (0, 0, 255)  # Keep color of left leg bar as red
                        color_right_leg_squatjump_set2 = (0, 0, 255)

                    if rightleg_squatjump_set2 >= 290:
                        if dir_squat_jump_set2 == 0:
                            count_squat_jump_set2 += 0.5
                            dir_squat_jump_set2 = 1
                            cooldown_timer_squatjump_set2 = cooldown_duration_squatjump_set2
                    elif rightleg_squatjump_set2 <= 190:
                        if dir_squat_jump_set2 == 1:
                            count_squat_jump_set2 += 0.5
                            dir_squat_jump_set2 = 0
                            cooldown_timer_squatjump_set2 = cooldown_duration_squatjump_set2
                    
                    if leftleg_squatjump_set2 >= 290:
                        if dir_squat_jump_set2 == 0:
                            count_squat_jump_set2 += 0.5
                            dir_squat_jump_set2 = 1
                            cooldown_timer_squatjump_set2 = cooldown_duration_squatjump_set2
                    elif leftleg_squatjump_set2 <= 190:
                        if dir_squat_jump == 1:
                            count_squat_jump_set2 += 0.5
                            dir_squat_jump_set2 = 0
                            cooldown_timer_squatjump_set2 = cooldown_duration_squatjump_set2


            elif orientation =='left' and orientation2 == 'left':
                if leftleg_squatjump_set2 is not None and rightleg_squatjump_set2 is not None:
                    per_right_leg_squatjump_set2 = np.interp(rightleg_squatjump_set2, (70, 150), (100, 0))
                    bar_right_leg_squatjump_set2 = np.interp(rightleg_squatjump_set2, (70, 150), (480, 680))
                    per_left_leg_squatjump_set2 = np.interp(leftleg_squatjump_set2, (70, 150), (100 ,0))
                    bar_left_leg_squatjump_set2 = np.interp(leftleg_squatjump_set2, (70, 150), (480, 680))

                    if int(per_left_leg_squatjump_set2) == 100 and int(per_right_leg_squatjump_set2) == 100:
                        color_left_leg_squatjump_set2 = (0, 255, 0)
                        color_right_leg_squatjump_set2 = (0, 255, 0)  # Change color of left leg bar to green
                    else:
                        color_left_leg_squatjump_set2 = (0, 0, 255)  # Keep color of left leg bar as red
                        color_right_leg_squatjump_set2 = (0, 0, 255)
              
                    if rightleg_squatjump_set2 <= 70:
                        if dir_squat_jump_set2 == 0:
                            count_squat_jump_set2 += 0.5
                            dir_squat_jump_set2 = 1
                            cooldown_timer_squatjump_set2 = cooldown_duration_squatjump_set2
                    elif rightleg_squatjump_set2 >= 150:
                        if dir_squat_jump_set2 == 1:
                            count_squat_jump_set2 += 0.5
                            dir_squat_jump_set2 = 0
                            cooldown_timer_squatjump_set2 = cooldown_duration_squatjump_set2

                    if leftleg_squatjump_set2 <= 70:
                        if dir_squat_jump_set2 == 0:
                            count_squat_jump_set2 += 0.5
                            dir_squat_jump_set2 = 1
                            cooldown_timer_squatjump_set2 = cooldown_duration_squatjump_set2
                    elif leftleg_squatjump_set2 >= 150:
                        if dir_squat_jump_set2 == 1:
                            count_squat_jump_set2 += 0.5
                            dir_squat_jump_set2 = 0
                            cooldown_timer_squatjump_set2 = cooldown_duration_squatjump_set2

            elif orientation == 'front' and orientation2 == 'front':
                    
                    per_right_leg_squatjump_set2 = np.interp(rightleg_squatjump_set2, (170, 280), (100, 0))
                    bar_right_leg_squatjump_set2 = np.interp(rightleg_squatjump_set2, (170, 280), (480, 680))
                    per_left_leg_squatjump_set2 = np.interp(leftleg_squatjump_set2, (170, 280), (100, 0))
                    bar_left_leg_squatjump_set2 = np.interp(leftleg_squatjump_set2, (170, 280), (480, 680))

                    if int(per_left_leg_squatjump_set2) == 100 and int(per_right_leg_squatjump_set2) == 100:
                        color_left_leg_squatjump_set2 = (0, 255, 0)
                        color_right_leg_squatjump_set2 = (0, 255, 0)  # Change color of left leg bar to green
                    else:
                        color_left_leg_squatjump_set2 = (0, 0, 255)  # Keep color of left leg bar as red
                        color_right_leg_squatjump_set2 = (0, 0, 255)  # Keep color of right leg bar as red

                    if rightleg_squatjump_set2 <= 170:
                        if dir_squat_jump_set2 == 0:
                            count_squat_jump_set2 += 0.5
                            dir_squat_jump_set2 = 1
                            cooldown_timer_squatjump_set2 = cooldown_duration_squatjump_set2
                    elif rightleg_squatjump_set2 >= 280: 
                        if dir_squat_jump_set2 == 1:
                            count_squat_jump_set2 += 0.5
                            dir_squat_jump_set2 = 0
                            cooldown_timer_squatjump_set2 = cooldown_duration_squatjump_set2
                    if leftleg_squatjump_set2 <= 170:
                        if dir_squat_jump_set2 == 0:
                            count_squat_jump_set2 += 0.5
                            dir_squat_jump_set2 = 1
                            cooldown_timer_set2 = cooldown_duration_squatjump_set2
                    elif leftleg_squatjump_set2 >= 280:
                        if dir_squat_jump_set2 == 1:
                            count_squat_jump_set2 += 0.5
                            dir_squat_jump_set2 = 0
                            cooldown_timer_squatjump_set2 = cooldown_duration_squatjump_set2

        cvzone.putTextRect(img, 'Squat Jump SET 2', [420, 30], thickness=2, border=2, scale=2.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)
       
        # Orientation
        cv2.rectangle(img, (890, 100), (1180, 160), (0, 0, 255), -2)
        cv2.putText(img, f"Orientation: {orientation}", (900, 140), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)

        # RIGHT LEG
        cv2.putText(img, f"R {int(per_right_leg_squatjump_set2)}%", (24, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 480), (50, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_leg_squatjump_set2)), (50, 680), color_right_leg_squatjump_set2, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_left_leg_squatjump_set2)}%", (962, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 480), (995, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_leg_squatjump_set2)), (995, 680), color_left_leg_squatjump_set2, -1)

    # Counter 
    cv2.rectangle(img, (20, 20), (200, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(count_squat_jump_set2)}/5", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    # Timer
    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
        display_info_squatjump_set2 = False
        exercise_mode = "rest_squatjump_set2"
        rest_squatjump_start_time_set2 = time.time()

    # Repetition
    if count_squat_jump_set2 == 5:  # Assuming 10 jumping jacks for demonstration
        cvzone.putTextRect(img, 'Exercise Complete', [390, 30], thickness=2, border=2, scale=2.5)
        display_info_squatjump_set2 = False
        exercise_mode = "rest_squatjump_set2"
        rest_squatjump_start_time_set2 = time.time()
    return img

def rest_squatjump_set2(img):
    global exercise_mode, rest_squatjump_start_time_set2, start_time_squatjump_set3
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_squatjump_start_time_set2
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "squatjump_set3"
        start_time_squatjump_set3 = time.time()

    return img

def detect_squatjump_set3(img):
    global count_squat_jump_set3, dir_squat_jump_set3, start_time_squatjump_set3, repetition_time_squatjump_set3, display_info_squatjump_set3, per_left_leg_squatjump_set3, bar_left_leg_squatjump_set3, per_right_leg_squatjump_set3, bar_right_leg_squatjump_set3, leftleg_squatjump_set3, rightleg_squatjump_set3, cooldown_duration_squatjump_set3, cooldown_timer_squatjump_set3, color_left_leg_squatjump_set3, color_right_leg_squatjump_set3, rest_squatjump_start_time_set3, orientation, orientation2, exercise_mode

    img = cv2.resize(img, (1280, 720))

    elapsed_time = time.time() - start_time_squatjump_set3
    remaining_time = max(0, 60 - elapsed_time)

    if display_info_squatjump_set3:  # Check if to display counter, bar, and percentage
        img = detector_squatjump.findPose(img, False)
        lmList_squat_jump = detector_squatjump.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_squat_jump) != 0:

            # Right and Left keypoints
            rightleg_squatjump_set3, orientation, lift_off = detector_squatjump.SquatJump(img, 12, 24, 26, True)
            leftleg_squatjump_set3, orientation2, lift_off = detector_squatjump.SquatJump(img, 11, 23, 25, True)

            if cooldown_timer_squatjump_set3 > 0:
                cooldown_timer_squatjump_set3 -= 1

            if orientation == 'right' and orientation2 == 'right':
                    
                    per_right_leg_squatjump_set3 = np.interp(rightleg_squatjump_set3, (190, 290), (0, 100))
                    bar_right_leg_squatjump_set3 = np.interp(rightleg_squatjump_set3, (190, 290), (680, 480))
                    per_left_leg_squatjump_set3 = np.interp(leftleg_squatjump_set3, (190, 290), (0, 100))
                    bar_left_leg_squatjump_set3 = np.interp(leftleg_squatjump_set3, (190, 290), (680, 480))

                    if int(per_left_leg_squatjump_set3) == 100 and int(per_right_leg_squatjump_set3) == 100:
                        color_left_leg_squatjump_set3 = (0, 255, 0)
                        color_right_leg_squatjump_set3 = (0, 255, 0)  # Change color of left leg bar to green
                    else:
                        color_left_leg_squatjump_set3 = (0, 0, 255)  # Keep color of left leg bar as red
                        color_right_leg_squatjump_set3 = (0, 0, 255)

                    if rightleg_squatjump_set3 >= 290:
                        if dir_squat_jump_set3 == 0:
                            count_squat_jump_set3 += 0.5
                            dir_squat_jump_set3 = 1
                            cooldown_timer_squatjump_set3 = cooldown_duration_squatjump_set3
                    elif rightleg_squatjump_set3 <= 190:
                        if dir_squat_jump_set3 == 1:
                            count_squat_jump_set3 += 0.5
                            dir_squat_jump_set3 = 0
                            cooldown_timer_squatjump_set3 = cooldown_duration_squatjump_set3
                    
                    if leftleg_squatjump_set3 >= 290:
                        if dir_squat_jump_set3 == 0:
                            count_squat_jump_set3 += 0.5
                            dir_squat_jump_set3 = 1
                            cooldown_timer_squatjump_set3 = cooldown_duration_squatjump_set3
                    elif leftleg_squatjump_set3 <= 190:
                        if dir_squat_jump_set3 == 1:
                            count_squat_jump_set3 += 0.5
                            dir_squat_jump_set3 = 0
                            cooldown_timer_squatjump_set3 = cooldown_duration_squatjump_set3


            elif orientation =='left' and orientation2 == 'left':
                if leftleg_squatjump_set3 is not None and rightleg_squatjump_set3 is not None:
                    per_right_leg_squatjump_set3 = np.interp(rightleg_squatjump_set3, (70, 150), (100, 0))
                    bar_right_leg_squatjump_set3 = np.interp(rightleg_squatjump_set3, (70, 150), (480, 680))
                    per_left_leg_squatjump_set3 = np.interp(leftleg_squatjump_set3, (70, 150), (100 ,0))
                    bar_left_leg_squatjump_set3 = np.interp(leftleg_squatjump_set3, (70, 150), (480, 680))

                    if int(per_left_leg_squatjump_set3) == 100 and int(per_right_leg_squatjump_set3) == 100:
                        color_left_leg_squatjump_set3 = (0, 255, 0)
                        color_right_leg_squatjump_set3 = (0, 255, 0)  # Change color of left leg bar to green
                    else:
                        color_left_leg_squatjump_set3 = (0, 0, 255)  # Keep color of left leg bar as red
                        color_right_leg_squatjump_set3 = (0, 0, 255)
              
                    if rightleg_squatjump_set3 <= 70:
                        if dir_squat_jump_set3 == 0:
                            count_squat_jump_set3 += 0.5
                            dir_squat_jump_set3 = 1
                            cooldown_timer_squatjump_set3 = cooldown_duration_squatjump_set3
                    elif rightleg_squatjump_set3 >= 150:
                        if dir_squat_jump_set3 == 1:
                            count_squat_jump_set3 += 0.5
                            dir_squat_jump_set3 = 0
                            cooldown_timer_squatjump_set3 = cooldown_duration_squatjump_set3

                    if leftleg_squatjump_set3 <= 70:
                        if dir_squat_jump_set3 == 0:
                            count_squat_jump_set3 += 0.5
                            dir_squat_jump_set3 = 1
                            cooldown_timer_squatjump_set3 = cooldown_duration_squatjump_set3
                    elif leftleg_squatjump_set3 >= 150:
                        if dir_squat_jump_set3 == 1:
                            count_squat_jump_set3 += 0.5
                            dir_squat_jump_set3 = 0
                            cooldown_timer_squatjump_set3 = cooldown_duration_squatjump_set3

            elif orientation == 'front' and orientation2 == 'front':
                    
                    per_right_leg_squatjump_set3 = np.interp(rightleg_squatjump_set3, (170, 280), (100, 0))
                    bar_right_leg_squatjump_set3 = np.interp(rightleg_squatjump_set3, (170, 280), (480, 680))
                    per_left_leg_squatjump_set3 = np.interp(leftleg_squatjump_set3, (170, 280), (100, 0))
                    bar_left_leg_squatjump_set3 = np.interp(leftleg_squatjump_set3, (170, 280), (480, 680))

                    if int(per_left_leg_squatjump_set3) == 100 and int(per_right_leg_squatjump_set3) == 100:
                        color_left_leg_squatjump_set3 = (0, 255, 0)
                        color_right_leg_squatjump_set3 = (0, 255, 0)  # Change color of left leg bar to green
                    else:
                        color_left_leg_squatjump_set3 = (0, 0, 255)  # Keep color of left leg bar as red
                        color_right_leg_squatjump_set3 = (0, 0, 255)  # Keep color of right leg bar as red

                    if rightleg_squatjump_set3 <= 170:
                        if dir_squat_jump_set3 == 0:
                            count_squat_jump_set3 += 0.5
                            dir_squat_jump_set3 = 1
                            cooldown_timer_squatjump_set3 = cooldown_duration_squatjump_set3
                    elif rightleg_squatjump_set3 >= 280: 
                        if dir_squat_jump_set3 == 1:
                            count_squat_jump_set3 += 0.5
                            dir_squat_jump_set3 = 0
                            cooldown_timer_squatjump_set3 = cooldown_duration_squatjump_set3
                    if leftleg_squatjump_set3 <= 170:
                        if dir_squat_jump_set3 == 0:
                            count_squat_jump_set3 += 0.5
                            dir_squat_jump_set3 = 1
                            cooldown_timer_squatjump_set3 = cooldown_duration_squatjump_set3
                    elif leftleg_squatjump_set3 >= 280:
                        if dir_squat_jump_set3 == 1:
                            count_squat_jump_set3 += 0.5
                            dir_squat_jump_set3 = 0
                            cooldown_timer_squatjump_set3 = cooldown_duration_squatjump_set3

        cvzone.putTextRect(img, 'Squat Jump SET 3', [420, 30], thickness=2, border=2, scale=2.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)
       
        # Orientation
        cv2.rectangle(img, (890, 100), (1180, 160), (0, 0, 255), -2)
        cv2.putText(img, f"Orientation: {orientation}", (900, 140), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)

        # RIGHT LEG
        cv2.putText(img, f"R {int(per_right_leg_squatjump_set3)}%", (24, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 480), (50, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_leg_squatjump_set3)), (50, 680), color_right_leg_squatjump_set3, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_left_leg_squatjump_set3)}%", (962, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 480), (995, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_leg_squatjump_set3)), (995, 680), color_left_leg_squatjump_set3, -1)

    # Counter 
    cv2.rectangle(img, (20, 20), (200, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(count_squat_jump_set3)}/5", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    # Timer
    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [390, 30], thickness=2, border=2, scale=2.5)
        display_info_squatjump_set3 = False
        exercise_mode = "rest_squatjump_set3"
        rest_squatjump_start_time_set3 = time.time()

    # Repetition
    if count_squat_jump_set3 == 5:  # Assuming 10 jumping jacks for demonstration
        cvzone.putTextRect(img, 'Exercise Complete', [390, 30], thickness=2, border=2, scale=2.5)
        display_info_squatjump_set3 = False
        exercise_mode = "rest_squatjump_set3"
        rest_squatjump_start_time_set3 = time.time()
    return img

def rest_squatjump_set3(img):
    global exercise_mode, rest_squatjump_start_time_set3, start_time_squatsidekick
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_squatjump_start_time_set3
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "squatsidekick"
        start_time_squatsidekick = time.time()
    return img 

def detect_squatsidekick(img):
    global count_squatsidekick, dir_squatsidekick, count_left_kick_squatsidekick, dir_kick_left_squatsidekick, count_right_kick_squatsidekick, dir_kick_right_squatsidekick, start_time_squatsidekick, repetition_time_squatsidekick, display_info_squatsidekick, per_left_leg_squatsidekick, bar_left_leg_squatsidekick, per_left_leg_left_kick_squatsidekick, bar_left_leg_left_kick_squatsidekick, per_right_leg_squatsidekick, bar_right_leg_squatsidekick, per_right_leg_right_kick_squatsidekick, bar_right_leg_right_kick_squatsidekick, cooldown_duration_squatsidekick, cooldown_timer_squatsidekick, color_left_leg_squatsidekick, color_right_leg_squatsidekick, color_left_leg_left_kick_squatsidekick, color_right_leg_right_kick_squatsidekick, rightleg_squatsidekick, leftleg_squatsidekick, kickleft_squatsidekick, kickright_squatsidekick, squat_completed_squatsidekick, performing_squat_squatsidekick, orientation, orientation2, exercise_mode, rest_squatsidekick_start_time

    img = cv2.resize(img, (1280, 720))

    elapsed_time = time.time() - start_time_squatsidekick
    remaining_time = max(0, 60 - elapsed_time) #repetition_time_squatsidekick

    if display_info_squatsidekick:  # Check if to display counter, bar, and percentage
        img = detector_SquatSideKick.findPose(img, False)
        lmList_squat_side_kick = detector_SquatSideKick.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_squat_side_kick) != 0:

            rightleg_squatsidekick = detector_SquatSideKick.Squat(img, 24, 26, 28, True)
            leftleg_squatsidekick = detector_SquatSideKick.Squat(img, 23, 25, 27, True)

            kickleft_squatsidekick = detector_SquatSideKick.SideKick(img, 11, 23 ,25,True)
            kickright_squatsidekick = detector_SquatSideKick.SideKick(img, 12, 24, 26, True)

            if cooldown_timer_squatsidekick > 0:
                cooldown_timer_squatsidekick -= 1

            per_right_leg_right_kick_squatsidekick = np.interp(240, (150, 240), (100, 0))
            bar_right_leg_right_kick_squatsidekick = np.interp(240, (150, 240), (200, 400))
            per_left_leg_left_kick_squatsidekick = np.interp(240, (150, 240), (100, 0))
            bar_left_leg_left_kick_squatsidekick = np.interp(240, (150, 240), (200, 400))

            per_right_leg_squatsidekick = np.interp(rightleg_squatsidekick, (150, 240), (100, 0))
            bar_right_leg_squatsidekick = np.interp(rightleg_squatsidekick, (150, 240), (480, 680))
            per_left_leg_squatsidekick = np.interp(leftleg_squatsidekick, (150, 240), (100, 0))
            bar_left_leg_squatsidekick = np.interp(leftleg_squatsidekick, (150, 240), (480, 680))

            if int(per_left_leg_squatsidekick) == 100 and int(per_right_leg_squatsidekick) == 100:
                color_left_leg_squatsidekick = (0, 255, 0) 
                color_right_leg_squatsidekick = (0, 255, 0) 
            else:
                color_left_leg_squatsidekick = (0, 0, 255)  
                color_right_leg_squatsidekick = (0, 0, 255) 

            if performing_squat_squatsidekick:
                if rightleg_squatsidekick <= 160 and leftleg_squatsidekick <= 160:
                    if dir_squatsidekick == 0:
                        count_squatsidekick += 0.5
                        dir_squatsidekick = 1
                        cooldown_timer_squatsidekick = cooldown_duration_squatsidekick
                elif rightleg_squatsidekick >= 240 and leftleg_squatsidekick >= 240: 
                    if dir_squatsidekick == 1:
                        count_squatsidekick += 0.5
                        dir_squatsidekick = 0
                        cooldown_timer_squatsidekick = cooldown_duration_squatsidekick
                        squat_completed_squatsidekick = True
                        performing_squat_squatsidekick = False

            if squat_completed_squatsidekick:
                performing_squat_squatsidekick = True
                per_right_leg_squatsidekick = np.interp(240, (150, 240), (100, 0))
                bar_right_leg_squatsidekick = np.interp(240, (150, 240), (480, 680))
                per_left_leg_squatsidekick = np.interp(240, (150, 240), (100, 0))
                bar_left_leg_squatsidekick = np.interp(240, (150, 240), (480, 680))
                    
                per_right_leg_right_kick_squatsidekick = np.interp(kickright_squatsidekick, (180, 250), (0, 100))
                bar_right_leg_right_kick_squatsidekick = np.interp(kickright_squatsidekick, (180, 250), (400, 200))
                per_left_leg_left_kick_squatsidekick = np.interp(kickleft_squatsidekick, (100, 160), (100, 0))
                bar_left_leg_left_kick_squatsidekick = np.interp(kickleft_squatsidekick, (100, 160), (200, 400))

                if int(per_left_leg_left_kick_squatsidekick) == 100:
                    color_left_leg_left_kick_squatsidekick = (0, 255, 0) 
                elif int (per_right_leg_right_kick_squatsidekick) == 100:
                    color_right_leg_right_kick_squatsidekick = (0, 255, 0)
                else:
                    color_left_leg_left_kick_squatsidekick = (0, 0, 255)  
                    color_right_leg_right_kick_squatsidekick = (0, 0, 255)

                if kickright_squatsidekick >= 250:
                    if dir_kick_right_squatsidekick == 0:
                        count_right_kick_squatsidekick += 0.5
                        dir_kick_right_squatsidekick = 1
                elif kickright_squatsidekick <= 190:
                    if dir_kick_right_squatsidekick == 1:
                        count_right_kick_squatsidekick += 0.5
                        dir_kick_right_squatsidekick = 0
                        performing_squat_squatsidekick = True
                        squat_completed_squatsidekick = False
                if kickleft_squatsidekick <= 100:
                    if dir_kick_left_squatsidekick == 0:
                        count_left_kick_squatsidekick += 0.5
                        dir_kick_left_squatsidekick = 1
                
                elif kickleft_squatsidekick >= 160:
                    if dir_kick_left_squatsidekick == 1:
                        count_left_kick_squatsidekick += 0.5
                        dir_kick_left_squatsidekick = 0
                        performing_squat_squatsidekick = True
                        squat_completed_squatsidekick = False


        cvzone.putTextRect(img, 'Squat Side Kick', [420, 30], thickness=2, border=2, scale=2)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        cv2.putText(img, f"R {int(per_right_leg_right_kick_squatsidekick)}%", (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_leg_right_kick_squatsidekick)), (50, 400), color_right_leg_right_kick_squatsidekick, -1)

        # ARM LEFT
        cv2.putText(img, f"L {int(per_left_leg_left_kick_squatsidekick)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_leg_left_kick_squatsidekick)), (995, 400), color_left_leg_left_kick_squatsidekick, -1)

        # RIGHT LEG
        cv2.putText(img, f"R {int(per_right_leg_squatsidekick)}%", (24, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 480), (50, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_leg_squatsidekick)), (50, 680), color_right_leg_squatsidekick, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_left_leg_squatsidekick)}%", (962, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 480), (995, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_leg_squatsidekick)), (995, 680), color_left_leg_squatsidekick, -1)

    # Counter 
    cv2.rectangle(img, (20, 10), (370, 90), (0, 100, 0), -1)  # Adjusted rectangle size
    cv2.putText(img, f"{int(count_squatsidekick)}/10", (145, 65), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.5, (255, 255, 255), 4)  # Adjusted text position and size

    cv2.rectangle(img, (20, 100), (180, 150), (255, 0, 0), -1)  # Adjusted rectangle size
    cv2.putText(img, f"{int(count_right_kick_squatsidekick)}/5", (70, 135), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.0, (255, 255, 255), 4)  # Adjusted text position and size

    cv2.rectangle(img, (190, 100), (370, 150), (0, 0, 255), -1) 
    cv2.putText(img, f"{int(count_left_kick_squatsidekick)}/5", (250, 135), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.0, (255, 255, 255), 4)  # Adjusted text position and size

    #Timer
    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [420, 30], thickness=2, border=2, scale=2.5)
        display_info_squatsidekick = False
        exercise_mode = "rest_squatsidekick"
        rest_squatsidekick_start_time = time.time()

    # Repetition
    if count_squatsidekick == 10 and count_right_kick_squatsidekick == 5 and count_left_kick_squatsidekick == 5:  # Assuming 10 jumping jacks for demonstration
        cvzone.putTextRect(img, 'Exercise Complete', [420, 30], thickness=2, border=2, scale=2.5)
        display_info_squatsidekick = False
        exercise_mode = "rest_squatsidekick"
        rest_squatsidekick_start_time = time.time()

    return img

def rest_squatsidekick(img):
    global exercise_mode, rest_squatsidekick_start_time, start_time_squatsidekick_set2
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_squatsidekick_start_time
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "squatsidekick_set2"
        start_time_squatsidekick_set2 = time.time()
    return img
    
def detect_squatsidekick_set2(img):
    global count_squatsidekick_set2, dir_squatsidekick_set2, count_left_kick_squatsidekick_set2, dir_kick_left_squatsidekick_set2, count_right_kick_squatsidekick_set2, dir_kick_right_squatsidekick_set2, start_time_squatsidekick_set2, repetition_time_squatsidekick_set2, display_info_squatsidekick_set2, per_left_leg_squatsidekick_set2, bar_left_leg_squatsidekick_set2, per_left_leg_left_kick_squatsidekick_set2, bar_left_leg_left_kick_squatsidekick_set2, per_right_leg_squatsidekick_set2, bar_right_leg_squatsidekick_set2, per_right_leg_right_kick_squatsidekick_set2, bar_right_leg_right_kick_squatsidekick_set2, cooldown_duration_squatsidekick_set2, cooldown_timer_squatsidekick_set2, color_left_leg_squatsidekick_set2, color_right_leg_squatsidekick_set2, color_left_leg_left_kick_squatsidekick_set2, color_right_leg_right_kick_squatsidekick_set2, rightleg_squatsidekick_set2, leftleg_squatsidekick_set2, kickleft_squatsidekick_set2, kickright_squatsidekick_set2, squat_completed_squatsidekick_set2, performing_squat_squatsidekick_set2, orientation, orientation2, exercise_mode, rest_squatsidekick_start_time_set2

    img = cv2.resize(img, (1280, 720))

    elapsed_time = time.time() - start_time_squatsidekick_set2
    remaining_time = max(0, 60 - elapsed_time) #repetition_time_squatsidekick

    if display_info_squatsidekick_set2:  # Check if to display counter, bar, and percentage
        img = detector_SquatSideKick.findPose(img, False)
        lmList_squat_side_kick = detector_SquatSideKick.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_squat_side_kick) != 0:

            rightleg_squatsidekick_set2 = detector_SquatSideKick.Squat(img, 24, 26, 28, True)
            leftleg_squatsidekick_set2 = detector_SquatSideKick.Squat(img, 23, 25, 27, True)

            kickleft_squatsidekick_set2 = detector_SquatSideKick.SideKick(img, 11, 23 ,25,True)
            kickright_squatsidekick_set2 = detector_SquatSideKick.SideKick(img, 12, 24, 26, True)

            if cooldown_timer_squatsidekick_set2 > 0:
                cooldown_timer_squatsidekick_set2 -= 1

            per_right_leg_right_kick_squatsidekick_set2 = np.interp(240, (150, 240), (100, 0))
            bar_right_leg_right_kick_squatsidekick_set2 = np.interp(240, (150, 240), (200, 400))
            per_left_leg_left_kick_squatsidekick_set2 = np.interp(240, (150, 240), (100, 0))
            bar_left_leg_left_kick_squatsidekick_set2 = np.interp(240, (150, 240), (200, 400))

            per_right_leg_squatsidekick_set2 = np.interp(rightleg_squatsidekick_set2, (150, 240), (100, 0))
            bar_right_leg_squatsidekick_set2 = np.interp(rightleg_squatsidekick_set2, (150, 240), (480, 680))
            per_left_leg_squatsidekick_set2 = np.interp(leftleg_squatsidekick_set2, (150, 240), (100, 0))
            bar_left_leg_squatsidekick_set2 = np.interp(leftleg_squatsidekick_set2, (150, 240), (480, 680))

            if int(per_left_leg_squatsidekick_set2) == 100 and int(per_right_leg_squatsidekick_set2) == 100:
                color_left_leg_squatsidekick_set2 = (0, 255, 0) 
                color_right_leg_squatsidekick_set2 = (0, 255, 0) 
            else:
                color_left_leg_squatsidekick_set2 = (0, 0, 255)  
                color_right_leg_squatsidekick_set2 = (0, 0, 255) 

            if performing_squat_squatsidekick_set2:
                if rightleg_squatsidekick_set2 <= 160 and leftleg_squatsidekick_set2 <= 160:
                    if dir_squatsidekick_set2 == 0:
                        count_squatsidekick_set2 += 0.5
                        dir_squatsidekick_set2 = 1
                        cooldown_timer_squatsidekick_set2 = cooldown_duration_squatsidekick_set2
                elif rightleg_squatsidekick_set2 >= 240 and leftleg_squatsidekick_set2 >= 240: 
                    if dir_squatsidekick_set2 == 1:
                        count_squatsidekick_set2 += 0.5
                        dir_squatsidekick_set2 = 0
                        cooldown_timer_squatsidekick_set2 = cooldown_duration_squatsidekick_set2
                        squat_completed_squatsidekick_set2 = True
                        performing_squat_squatsidekick_set2 = False

            if squat_completed_squatsidekick_set2:
                performing_squat_squatsidekick_set2 = True
                per_right_leg_squatsidekick_set2 = np.interp(240, (150, 240), (100, 0))
                bar_right_leg_squatsidekick_set2 = np.interp(240, (150, 240), (480, 680))
                per_left_leg_squatsidekick_set2 = np.interp(240, (150, 240), (100, 0))
                bar_left_leg_squatsidekick_set2 = np.interp(240, (150, 240), (480, 680))
                    
                per_right_leg_right_kick_squatsidekick_set2 = np.interp(kickright_squatsidekick_set2, (180, 250), (0, 100))
                bar_right_leg_right_kick_squatsidekick_set2 = np.interp(kickright_squatsidekick_set2, (180, 250), (400, 200))
                per_left_leg_left_kick_squatsidekick_set2 = np.interp(kickleft_squatsidekick_set2, (100, 160), (100, 0))
                bar_left_leg_left_kick_squatsidekick_set2 = np.interp(kickleft_squatsidekick_set2, (100, 160), (200, 400))

                if int(per_left_leg_left_kick_squatsidekick_set2) == 100:
                    color_left_leg_left_kick_squatsidekick_set2 = (0, 255, 0) 
                elif int (per_right_leg_right_kick_squatsidekick_set2) == 100:
                    color_right_leg_right_kick_squatsidekick_set2 = (0, 255, 0)
                else:
                    color_left_leg_left_kick_squatsidekick_set2 = (0, 0, 255)  
                    color_right_leg_right_kick_squatsidekick_set2 = (0, 0, 255)

                if kickright_squatsidekick_set2 >= 250:
                    if dir_kick_right_squatsidekick_set2 == 0:
                        count_right_kick_squatsidekick_set2 += 0.5
                        dir_kick_right_squatsidekick_set2 = 1
                elif kickright_squatsidekick_set2 <= 190:
                    if dir_kick_right_squatsidekick_set2 == 1:
                        count_right_kick_squatsidekick_set2 += 0.5
                        dir_kick_right_squatsidekick_set2 = 0
                        performing_squat_squatsidekick_set2 = True
                        squat_completed_squatsidekick_set2 = False
                if kickleft_squatsidekick_set2 <= 100:
                    if dir_kick_left_squatsidekick_set2 == 0:
                        count_left_kick_squatsidekick_set2 += 0.5
                        dir_kick_left_squatsidekick_set2 = 1
                
                elif kickleft_squatsidekick_set2 >= 160:
                    if dir_kick_left_squatsidekick_set2 == 1:
                        count_left_kick_squatsidekick_set2 += 0.5
                        dir_kick_left_squatsidekick_set2 = 0
                        performing_squat_squatsidekick_set2 = True
                        squat_completed_squatsidekick_set2 = False


        cvzone.putTextRect(img, 'Squat Side Kick SET 2', [420, 30], thickness=2, border=2, scale=2)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        cv2.putText(img, f"R {int(per_right_leg_right_kick_squatsidekick_set2)}%", (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_leg_right_kick_squatsidekick_set2)), (50, 400), color_right_leg_right_kick_squatsidekick_set2, -1)

        # ARM LEFT
        cv2.putText(img, f"L {int(per_left_leg_left_kick_squatsidekick_set2)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_leg_left_kick_squatsidekick_set2)), (995, 400), color_left_leg_left_kick_squatsidekick_set2, -1)

        # RIGHT LEG
        cv2.putText(img, f"R {int(per_right_leg_squatsidekick_set2)}%", (24, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 480), (50, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_leg_squatsidekick_set2)), (50, 680), color_right_leg_squatsidekick_set2, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_left_leg_squatsidekick_set2)}%", (962, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 480), (995, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_leg_squatsidekick_set2)), (995, 680), color_left_leg_squatsidekick_set2, -1)

    # Counter 
    cv2.rectangle(img, (20, 10), (370, 90), (0, 100, 0), -1)  # Adjusted rectangle size
    cv2.putText(img, f"{int(count_squatsidekick_set2)}/10", (145, 65), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.5, (255, 255, 255), 4)  # Adjusted text position and size

    cv2.rectangle(img, (20, 100), (180, 150), (255, 0, 0), -1)  # Adjusted rectangle size
    cv2.putText(img, f"{int(count_right_kick_squatsidekick_set2)}/5", (70, 135), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.0, (255, 255, 255), 4)  # Adjusted text position and size

    cv2.rectangle(img, (190, 100), (370, 150), (0, 0, 255), -1) 
    cv2.putText(img, f"{int(count_left_kick_squatsidekick_set2)}/5", (250, 135), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.0, (255, 255, 255), 4)  # Adjusted text position and size

    #Timer
    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [420, 30], thickness=2, border=2, scale=2.5)
        display_info_squatsidekick_set2 = False
        exercise_mode = "rest_squatsidekick_set2"
        rest_squatsidekick_start_time_set2 = time.time()

    # Repetition
    if count_squatsidekick_set2 == 10 and count_right_kick_squatsidekick_set2 == 5 and count_left_kick_squatsidekick_set2 == 5:  # Assuming 10 jumping jacks for demonstration
        cvzone.putTextRect(img, 'Exercise Complete', [420, 30], thickness=2, border=2, scale=2.5)
        display_info_squatsidekick_set2 = False
        exercise_mode = "rest_squatsidekick_set2"
        rest_squatsidekick_start_time_set2 = time.time()
        
    return img

def rest_squatsidekick_set2(img):
    global exercise_mode, rest_squatsidekick_start_time_set2, start_time_squatsidekick_set3
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_squatsidekick_start_time_set2
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "squatsidekick_set3"
        start_time_squatsidekick_set3 = time.time()
    return img

def detect_squatsidekick_set3(img):
    global count_squatsidekick_set3, dir_squatsidekick_set3, count_left_kick_squatsidekick_set3, dir_kick_left_squatsidekick_set3, count_right_kick_squatsidekick_set3, dir_kick_right_squatsidekick_set3, start_time_squatsidekick_set3, repetition_time_squatsidekick_set3, display_info_squatsidekick_set3, per_left_leg_squatsidekick_set3, bar_left_leg_squatsidekick_set3, per_left_leg_left_kick_squatsidekick_set3, bar_left_leg_left_kick_squatsidekick_set3, per_right_leg_squatsidekick_set3, bar_right_leg_squatsidekick_set3, per_right_leg_right_kick_squatsidekick_set3, bar_right_leg_right_kick_squatsidekick_set3, cooldown_duration_squatsidekick_set3, cooldown_timer_squatsidekick_set3, color_left_leg_squatsidekick_set3, color_right_leg_squatsidekick_set3, color_left_leg_left_kick_squatsidekick_set3, color_right_leg_right_kick_squatsidekick_set3, rightleg_squatsidekick_set3, leftleg_squatsidekick_set3, kickleft_squatsidekick_set3, kickright_squatsidekick_set3, squat_completed_squatsidekick_set3, performing_squat_squatsidekick_set3, orientation, orientation2, exercise_mode, rest_squatsidekick_start_time_set3

    img = cv2.resize(img, (1280, 720))

    elapsed_time = time.time() - start_time_squatsidekick_set3
    remaining_time = max(0, 60 - elapsed_time) #repetition_time_squatsidekick

    if display_info_squatsidekick_set3:  # Check if to display counter, bar, and percentage
        img = detector_SquatSideKick.findPose(img, False)
        lmList_squat_side_kick = detector_SquatSideKick.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_squat_side_kick) != 0:

            rightleg_squatsidekick_set3 = detector_SquatSideKick.Squat(img, 24, 26, 28, True)
            leftleg_squatsidekick_set3 = detector_SquatSideKick.Squat(img, 23, 25, 27, True)

            kickleft_squatsidekick_set3 = detector_SquatSideKick.SideKick(img, 11, 23 ,25,True)
            kickright_squatsidekick_set3 = detector_SquatSideKick.SideKick(img, 12, 24, 26, True)

            if cooldown_timer_squatsidekick_set3 > 0:
                cooldown_timer_squatsidekick_set3 -= 1

            per_right_leg_right_kick_squatsidekick_set3 = np.interp(240, (150, 240), (100, 0))
            bar_right_leg_right_kick_squatsidekick_set3 = np.interp(240, (150, 240), (200, 400))
            per_left_leg_left_kick_squatsidekick_set3 = np.interp(240, (150, 240), (100, 0))
            bar_left_leg_left_kick_squatsidekick_set3 = np.interp(240, (150, 240), (200, 400))

            per_right_leg_squatsidekick_set3 = np.interp(rightleg_squatsidekick_set3, (150, 240), (100, 0))
            bar_right_leg_squatsidekick_set3 = np.interp(rightleg_squatsidekick_set3, (150, 240), (480, 680))
            per_left_leg_squatsidekick_set3 = np.interp(leftleg_squatsidekick_set3, (150, 240), (100, 0))
            bar_left_leg_squatsidekick_set3 = np.interp(leftleg_squatsidekick_set3, (150, 240), (480, 680))

            if int(per_left_leg_squatsidekick_set3) == 100 and int(per_right_leg_squatsidekick_set3) == 100:
                color_left_leg_squatsidekick_set3 = (0, 255, 0) 
                color_right_leg_squatsidekick_set3 = (0, 255, 0) 
            else:
                color_left_leg_squatsidekick_set3 = (0, 0, 255)  
                color_right_leg_squatsidekick_set3 = (0, 0, 255) 

            if performing_squat_squatsidekick_set3:
                if rightleg_squatsidekick_set3 <= 160 and leftleg_squatsidekick_set3 <= 160:
                    if dir_squatsidekick_set3 == 0:
                        count_squatsidekick_set3 += 0.5
                        dir_squatsidekick_set3 = 1
                        cooldown_timer_squatsidekick_set3 = cooldown_duration_squatsidekick_set3
                elif rightleg_squatsidekick_set3 >= 240 and leftleg_squatsidekick_set3 >= 240: 
                    if dir_squatsidekick_set3 == 1:
                        count_squatsidekick_set3 += 0.5
                        dir_squatsidekick_set3 = 0
                        cooldown_timer_squatsidekick_set3 = cooldown_duration_squatsidekick_set3
                        squat_completed_squatsidekick_set3 = True
                        performing_squat_squatsidekick_set3 = False

            if squat_completed_squatsidekick_set3:
                performing_squat_squatsidekick_set3 = True
                per_right_leg_squatsidekick_set3 = np.interp(240, (150, 240), (100, 0))
                bar_right_leg_squatsidekick_set3 = np.interp(240, (150, 240), (480, 680))
                per_left_leg_squatsidekick_set3 = np.interp(240, (150, 240), (100, 0))
                bar_left_leg_squatsidekick_set3 = np.interp(240, (150, 240), (480, 680))
                    
                per_right_leg_right_kick_squatsidekick_set3 = np.interp(kickright_squatsidekick_set3, (180, 250), (0, 100))
                bar_right_leg_right_kick_squatsidekick_set3 = np.interp(kickright_squatsidekick_set3, (180, 250), (400, 200))
                per_left_leg_left_kick_squatsidekick_set3 = np.interp(kickleft_squatsidekick_set3, (100, 160), (100, 0))
                bar_left_leg_left_kick_squatsidekick_set3 = np.interp(kickleft_squatsidekick_set3, (100, 160), (200, 400))

                if int(per_left_leg_left_kick_squatsidekick_set3) == 100:
                    color_left_leg_left_kick_squatsidekick_set3 = (0, 255, 0) 
                elif int (per_right_leg_right_kick_squatsidekick_set3) == 100:
                    color_right_leg_right_kick_squatsidekick_set3 = (0, 255, 0)
                else:
                    color_left_leg_left_kick_squatsidekick_set3 = (0, 0, 255)  
                    color_right_leg_right_kick_squatsidekick_set3 = (0, 0, 255)

                if kickright_squatsidekick_set3 >= 250:
                    if dir_kick_right_squatsidekick_set3 == 0:
                        count_right_kick_squatsidekick_set3 += 0.5
                        dir_kick_right_squatsidekick_set3 = 1
                elif kickright_squatsidekick_set3 <= 190:
                    if dir_kick_right_squatsidekick_set3 == 1:
                        count_right_kick_squatsidekick_set3 += 0.5
                        dir_kick_right_squatsidekick_set3 = 0
                        performing_squat_squatsidekick_set3 = True
                        squat_completed_squatsidekick_set3 = False
                if kickleft_squatsidekick_set3 <= 100:
                    if dir_kick_left_squatsidekick_set3 == 0:
                        count_left_kick_squatsidekick_set3 += 0.5
                        dir_kick_left_squatsidekick_set3 = 1
                
                elif kickleft_squatsidekick_set3 >= 160:
                    if dir_kick_left_squatsidekick_set3 == 1:
                        count_left_kick_squatsidekick_set3 += 0.5
                        dir_kick_left_squatsidekick_set3 = 0
                        performing_squat_squatsidekick_set3 = True
                        squat_completed_squatsidekick_set3 = False


        cvzone.putTextRect(img, 'Squat Side Kick SET 3', [420, 30], thickness=2, border=2, scale=2)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        cv2.putText(img, f"R {int(per_right_leg_right_kick_squatsidekick_set3)}%", (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_leg_right_kick_squatsidekick_set3)), (50, 400), color_right_leg_right_kick_squatsidekick_set3, -1)

        # ARM LEFT
        cv2.putText(img, f"L {int(per_left_leg_left_kick_squatsidekick_set3)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_leg_left_kick_squatsidekick_set3)), (995, 400), color_left_leg_left_kick_squatsidekick_set3, -1)

        # RIGHT LEG
        cv2.putText(img, f"R {int(per_right_leg_squatsidekick_set3)}%", (24, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 480), (50, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_leg_squatsidekick_set3)), (50, 680), color_right_leg_squatsidekick_set3, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_left_leg_squatsidekick_set3)}%", (962, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 480), (995, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_leg_squatsidekick_set3)), (995, 680), color_left_leg_squatsidekick_set3, -1)

    # Counter 
    cv2.rectangle(img, (20, 10), (370, 90), (0, 100, 0), -1)  # Adjusted rectangle size
    cv2.putText(img, f"{int(count_squatsidekick_set3)}/10", (145, 65), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.5, (255, 255, 255), 4)  # Adjusted text position and size

    cv2.rectangle(img, (20, 100), (180, 150), (255, 0, 0), -1)  # Adjusted rectangle size
    cv2.putText(img, f"{int(count_right_kick_squatsidekick_set3)}/5", (70, 135), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.0, (255, 255, 255), 4)  # Adjusted text position and size

    cv2.rectangle(img, (190, 100), (370, 150), (0, 0, 255), -1) 
    cv2.putText(img, f"{int(count_left_kick_squatsidekick_set3)}/5", (250, 135), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.0, (255, 255, 255), 4)  # Adjusted text position and size

    #Timer
    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [420, 30], thickness=2, border=2, scale=2.5)
        display_info_squatsidekick_set3 = False
        exercise_mode = "rest_squatsidekick_set3"
        rest_squatsidekick_start_time_set3 = time.time()

    # Repetition
    if count_squatsidekick_set3 == 10 and count_right_kick_squatsidekick_set3 == 5 and count_left_kick_squatsidekick_set3 == 5:  # Assuming 10 jumping jacks for demonstration
        cvzone.putTextRect(img, 'Exercise Complete', [420, 30], thickness=2, border=2, scale=2.5)
        display_info_squatsidekick_set3 = False
        exercise_mode = "rest_squatsidekick_set3"
        rest_squatsidekick_start_time_set3 = time.time()
    return img

def rest_squatsidekick_set3(img):
    global exercise_mode, rest_squatsidekick_start_time_set3, start_time_jumpinglunge
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_squatsidekick_start_time_set3
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "jumpinglunge"
        start_time_jumpinglunge = time.time()
    return img

def detect_jumpinglunge(img):
    global count_alternating_right_lunge_jumpinglunge, count_alternating_left_lunge_jumpinglunge, dir_alternating_left_lunge_jumpinglunge, dir_alternating_right_lunge_jumpinglunge, start_time_jumpinglunge, repetition_time_jumpinglunge, display_info_jumpinglunge, per_left_leg_jumpinglunge, bar_left_leg_jumpinglunge, per_right_leg_jumpinglunge, bar_right_leg_jumpinglunge, cooldown_duration_jumpinglunge, cooldown_timer_jumpinglunge, color_left_leg_jumpinglunge, color_right_leg_jumpinglunge, orientation, orientation2, exercise_mode, rest_jumpinglunge_start_time

    img = cv2.resize(img, (1280, 720))

    elapsed_time = time.time() - start_time_jumpinglunge
    remaining_time = max(0, 60 - elapsed_time) #repetition_time_jumpinglunge

    if display_info_jumpinglunge:  # Check if to display counter, bar, and percentage
        img = detector_jumpinglunge.findPose(img, False)
        lmList_jumping_jacks = detector_jumpinglunge.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_jumping_jacks) != 0:

            # Right and Left keypoints
            rightleg_jumpinglunge, orientation = detector_jumpinglunge.JumpingLunge(img, 24, 26, 28, True)
            leftleg_jumpinglunge, orientation2 = detector_jumpinglunge.JumpingLunge(img, 23, 25, 27, True)

            if cooldown_timer_jumpinglunge > 0:
                cooldown_timer_jumpinglunge -= 1

        
            if orientation == 'right' and orientation2 == 'right':
                    per_right_leg_jumpinglunge = np.interp(rightleg_jumpinglunge, (90, 170), (100, 0))
                    bar_right_leg_jumpinglunge = np.interp(rightleg_jumpinglunge, (90, 170), (480, 680))
                    per_left_leg_jumpinglunge = np.interp(leftleg_jumpinglunge, (90, 170), (100, 0))
                    bar_left_leg_jumpinglunge = np.interp(leftleg_jumpinglunge, (90, 170), (480, 680))

                    if int(per_left_leg_jumpinglunge) == 100:
                        color_left_leg_jumpinglunge = (0, 255, 0)  # Change color of left leg bar to green
                    elif int(per_right_leg_jumpinglunge) == 100:
                        color_right_leg_jumpinglunge = (0, 255, 0)
                    else:
                        color_left_leg_jumpinglunge = (0, 0, 255)  # Keep color of left leg bar as red
                        color_right_leg_jumpinglunge = (0, 0, 255)

                    if rightleg_jumpinglunge <= 90:
                        if dir_alternating_right_lunge_jumpinglunge == 0 and count_alternating_right_lunge_jumpinglunge <= 5:
                            count_alternating_right_lunge_jumpinglunge += 0.5
                            if count_alternating_right_lunge_jumpinglunge == 5:
                                dir_alternating_left_lunge_jumpinglunge = 1
                            else:
                                dir_alternating_right_lunge_jumpinglunge = 1
                                cooldown_timer_jumpinglunge = cooldown_duration_jumpinglunge
                    elif rightleg_jumpinglunge >= 150:
                        if dir_alternating_right_lunge_jumpinglunge == 1 and count_alternating_right_lunge_jumpinglunge <= 5:
                            count_alternating_right_lunge_jumpinglunge += 0.5
                            if count_alternating_right_lunge_jumpinglunge == 5:
                                dir_alternating_right_lunge_jumpinglunge = 1
                            else:
                                dir_alternating_right_lunge_jumpinglunge = 0
                                cooldown_timer_jumpinglunge = cooldown_duration_jumpinglunge
                    
                    if leftleg_jumpinglunge <= 90:
                        if dir_alternating_left_lunge_jumpinglunge == 0 and count_alternating_left_lunge_jumpinglunge <= 5:
                            count_alternating_left_lunge_jumpinglunge += 0.5
                            if count_alternating_left_lunge_jumpinglunge == 5:
                                dir_alternating_left_lunge_jumpinglunge = 0
                            else:
                                dir_alternating_left_lunge_jumpinglunge = 1
                                cooldown_timer_jumpinglunge = cooldown_duration_jumpinglunge
                    elif leftleg_jumpinglunge >= 150:
                        if dir_alternating_left_lunge_jumpinglunge == 1 and count_alternating_left_lunge_jumpinglunge <= 5:
                            count_alternating_left_lunge_jumpinglunge += 0.5
                            if count_alternating_left_lunge_jumpinglunge == 5:
                                dir_alternating_left_lunge_jumpinglunge = 1
                            else:
                                dir_alternating_left_lunge_jumpinglunge = 0
                                cooldown_timer_jumpinglunge = cooldown_duration_jumpinglunge


            elif orientation =='left' and orientation2 == 'left':
                if leftleg_jumpinglunge is not None and rightleg_jumpinglunge is not None:
                    per_right_leg_jumpinglunge = np.interp(rightleg_jumpinglunge, (190, 280), (0, 100))
                    bar_right_leg_jumpinglunge = np.interp(rightleg_jumpinglunge, (190, 280), (680, 480))
                    per_left_leg_jumpinglunge = np.interp(leftleg_jumpinglunge, (190, 280), (0, 100))
                    bar_left_leg_jumpinglunge = np.interp(leftleg_jumpinglunge, (190, 280), (680, 480))

                    if int(per_left_leg_jumpinglunge) == 100:
                        color_left_leg_jumpinglunge = (0, 255, 0)  # Change color of left leg bar to green
                    elif int(per_right_leg_jumpinglunge) == 100:
                        color_right_leg_jumpinglunge = (0, 255, 0)
                    else:
                        color_left_leg_jumpinglunge = (0, 0, 255)  # Keep color of left leg bar as red
                        color_right_leg_jumpinglunge = (0, 0, 255)
              
                    if rightleg_jumpinglunge >= 280:
                        if dir_alternating_right_lunge_jumpinglunge == 0 and count_alternating_right_lunge_jumpinglunge <= 5:
                            count_alternating_right_lunge_jumpinglunge += 0.5
                            if count_alternating_right_lunge_jumpinglunge == 5:
                                dir_alternating_right_lunge_jumpinglunge = 0
                            else:
                                dir_alternating_right_lunge_jumpinglunge = 1
                                cooldown_timer_jumpinglunge = cooldown_duration_jumpinglunge
                    elif rightleg_jumpinglunge <= 190:
                        if dir_alternating_right_lunge_jumpinglunge == 1 and count_alternating_right_lunge_jumpinglunge <= 5:
                            count_alternating_right_lunge_jumpinglunge += 0.5
                            if count_alternating_right_lunge_jumpinglunge == 5:
                                dir_alternating_right_lunge_jumpinglunge = 1
                            else:
                                dir_alternating_right_lunge_jumpinglunge = 0
                                cooldown_timer_jumpinglunge = cooldown_duration_jumpinglunge

                    if leftleg_jumpinglunge >= 280:
                        if dir_alternating_left_lunge_jumpinglunge == 0 and count_alternating_left_lunge_jumpinglunge <= 5:
                            count_alternating_left_lunge_jumpinglunge += 0.5
                            if count_alternating_left_lunge_jumpinglunge == 5:
                                dir_alternating_left_lunge_jumpinglunge = 0
                            else:
                                dir_alternating_left_lunge_jumpinglunge = 1
                                cooldown_timer_jumpinglunge = cooldown_duration_jumpinglunge
                    elif leftleg_jumpinglunge <= 190:
                        if dir_alternating_left_lunge_jumpinglunge == 1 and count_alternating_left_lunge_jumpinglunge <= 5:
                            count_alternating_left_lunge_jumpinglunge += 0.5
                            if count_alternating_left_lunge_jumpinglunge == 5:
                                dir_alternating_left_lunge_jumpinglunge = 1
                            else:
                                dir_alternating_left_lunge_jumpinglunge = 0
                                cooldown_timer_jumpinglunge = cooldown_duration_jumpinglunge

            elif orientation == 'front' and orientation2 == 'front':
                    
                    per_right_leg_jumpinglunge = np.interp(rightleg_jumpinglunge, (100, 200), (100, 0))
                    bar_right_leg_jumpinglunge = np.interp(rightleg_jumpinglunge, (100, 200), (480, 680))
                    per_left_leg_jumpinglunge = np.interp(leftleg_jumpinglunge, (100, 200), (100, 0))
                    bar_left_leg_jumpinglunge = np.interp(leftleg_jumpinglunge, (100, 200), (480, 680))

                    if int(per_left_leg_jumpinglunge) == 100:
                        color_left_leg_jumpinglunge = (0, 255, 0)  # Change color of left leg bar to green
                    elif int(per_right_leg_jumpinglunge) == 100:
                        color_right_leg_jumpinglunge = (0, 255, 0)
                    else:
                        color_left_leg_jumpinglunge = (0, 0, 255)  # Keep color of left leg bar as red
                        color_right_leg_jumpinglunge = (0, 0, 255)  # Keep color of right leg bar as red

                    
                    if rightleg_jumpinglunge <= 150 and leftleg_jumpinglunge <= 100:
                        if dir_alternating_right_lunge_jumpinglunge == 0 and count_alternating_right_lunge_jumpinglunge <= 5:
                            count_alternating_right_lunge_jumpinglunge += 0.5
                            if count_alternating_right_lunge_jumpinglunge == 5:
                                dir_alternating_right_lunge_jumpinglunge = 0
                            else:
                                dir_alternating_right_lunge_jumpinglunge = 1
                                cooldown_timer_jumpinglunge = cooldown_duration_jumpinglunge
                    else: 
                        if dir_alternating_right_lunge_jumpinglunge == 1 and count_alternating_right_lunge_jumpinglunge <= 5:
                            count_alternating_right_lunge_jumpinglunge += 0.5
                            if count_alternating_right_lunge_jumpinglunge == 5:
                                dir_alternating_right_lunge_jumpinglunge = 1
                            else:
                                dir_alternating_right_lunge_jumpinglunge = 0
                                cooldown_timer_jumpinglunge = cooldown_duration_jumpinglunge

                    if rightleg_jumpinglunge <= 100 and leftleg_jumpinglunge <= 150:
                        if dir_alternating_left_lunge_jumpinglunge == 0 and count_alternating_left_lunge_jumpinglunge <= 5:
                            count_alternating_left_lunge_jumpinglunge += 0.5
                            if count_alternating_left_lunge_jumpinglunge == 5:
                                dir_alternating_left_lunge_jumpinglunge = 0
                            else:
                                dir_alternating_left_lunge_jumpinglunge = 1
                                cooldown_timer_jumpinglunge = cooldown_duration_jumpinglunge
                    else:
                        if dir_alternating_left_lunge_jumpinglunge == 1 and count_alternating_left_lunge_jumpinglunge <= 5:
                            count_alternating_left_lunge_jumpinglunge += 0.5
                            if count_alternating_left_lunge_jumpinglunge == 5:
                                dir_alternating_left_lunge_jumpinglunge = 1
                            else:
                                dir_alternating_left_lunge_jumpinglunge = 0
                                cooldown_timer_jumpinglunge = cooldown_duration_jumpinglunge

        cvzone.putTextRect(img, 'Jumping Lunge (alternate)', [310, 30], thickness=2, border=2, scale=2.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # Orientation
        cv2.rectangle(img, (890, 100), (1180, 160), (0, 0, 255), -2)
        cv2.putText(img, f"Orientation: {orientation}", (900, 140), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)

        # RIGHT LEG
        cv2.putText(img, f"R {int(per_right_leg_jumpinglunge)}%", (24, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 480), (50, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_leg_jumpinglunge)), (50, 680), color_right_leg_jumpinglunge, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_left_leg_jumpinglunge)}%", (962, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 480), (995, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_leg_jumpinglunge)), (995, 680), color_left_leg_jumpinglunge, -1)

    # Counter 
    cv2.rectangle(img, (20, 20), (140, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(count_alternating_right_lunge_jumpinglunge)}/5", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (150, 20), (270, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(count_alternating_left_lunge_jumpinglunge)}/5", (160, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    # Timer
    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [3390, 30], thickness=2, border=2, scale=2.5)
        display_info_jumpinglunge = False
        exercise_mode = "rest_jumpinglunge"
        rest_jumpinglunge_start_time = time.time()

    # Repetition
    if count_alternating_left_lunge_jumpinglunge >= 5 and count_alternating_right_lunge_jumpinglunge >= 5: 
        cvzone.putTextRect(img, 'Exercise Complete', [3390, 30], thickness=2, border=2, scale=2.5)
        display_info_jumpinglunge = False
        exercise_mode = "rest_jumpinglunge"
        rest_jumpinglunge_start_time = time.time()
    return img

def rest_jumpinglunge(img):
    global exercise_mode, rest_jumpinglunge_start_time, start_time_jumpinglunge_set2
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_jumpinglunge_start_time
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "jumpinglunge_set2"
        start_time_jumpinglunge_set2 = time.time()
    return img

def detect_jumpinglunge_set2(img):
    global count_alternating_right_lunge_jumpinglunge_set2, count_alternating_left_lunge_jumpinglunge_set2, dir_alternating_left_lunge_jumpinglunge_set2, dir_alternating_right_lunge_jumpinglunge_set2, start_time_jumpinglunge_set2, repetition_time_jumpinglunge_set2, display_info_jumpinglunge_set2, per_left_leg_jumpinglunge_set2, bar_left_leg_jumpinglunge_set2, per_right_leg_jumpinglunge_set2, bar_right_leg_jumpinglunge_set2, cooldown_duration_jumpinglunge_set2, cooldown_timer_jumpinglunge_set2, color_left_leg_jumpinglunge_set2, color_right_leg_jumpinglunge_set2, orientation, orientation2, exercise_mode, rest_jumpinglunge_start_time_set2

    img = cv2.resize(img, (1280, 720))

    elapsed_time = time.time() - start_time_jumpinglunge_set2
    remaining_time = max(0, 60 - elapsed_time) #repetition_time_jumpinglunge

    if display_info_jumpinglunge_set2:  # Check if to display counter, bar, and percentage
        img = detector_jumpinglunge.findPose(img, False)
        lmList_jumping_jacks = detector_jumpinglunge.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_jumping_jacks) != 0:

            # Right and Left keypoints
            rightleg_jumpinglunge_set2, orientation = detector_jumpinglunge.JumpingLunge(img, 24, 26, 28, True)
            leftleg_jumpinglunge_set2, orientation2 = detector_jumpinglunge.JumpingLunge(img, 23, 25, 27, True)

            if cooldown_timer_jumpinglunge_set2 > 0:
                cooldown_timer_jumpinglunge_set2 -= 1

        
            if orientation == 'right' and orientation2 == 'right':
                    per_right_leg_jumpinglunge_set2 = np.interp(rightleg_jumpinglunge_set2, (90, 170), (100, 0))
                    bar_right_leg_jumpinglunge_set2 = np.interp(rightleg_jumpinglunge_set2, (90, 170), (480, 680))
                    per_left_leg_jumpinglunge_set2 = np.interp(leftleg_jumpinglunge_set2, (90, 170), (100, 0))
                    bar_left_leg_jumpinglunge_set2 = np.interp(leftleg_jumpinglunge_set2, (90, 170), (480, 680))

                    if int(per_left_leg_jumpinglunge_set2) == 100:
                        color_left_leg_jumpinglunge_set2 = (0, 255, 0)  # Change color of left leg bar to green
                    elif int(per_right_leg_jumpinglunge_set2) == 100:
                        color_right_leg_jumpinglunge_set2 = (0, 255, 0)
                    else:
                        color_left_leg_jumpinglunge_set2 = (0, 0, 255)  # Keep color of left leg bar as red
                        color_right_leg_jumpinglunge_set2 = (0, 0, 255)

                    if rightleg_jumpinglunge_set2 <= 90:
                        if dir_alternating_right_lunge_jumpinglunge_set2 == 0 and count_alternating_right_lunge_jumpinglunge_set2 <= 5:
                            count_alternating_right_lunge_jumpinglunge_set2 += 0.5
                            if count_alternating_right_lunge_jumpinglunge_set2 == 5:
                                dir_alternating_left_lunge_jumpinglunge_set2 = 1
                            else:
                                dir_alternating_right_lunge_jumpinglunge_set2 = 1
                                cooldown_timer_jumpinglunge_set2 = cooldown_duration_jumpinglunge_set2
                    elif rightleg_jumpinglunge_set2 >= 150:
                        if dir_alternating_right_lunge_jumpinglunge_set2 == 1 and count_alternating_right_lunge_jumpinglunge_set2 <= 5:
                            count_alternating_right_lunge_jumpinglunge_set2 += 0.5
                            if count_alternating_right_lunge_jumpinglunge_set2 == 5:
                                dir_alternating_right_lunge_jumpinglunge_set2 = 1
                            else:
                                dir_alternating_right_lunge_jumpinglunge_set2 = 0
                                cooldown_timer_jumpinglunge_set2 = cooldown_duration_jumpinglunge_set2
                    
                    if leftleg_jumpinglunge_set2 <= 90:
                        if dir_alternating_left_lunge_jumpinglunge_set2 == 0 and count_alternating_left_lunge_jumpinglunge_set2 <= 5:
                            count_alternating_left_lunge_jumpinglunge_set2 += 0.5
                            if count_alternating_left_lunge_jumpinglunge_set2 == 5:
                                dir_alternating_left_lunge_jumpinglunge_set2 = 0
                            else:
                                dir_alternating_left_lunge_jumpinglunge_set2 = 1
                                cooldown_timer_jumpinglunge_set2 = cooldown_duration_jumpinglunge_set2
                    elif leftleg_jumpinglunge_set2 >= 150:
                        if dir_alternating_left_lunge_jumpinglunge_set2 == 1 and count_alternating_left_lunge_jumpinglunge_set2 <= 5:
                            count_alternating_left_lunge_jumpinglunge_set2 += 0.5
                            if count_alternating_left_lunge_jumpinglunge_set2 == 5:
                                dir_alternating_left_lunge_jumpinglunge_set2 = 1
                            else:
                                dir_alternating_left_lunge_jumpinglunge_set2 = 0
                                cooldown_timer_jumpinglunge_set2 = cooldown_duration_jumpinglunge_set2


            elif orientation =='left' and orientation2 == 'left':
                if leftleg_jumpinglunge_set2 is not None and rightleg_jumpinglunge_set2 is not None:
                    per_right_leg_jumpinglunge_set2 = np.interp(rightleg_jumpinglunge_set2, (190, 280), (0, 100))
                    bar_right_leg_jumpinglunge_set2 = np.interp(rightleg_jumpinglunge_set2, (190, 280), (680, 480))
                    per_left_leg_jumpinglunge_set2 = np.interp(leftleg_jumpinglunge_set2, (190, 280), (0, 100))
                    bar_left_leg_jumpinglunge_set2 = np.interp(leftleg_jumpinglunge_set2, (190, 280), (680, 480))

                    if int(per_left_leg_jumpinglunge_set2) == 100:
                        color_left_leg_jumpinglunge_set2 = (0, 255, 0)  # Change color of left leg bar to green
                    elif int(per_right_leg_jumpinglunge_set2) == 100:
                        color_right_leg_jumpinglunge_set2 = (0, 255, 0)
                    else:
                        color_left_leg_jumpinglunge_set2 = (0, 0, 255)  # Keep color of left leg bar as red
                        color_right_leg_jumpinglunge_set2 = (0, 0, 255)
              
                    if rightleg_jumpinglunge_set2 >= 280:
                        if dir_alternating_right_lunge_jumpinglunge_set2 == 0 and count_alternating_right_lunge_jumpinglunge_set2 <= 5:
                            count_alternating_right_lunge_jumpinglunge_set2 += 0.5
                            if count_alternating_right_lunge_jumpinglunge_set2 == 5:
                                dir_alternating_right_lunge_jumpinglunge_set2 = 0
                            else:
                                dir_alternating_right_lunge_jumpinglunge_set2 = 1
                                cooldown_timer_jumpinglunge_set2 = cooldown_duration_jumpinglunge_set2
                    elif rightleg_jumpinglunge_set2 <= 190:
                        if dir_alternating_right_lunge_jumpinglunge_set2 == 1 and count_alternating_right_lunge_jumpinglunge_set2 <= 5:
                            count_alternating_right_lunge_jumpinglunge_set2 += 0.5
                            if count_alternating_right_lunge_jumpinglunge_set2 == 5:
                                dir_alternating_right_lunge_jumpinglunge_set2 = 1
                            else:
                                dir_alternating_right_lunge_jumpinglunge_set2 = 0
                                cooldown_timer_jumpinglunge_set2 = cooldown_duration_jumpinglunge_set2

                    if leftleg_jumpinglunge_set2 >= 280:
                        if dir_alternating_left_lunge_jumpinglunge_set2 == 0 and count_alternating_left_lunge_jumpinglunge_set2 <= 5:
                            count_alternating_left_lunge_jumpinglunge_set2 += 0.5
                            if count_alternating_left_lunge_jumpinglunge_set2 == 5:
                                dir_alternating_left_lunge_jumpinglunge_set2 = 0
                            else:
                                dir_alternating_left_lunge_jumpinglunge_set2 = 1
                                cooldown_timer_jumpinglunge_set2 = cooldown_duration_jumpinglunge_set2
                    elif leftleg_jumpinglunge_set2 <= 190:
                        if dir_alternating_left_lunge_jumpinglunge_set2 == 1 and count_alternating_left_lunge_jumpinglunge_set2 <= 5:
                            count_alternating_left_lunge_jumpinglunge_set2 += 0.5
                            if count_alternating_left_lunge_jumpinglunge_set2 == 5:
                                dir_alternating_left_lunge_jumpinglunge_set2 = 1
                            else:
                                dir_alternating_left_lunge_jumpinglunge_set2 = 0
                                cooldown_timer_jumpinglunge_set2 = cooldown_duration_jumpinglunge_set2

            elif orientation == 'front' and orientation2 == 'front':
                    
                    per_right_leg_jumpinglunge_set2 = np.interp(rightleg_jumpinglunge_set2, (100, 200), (100, 0))
                    bar_right_leg_jumpinglunge_set2 = np.interp(rightleg_jumpinglunge_set2, (100, 200), (480, 680))
                    per_left_leg_jumpinglunge_set2 = np.interp(leftleg_jumpinglunge_set2, (100, 200), (100, 0))
                    bar_left_leg_jumpinglunge_set2 = np.interp(leftleg_jumpinglunge_set2, (100, 200), (480, 680))

                    if int(per_left_leg_jumpinglunge_set2) == 100:
                        color_left_leg_jumpinglunge_set2 = (0, 255, 0)  # Change color of left leg bar to green
                    elif int(per_right_leg_jumpinglunge_set2) == 100:
                        color_right_leg_jumpinglunge_set2 = (0, 255, 0)
                    else:
                        color_left_leg_jumpinglunge_set2 = (0, 0, 255)  # Keep color of left leg bar as red
                        color_right_leg_jumpinglunge_set2 = (0, 0, 255)  # Keep color of right leg bar as red

                    
                    if rightleg_jumpinglunge_set2 <= 150 and leftleg_jumpinglunge_set2 <= 100:
                        if dir_alternating_right_lunge_jumpinglunge_set2 == 0 and count_alternating_right_lunge_jumpinglunge_set2 <= 5:
                            count_alternating_right_lunge_jumpinglunge_set2 += 0.5
                            if count_alternating_right_lunge_jumpinglunge_set2 == 5:
                                dir_alternating_right_lunge_jumpinglunge_set2 = 0
                            else:
                                dir_alternating_right_lunge_jumpinglunge_set2 = 1
                                cooldown_timer_jumpinglunge_set2 = cooldown_duration_jumpinglunge_set2
                    else: 
                        if dir_alternating_right_lunge_jumpinglunge_set2 == 1 and count_alternating_right_lunge_jumpinglunge_set2 <= 5:
                            count_alternating_right_lunge_jumpinglunge_set2 += 0.5
                            if count_alternating_right_lunge_jumpinglunge_set2 == 5:
                                dir_alternating_right_lunge_jumpinglunge_set2 = 1
                            else:
                                dir_alternating_right_lunge_jumpinglunge_set2 = 0
                                cooldown_timer_jumpinglunge_set2 = cooldown_duration_jumpinglunge_set2

                    if rightleg_jumpinglunge_set2 <= 100 and leftleg_jumpinglunge_set2 <= 150:
                        if dir_alternating_left_lunge_jumpinglunge_set2 == 0 and count_alternating_left_lunge_jumpinglunge_set2 <= 5:
                            count_alternating_left_lunge_jumpinglunge_set2 += 0.5
                            if count_alternating_left_lunge_jumpinglunge_set2 == 5:
                                dir_alternating_left_lunge_jumpinglunge_set2 = 0
                            else:
                                dir_alternating_left_lunge_jumpinglunge_set2 = 1
                                cooldown_timer_jumpinglunge_set2 = cooldown_duration_jumpinglunge_set2
                    else:
                        if dir_alternating_left_lunge_jumpinglunge_set2 == 1 and count_alternating_left_lunge_jumpinglunge_set2 <= 5:
                            count_alternating_left_lunge_jumpinglunge_set2 += 0.5
                            if count_alternating_left_lunge_jumpinglunge_set2 == 5:
                                dir_alternating_left_lunge_jumpinglunge_set2 = 1
                            else:
                                dir_alternating_left_lunge_jumpinglunge_set2 = 0
                                cooldown_timer_jumpinglunge_set2 = cooldown_duration_jumpinglunge_set2

        cvzone.putTextRect(img, 'Jumping Lunge (alternate) SET 2', [310, 30], thickness=2, border=2, scale=2.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # Orientation
        cv2.rectangle(img, (890, 100), (1180, 160), (0, 0, 255), -2)
        cv2.putText(img, f"Orientation: {orientation}", (900, 140), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)

        # RIGHT LEG
        cv2.putText(img, f"R {int(per_right_leg_jumpinglunge_set2)}%", (24, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 480), (50, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_leg_jumpinglunge_set2)), (50, 680), color_right_leg_jumpinglunge_set2, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_left_leg_jumpinglunge_set2)}%", (962, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 480), (995, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_leg_jumpinglunge_set2)), (995, 680), color_left_leg_jumpinglunge_set2, -1)

    # Counter 
    cv2.rectangle(img, (20, 20), (140, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(count_alternating_right_lunge_jumpinglunge_set2)}/5", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (150, 20), (270, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(count_alternating_left_lunge_jumpinglunge_set2)}/5", (160, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    # Timer
    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [3390, 30], thickness=2, border=2, scale=2.5)
        display_info_jumpinglunge_set2 = False
        exercise_mode = "rest_jumpinglunge_set2"
        rest_jumpinglunge_start_time_set2 = time.time()

    # Repetition
    if count_alternating_left_lunge_jumpinglunge_set2 >= 5 and count_alternating_right_lunge_jumpinglunge_set2 >= 5: 
        cvzone.putTextRect(img, 'Exercise Complete', [3390, 30], thickness=2, border=2, scale=2.5)
        display_info_jumpinglunge_set2 = False
        exercise_mode = "rest_jumpinglunge_set2"
        rest_jumpinglunge_start_time_set2 = time.time()
    return img 

def rest_jumpinglunge_set2(img):
    global exercise_mode, rest_jumpinglunge_start_time_set2, start_time_jumpinglunge_set3
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_jumpinglunge_start_time_set2
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "jumpinglunge_set3"
        start_time_jumpinglunge_set3 = time.time()
    return img

def detect_jumpinglunge_set3(img):
    global count_alternating_right_lunge_jumpinglunge_set3, count_alternating_left_lunge_jumpinglunge_set3, dir_alternating_left_lunge_jumpinglunge_set3, dir_alternating_right_lunge_jumpinglunge_set3, start_time_jumpinglunge_set3, repetition_time_jumpinglunge_set3, display_info_jumpinglunge_set3, per_left_leg_jumpinglunge_set3, bar_left_leg_jumpinglunge_set3, per_right_leg_jumpinglunge_set3, bar_right_leg_jumpinglunge_set3, cooldown_duration_jumpinglunge_set3, cooldown_timer_jumpinglunge_set3, color_left_leg_jumpinglunge_set3, color_right_leg_jumpinglunge_set3, orientation, orientation2, exercise_mode, rest_jumpinglunge_start_time_set3

    img = cv2.resize(img, (1280, 720))

    elapsed_time = time.time() - start_time_jumpinglunge_set3
    remaining_time = max(0, 60 - elapsed_time) #repetition_time_jumpinglunge

    if display_info_jumpinglunge_set3:  # Check if to display counter, bar, and percentage
        img = detector_jumpinglunge.findPose(img, False)
        lmList_jumping_jacks = detector_jumpinglunge.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_jumping_jacks) != 0:

            # Right and Left keypoints
            rightleg_jumpinglunge_set3, orientation = detector_jumpinglunge.JumpingLunge(img, 24, 26, 28, True)
            leftleg_jumpinglunge_set3, orientation2 = detector_jumpinglunge.JumpingLunge(img, 23, 25, 27, True)

            if cooldown_timer_jumpinglunge_set3 > 0:
                cooldown_timer_jumpinglunge_set3 -= 1

        
            if orientation == 'right' and orientation2 == 'right':
                    per_right_leg_jumpinglunge_set3 = np.interp(rightleg_jumpinglunge_set3, (90, 170), (100, 0))
                    bar_right_leg_jumpinglunge_set3 = np.interp(rightleg_jumpinglunge_set3, (90, 170), (480, 680))
                    per_left_leg_jumpinglunge_set3 = np.interp(leftleg_jumpinglunge_set3, (90, 170), (100, 0))
                    bar_left_leg_jumpinglunge_set3 = np.interp(leftleg_jumpinglunge_set3, (90, 170), (480, 680))

                    if int(per_left_leg_jumpinglunge_set3) == 100:
                        color_left_leg_jumpinglunge_set3 = (0, 255, 0)  # Change color of left leg bar to green
                    elif int(per_right_leg_jumpinglunge_set3) == 100:
                        color_right_leg_jumpinglunge_set3 = (0, 255, 0)
                    else:
                        color_left_leg_jumpinglunge_set3 = (0, 0, 255)  # Keep color of left leg bar as red
                        color_right_leg_jumpinglunge_set3 = (0, 0, 255)

                    if rightleg_jumpinglunge_set3 <= 90:
                        if dir_alternating_right_lunge_jumpinglunge_set3 == 0 and count_alternating_right_lunge_jumpinglunge_set3 <= 5:
                            count_alternating_right_lunge_jumpinglunge_set3 += 0.5
                            if count_alternating_right_lunge_jumpinglunge_set3 == 5:
                                dir_alternating_left_lunge_jumpinglunge_set3 = 1
                            else:
                                dir_alternating_right_lunge_jumpinglunge_set3 = 1
                                cooldown_timer_jumpinglunge_set3 = cooldown_duration_jumpinglunge_set3
                    elif rightleg_jumpinglunge_set3 >= 150:
                        if dir_alternating_right_lunge_jumpinglunge_set3 == 1 and count_alternating_right_lunge_jumpinglunge_set3 <= 5:
                            count_alternating_right_lunge_jumpinglunge_set3 += 0.5
                            if count_alternating_right_lunge_jumpinglunge_set3 == 5:
                                dir_alternating_right_lunge_jumpinglunge_set3 = 1
                            else:
                                dir_alternating_right_lunge_jumpinglunge_set3 = 0
                                cooldown_timer_jumpinglunge_set3 = cooldown_duration_jumpinglunge_set3
                    
                    if leftleg_jumpinglunge_set3 <= 90:
                        if dir_alternating_left_lunge_jumpinglunge_set3 == 0 and count_alternating_left_lunge_jumpinglunge_set3 <= 5:
                            count_alternating_left_lunge_jumpinglunge_set3 += 0.5
                            if count_alternating_left_lunge_jumpinglunge_set3 == 5:
                                dir_alternating_left_lunge_jumpinglunge_set3 = 0
                            else:
                                dir_alternating_left_lunge_jumpinglunge_set3 = 1
                                cooldown_timer_jumpinglunge_set3 = cooldown_duration_jumpinglunge_set3
                    elif leftleg_jumpinglunge_set3 >= 150:
                        if dir_alternating_left_lunge_jumpinglunge_set3 == 1 and count_alternating_left_lunge_jumpinglunge_set3 <= 5:
                            count_alternating_left_lunge_jumpinglunge_set3 += 0.5
                            if count_alternating_left_lunge_jumpinglunge_set3 == 5:
                                dir_alternating_left_lunge_jumpinglunge_set3 = 1
                            else:
                                dir_alternating_left_lunge_jumpinglunge_set3 = 0
                                cooldown_timer_jumpinglunge_set3 = cooldown_duration_jumpinglunge_set3


            elif orientation =='left' and orientation2 == 'left':
                if leftleg_jumpinglunge_set3 is not None and rightleg_jumpinglunge_set3 is not None:
                    per_right_leg_jumpinglunge_set3 = np.interp(rightleg_jumpinglunge_set3, (190, 280), (0, 100))
                    bar_right_leg_jumpinglunge_set3 = np.interp(rightleg_jumpinglunge_set3, (190, 280), (680, 480))
                    per_left_leg_jumpinglunge_set3 = np.interp(leftleg_jumpinglunge_set3, (190, 280), (0, 100))
                    bar_left_leg_jumpinglunge_set3 = np.interp(leftleg_jumpinglunge_set3, (190, 280), (680, 480))

                    if int(per_left_leg_jumpinglunge_set3) == 100:
                        color_left_leg_jumpinglunge_set3 = (0, 255, 0)  # Change color of left leg bar to green
                    elif int(per_right_leg_jumpinglunge_set3) == 100:
                        color_right_leg_jumpinglunge_set3 = (0, 255, 0)
                    else:
                        color_left_leg_jumpinglunge_set3 = (0, 0, 255)  # Keep color of left leg bar as red
                        color_right_leg_jumpinglunge_set3 = (0, 0, 255)
              
                    if rightleg_jumpinglunge_set3 >= 280:
                        if dir_alternating_right_lunge_jumpinglunge_set3 == 0 and count_alternating_right_lunge_jumpinglunge_set3 <= 5:
                            count_alternating_right_lunge_jumpinglunge_set3 += 0.5
                            if count_alternating_right_lunge_jumpinglunge_set3 == 5:
                                dir_alternating_right_lunge_jumpinglunge_set3 = 0
                            else:
                                dir_alternating_right_lunge_jumpinglunge_set3 = 1
                                cooldown_timer_jumpinglunge_set3 = cooldown_duration_jumpinglunge_set3
                    elif rightleg_jumpinglunge_set3 <= 190:
                        if dir_alternating_right_lunge_jumpinglunge_set3 == 1 and count_alternating_right_lunge_jumpinglunge_set3 <= 5:
                            count_alternating_right_lunge_jumpinglunge_set3 += 0.5
                            if count_alternating_right_lunge_jumpinglunge_set3 == 5:
                                dir_alternating_right_lunge_jumpinglunge_set3 = 1
                            else:
                                dir_alternating_right_lunge_jumpinglunge_set3 = 0
                                cooldown_timer_jumpinglunge_set3 = cooldown_duration_jumpinglunge_set3

                    if leftleg_jumpinglunge_set3 >= 280:
                        if dir_alternating_left_lunge_jumpinglunge_set3 == 0 and count_alternating_left_lunge_jumpinglunge_set3 <= 5:
                            count_alternating_left_lunge_jumpinglunge_set3 += 0.5
                            if count_alternating_left_lunge_jumpinglunge_set3 == 5:
                                dir_alternating_left_lunge_jumpinglunge_set3 = 0
                            else:
                                dir_alternating_left_lunge_jumpinglunge_set3 = 1
                                cooldown_timer_jumpinglunge_set3 = cooldown_duration_jumpinglunge_set3
                    elif leftleg_jumpinglunge_set3 <= 190:
                        if dir_alternating_left_lunge_jumpinglunge_set3 == 1 and count_alternating_left_lunge_jumpinglunge_set3 <= 5:
                            count_alternating_left_lunge_jumpinglunge_set3 += 0.5
                            if count_alternating_left_lunge_jumpinglunge_set3 == 5:
                                dir_alternating_left_lunge_jumpinglunge_set3 = 1
                            else:
                                dir_alternating_left_lunge_jumpinglunge_set3 = 0
                                cooldown_timer_jumpinglunge_set3 = cooldown_duration_jumpinglunge_set3

            elif orientation == 'front' and orientation2 == 'front':
                    
                    per_right_leg_jumpinglunge_set3 = np.interp(rightleg_jumpinglunge_set3, (100, 200), (100, 0))
                    bar_right_leg_jumpinglunge_set3 = np.interp(rightleg_jumpinglunge_set3, (100, 200), (480, 680))
                    per_left_leg_jumpinglunge_set3 = np.interp(leftleg_jumpinglunge_set3, (100, 200), (100, 0))
                    bar_left_leg_jumpinglunge_set3 = np.interp(leftleg_jumpinglunge_set3, (100, 200), (480, 680))

                    if int(per_left_leg_jumpinglunge_set3) == 100:
                        color_left_leg_jumpinglunge_set3 = (0, 255, 0)  # Change color of left leg bar to green
                    elif int(per_right_leg_jumpinglunge_set3) == 100:
                        color_right_leg_jumpinglunge_set3 = (0, 255, 0)
                    else:
                        color_left_leg_jumpinglunge_set3 = (0, 0, 255)  # Keep color of left leg bar as red
                        color_right_leg_jumpinglunge_set3 = (0, 0, 255)  # Keep color of right leg bar as red

                    
                    if rightleg_jumpinglunge_set3 <= 150 and leftleg_jumpinglunge_set3 <= 100:
                        if dir_alternating_right_lunge_jumpinglunge_set3 == 0 and count_alternating_right_lunge_jumpinglunge_set3 <= 5:
                            count_alternating_right_lunge_jumpinglunge_set3 += 0.5
                            if count_alternating_right_lunge_jumpinglunge_set3 == 5:
                                dir_alternating_right_lunge_jumpinglunge_set3 = 0
                            else:
                                dir_alternating_right_lunge_jumpinglunge_set3 = 1
                                cooldown_timer_jumpinglunge_set3 = cooldown_duration_jumpinglunge_set3
                    else: 
                        if dir_alternating_right_lunge_jumpinglunge_set3 == 1 and count_alternating_right_lunge_jumpinglunge_set3 <= 5:
                            count_alternating_right_lunge_jumpinglunge_set3 += 0.5
                            if count_alternating_right_lunge_jumpinglunge_set3 == 5:
                                dir_alternating_right_lunge_jumpinglunge_set3 = 1
                            else:
                                dir_alternating_right_lunge_jumpinglunge_set3 = 0
                                cooldown_timer_jumpinglunge_set3 = cooldown_duration_jumpinglunge_set3

                    if rightleg_jumpinglunge_set3 <= 100 and leftleg_jumpinglunge_set3 <= 150:
                        if dir_alternating_left_lunge_jumpinglunge_set3 == 0 and count_alternating_left_lunge_jumpinglunge_set3 <= 5:
                            count_alternating_left_lunge_jumpinglunge_set3 += 0.5
                            if count_alternating_left_lunge_jumpinglunge_set3 == 5:
                                dir_alternating_left_lunge_jumpinglunge_set3 = 0
                            else:
                                dir_alternating_left_lunge_jumpinglunge_set3 = 1
                                cooldown_timer_jumpinglunge_set3 = cooldown_duration_jumpinglunge_set3
                    else:
                        if dir_alternating_left_lunge_jumpinglunge_set3 == 1 and count_alternating_left_lunge_jumpinglunge_set3 <= 5:
                            count_alternating_left_lunge_jumpinglunge_set3 += 0.5
                            if count_alternating_left_lunge_jumpinglunge_set3 == 5:
                                dir_alternating_left_lunge_jumpinglunge_set3 = 1
                            else:
                                dir_alternating_left_lunge_jumpinglunge_set3 = 0
                                cooldown_timer_jumpinglunge_set3 = cooldown_duration_jumpinglunge_set3

        cvzone.putTextRect(img, 'Jumping Lunge (alternate) SET 3', [310, 30], thickness=2, border=2, scale=2.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # Orientation
        cv2.rectangle(img, (890, 100), (1180, 160), (0, 0, 255), -2)
        cv2.putText(img, f"Orientation: {orientation}", (900, 140), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)

        # RIGHT LEG
        cv2.putText(img, f"R {int(per_right_leg_jumpinglunge_set3)}%", (24, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 480), (50, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_leg_jumpinglunge_set3)), (50, 680), color_right_leg_jumpinglunge_set3, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_left_leg_jumpinglunge_set3)}%", (962, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 480), (995, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_leg_jumpinglunge_set3)), (995, 680), color_left_leg_jumpinglunge_set3, -1)

    # Counter 
    cv2.rectangle(img, (20, 20), (140, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(count_alternating_right_lunge_jumpinglunge_set3)}/5", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (150, 20), (270, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(count_alternating_left_lunge_jumpinglunge_set3)}/5", (160, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    # Timer
    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [3390, 30], thickness=2, border=2, scale=2.5)
        display_info_jumpinglunge_set3 = False
        exercise_mode = "rest_jumpinglunge_set3"
        rest_jumpinglunge_start_time_set3 = time.time()

    # Repetition
    if count_alternating_left_lunge_jumpinglunge_set3 >= 5 and count_alternating_right_lunge_jumpinglunge_set3 >= 5: 
        cvzone.putTextRect(img, 'Exercise Complete', [3390, 30], thickness=2, border=2, scale=2.5)
        display_info_jumpinglunge_set3 = False
        exercise_mode = "rest_jumpinglunge_set3"
        rest_jumpinglunge_start_time_set3 = time.time()
    return img

def rest_jumpinglunge_set3(img):
    global exercise_mode, rest_jumpinglunge_start_time_set3, start_time_plankjacks
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_jumpinglunge_start_time_set3
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "plankjacks"
        start_time_plankjacks = time.time()
    return img

def detect_plankjacks(img):
    global count_Plank_Jacks, dir_Plank_Jacks, start_time_plankjacks, repetition_time_plankjacks, display_info_plankjacks, per_right_leg_plankjacks, bar_left_leg_plankjacks, cooldown_duration_plankjacks, cooldown_timer_plankjacks, color_left_leg_plankjacks, color_right_leg_plankjacks, exercise_mode, rest_plankjacks_start_time, per_left_leg_plankjacks, bar_right_leg_plankjacks

    img = cv2.resize(img, (1280, 720))

    elapsed_time = time.time() - start_time_plankjacks
    remaining_time = max(0, 60 - elapsed_time)

    if display_info_plankjacks:  # Check if to display counter, bar, and percentage
        img = detector_PlankJacks.findPose(img, False)
        lmList_jumping_jacks = detector_PlankJacks.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_jumping_jacks) != 0:

            measure = detector_PlankJacks.Plankjack(img, 28, 26, 24, 23, 25, 27, True)

            if cooldown_timer_plankjacks > 0:
                cooldown_timer_plankjacks -= 1

            per_left_leg_plankjacks = np.interp(measure, (40, 170), (0, 100))
            bar_left_leg_plankjacks = np.interp(measure, (40, 170), (680, 480))

            per_right_leg_plankjacks = np.interp(measure, (40, 170), (0, 100))
            bar_right_leg_plankjacks = np.interp(measure, (40, 170), (680, 480))

            if per_left_leg_plankjacks == 100 and per_right_leg_plankjacks == 100:
                color_left_leg_plankjacks = (0, 255, 0)
                color_right_leg_plankjacks = (0, 255, 0) 
            else:
                color_left_leg_plankjacks = (0, 0, 255)  
                color_right_leg_plankjacks = (0, 0, 255)

            if measure >= 170:
                if dir_Plank_Jacks == 0:
                    count_Plank_Jacks += 0.5
                    dir_Plank_Jacks = 1
            elif measure <= 80:
                if dir_Plank_Jacks == 1:
                    count_Plank_Jacks += 0.5
                    dir_Plank_Jacks = 0

        #Delay Timer for Pose Estimation

        cvzone.putTextRect(img, 'Plank Jacks', [345, 30], thickness=2, border=2, scale=2.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # RIGHT LEG
        cv2.putText(img, f"R {int(per_right_leg_plankjacks)}%", (24, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 480), (50, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_leg_plankjacks)), (50, 680), color_right_leg_plankjacks, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_left_leg_plankjacks)}%", (962, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 480), (995, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_leg_plankjacks)), (995, 680), color_left_leg_plankjacks, -1)

    # Counter 
    cv2.rectangle(img, (20, 20), (170, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(count_Plank_Jacks)}/5", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    # Timer
    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [345, 30], thickness=2, border=2, scale=2.5)
        display_info_plankjacks = False
        exercise_mode = "rest_plankjacks"
        rest_plankjacks_start_time = time.time()

    # Repetition
    if count_Plank_Jacks >= 5:  # Assuming 10 jumping jacks for demonstration
        cvzone.putTextRect(img, 'Exercise Complete', [345, 30], thickness=2, border=2, scale=2.5)
        display_info_plankjacks = False
        exercise_mode = "rest_plankjacks"
        rest_plankjacks_start_time = time.time()

    return img

def rest_plankjacks(img):
    global exercise_mode, rest_plankjacks_start_time, start_time_plankjacks_set2
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_plankjacks_start_time
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "plankjacks_set2"
        start_time_plankjacks_set2 = time.time()
    return img 

def detect_plankjacks_set2(img):
    global count_Plank_Jacks_set2, dir_Plank_Jacks_set2, start_time_plankjacks_set2, repetition_time_plankjacks_set2, display_info_plankjacks_set2, per_right_leg_plankjacks_set2, bar_left_leg_plankjacks_set2, cooldown_duration_plankjacks_set2, cooldown_timer_plankjacks_set2, color_left_leg_plankjacks_set2, color_right_leg_plankjacks_set2, exercise_mode, rest_plankjacks_start_time_set2, per_left_leg_plankjacks_set2, per_right_leg_plankjacks_set2, bar_left_leg_plankjacks_set2, bar_right_leg_plankjacks_set2

    img = cv2.resize(img, (1280, 720))

    elapsed_time = time.time() - start_time_plankjacks_set2
    remaining_time = max(0, 60 - elapsed_time)

    if display_info_plankjacks_set2:  # Check if to display counter, bar, and percentage
        img = detector_PlankJacks.findPose(img, False)
        lmList_jumping_jacks = detector_PlankJacks.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_jumping_jacks) != 0:

            measure = detector_PlankJacks.Plankjack(img, 28, 26, 24, 23, 25, 27, True)

            if cooldown_timer_plankjacks_set2 > 0:
                cooldown_timer_plankjacks_set2 -= 1

            per_left_leg_plankjacks_set2 = np.interp(measure, (40, 170), (0, 100))
            bar_left_leg_plankjacks_set2 = np.interp(measure, (40, 170), (680, 480))

            per_right_leg_plankjacks_set2 = np.interp(measure, (40, 170), (0, 100))
            bar_right_leg_plankjacks_set2 = np.interp(measure, (40, 170), (680, 480))

            if per_left_leg_plankjacks_set2 == 100 and per_right_leg_plankjacks_set2 == 100:
                color_left_leg_plankjacks_set2 = (0, 255, 0)
                color_right_leg_plankjacks_set2 = (0, 255, 0) 
            else:
                color_left_leg_plankjacks_set2 = (0, 0, 255)  
                color_right_leg_plankjacks_set2 = (0, 0, 255)

            if measure >= 170:
                if dir_Plank_Jacks_set2 == 0:
                    count_Plank_Jacks_set2 += 0.5
                    dir_Plank_Jacks_set2 = 1
            elif measure <= 80:
                if dir_Plank_Jacks_set2 == 1:
                    count_Plank_Jacks_set2 += 0.5
                    dir_Plank_Jacks_set2 = 0

        #Delay Timer for Pose Estimation

        cvzone.putTextRect(img, 'Plank Jacks SET 2', [345, 30], thickness=2, border=2, scale=2.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # RIGHT LEG
        cv2.putText(img, f"R {int(per_right_leg_plankjacks_set2)}%", (24, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 480), (50, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_leg_plankjacks_set2)), (50, 680), color_right_leg_plankjacks_set2, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_left_leg_plankjacks_set2)}%", (962, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 480), (995, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_leg_plankjacks_set2)), (995, 680), color_left_leg_plankjacks_set2, -1)

    # Counter 
    cv2.rectangle(img, (20, 20), (170, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(count_Plank_Jacks_set2)}/5", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    # Timer
    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [345, 30], thickness=2, border=2, scale=2.5)
        display_info_plankjacks_set2 = False
        exercise_mode = "rest_plankjacks_set2"
        rest_plankjacks_start_time_set2 = time.time()

    # Repetition
    if count_Plank_Jacks_set2 >= 5:  # Assuming 10 jumping jacks for demonstration
        cvzone.putTextRect(img, 'Exercise Complete', [345, 30], thickness=2, border=2, scale=2.5)
        display_info_plankjacks_set2 = False
        exercise_mode = "rest_plankjacks_set2"
        rest_plankjacks_start_time_set2 = time.time()
    return img 

def rest_plankjacks_set2(img):
    global exercise_mode, rest_plankjacks_start_time_set2, start_time_plankjacks_set3
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_plankjacks_start_time_set2
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "plankjacks_set3"
        start_time_plankjacks_set3 = time.time()
    return img

def detect_plankjacks_set3(img):
    global count_Plank_Jacks_set3, dir_Plank_Jacks_set3, start_time_plankjacks_set3, repetition_time_plankjacks_set3, display_info_plankjacks_set3, per_right_leg_plankjacks_set3, bar_left_leg_plankjacks_set3, cooldown_duration_plankjacks_set3, cooldown_timer_plankjacks_set3, color_left_leg_plankjacks_set3, color_right_leg_plankjacks_set3, exercise_mode, rest_plankjacks_start_time_set3, per_left_leg_plankjacks_set3, per_right_leg_plankjacks_set3, bar_left_leg_plankjacks_set3, bar_right_leg_plankjacks_set3


    img = cv2.resize(img, (1280, 720))

    elapsed_time = time.time() - start_time_plankjacks_set3
    remaining_time = max(0, 60 - elapsed_time)

    if display_info_plankjacks_set3:  # Check if to display counter, bar, and percentage
        img = detector_PlankJacks.findPose(img, False)
        lmList_jumping_jacks = detector_PlankJacks.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_jumping_jacks) != 0:

            measure = detector_PlankJacks.Plankjack(img, 28, 26, 24, 23, 25, 27, True)

            if cooldown_timer_plankjacks_set3 > 0:
                cooldown_timer_plankjacks_set3 -= 1

            per_left_leg_plankjacks_set3 = np.interp(measure, (40, 170), (0, 100))
            bar_left_leg_plankjacks_set3 = np.interp(measure, (40, 170), (680, 480))

            per_right_leg_plankjacks_set3 = np.interp(measure, (40, 170), (0, 100))
            bar_right_leg_plankjacks_set3 = np.interp(measure, (40, 170), (680, 480))

            if per_left_leg_plankjacks_set3 == 100 and per_right_leg_plankjacks_set3 == 100:
                color_left_leg_plankjacks_set3 = (0, 255, 0)
                color_right_leg_plankjacks_set3 = (0, 255, 0) 
            else:
                color_left_leg_plankjacks_set3 = (0, 0, 255)  
                color_right_leg_plankjacks_set3 = (0, 0, 255)

            if measure >= 170:
                if dir_Plank_Jacks_set3 == 0:
                    count_Plank_Jacks_set3 += 0.5
                    dir_Plank_Jacks_set3 = 1
            elif measure <= 80:
                if dir_Plank_Jacks_set3 == 1:
                    count_Plank_Jacks_set3 += 0.5
                    dir_Plank_Jacks_set3 = 0

        #Delay Timer for Pose Estimation

        cvzone.putTextRect(img, 'Plank Jacks SET 3', [345, 30], thickness=2, border=2, scale=2.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # RIGHT LEG
        cv2.putText(img, f"R {int(per_right_leg_plankjacks_set3)}%", (24, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 480), (50, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_leg_plankjacks_set3)), (50, 680), color_right_leg_plankjacks_set3, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_left_leg_plankjacks_set3)}%", (962, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 480), (995, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_leg_plankjacks_set3)), (995, 680), color_left_leg_plankjacks_set3, -1)

    # Counter 
    cv2.rectangle(img, (20, 20), (170, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(count_Plank_Jacks_set3)}/5", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    # Timer
    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [345, 30], thickness=2, border=2, scale=2.5)
        display_info_plankjacks_set3 = False
        exercise_mode = "rest_plankjacks_set3"
        rest_plankjacks_start_time_set3 = time.time()

    # Repetition
    if count_Plank_Jacks_set3 >= 5:  # Assuming 10 jumping jacks for demonstration
        cvzone.putTextRect(img, 'Exercise Complete', [345, 30], thickness=2, border=2, scale=2.5)
        display_info_plankjacks_set3 = False
        exercise_mode = "rest_plankjacks_set3"
        rest_plankjacks_start_time_set3 = time.time()
    return img

def rest_plankjacks_set3(img):
    global exercise_mode, rest_plankjacks_start_time_set3, start_time_ptt
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_plankjacks_start_time_set3
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "ptt"
        start_time_ptt = time.time()
    return img

def detect_ptt(img):
    global count_plank_toe_taps_right, count_plank_toe_taps_left, dir_plank_toe_taps_right, dir_plank_toe_taps_left, start_time_ptt, repetition_time_ptt, display_info_ptt, per_left_leg_ptt, bar_left_leg_ptt, per_right_leg_ptt, bar_right_leg_ptt, cooldown_duration_ptt, cooldown_timer_ptt, color_left_leg_ptt, color_right_leg_ptt, orientation, orientation2, exercise_mode, rest_ptt_start_time

    img = cv2.resize(img, (1280, 720))

    elapsed_time = time.time() - start_time_ptt
    remaining_time = max(0, 60 - elapsed_time)

    if display_info_ptt:  # Check if to display counter, bar, and percentage
        img = detector_PlankToeTaps.findPose(img, False)
        lmList_jumping_jacks = detector_PlankToeTaps.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_jumping_jacks) != 0:

            # Right and Left keypoints
            distance1, distance2 = detector_PlankToeTaps.PlankToeTaps(img, 16, 14, 12, 24, 26, 28, 32, 15, 13, 11, 23, 25, 27, 31, True)
           
            #print("right: ", distance1, "left: ", distance2)

            if cooldown_timer_ptt > 0:
                cooldown_timer_ptt -= 1

            per_right_leg_ptt = np.interp(distance1, (40, 350), (100, 0))
            bar_right_leg_ptt = np.interp(distance1, (40, 350), (480, 680))
            per_left_leg_ptt = np.interp(distance2, (40, 350), (100, 0))
            bar_left_leg_ptt = np.interp(distance2, (40, 350), (480, 680))

            if int(per_left_leg_ptt) == 100:
                color_left_leg_ptt = (0, 255, 0)  # Change color of left leg bar to green
            elif int(per_right_leg_ptt) == 100:
                color_right_leg_ptt = (0, 255, 0)
            else:
                color_left_leg_ptt = (0, 0, 255)  # Keep color of left leg bar as red
                color_right_leg_ptt = (0, 0, 255)

            if distance1 <= 40:
                if dir_plank_toe_taps_right == 0 and count_plank_toe_taps_right <= 6:
                    count_plank_toe_taps_right += 0.5
                    if count_plank_toe_taps_right == 6:
                        dir_plank_toe_taps_right = 0
                    else:
                        dir_plank_toe_taps_right = 1
                        #print("right up: ",count_plank_toe_taps_right)
            elif distance1 >= 300:
                if dir_plank_toe_taps_right == 1 and count_plank_toe_taps_right <= 6:
                    count_plank_toe_taps_right += 0.5
                    if count_plank_toe_taps_right == 6:
                        dir_plank_toe_taps_right = 1
                    else:
                        dir_plank_toe_taps_right = 0
                        #print("right down: ",count_plank_toe_taps_right)
            
            if distance2 <= 40:
                if dir_plank_toe_taps_left == 0 and count_plank_toe_taps_left <= 6:
                    count_plank_toe_taps_left += 0.5
                    if count_plank_toe_taps_left == 6:
                        dir_plank_toe_taps_left = 0
                    else:
                        dir_plank_toe_taps_left = 1
                        #print("left up: ",count_plank_toe_taps_left)
            elif distance2 >= 300:
                if dir_plank_toe_taps_left == 1 and count_plank_toe_taps_left <= 6:
                    count_plank_toe_taps_left += 0.5
                    if count_plank_toe_taps_left == 6:
                        dir_plank_toe_taps_left = 1
                    else:
                        dir_plank_toe_taps_left = 0
                        #print("left down: ",count_plank_toe_taps_left)

        cvzone.putTextRect(img, 'Plank Toe Taps', [390, 30], thickness=2, border=2, scale=2.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # RIGHT LEG
        cv2.putText(img, f"R {int(per_right_leg_ptt)}%", (24, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 480), (50, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_leg_ptt)), (50, 680), color_right_leg_ptt, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_left_leg_ptt)}%", (962, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 480), (995, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_leg_ptt)), (995, 680), color_left_leg_ptt, -1)

    # Counter 
    cv2.rectangle(img, (20, 20), (140, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(count_plank_toe_taps_right)}/6", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (150, 20), (270, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(count_plank_toe_taps_left)}/6", (160, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    # Timer
    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [345, 30], thickness=2, border=2, scale=2.5)
        display_info_ptt = False
        exercise_mode = "rest_ptt"
        rest_ptt_start_time = time.time()

    # Repetition
    if count_plank_toe_taps_right == 5 and count_plank_toe_taps_left == 5:  # Assuming 10 jumping jacks for demonstration
        cvzone.putTextRect(img, 'Exercise Complete', [345, 30], thickness=2, border=2, scale=2.5)
        display_info_ptt = False
        exercise_mode = "rest_ptt"
        rest_ptt_start_time = time.time()
    return img

def rest_ptt(img):
    global exercise_mode, rest_ptt_start_time, start_time_ptt_set2
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_ptt_start_time
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "ptt_set2"
        start_time_ptt_set2 = time.time()
    return img

def detect_ptt_set2(img):
    global count_plank_toe_taps_right_set2, count_plank_toe_taps_left_set2, dir_plank_toe_taps_right_set2, dir_plank_toe_taps_left_set2, start_time_ptt_set2, repetition_time_ptt_set2, display_info_ptt_set2, per_left_leg_ptt_set2, bar_left_leg_ptt_set2, per_right_leg_ptt_set2, bar_right_leg_ptt_set2, cooldown_duration_ptt_set2, cooldown_timer_ptt_set2, color_left_leg_ptt_set2, color_right_leg_ptt_set2, orientation, orientation2, exercise_mode, rest_ptt_start_time_set2

    img = cv2.resize(img, (1280, 720))

    elapsed_time = time.time() - start_time_ptt_set2
    remaining_time = max(0, 60 - elapsed_time)

    if display_info_ptt_set2:  # Check if to display counter, bar, and percentage
        img = detector_PlankToeTaps.findPose(img, False)
        lmList_jumping_jacks = detector_PlankToeTaps.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_jumping_jacks) != 0:

            # Right and Left keypoints
            distance1, distance2 = detector_PlankToeTaps.PlankToeTaps(img, 16, 14, 12, 24, 26, 28, 32, 15, 13, 11, 23, 25, 27, 31, True)
           
            #print("right: ", distance1, "left: ", distance2)

            if cooldown_timer_ptt_set2 > 0:
                cooldown_timer_ptt_set2 -= 1

            per_right_leg_ptt_set2 = np.interp(distance1, (40, 350), (100, 0))
            bar_right_leg_ptt_set2 = np.interp(distance1, (40, 350), (480, 680))
            per_left_leg_ptt_set2 = np.interp(distance2, (40, 350), (100, 0))
            bar_left_leg_ptt_set2 = np.interp(distance2, (40, 350), (480, 680))

            if int(per_left_leg_ptt_set2) == 100:
                color_left_leg_ptt_set2 = (0, 255, 0)  # Change color of left leg bar to green
            elif int(per_right_leg_ptt_set2) == 100:
                color_right_leg_ptt_set2 = (0, 255, 0)
            else:
                color_left_leg_ptt_set2 = (0, 0, 255)  # Keep color of left leg bar as red
                color_right_leg_ptt_set2 = (0, 0, 255)

            if distance1 <= 40:
                if dir_plank_toe_taps_right_set2 == 0 and count_plank_toe_taps_right_set2 <= 6:
                    count_plank_toe_taps_right_set2 += 0.5
                    if count_plank_toe_taps_right_set2 == 6:
                        dir_plank_toe_taps_right_set2 = 0
                    else:
                        dir_plank_toe_taps_right_set2 = 1
                        #print("right up: ",count_plank_toe_taps_right)
            elif distance1 >= 300:
                if dir_plank_toe_taps_right_set2 == 1 and count_plank_toe_taps_right_set2 <= 6:
                    count_plank_toe_taps_right_set2 += 0.5
                    if count_plank_toe_taps_right_set2 == 6:
                        dir_plank_toe_taps_right_set2 = 1
                    else:
                        dir_plank_toe_taps_right_set2 = 0
                        #print("right down: ",count_plank_toe_taps_right)
            
            if distance2 <= 40:
                if dir_plank_toe_taps_left_set2 == 0 and count_plank_toe_taps_left_set2 <= 6:
                    count_plank_toe_taps_left_set2 += 0.5
                    if count_plank_toe_taps_left_set2 == 6:
                        dir_plank_toe_taps_left_set2 = 0
                    else:
                        dir_plank_toe_taps_left_set2 = 1
                        #print("left up: ",count_plank_toe_taps_left)
            elif distance2 >= 300:
                if dir_plank_toe_taps_left_set2 == 1 and count_plank_toe_taps_left_set2 <= 6:
                    count_plank_toe_taps_left_set2 += 0.5
                    if count_plank_toe_taps_left_set2 == 6:
                        dir_plank_toe_taps_left_set2 = 1
                    else:
                        dir_plank_toe_taps_left_set2 = 0
                        #print("left down: ",count_plank_toe_taps_left)

        cvzone.putTextRect(img, 'Plank Toe Taps SET 2', [390, 30], thickness=2, border=2, scale=2.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # RIGHT LEG
        cv2.putText(img, f"R {int(per_right_leg_ptt_set2)}%", (24, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 480), (50, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_leg_ptt_set2)), (50, 680), color_right_leg_ptt_set2, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_left_leg_ptt_set2)}%", (962, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 480), (995, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_leg_ptt_set2)), (995, 680), color_left_leg_ptt_set2, -1)

    # Counter 
    cv2.rectangle(img, (20, 20), (140, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(count_plank_toe_taps_right_set2)}/6", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (150, 20), (270, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(count_plank_toe_taps_left_set2)}/6", (160, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    # Timer
    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [345, 30], thickness=2, border=2, scale=2.5)
        display_info_ptt_set2 = False
        exercise_mode = "rest_ptt_set2"
        rest_ptt_start_time_set2 = time.time()

    # Repetition
    if count_plank_toe_taps_right_set2 == 5 and count_plank_toe_taps_left_set2 == 5:  # Assuming 10 jumping jacks for demonstration
        cvzone.putTextRect(img, 'Exercise Complete', [345, 30], thickness=2, border=2, scale=2.5)
        display_info_ptt_set2 = False
        exercise_mode = "rest_ptt_set2"
        rest_ptt_start_time_set2 = time.time()
    return img

def rest_ptt_set2(img):
    global exercise_mode, rest_ptt_start_time_set2, start_time_ptt_set3
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_ptt_start_time_set2
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "ptt_set3"
        start_time_ptt_set3 = time.time()
    return img

def detect_ptt_set3(img):
    global count_plank_toe_taps_right_set3, count_plank_toe_taps_left_set3, dir_plank_toe_taps_right_set3, dir_plank_toe_taps_left_set3, start_time_ptt_set3, repetition_time_ptt_set3, display_info_ptt_set3, per_left_leg_ptt_set3, bar_left_leg_ptt_set3, per_right_leg_ptt_set3, bar_right_leg_ptt_set3, cooldown_duration_ptt_set3, cooldown_timer_ptt_set3, color_left_leg_ptt_set3, color_right_leg_ptt_set3, orientation, orientation2, exercise_mode, rest_ptt_start_time_set3

    img = cv2.resize(img, (1280, 720))

    elapsed_time = time.time() - start_time_ptt_set3
    remaining_time = max(0, 60 - elapsed_time)

    if display_info_ptt_set3:  # Check if to display counter, bar, and percentage
        img = detector_PlankToeTaps.findPose(img, False)
        lmList_jumping_jacks = detector_PlankToeTaps.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_jumping_jacks) != 0:

            # Right and Left keypoints
            distance1, distance2 = detector_PlankToeTaps.PlankToeTaps(img, 16, 14, 12, 24, 26, 28, 32, 15, 13, 11, 23, 25, 27, 31, True)
           
            #print("right: ", distance1, "left: ", distance2)

            if cooldown_timer_ptt_set3 > 0:
                cooldown_timer_ptt_set3 -= 1

            per_right_leg_ptt_set3 = np.interp(distance1, (40, 350), (100, 0))
            bar_right_leg_ptt_set3 = np.interp(distance1, (40, 350), (480, 680))
            per_left_leg_ptt_set3 = np.interp(distance2, (40, 350), (100, 0))
            bar_left_leg_ptt_set3 = np.interp(distance2, (40, 350), (480, 680))

            if int(per_left_leg_ptt_set3) == 100:
                color_left_leg_ptt_set3 = (0, 255, 0)  # Change color of left leg bar to green
            elif int(per_right_leg_ptt_set3) == 100:
                color_right_leg_ptt_set3 = (0, 255, 0)
            else:
                color_left_leg_ptt_set3 = (0, 0, 255)  # Keep color of left leg bar as red
                color_right_leg_ptt_set3 = (0, 0, 255)

            if distance1 <= 40:
                if dir_plank_toe_taps_right_set3 == 0 and count_plank_toe_taps_right_set3 <= 6:
                    count_plank_toe_taps_right_set3 += 0.5
                    if count_plank_toe_taps_right_set3 == 6:
                        dir_plank_toe_taps_right_set3 = 0
                    else:
                        dir_plank_toe_taps_right_set3 = 1
                        #print("right up: ",count_plank_toe_taps_right)
            elif distance1 >= 300:
                if dir_plank_toe_taps_right_set3 == 1 and count_plank_toe_taps_right_set3 <= 6:
                    count_plank_toe_taps_right_set3 += 0.5
                    if count_plank_toe_taps_right_set3 == 6:
                        dir_plank_toe_taps_right_set3 = 1
                    else:
                        dir_plank_toe_taps_right_set3 = 0
                        #print("right down: ",count_plank_toe_taps_right)
            
            if distance2 <= 40:
                if dir_plank_toe_taps_left_set3 == 0 and count_plank_toe_taps_left_set3 <= 6:
                    count_plank_toe_taps_left_set3 += 0.5
                    if count_plank_toe_taps_left_set3 == 6:
                        dir_plank_toe_taps_left_set3 = 0
                    else:
                        dir_plank_toe_taps_left_set3 = 1
                        #print("left up: ",count_plank_toe_taps_left)
            elif distance2 >= 300:
                if dir_plank_toe_taps_left_set3 == 1 and count_plank_toe_taps_left_set3 <= 6:
                    count_plank_toe_taps_left_set3 += 0.5
                    if count_plank_toe_taps_left_set3 == 6:
                        dir_plank_toe_taps_left_set3 = 1
                    else:
                        dir_plank_toe_taps_left_set3 = 0
                        #print("left down: ",count_plank_toe_taps_left)

        cvzone.putTextRect(img, 'Plank Toe Taps SET 3', [390, 30], thickness=2, border=2, scale=2.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # RIGHT LEG
        cv2.putText(img, f"R {int(per_right_leg_ptt_set3)}%", (24, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 480), (50, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_leg_ptt_set3)), (50, 680), color_right_leg_ptt_set3, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_left_leg_ptt_set3)}%", (962, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 480), (995, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_leg_ptt_set3)), (995, 680), color_left_leg_ptt_set3, -1)

    # Counter 
    cv2.rectangle(img, (20, 20), (140, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(count_plank_toe_taps_right_set3)}/6", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (150, 20), (270, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(count_plank_toe_taps_left_set3)}/6", (160, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    # Timer
    if remaining_time <= 0:
        cvzone.putTextRect(img, "Time's Up", [345, 30], thickness=2, border=2, scale=2.5)
        display_info_ptt_set3 = False
        exercise_mode = "rest_ptt_set3"
        rest_ptt_start_time_set3 = time.time()

    # Repetition
    if count_plank_toe_taps_right_set3 == 5 and count_plank_toe_taps_left_set3 == 5:  # Assuming 10 jumping jacks for demonstration
        cvzone.putTextRect(img, 'Exercise Complete', [345, 30], thickness=2, border=2, scale=2.5)
        display_info_ptt_set3 = False
        exercise_mode = "rest_ptt_set3"
        rest_ptt_start_time_set3 = time.time()
    return img 

def rest_ptt_set3(img):
    global exercise_mode, rest_ptt_start_time_set3
    img = cv2.resize(img, (1280, 720))

    rest_elapsed_time = time.time() - rest_ptt_start_time_set3
    rest_remaining_time = max(0, 60 - rest_elapsed_time)

        # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        exercise_mode = "done_lossWeight"
        print(exercise_mode)
    return img
