from gpiozero import PWMLED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep
import RPi.GPIO as GPIO
from classes.torch import Torch

mirage = Torch()

mirage.on(1, 1, 1, 1)
print(2)
sleep(.2)
mirage.off()

GPIO.cleanup()