from gpiozero import PWMLED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep


sol = PWMLED(26)
sol.value = 1
sleep(1)
print(1)
sol.value = 0
sleep (1)

    
