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

                #BUBBLE CONDENSE

for x in range(3):
    mirage.on(.57, .825, 0, .6)
    sleep(.15)
    bubble_counter = 0
    range_max = 13
    for x in range(range_max):
        car.left(.05, 1)
        sleep(2)
        bubble_counter += 1
        if bubble_counter >= 6:
            chk.left(.025, 1)
        if bubble_counter == range_max:
            car.right(.1, 1)
            sleep(.2)
    chk.left(.025, 1)
    mirage.off()
    sleep(1.75)
                                    #BLOW
    pump.blow(.2)
    sleep(2)
    pump.blow(.075)
    chk.left(.125, 1)
                            #COOL OFF
    mirage.on(0, 1, 0, 0)
    sleep(8)
    mirage.off()

                                #MOVE TO NEXT OPERATION 1
    car.left(1.1, 1)

                                #MARIA
                        #VARIABLES
    maria_counter = 0
    range_max = 12
                                #MARIA CONDENSE
    mirage.on(.54, .86, 0, .6)
    sleep(.075)
    for x in range(range_max):
        print("step 1")
        car.left(.0675, 1)
        sleep(2)
        maria_counter += 1
        print("step 2")
        if maria_counter >= 5:
            chk.left(.14, 1)
            print("step 3")
        if maria_counter >=9:
            mirage.on(.53, .87, 0, .6)

    mirage.off()
    sleep(.2)
                                #PUSH
    push_count = 3
    for x in range(push_count):
        sleep(1)
        chk.left(.05, 1)
                                #MOVE TO NEXT OPERATION
    print("step 6")
    sleep(1.75)
    car.right(1.25, 1)
    sleep(10)
                                #TIP
    mirage.on(.53, .87, 0, .6)
    sleep(12)
    mirage.off()
    chk.right(.115, 1)

                                #MOVE TO NEXT OPERATION
    print("step 6")
    sleep(1.75)
    car.left(1.9, 1)


GPIO.cleanup()