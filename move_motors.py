from gpiozero import PWMLED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep
import RPi.GPIO as GPIO
from classes.motor import Motor

                #MOTOR TEST
car = Motor("car")
chk = Motor("chk")
while True:
    task = input("use a  s  d  f  g  h  or j  k  l  ;   ' to move motors\n    20 10 1  1  11 26    10 1  1  5  10\n:")
    type(task)
    if task == "a":
        car.left(1, 20)
    if task == "s":
        car.left(1, 10)
    if task == "d":
        car.left(.25, 1)
    if task == "f":
        car.right(1, 1)
    if task == "g":
        car.right(1, 11)
    if task == "h":
        car.right(1, 26)
    if task == "j":
        chk.left(1, 10)
    if task == "k":
        chk.left(1, 1)
    if task == "l":
        chk.right(1, 1)
    if task == ";":
        chk.right(1, 5)
    if task == "'":
        chk.right(1, 20)

GPIO.cleanup()