import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT) #make pin 3 output
onTime = 1.4
offTime = 0.8


def blink():
	GPIO.output(4, 1) #output high on 3
	time.sleep(onTime)
	GPIO.output(4, 0) #output high on 3
	time.sleep(offTime)
	GPIO.output(4, 1) #output high on 3
	time.sleep(onTime)
	GPIO.output(4, 0) #output high on 3
	time.sleep(offTime)
#       GPIO.output(4, 1) #output high on 3
#	time.sleep(onTime)
#	GPIO.output(4, 0) #output high on 3
#	time.sleep(offTime)
