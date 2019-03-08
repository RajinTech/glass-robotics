from gpiozero import PWMLED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

torch = PiGPIOFactory(host='192.168.1.14')
relays = PiGPIOFactory(host='192.168.1.20')
motors = PiGPIOFactory(host='192.168.1.21')
                                            #RELAY PINS
air = PWMLED(18, pin_factory=relay)
                                            #CARRIAGE PINS
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
                                        #TORCH PINS
inpr = PWMLED(18, pin_factory=torch)
inox = PWMLED(25, pin_factory=torch)
ospr = PWMLED(23, pin_factory=torch)
osox = PWMLED(24, pin_factory=torch)


    

while True:
    inpr.value = 1
    inox.value = 1
    ospr.value = 1
    osox.value = 1
    