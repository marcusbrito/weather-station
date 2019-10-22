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
    if temperature != None and humidity != None:
        print('Temperature: {}'.format(temperature))
        print('Humidity: {}\n'.format(humidity))
    else:
        print('Reading error!')
    sleep(2)
