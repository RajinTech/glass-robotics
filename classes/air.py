from gpiozero import PWMLED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep
import RPi.GPIO as GPIO


class Air:
    relays = PiGPIOFactory(host='192.168.1.20') #RELAY PINS
    air_pin = PWMLED(18, pin_factory=relays)

    def __init__(self):
        self.data = []
        
    def blow(self, time):
        relays = self.relays
        air_pin = self.air_pin
        air_pin.value = 1
        print("blow")
        print(time)
        sleep(time)
        air_pin.value = 0

GPIO.cleanup()

