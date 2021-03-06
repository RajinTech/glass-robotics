from gpiozero import PWMLED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep
import RPi.GPIO as GPIO

class Motor:
    delay = .005
    motors = PiGPIOFactory(host='192.168.1.21')#Create Factory

    CAR_STEP = PWMLED(25, pin_factory=motors)
    CAR_DIR = PWMLED(12, pin_factory=motors)
    CAR_M0 = PWMLED(18, pin_factory=motors)
    CAR_M1 = PWMLED(23, pin_factory=motors)
    CAR_M2 = PWMLED(24, pin_factory=motors)
                                            #CHUCK PINS
    CHK_STEP = PWMLED(19, pin_factory=motors)
    CHK_DIR = PWMLED(26, pin_factory=motors)
    CHK_M0 = PWMLED(16, pin_factory=motors)
    CHK_M1 = PWMLED(20, pin_factory=motors)
    CHK_M2 = PWMLED(21, pin_factory=motors)
    
    
    def __init__(self, name):
        self.data = []
        self.name = name
     
                                        #RIGHT        
    def right(self, speed, length):
        motors = self.motors
        if self.name == "car":
            dir = self.CAR_DIR
            step = self.CAR_STEP
            for x in range(length):
                print(self.name)
                dir.value = 0
                step.value = .5
                sleep(speed)
                step.value = 0
        if self.name == "chk":
            dir = self.CHK_DIR
            step = self.CHK_STEP
            for x in range(length):
                print(self.name)
                dir.value = 0
                step.value = .5
                sleep(speed)
                step.value = 0
                                       #LEFT
    def left(self, speed, length):
        motors = self.motors
        if self.name == "car" and self.name != "chk":
            dir = self.CAR_DIR
            step = self.CAR_STEP
            for x in range(length):
                print(self.name)
                dir.value = 1
                step.value = .5
                sleep(speed)
                step.value = 0
        if self.name == "chk" and self.name != "car":
            dir = self.CHK_DIR
            step = self.CHK_STEP
            for x in range(length):
                print(self.name)
                dir.value = 1
                step.value = .5
                sleep(speed)
                step.value = 0
                                          #STEP LEFT
    def stepleft(self, steps):
        motors = self.motors
        if self.name == "car" and self.name != "chk":
            dir = self.CAR_DIR
            step = self.CAR_STEP
            print(self.name, "<", steps)
            for x in range(steps):
                dir.value = 1
                step.on()
                sleep(self.delay)
                step.off()
                sleep(self.delay)
        if self.name == "chk" and self.name != "car":
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
        if self.name == "car" and self.name != "chk":
            dir = self.CAR_DIR
            step = self.CAR_STEP
            print(self.name, steps, ">")
            for x in range(steps):
                dir.value = 0
                step.on()
                sleep(self.delay)
                step.off()
                sleep(self.delay)
        if self.name == "chk" and self.name != "car":
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
        
    
