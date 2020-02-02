from time import sleep
import RPi.GPIO as GPIO
from gpiozero import PWMLED

TRACK_STEP = PWMLED(20)  # Step GPIO Pin
TRACK_DIR = PWMLED(21)   # Direction GPIO Pin
CW = 1     # Clockwise Rotation
CCW = 0    # Counterclockwise Rotation

sleep_count = 0.5

TRACK_DIR.value = CCW
for x in range(sleep_count):
    TRACK_STEP.value = 0.25
    sleep(sleep_count)
    TRACK_STEP.value = 0
    TRACK_DIR.value = CW
    TRACK_STEP.value = 0.25
    sleep(sleep_count)
    TRACK_STEP.value = 0

GPIO.cleanup()
