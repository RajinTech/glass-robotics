from gpiozero import PWMLED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep
import RPi.GPIO as GPIO
from classes.air import Air
from classes.motor import Motor
from classes.torch import Torch
                
                #OBJECT INITIALIZATION
pump = Air()
car = Motor("car")
chk = Motor("chk")
mirage = Torch()
                #AIR TEST

pump.blow(.2)
                #MOTOR TEST

chk.left(1, 1) #speed, length
car.left(1, 1)
chk.right(1, 1)
car.right(1, 1)
                #TORCH TEST

mirage.on(1, 0, 0, 0)
sleep(1)
mirage.off()

GPIO.cleanup()