import RPi.GPIO as GPIO
import Adafruit_DHT
from time import sleep
import datetime

#Configuration of GPIO
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setwarnings(False)

#Selecting sensor from Adafruit libreary
sensor = Adafruit_DHT.DHT11

#Pin 17 on raspberry pi A+
pin = 17

while True:
    humidity, temperature = Adafruit_DHT.read(sensor, pin)
    print('Temperature: {}\n'.format(temperature))
    print('Temperature: {}\n'.format(humidity))
