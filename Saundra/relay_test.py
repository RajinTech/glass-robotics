
#RELAY
import time
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(25, GPIO.OUT)

while True: # Run forever
    GPIO.output(25, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(25, GPIO.LOW)
    time.sleep(1)
GPIO.cleanup()






















#
