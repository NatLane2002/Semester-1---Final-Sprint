import time

person_found = False
marker_found = True


def start():
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    chassis_ctrl.set_trans_speed(.6)

    # move to first door
    chassis_ctrl.move_with_distance(0, 5.00)
    chassis_ctrl.move_with_distance(0, 2.35)

    # turn to enter first room
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)

    # add function to enter room and scan for a marker.  This function is set up before the start() scan_for_marker()

    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)  # replace when room function is complete

    # move to corner of hall
    chassis_ctrl.move_with_distance(0, 5.00)
    chassis_ctrl.move_with_distance(0, 2.60)

    # navigate corner
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 45)
    chassis_ctrl.move_with_distance(0, 2.70)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 45)

    # pause for 5 seconds to re-align
    time.sleep(5)

    # move to second door
    chassis_ctrl.move_with_distance(0, 5.00)
    chassis_ctrl.move_with_distance(0, 0.10)

    # turn to enter room. This room will be a 2, and won't be entered
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)

    # move to third door
    chassis_ctrl.move_with_distance(0, 5.00)
    chassis_ctrl.move_with_distance(0, 3.80)

    # turn to enter third room
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    # enter room and scan for marker
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)  # replace when room is measured

    # move to fourth room
    chassis_ctrl.move_with_distance(0, 5.00)
    chassis_ctrl.move_with_distance(0, 5.00)
    chassis_ctrl.move_with_distance(0, 0.40)

    # turn to enter fourth room
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    # enter room and scan for marker
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)  # replace when room is measured
