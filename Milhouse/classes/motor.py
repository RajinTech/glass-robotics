from gpiozero import PWMLED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep
import RPi.GPIO as GPIO

class Motor:
    motors = PiGPIOFactory(host='192.168.1.21')#Create Factory

    TRACK_STEP = PWMLED(25)
    TRACK_DIR = PWMLED(12)
    ROTATE_STEP = PWMLED(19)
    ROTATE_DIR = PWMLED(26)
    TILT_STEP = PWMLED(19)
    TILT_DIR = PWMLED(26)

    delay = .005

    def __init__(self, name):
        self.data = []
        self.name = name

                                        #RIGHT
    def right(self, speed, length):
        motors = self.motors
        if self.name == "track":
            dir = self.TRACK_DIR
            step = self.TRACK_STEP
            for x in range(length):
                print(self.name)
                dir.value = 0
                step.value = .5
                sleep(speed)
                step.value = 0
        if self.name == "tilt":
            dir = self.TILT_DIR
            step = self.TILT_STEP
            for x in range(length):
                print(self.name)
                dir.value = 0
                step.value = .5
                sleep(speed)
                step.value = 0
        if self.name == "rotate":
            dir = self.TILT_DIR
            step = self.TILT_STEP
            for x in range(length):
                print(self.name)
                dir.value = 0
                step.value = .5
                sleep(speed)
                step.value = 0
                                       #LEFT
    def leftt(self, speed, length):
        motors = self.motors
        if self.name == "track":
            dir = self.TRACK_DIR
            step = self.TRACK_STEP
            for x in range(length):
                print(self.name)
                dir.value = 1
                step.value = .5
                sleep(speed)
                step.value = 0
        if self.name == "tilt":
            dir = self.TILT_DIR
            step = self.TILT_STEP
            for x in range(length):
                print(self.name)
                dir.value = 1
                step.value = .5
                sleep(speed)
                step.value = 0
        if self.name == "rotate":
            dir = self.TILT_DIR
            step = self.TILT_STEP
            for x in range(length):
                print(self.name)
                dir.value = 1
                step.value = .5
                sleep(speed)
                step.value = 0
                                          #STEP LEFT
    def stepleft(self, steps):
        motors = self.motors
        if self.name == "track" and self.name != "chk":
            dir = self.CAR_DIR
            step = self.CAR_STEP
            print(self.name, "<", steps)
            for x in range(steps):
                dir.value = 1
                step.on()
                sleep(self.delay)
                step.off()
                sleep(self.delay)
        if self.name == "chk" and self.name != "track":
            dir = self.CHK_DIR
            step = self.CHK_STEP
            print(self.name, "<", steps)
            for x in range(steps):
                dir.value = 1
                step.on()
                sleep(self.delay)
                step.off()
                sleep(self.delay)
                                    #STEP RIGHT
    def stepright(self, steps):
        motors = self.motors
        if self.name == "track" and self.name != "chk":
            dir = self.CAR_DIR
            step = self.CAR_STEP
            print(self.name, steps, ">")
            for x in range(steps):
                dir.value = 0
                step.on()
                sleep(self.delay)
                step.off()
                sleep(self.delay)
        if self.name == "chk" and self.name != "track":
            dir = self.CHK_DIR
            step = self.CHK_STEP
            print(self.name, steps, ">")
            for x in range(steps):
                dir.value = 0
                step.on()
                sleep(self.delay)
                step.off()
                sleep(self.delay)

GPIO.cleanup()
