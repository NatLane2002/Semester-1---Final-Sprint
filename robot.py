import time

# room types -  will be defined before starting the course
# 1 - fire
# 2 - skip
# 3 - person
room_one_type = 3
room_two_type = 2
room_three_type = 1
room_four_type = 3

person_found = False
marker_found = False


def scan_for_marker():
    global marker_found
    vision_ctrl.enable_detection(rm_define.vision_detection_marker)
    marker_found = False
    gimbal_ctrl.pitch_ctrl(10)
    while marker_found == False:
        gimbal_ctrl.yaw_ctrl(+180)
        gimbal_ctrl.yaw_ctrl(-180)


def vision_recognized_marker_letter_F(msg):
    global marker_found
    vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_F)
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
    gun_ctrl.fire_once()
    marker_found = True


def scan_for_people():
    global person_found
    vision_ctrl.enable_detection(rm_define.vision_detection_people)
    person_found = False
    gimbal_ctrl.pitch_ctrl(10)
    while person_found == False:
        gimbal_ctrl.yaw_ctrl(+180)
        gimbal_ctrl.yaw_ctrl(-180)


def vision_recognized_people(msg):
    global person_found
    vision_ctrl.disable_detection(rm_define.vision_detection_people)
    media_ctrl.play_sound(rm_define.media_sound_solmization_1C)
    person_found = True


def room_one():
    # turn to enter first room
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    gimbal_ctrl.recenter()
    # move to target
    # chassis_ctrl.move_with_distance(0, 4.70)

    if room_one_type == 1:
        scan_for_marker()
    elif room_one_type == 3:
        scan_for_people()
        # call function to return person to start and gpo back to door one

    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
    gimbal_ctrl.recenter()
    # chassis_ctrl.move_with_distance(0, 4.70)
    if room_one_type == 1:
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        gimbal_ctrl.recenter()
    elif room_one_type == 3:
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        # go back to start, and return to outside room one


# This code moves the robot through the third room and back
def room_three():
    # Rotate robot left 90 degrees
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    gimbal_ctrl.recenter()
    # Move robot forward 2.37 meters
    chassis_ctrl.move_with_distance(0, 2.37)
    # Rotate robot right 90 degrees
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
    gimbal_ctrl.recenter()
    # Move robot forward 1.50 meters
    chassis_ctrl.move_with_distance(0, 1.50)
    # Rotate robot left 90 degrees
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    gimbal_ctrl.recenter()
    # Move robot forward 4.71 meters
    chassis_ctrl.move_with_distance(0, 4.71)
    # Rotate robot right 90 degrees
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
    gimbal_ctrl.recenter()
    # Move robot forward 1.20 meters
    chassis_ctrl.move_with_distance(0, 1.20)

    if room_three_type == 1:
        scan_for_marker()
    elif room_three_type == 3:
        scan_for_people()
        # call function to return person to start, and go back to door three

    # Rotate the robot 180 degrees
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
    gimbal_ctrl.recenter()
    # Move the robot forward 1.20 meters
    chassis_ctrl.move_with_distance(0, 1.20)
    # Rotate the robot left 90 degrees
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    gimbal_ctrl.recenter()
    # Move the robot forward 4.71 meters
    chassis_ctrl.move_with_distance(0, 4.71)
    # Rotate the robot right 90 degrees
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
    gimbal_ctrl.recenter()
    # Move robot forward 1.50 meters
    chassis_ctrl.move_with_distance(0, 1.50)
    # Rotate robot left 90 degrees
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    gimbal_ctrl.recenter()
    # Move robot forward 2.37 meters
    chassis_ctrl.move_with_distance(0, 2.37)
    # Rotate robot left 90 degrees to face the remainder of the course
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    gimbal_ctrl.recenter()


def room_four():
    # Rotate robot left 90 degrees to face final door
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    gimbal_ctrl.recenter()
    # Move the robot forward into the room
    chassis_ctrl.move_with_distance(0, 2.10)
    # Rotate robot right 90 degrees
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
    gimbal_ctrl.recenter()
    # Move the robot forward 2.20 meters
    chassis_ctrl.move_with_distance(0, 2.12)
    # Turn the robot right 90 degrees
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)

    if room_four_type == 1:
        # Call the scan marker function
        scan_for_marker()
    elif room_four_type == 3:
        scan_for_people()

    # Rotate robot 90 degrees right
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
    gimbal_ctrl.recenter()
    # Move the robot forward 2.12 meters
    chassis_ctrl.move_with_distance(0, 2.12)
    # Rotate robot 90 degrees left
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    gimbal_ctrl.recenter()
    # Move the robot forward 2.10 meters into the hall
    chassis_ctrl.move_with_distance(0, 2.10)
    # Rotate the robot 90 degrees right
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
    gimbal_ctrl.recenter()
    # pause to re-align
    media_ctrl.play_sound(rm_define.media_sound_count_down)
    time.sleep(5)
    # Move the robot a total of 24.45 meters to the end of the hall (can only move 5 meters per command)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 4.45)
    # Rotate the robot right 45 degrees
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 45)
    gimbal_ctrl.recenter()
    # Move the robot forward 2.70 meters
    chassis_ctrl.move_with_distance(0, 2.70)
    # Rotate the robot right 45 degrees to face the start of the course
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 45)
    gimbal_ctrl.recenter()
    media_ctrl.play_sound(rm_define.media_sound_count_down)
    time.sleep(5)
    # Move the robot forward a total of 15.05 meters to reach the start of the obstacle course
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 0.05)
    # Rotate the robot 180 degrees to reset its original position
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
    gimbal_ctrl.recenter()


def start():
    # set mode and speeds
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    chassis_ctrl.set_trans_speed(.7)

    # move to first door
    chassis_ctrl.move_with_distance(0, 5.00)
    chassis_ctrl.move_with_distance(0, 2.45)

    if room_one_type != 2:
        room_one()

    # move to corner of hall
    chassis_ctrl.move_with_distance(0, 5.00)
    chassis_ctrl.move_with_distance(0, 2.60)

    # navigate corner
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 45)
    gimbal_ctrl.recenter()
    chassis_ctrl.move_with_distance(0, 2.70)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 45)
    gimbal_ctrl.recenter()

    # pause for 5 seconds to re-align
    media_ctrl.play_sound(rm_define.media_sound_count_down)
    time.sleep(5)

    # move to second door
    chassis_ctrl.move_with_distance(0, 5.00)
    chassis_ctrl.move_with_distance(0, 0.17)

    # turn to enter room. This room will be a 2, and won't be entered
    if room_two_type != 2:
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)

    # move to third door
    chassis_ctrl.move_with_distance(0, 5.00)
    chassis_ctrl.move_with_distance(0, 3.85)

    if room_three_type != 2:
        room_three()

    # move to fourth room
    chassis_ctrl.move_with_distance(0, 5.00)
    chassis_ctrl.move_with_distance(0, 5.00)
    chassis_ctrl.move_with_distance(0, 0.45)

    # enter fourth room
    if room_four_type != 2:
        room_four()