def start():
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    RoomType = ScanRoomType()

    if RoomType == 1:
        FireRoom()
    elif RoomType == 2:
        PersonRoom()
    elif RoomType == 3:
        PoisonRoom()

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


