from time import sleep
import RPi.GPIO as GPIO
from gpiozero import PWMLED

TILT_STEP = PWMLED(20)  # Step GPIO Pin
TILT_DIR = PWMLED(21)   # Direction GPIO Pin
TRACK_STEP = PWMLED(2)   # Direction GPIO Pin
TRACK_DIR = PWMLED(3)   # Direction GPIO Pin
#DRILL_STEP = PWMLED(20)  # Step GPIO Pin
#DRILL_DIR = PWMLED(21)   # Direction GPIO Pin
ROTATE_STEP = PWMLED(12)   # Direction GPIO Pin
ROTATE_DIR = PWMLED(16)   # Direction GPIO Pin
CW = 1     # Clockwise Rotation
CCW = 0    # Counterclockwise Rotation
SPR = 1   # Steps per Revolution (360 / 7.5)

sleep_count = SPR
delay = .0025

TILT_DIR.value = CCW
for x in range(sleep_count):
    TILT_STEP.value = 0.25
    sleep(sleep_count)
    TILT_STEP.value = 0
    TILT_DIR.value = CW
    TILT_STEP.value = 0.25
    sleep(sleep_count)
    TILT_STEP.value = 0

sleep(0.5)

TRACK_DIR.value = CCW
for x in range(sleep_count):
    TRACK_STEP.value = 0.25
    sleep(sleep_count)
    TRACK_STEP.value = 0
    TRACK_DIR.value = CW
    TRACK_STEP.value = 0.25
    sleep(sleep_count)
    TRACK_STEP.value = 0

sleep(0.5)

ROTATE_DIR.value = CCW
for x in range(sleep_count):
    ROTATE_STEP.value = 0.25
    sleep(sleep_count)
    ROTATE_STEP.value = 0
    ROTATE_DIR.value = CW
    ROTATE_STEP.value = 0.25
    sleep(sleep_count)
    ROTATE_STEP.value = 0

sleep(0.5)


    print('done')

GPIO.cleanup()
