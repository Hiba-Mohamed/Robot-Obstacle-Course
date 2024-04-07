def scan_for_marker():
   vision_ctrl.enable_detection(rm_define.vision_detection_marker)
   gimbal_ctrl.yaw_ctrl(-100)
   gimbal_ctrl.yaw_ctrl(90)
   vision_ctrl.disable_detection(rm_define.vision_detection_marker)
   vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_F)

def ScanRoomType():
    # Turn on detection and scan left and right until you hit a marker. 
    vision_ctrl.enable_detection(rm_define.vision_detection_marker)
    gimbal_ctrl.yaw_ctrl(-90)
    gimbal_ctrl.yaw_ctrl(+180)
    RoomType = 0
    while True:
        if vision_recognized_marker_number_[one](msg):
            RoomType = 1
            break
        elif vision_recognized_marker_number_[two](msg):
            RoomType = 2
            break
        elif vision_recognized_marker_number_[three](msg):
            RoomType = 3
            break
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
    return RoomType

def ScanPositionF():
    # Function to detect the number on position F and call the respective function
    # Turn on detection and scan left and right until you hit a marker. 
    vision_ctrl.enable_detection(rm_define.vision_detection_marker)
    gimbal_ctrl.yaw_ctrl(-90)
    gimbal_ctrl.yaw_ctrl(+180)
    while True:
        if vision_recognized_marker_number_[one](msg):
            PositionFMarker1()
            break
        elif vision_recognized_marker_number_[two](msg):
            PositionFMarker2()
            break
        elif vision_recognized_marker_number_[three](msg):
            PositionFMarker3()
            break
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)

def PositionFMarker1():
    # Rotate chassis and gimbal 360 degrees opposite to each other
    chassis_ctrl.move_with_time(0, 0, 2000)  # Rotate chassis for 2000 milliseconds (assuming 2000ms is full rotation)
    gimbal_ctrl.yaw_ctrl(180, 2000)  # Rotate gimbal by 180 degrees opposite direction in the same duration
    led_ctrl.set_top_led(rm_define.armor_top_all, 0, 255, 0, effect='off')  # Turn off LED lights

def PositionFMarker2():
    # Do something with the LED lights
    led_ctrl.set_top_led(rm_define.armor_top_all, 255, 0, 0, effect='on')  # Set LED lights to red
    chassis_ctrl.move_with_speed(0, 0)  # Stop chassis movement
    gimbal_ctrl.yaw_ctrl(0, 0)  # Stop gimbal movement

def PositionFMarker3():
    chassis_ctrl.move_with_time(0, 0, 2000)  # Rotate chassis for 2000 milliseconds (assuming 2000ms is full rotation)
    gimbal_ctrl.yaw_ctrl(180, 2000)  # Rotate gimbal by 180 degrees opposite direction in the same duration
    led_ctrl.set_top_led(rm_define.armor_top_all, 0, 255, 0, effect='on')  # Set LED lights to green

def FireRoom():
    gun_ctrl.fire_once()

def PersonRoom():
    # Play "follow me back to safety" audio
    media_ctrl.play_sound(sound_enum, wait_complete_flag=False)

def PoisonRoom():
    pass


def start():
    RoomType = ScanRoomType()


    robot_ctrl.set_mode(rm_define.robot_mode_free)
#     #A to B
    chassis_ctrl.move_with_distance(0,5)
    chassis_ctrl.move_with_distance(0,0.47)
    time.sleep(5)
#     #B Obstacle course
    chassis_ctrl.move_with_distance(0,0.36)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
    chassis_ctrl.move_with_distance(0,0.8)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
    chassis_ctrl.move_with_distance(0,0.45)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
    chassis_ctrl.move_with_distance(0,1.6)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
    chassis_ctrl.move_with_distance(0,0.43)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
    chassis_ctrl.move_with_distance(0,0.53)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,43)
    chassis_ctrl.move_with_distance(0,1.5)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,47)
    chassis_ctrl.move_with_distance(0,0.56)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,95)
    chassis_ctrl.move_with_distance(0,0.86)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
    chassis_ctrl.move_with_distance(0,0.41)
    time.sleep(5)
#     #B to C
    chassis_ctrl.move_with_distance(0,5)
    chassis_ctrl.move_with_distance(0,1.5)
   #Room C
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
    ScanRoomType()
    chassis_ctrl.move_with_distance(0,2.13)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
    chassis_ctrl.move_with_distance(0,2.13)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
    scan_for_marker()
    if RoomType == 1:
        FireRoom()
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
        chassis_ctrl.move_with_distance(0,2.13)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
        chassis_ctrl.move_with_distance(0,2.13)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
        time.sleep(5)

    elif RoomType == 2:
        PersonRoom()
        # take the person back to point A
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
        chassis_ctrl.move_with_distance(0,2.13)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
        chassis_ctrl.move_with_distance(0,2.13)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
        # need messarment from C to A
        chassis_ctrl.move_with_distance(0,5)
        chassis_ctrl.move_with_distance(0,5)
        # turn facing the opposite way
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
        # Go from A to C
        chassis_ctrl.move_with_distance(0,5)
        chassis_ctrl.move_with_distance(0,5)

    elif RoomType == 3:
        PoisonRoom()
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
        chassis_ctrl.move_with_distance(0,2.13)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
        chassis_ctrl.move_with_distance(0,2.13)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
        time.sleep(5)
   #C To D
    chassis_ctrl.move_with_distance(0,5)
    chassis_ctrl.move_with_distance(0,5)
    chassis_ctrl.move_with_distance(0,0.35)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
    ScanRoomType()
    chassis_ctrl.move_with_distance(0,2.5)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
    chassis_ctrl.move_with_distance(0,1.8)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
    chassis_ctrl.move_with_distance(0,4.4)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
    chassis_ctrl.move_with_distance(0,1.37)
    scan_for_marker()
    if RoomType == 1:
        FireRoom()
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,180)
        chassis_ctrl.move_with_distance(0,1.37)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
        chassis_ctrl.move_with_distance(0,4.5)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
        chassis_ctrl.move_with_distance(0,1.8)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
        chassis_ctrl.move_with_distance(0,2.5)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
    elif RoomType == 2:
        PersonRoom()
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,180)
        chassis_ctrl.move_with_distance(0,1.37)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
        chassis_ctrl.move_with_distance(0,4.5)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
        chassis_ctrl.move_with_distance(0,1.8)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
        chassis_ctrl.move_with_distance(0,2.5)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
        # need messarment from E to A
        chassis_ctrl.move_with_distance(0,5)
        chassis_ctrl.move_with_distance(0,5)
        chassis_ctrl.move_with_distance(0,5)
        # turn facing the opposite way
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
        # Go from A to E
        chassis_ctrl.move_with_distance(0,5)
        chassis_ctrl.move_with_distance(0,5)
        chassis_ctrl.move_with_distance(0,5)

    elif RoomType == 3:
        PoisonRoom()
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,180)
        chassis_ctrl.move_with_distance(0,1.37)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
        chassis_ctrl.move_with_distance(0,4.5)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
        chassis_ctrl.move_with_distance(0,1.8)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
        chassis_ctrl.move_with_distance(0,2.5)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)

    # Go from E to F   #Measurements needed
    chassis_ctrl.move_with_distance(0,2.5) 
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
    chassis_ctrl.move_with_distance(0,2.5)

    #Position F    #Measurements needed
    ScanPositionF()
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
    chassis_ctrl.move_with_distance(0,2.5)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)

    #Go from F to G     #Measurements needed
    chassis_ctrl.move_with_distance(0,2.5)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
    chassis_ctrl.move_with_distance(0,1)

    # skip this room, it is the poison room #Measurements needed
    PoisonRoom()
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
    chassis_ctrl.move_with_distance(0,1)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)

    # Go from G to H    #Measurements needed
    chassis_ctrl.move_with_distance(0,7)

    # face the opposite direction of the hallway
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)

    # Go from H to position D
    chassis_ctrl.move_with_distance(0,5)
    chassis_ctrl.move_with_distance(0,5)
    chassis_ctrl.move_with_distance(0,5)
    chassis_ctrl.move_with_distance(0,4)












