import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from gpiozero import LED
from time import sleep
#LEDS
white = LED(06)
red = LED(13)
yellow = LED(19)
green = LED(26)
print("start")
white.value = 1
red.value = 1
yellow.value = 1
green.value = 1
sleep(1)
white.value = 0
red.value = 0
yellow.value = 0
green.value = 0
print("end")




















#
