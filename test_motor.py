from gpiozero import PWMLED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep
import RPi.GPIO as GPIO
from classes.motor import Motor


car = Motor("car")
chk = Motor("chk")
##car.stepleft(200)
##chk.stepleft(200)
##car.stepright(200)
##chk.stepright(200)
car.left(1, 1)#(time on, times on)
chk.left(1, 1)

car.right(1, 1)
chk.right(1, 1)
GPIO.cleanup()
