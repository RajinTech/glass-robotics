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
mode_index = 0
active_mode = "Move"
speed_timer = 0
count = 0
CW = 1     # Clockwise Rotation
CCW = 0    # Counterclockwise Rotation
speed = 0.5
distance = 200 #steps

print("start")
print(count)

#METHODS
def changeMode():
    return new_mode
while True: # Run forever

    if GPIO.input(17) == False:
        print("Down Button was pushed!")
        display.lcd_display_string(active_mode + " Down Pushed", 1)
        display.lcd_display_string(str(count), 2)
        count = count - 1
        speed_timer = speed_timer + 1
        print(count)
        if speed_timer < 7:
            time.sleep(1)
















#
