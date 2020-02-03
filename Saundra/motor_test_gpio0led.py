from time import sleep
import RPi.GPIO as GPIO
from gpiozero import LED

GPIO.setmode(GPIO.BCM)
TRACK_STEP = LED(20)  # Step GPIO Pin
TRACK_DIR = LED(21)   # Direction GPIO Pin
CW = 1     # Clockwise Rotation
CCW = 0    # Counterclockwise Rotation
speed = 0.1
distance = 200 #steps

for x in range(distance):
    TRACK_DIR.value = CCW
    TRACK_STEP.value = 1
    sleep(speed)
    TRACK_STEP.value = 0

for x in range(distance):
    TRACK_DIR.value = CW
    TRACK_STEP.value = 1
    sleep(speed)
    TRACK_STEP.value = 0
