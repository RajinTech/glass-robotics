from gpiozero import PWMLED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep
import RPi.GPIO as GPIO

class Torch:
    torch = PiGPIOFactory(host='192.168.1.14')
                              #TORCH PINS
    inpr = PWMLED(27, pin_factory=torch)
    inox = PWMLED(25, pin_factory=torch)
    ospr = PWMLED(23, pin_factory=torch)
    osox = PWMLED(24, pin_factory=torch)

    def __init__(self):
        self.data = []
        
    def on(self, inpr_val, inox_val, ospr_val=0, osox_val=0):
        torch = self.torch
        inpr = self.inpr
        inox = self.inox
        ospr = self.ospr
        osox = self.osox
        inpr.value = inpr_val
        inox.value = inox_val
        ospr.value = ospr_val
        osox.value = osox_val
        print("torch on")


    def off(self):
        torch = self.torch
        inpr = self.inpr
        inox = self.inox
        ospr = self.ospr
        osox = self.osox
        inpr.value = 0
        inox.value = 0
        ospr.value = 0
        osox.value = 0
        print("torch off")
GPIO.cleanup()
