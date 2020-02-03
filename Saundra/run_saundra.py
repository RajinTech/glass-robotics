import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from gpiozero import LED
from gpiozero import PWMLED
from time import sleep
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setwarnings(False) # Ignore warning for now

#BUTTONS
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 17 to be an input pin and set initial value to be pulled low (off)

#RELAY
RELAY = LED(25)

#LEDS
WHITE = LED(06)
RED = LED(13)
YELLOW = LED(19)
GREEN = LED(26)

#MOTOR
TRACK_STEP = PWMLED(20)  # Step GPIO Pin
TRACK_DIR = PWMLED(21)   # Direction GPIO Pin

#LCD SETUP
import lcddriver
import time
display = lcddriver.lcd()

#STATE
modes = ["Move", "Distance", "Speed", "Ready?", "Running"]
active_mode = "Move"
speed_timer = 0
position = 0
backward = 1     # Clockwise Rotation
forward = 0    # Counterclockwise Rotation
speed = 0.5
distance = 900 #steps

print("start")
print(position)
def moveTrack(dir, dis, spd):
    for x in range(dis):
        TRACK_DIR.value = dir
        TRACK_STEP.value = 1
        sleep(spd)
        TRACK_STEP.value = 0
    print("dir " + str(dir) + "dis" + str(dis) + "spd" + str(spd))
while True: # Run forever

    if active_mode == "Move":
                                                                                #MOVE
        if GPIO.input(17) == False:
            WHITE.value = 1
            display.lcd_clear()
            print("Changing Mode" + active_mode)
            active_mode = "Distance"
            display.lcd_display_string(active_mode, 1)
            speed_timer = speed_timer + 1
            if speed_timer < 3:
                time.sleep(1)
        elif GPIO.input(23) == False:
            WHITE.value = 1
            print("Down Button was pushed!")

            TRACK_DIR.value = backward
            TRACK_STEP.value = 0.5
        elif GPIO.input(24) == False:
            print("Up Button was pushed!")
            WHITE.value = 1
            TRACK_DIR.value = forward
            TRACK_STEP.value = 0.5
        else:
            speed_timer = 0
            WHITE.value = 0
            TRACK_STEP.value = 0
            display.lcd_display_string(active_mode, 1)
            display.lcd_display_string(str(position), 2)




    elif active_mode == "Distance":
                                                                                #DISTANCE
        if GPIO.input(17) == False:
            WHITE.value = 1
            display.lcd_clear()
            print("Changing Mode" + active_mode)
            active_mode = "Speed"
            display.lcd_display_string(active_mode, 1)
            speed_timer = speed_timer + 1
            if speed_timer < 3:
                time.sleep(1)
        elif GPIO.input(23) == False:
            print("Down Button was pushed!")
            WHITE.value = 1
            display.lcd_display_string(active_mode + " Down Pushed", 1)
            display.lcd_display_string(str(distance), 2)
            distance = distance - 1
            speed_timer = speed_timer + 1
            print(distance)
            if speed_timer < 3:
                time.sleep(1)
        elif GPIO.input(24) == False:
            print("Up Button was pushed!")
            WHITE.value = 1
            display.lcd_display_string(active_mode + " Up Pushed", 1)
            display.lcd_display_string(str(distance), 2)
            distance = distance + 1
            speed_timer = speed_timer + 1
            print(distance)
            if speed_timer < 3:
                time.sleep(1)
        else:
            WHITE.value = 0
            speed_timer = 0
            display.lcd_display_string(active_mode, 1)
            display.lcd_display_string(str(distance), 2)


    elif active_mode == "Speed":
                                                                                #SPEED
        if GPIO.input(17) == False:
            WHITE.value = 1
            display.lcd_clear()
            print("Changing Mode" + active_mode)
            active_mode = "Ready?"
            display.lcd_display_string(active_mode, 1)
            speed_timer = speed_timer + 1
            if speed_timer < 3:
                time.sleep(1)
        elif GPIO.input(23) == False:
            print("Down Button was pushed!")
            WHITE.value = 1
            display.lcd_display_string(active_mode + " Down Pushed", 1)
            display.lcd_display_string(str(speed), 2)
            speed = speed - 0.01
            if speed <= 0.01:
                speed = 0.01
            speed_timer = speed_timer + 1
            print(speed)
            if speed_timer < 3:
                time.sleep(1)
        elif GPIO.input(24) == False:
            print("Up Button was pushed!")
            WHITE.value = 1
            LCD_ENTRYRIGHT = 0x00
            display.lcd_display_string(active_mode + " Up Pushed", 1)
            display.lcd_display_string(str(speed), 2)
            speed = speed + 0.01
            if speed <= 0.01:
                speed = 0.01
            speed_timer = speed_timer + 1
            print(speed)
            if speed_timer < 3:
                time.sleep(1)
        else:
            WHITE.value = 0
            speed_timer = 0
            display.lcd_display_string(active_mode, 1)
            display.lcd_display_string(str(speed), 2)



    elif active_mode == "Ready?":
                                                                                #READY?

        if GPIO.input(17) == False:
            WHITE.value = 1
            display.lcd_clear()
            print("Changing Mode" + active_mode)
            active_mode = "Move"
            display.lcd_display_string(active_mode, 1)
            speed_timer = speed_timer + 1
            if speed_timer < 3:
                time.sleep(1)
        elif GPIO.input(23) == False:
            print("Down Button was pushed!")
            WHITE.value = 1
            display.lcd_clear()
            print("Now Ready" + active_mode)
            active_mode = "Running"
            display.lcd_display_string(active_mode, 1)
            speed_timer = speed_timer + 1
            if speed_timer < 3:
                time.sleep(1)
        elif GPIO.input(24) == False:
            print("Up Button was pushed!")
            WHITE.value = 1
            display.lcd_clear()
            print("Now Ready" + active_mode)
            active_mode = "Running"
            display.lcd_display_string(active_mode, 1)
            speed_timer = speed_timer + 1
            print(position)
            if speed_timer < 3:
                time.sleep(1)
        else:
            WHITE.value = 0
            speed_timer = 0
            display.lcd_display_string(active_mode, 1)
            display.lcd_display_string("Press Up to Start", 2)

    elif active_mode == "Running":
                                                                                #RUNNING
        RED.value = 1
        time.sleep(1)
        YELLOW.value = 1
        RED.value = 0
        time.sleep(1)
        GREEN.value = 1
        YELLOW.value = 0
        time.sleep(1)
                                                                                #START RELAY
        RELAY.value = 1

                                                                                #START MOTOR

        for x in range(distance):
            TRACK_DIR.value = forward
            TRACK_STEP.value = 0.5
            print("step backward")
            time.sleep(0.01)
            TRACK_STEP.value = 0
            time.sleep(speed)
        for x in range(distance):
            TRACK_DIR.value = backward
            TRACK_STEP.value = 0.5
            print("step forward")
            time.sleep(0.01)
            TRACK_STEP.value = 0
            time.sleep(speed)
                                                                                #STOP RELAY
        GREEN.value = 0                                                                        
        RELAY.value = 0
        time.sleep(1)

        active_mode = "Move"
        display.lcd_clear()

        if GPIO.input(17) == False:
            TRACK_STEP.value = 0
            WHITE.value = 1
            display.lcd_clear()
            print("Changing Mode" + active_mode)
            active_mode = "Move"
            display.lcd_display_string(active_mode, 1)
            speed_timer = speed_timer + 1
            if speed_timer < 3:
                time.sleep(1)
        elif GPIO.input(23) == False:
            print("Down Button was pushed!")
            TRACK_STEP.value = 0
            WHITE.value = 1
            display.lcd_display_string(active_mode + " Down Pushed", 1)
            display.lcd_display_string(str(position), 2)
            position = position - 1
            speed_timer = speed_timer + 1
            print("Pause")
            if speed_timer < 3:
                time.sleep(1)
        elif GPIO.input(24) == False:
            print("Up Button was pushed!")
            TRACK_STEP.value = 0
            WHITE.value = 1
            display.lcd_display_string(active_mode + " Up Pushed", 1)
            display.lcd_display_string(str(position), 2)
            position = position + 1
            speed_timer = speed_timer + 1
            print(position)
            if speed_timer < 3:
                time.sleep(1)
        else:
            WHITE.value = 0
            speed_timer = 0
            display.lcd_display_string(active_mode, 1)


















#
