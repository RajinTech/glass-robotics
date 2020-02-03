#BUTTON SETUP
import RPi.GPIO as GPIO
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 17 to be an input pin and set initial value to be pulled low (off)


count = 0;
print("start")
print(count)
while True: # Run forever

    #Mode
    if GPIO.input(17) == False:
        count = count + 1
        print("Mode Button was pushed!")
        print(count)
    #Mode
    if GPIO.input(23) == False:
        count = count + 1
        print("Down Button was pushed!")
        print(count)
    #Mode
    if GPIO.input(24) == False:
        count = count + 1
        print("Up Button was pushed!")
        print(count)
