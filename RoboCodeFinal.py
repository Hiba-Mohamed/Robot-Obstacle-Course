def poison():
    media_ctrl.play_sound(rm_define.media_custom_audio_3)

    
def domo():
    media_ctrl.play_sound(rm_define.media_custom_audio_1)
def I_am_here():
    media_ctrl.play_sound(rm_define.media_custom_audio_2)
def vision_recognized_marker_letter_F(msg):
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
    vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_F)
    gun_ctrl.fire_once()

def scan_for_person():
    vision_ctrl.enable_detection(rm_define.vision_detection_people)
    gimbal_ctrl.pitch_ctrl(35)
    gimbal_ctrl.yaw_ctrl(-70)
    gimbal_ctrl.yaw_ctrl(70)
    I_am_here()
    vision_ctrl.disable_detection(rm_define.vision_detection_people)

def ddance():
    media_ctrl.enable_sound_recognition(rm_define.sound_detection_applause)
    media_ctrl.cond_wait(rm_define.cond_sound_recognized_applause_twice)
    media_ctrl.play_sound(rm_define.media_sound_count_down)
    led_ctrl.set_top_led(rm_define.armor_top_right, 255, 0, 0, rm_define.effect_flash)
    led_ctrl.set_top_led(rm_define.armor_top_left, 255, 0, 150, rm_define.effect_flash)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_front, 255, 193, 0, rm_define.effect_flash)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_right, 36, 103, 255, rm_define.effect_flash)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_left, 255, 50, 0, rm_define.effect_flash)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_back, 0, 127, 70, rm_define.effect_flash)
    media_ctrl.play_sound(rm_define.media_custom_audio_0)
    for count in range (3):
        robot_ctrl.set_mode(rm_define.robot_mode_free)
        chassis_ctrl.set_rotate_speed(110)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,45 )
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,45 )
        gimbal_ctrl.set_rotate_speed(120)
        gimbal_ctrl.rotate_with_degree(rm_define.gimbal_up,50)
        gimbal_ctrl.rotate_with_degree(rm_define.gimbal_down,40)
        gimbal_ctrl.rotate(rm_define.gimbal_right)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,360)
        gimbal_ctrl.rotate(rm_define.gimbal_left)
        gimbal_ctrl.rotate(rm_define.gimbal_right)
        
def Dend():
    led_ctrl.turn_off(rm_define.armor_all)
    time.sleep(5)       
        
        
            
        

    
def scan_for_marker():
    vision_ctrl.enable_detection(rm_define.vision_detection_marker)
    gimbal_ctrl.pitch_ctrl(8)
    gimbal_ctrl.yaw_ctrl(-70)
    gimbal_ctrl.yaw_ctrl(70)

def position_F_three():
    led_ctrl. set_flash(rm_define.armor_all, 10)
    led_ctrl. set_top_led(rm_define. armor_top_all,255, 0, 150, rm_define.effect_flash)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 50, 0, rm_define.effect_flash)
    gimbal_ctrl.yaw_ctrl(120)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 360)
    #possibly turn off LEDs after lightshow
def position_F_two():
    led_ctrl. set_flash(rm_define.armor_all, 10)
    led_ctrl. set_top_led(rm_define. armor_top_all,255, 0, 150, rm_define.effect_flash)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 50, 0, rm_define.effect_flash)
    #possibly turn off LEDs after lightshow
def position_F_one(): 
    gimbal_ctrl.yaw_ctrl(120)   
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 360)
#A scan spefically for point F
def ScanPositionF():
    vision_ctrl.enable_detection(rm_define.vision_detection_marker)
    gimbal_ctrl.pitch_ctrl(8)
    gimbal_ctrl.yaw_ctrl(-30)
    gimbal_ctrl.yaw_ctrl(30)
    
    
    if vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_one):
        position_F_one()
         
    elif vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_two):
        position_F_two()
         
    elif vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_three):
        position_F_three()
      
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)

def Room1Type1():
    #entering room
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
    chassis_ctrl.move_with_distance(0,2.13)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
    chassis_ctrl.move_with_distance(0,2.13)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
    scan_for_marker()
    #leaving room
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
    chassis_ctrl.move_with_distance(0,2.13)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
    chassis_ctrl.move_with_distance(0,2.13)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
    #moving to D
    chassis_ctrl.move_with_distance(0,5)
    chassis_ctrl.move_with_distance(0,0.2)
    
    

def Room1Type3():
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
    chassis_ctrl.move_with_distance(0,2.13)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
    chassis_ctrl.move_with_distance(0,2.13)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
    scan_for_person()
    media_ctrl.play_sound(rm_define.media_custom_audio_2)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_right, 36, 103, 255, rm_define.effect_flash)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_left, 255, 0, 0, rm_define.effect_flash)
    led_ctrl.set_top_led(rm_define.armor_top_right, 255, 0, 0, rm_define.effect_breath)
    led_ctrl.set_top_led(rm_define.armor_top_left, 36, 103, 255, rm_define.effect_breath)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_front, 255, 0, 0, rm_define.effect_always_on)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_back, 36, 103, 255, rm_define.effect_always_on)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
    chassis_ctrl.move_with_distance(0,2.13)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
    chassis_ctrl.move_with_distance(0,2.13)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
    chassis_ctrl.move_with_distance(0,5)
    chassis_ctrl.move_with_distance(0,1)
    
    time.sleep(5)
    chassis_ctrl.move_with_distance(0,5)
    chassis_ctrl.move_with_distance(0,3.3)
    led_ctrl.turn_off(rm_define.armor_all)
    
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,180)
    time.sleep(5)
    chassis_ctrl.move_with_distance(0,5)
    chassis_ctrl.move_with_distance(0,3.3)
    time.sleep(5)
    chassis_ctrl.move_with_distance(0,5)
    chassis_ctrl.move_with_distance(0,5)
    chassis_ctrl.move_with_distance(0,1.7)
    
def Room2Type1():
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
    chassis_ctrl.move_with_distance(0,2.5)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
    chassis_ctrl.move_with_distance(0,1.8)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
    chassis_ctrl.move_with_distance(0,4.4)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
    chassis_ctrl.move_with_distance(0,1.37)
    scan_for_marker()
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,180)
    chassis_ctrl.move_with_distance(0,1.37)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
    chassis_ctrl.move_with_distance(0,4.5)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
    chassis_ctrl.move_with_distance(0,1.8)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
    chassis_ctrl.move_with_distance(0,2.5)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
    chassis_ctrl.move_with_distance(0,3.8)
    time.sleep(5)
  
    

    
def Room2Type3():
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
    chassis_ctrl.move_with_distance(0,2.5)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
    chassis_ctrl.move_with_distance(0,1.8)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
    chassis_ctrl.move_with_distance(0,4.4)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
    scan_for_person()
    media_ctrl.play_sound(rm_define.media_custom_audio_2)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
    chassis_ctrl.move_with_distance(0,4.5)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
    chassis_ctrl.move_with_distance(0,1.8)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
    chassis_ctrl.move_with_distance(0,2.5)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
    chassis_ctrl.move_with_distance(0,5)
    chassis_ctrl.move_with_distance(0,0.8)
    time.sleep(5)
    chassis_ctrl.move_with_distance(0,5)
    chassis_ctrl.move_with_distance(0,5)
    chassis_ctrl.move_with_distance(0,1.7)
    time.sleep(5)
    chassis_ctrl.move_with_distance(0,5)
    chassis_ctrl.move_with_distance(0,3.3)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,180)
    chassis_ctrl.move_with_distance(0,5)
    chassis_ctrl.move_with_distance(0,3.3)
    time.sleep(5)
    chassis_ctrl.move_with_distance(0,5)
    chassis_ctrl.move_with_distance(0,5)
    chassis_ctrl.move_with_distance(0,1.7)
    time.sleep(5)
    chassis_ctrl.move_with_distance(0,5)
    chassis_ctrl.move_with_distance(0,3.8)

   

def Room2Type2():
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,360)
    chassis_ctrl.move_with_distance(0,3.5)



def Room1Type2():
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
    poison()
    
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)

    
    


def start():
    Room1Type = 3
    Room2Type = 1
    Room3Type = 2
    
    robot_ctrl.set_mode(rm_define.robot_mode_free)


# #     #A to B
    chassis_ctrl.move_with_distance(0,5) 
    chassis_ctrl.move_with_distance(0,0.47)
    
    
    # #B Obstacle course
    
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
#     # #B to C

    chassis_ctrl.move_with_distance(0,5)
    chassis_ctrl.move_with_distance(0,1.5)
    
    # # #Room C
    if Room1Type == 1:
        Room1Type1()
    elif Room1Type == 2:
        Room1Type2()
    elif Room1Type == 3:
        Room1Type3()

    
    #ALL OF THE ROOM C FUNCTIONS WILL END AT CHECKPOINT D THEN SLEEP
    


    #D to E
    time.sleep(5)
    chassis_ctrl.move_with_distance(0,5)
    chassis_ctrl.move_with_distance(0,0.1)

    
    if Room2Type == 1:
        Room2Type1()
    elif Room2Type == 2:
        Room2Type2()
    elif Room2Type == 3:
        Room2Type3()
    

#     # Point F, turns right to face marker and sleeps
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
    time.sleep(5) 
    #Will automatically scan and execute the required effect
    ScanPositionF()
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
    chassis_ctrl.move_with_distance(0,3.31)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
    time.sleep(2)
    poison()
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
    #Movement from last room to H
    chassis_ctrl.move_with_distance(0,5)
    chassis_ctrl.move_with_distance(0,2)
    
    #Arrives at H and goes to sleep for 5s
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,180)
    time.sleep(5)
    #Moves from H back to F
    chassis_ctrl.move_with_distance(0,5)
    chassis_ctrl.move_with_distance(0,5)
    chassis_ctrl.move_with_distance(0,0.31)
    time.sleep(5)
    chassis_ctrl.move_with_distance(0,5)
    chassis_ctrl.move_with_distance(0,3.8)
#     #D GOES HERE
    ddance()
    Dend()
    
    domo()
    
    chassis_ctrl.move_with_distance(0,5)
    chassis_ctrl.move_with_distance(0,5)
    chassis_ctrl.move_with_distance(0,1.7)
    time.sleep
    chassis_ctrl.move_with_distance(0,5)
    chassis_ctrl.move_with_distance(0,3.3)
