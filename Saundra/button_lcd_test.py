#BUTTONs
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 18 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 17 to be an input pin and set initial value to be pulled low (off)
MODE = GPIO.input(17)
PUSH = GPIO.input(18)
#UP = GPIO.input(17)
#DOWN = GPIO.input(17)


#LCD SETUP
import lcddriver
import time
display = lcddriver.lcd()

#STATE
active_mode="Jog"
count = 0;

while True: # Run forever
    print("start")
    print(count)
    display.lcd_display_string(active_mode, 1)
    display.lcd_display_string(str(count), 2)
    #PUSH
    if GPIO.input(18) == True:
        count = count + 1
        print("Press Button was pushed!")
        display.lcd_display_string("Press Button was Pushed", 1)
        display.lcd_display_string(str(count), 2)
        print(count)
    #TACTILE
    if MODE == False:
        count = count + 1
        print("Tactile Button was pushed!")
        display.lcd_display_string("Tactile Pushed", 1)
        display.lcd_display_string(str(count), 2)
        print(count)
