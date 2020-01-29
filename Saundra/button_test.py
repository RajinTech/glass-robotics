#BUTTON SETUP
import RPi.GPIO as GPIO
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 17 to be an input pin and set initial value to be pulled low (off)


count = 0;
while True: # Run forever
    print("start")
    print(count)

    #TACTILE
    if GPIO.input(17) == False:
        count = count + 1
        print("Tactile Button was pushed!")
        print(count)
