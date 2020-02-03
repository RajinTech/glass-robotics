import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from gpiozero import LED
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
TRACK_STEP = LED(20)  # Step GPIO Pin
TRACK_DIR = LED(21)   # Direction GPIO Pin

#LCD SETUP
import lcddriver
import time
display = lcddriver.lcd()

#STATE
modes = ["Move", "Distance", "Speed", "Ready?", "Running"]
active_mode = "Move"
speed_timer = 0
count = 0
backward = 1     # Clockwise Rotation
forward = 0    # Counterclockwise Rotation
speed = 0.5
distance = 200 #steps

print("start")
print(count)
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
            speed_timer = speed_timer + 1
            if speed_timer < 7:
                time.sleep(1)
        elif GPIO.input(23) == False:
            print("Down Button was pushed!")
            moveTrack(backward, 1, speed)
        elif GPIO.input(24) == False:
            print("Down Button was pushed!")
            moveTrack(forward, 1, speed)
        else:
            speed_timer = 0
            WHITE.value = 0
            display.lcd_display_string(active_mode, 1)
            display.lcd_display_string(str(count), 2)


    elif active_mode == "Distance":
                                                                                #DISTANCE
        if GPIO.input(17) == False:
            WHITE.value = 1
            display.lcd_clear()
            print("Changing Mode" + active_mode)
            active_mode = "Speed"
            speed_timer = speed_timer + 1
            if speed_timer < 7:
                time.sleep(1)
        elif GPIO.input(23) == False:
            print("Down Button was pushed!")
            display.lcd_display_string(active_mode + " Down Pushed", 1)
            display.lcd_display_string(str(count), 2)
            count = count - 1
            speed_timer = speed_timer + 1
            print(count)
            if speed_timer < 7:
                time.sleep(1)
        elif GPIO.input(24) == False:
            print("Up Button was pushed!")
            display.lcd_display_string(active_mode + " Up Pushed", 1)
            display.lcd_display_string(str(count), 2)
            count = count + 1
            speed_timer = speed_timer + 1
            print(count)
            if speed_timer < 7:
                time.sleep(1)
        else:
            WHITE.value = 0
            speed_timer = 0
            display.lcd_display_string(active_mode, 1)
            display.lcd_display_string(str(count), 2)


    elif active_mode == "Speed":
                                                                                #SPEED
        if GPIO.input(17) == False:
            WHITE.value = 1
            display.lcd_clear()
            print("Changing Mode" + active_mode)
            active_mode = "Ready?"
            speed_timer = speed_timer + 1
            if speed_timer < 7:
                time.sleep(1)
        elif GPIO.input(23) == False:
            print("Down Button was pushed!")
            display.lcd_display_string(active_mode + " Down Pushed", 1)
            display.lcd_display_string(str(count), 2)
            count = count - 1
            speed_timer = speed_timer + 1
            print(count)
            if speed_timer < 7:
                time.sleep(1)
        elif GPIO.input(24) == False:
            print("Up Button was pushed!")
            display.lcd_display_string(active_mode + " Up Pushed", 1)
            display.lcd_display_string(str(count), 2)
            count = count + 1
            speed_timer = speed_timer + 1
            print(count)
            if speed_timer < 7:
                time.sleep(1)
        else:
            WHITE.value = 0
            speed_timer = 0
            display.lcd_display_string(active_mode, 1)
            display.lcd_display_string(str(count), 2)



    elif active_mode == "Ready?":
                                                                                #READY?
        if GPIO.input(17) == False:
            WHITE.value = 1
            display.lcd_clear()
            print("Changing Mode" + active_mode)
            active_mode = "Running"
            speed_timer = speed_timer + 1
            if speed_timer < 7:
                time.sleep(1)
        elif GPIO.input(23) == False:
            print("Down Button was pushed!")
            display.lcd_display_string(active_mode + " Down Pushed", 1)
            display.lcd_display_string(str(count), 2)
            count = count - 1
            speed_timer = speed_timer + 1
            print(count)
            if speed_timer < 7:
                time.sleep(1)
        elif GPIO.input(24) == False:
            print("Up Button was pushed!")
            display.lcd_display_string(active_mode + " Up Pushed", 1)
            display.lcd_display_string(str(count), 2)
            count = count + 1
            speed_timer = speed_timer + 1
            print(count)
            if speed_timer < 7:
                time.sleep(1)
        else:
            WHITE.value = 0
            speed_timer = 0
            display.lcd_display_string(active_mode, 1)
            display.lcd_display_string(str(count), 2)

    elif active_mode == "Running":
                                                                                #RUNNING
        if GPIO.input(17) == False:
            WHITE.value = 1
            display.lcd_clear()
            print("Changing Mode" + active_mode)
            active_mode = "Move"
            speed_timer = speed_timer + 1
            if speed_timer < 7:
                time.sleep(1)
        elif GPIO.input(23) == False:
            print("Down Button was pushed!")
            display.lcd_display_string(active_mode + " Down Pushed", 1)
            display.lcd_display_string(str(count), 2)
            count = count - 1
            speed_timer = speed_timer + 1
            print(count)
            if speed_timer < 7:
                time.sleep(1)
        elif GPIO.input(24) == False:
            print("Up Button was pushed!")
            display.lcd_display_string(active_mode + " Up Pushed", 1)
            display.lcd_display_string(str(count), 2)
            count = count + 1
            speed_timer = speed_timer + 1
            print(count)
            if speed_timer < 7:
                time.sleep(1)
        else:
            WHITE.value = 0
            speed_timer = 0
            display.lcd_display_string(active_mode, 1)
            display.lcd_display_string(str(count), 2)

















#
