from time import sleep
import RPi.GPIO as GPIO
from gpiozero import PWMLED

GPIO.setmode(GPIO.BCM)
TRACK_STEP = PWMLED(20)  # Step GPIO Pin
TRACK_DIR = PWMLED(21)   # Direction GPIO Pin
CW = 1     # Clockwise Rotation
CCW = 0    # Counterclockwise Rotation
sleep_count = 1

TRACK_DIR.value = CCW
TRACK_STEP.value = 0.25
sleep(sleep_count)
TRACK_STEP.value = 0
TRACK_DIR.value = CW
TRACK_STEP.value = 0.25
sleep(sleep_count)
TRACK_STEP.value = 0
