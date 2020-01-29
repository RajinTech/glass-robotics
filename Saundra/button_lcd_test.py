#BUTTONs
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 18 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 17 to be an input pin and set initial value to be pulled low (off)
active_mode=""
MODE = GPIO.input(17)
PUSH = GPIO.input(18)
#UP = GPIO.input(17)
#DOWN = GPIO.input(17)


#LCD SETUP
import lcddriver
import time
display = lcddriver.lcd()


count = 0;
while True: # Run forever
    print("start")
    print(count)
    #PUSH
    if GPIO.input(18) == False:
        count = count + 1
        print("Press Button was pushed!")
        display.lcd_display_string("Press Button was Pushed", 1)
        print(count)
    #TACTILE
    if GPIO.input(17) == False:
        count = count + 1
        print("Tactile Button was pushed!")
        display.lcd_display_string("Tactile Button was Pushed", 1)

        print(count)
