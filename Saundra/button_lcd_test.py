#BUTTONs
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 17 to be an input pin and set initial value to be pulled low (off)



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

    #TACTILE
    if GPIO.input(17) == False:
        display.lcd_clear()
        count = count + 1
        print("Tactile Button was pushed!")
        display.lcd_display_string("Tactile Pushed", 1)
        display.lcd_display_string(str(count), 2)
        print(count)
        
