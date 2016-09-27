import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT) #make pin 3 output



def blink():
	GPIO.output(3, 1) #output high on 3
	time.sleep(0.7)
	GPIO.output(3, 0) #output high on 3
	time.sleep(0.3)
	GPIO.output(3, 1) #output high on 3
	time.sleep(0.7)
	GPIO.output(3, 0) #output high on 3
	time.sleep(0.3)
        GPIO.output(3, 1) #output high on 3
	time.sleep(0.7)
	GPIO.output(3, 0) #output high on 3
	time.sleep(0.3)

