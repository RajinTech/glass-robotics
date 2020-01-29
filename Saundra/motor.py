#PRESS BUTTON
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 18 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 17 to be an input pin and set initial value to be pulled low (off)

count = 0;
while True: # Run forever
    print("start")
    if GPIO.input(18) == GPIO.HIGH:
        count = count + 1
        print("Press Button was pushed!")
        print(count)
    if GPIO.input(17) == False:
        count = count + 1
        print("Tactile Button was pushed!")
        print(count)
