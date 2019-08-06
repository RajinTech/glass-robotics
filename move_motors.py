from gpiozero import PWMLED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep
import RPi.GPIO as GPIO
from classes.motor import Motor

                #MOTOR TEST
track = Motor("track")
rotate = Motor("rotate")
tilt = Motor("tilt")
while True:
    task = input("use a  s  d  f  g  h  or j  k  l  ;   ' to move motors\n    20 10 1  1  11 26    10 1  1  5  10\n:")
    type(task)
    if task == "a":
        track.left(1, 20)
    if task == "s":
        track.left(1, 10)
    if task == "d":
        track.left(.25, 1)
    if task == "f":
        track.right(1, 1)
    if task == "g":
        track.right(1, 11)
    if task == "h":
        track.right(1, 26)
    if task == "j":
        rotate.left(1, 10)
    if task == "k":
        rotate.left(1, 1)
    if task == "l":
        rotate.right(1, 1)
    if task == ";":
        rotate.right(1, 5)
    if task == "'":
        rotate.right(1, 20)

GPIO.cleanup()
