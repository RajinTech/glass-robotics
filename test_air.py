from gpiozero import PWMLED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep
import RPi.GPIO as GPIO
from classes.air import Air

pump = Air()
pump.blow(1)
GPIO.cleanup()

