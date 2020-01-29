#BUTTONs
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 17 to be an input pin and set initial value to be pulled low (off)

#RELAY
GPIO.setup(25, GPIO.OUT)


while True: # Run forever
    input_value = GPIO.input(17)
    if input_value == False:
        print("Tactile Button was pushed!")
        GPIO.output(25, GPIO.HIGH)
        while input_value == False:
            input_value = GPIO.input(17)























#
