from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep
import RPi.GPIO as GPIO

sol = LED(26)
GPIO.cleanup()