import RPi.GPIO as GPIO
import Adafruit_DHT
from time import sleep
import datetime

from firebase import firebase
import urllib, http
import json
import os

#Configuration of GPIO
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setwarnings(False)

#Selecting sensor from Adafruit libreary
sensor = Adafruit_DHT.DHT11

#Pin 17 on raspberry pi A+
pin = 17

#URL of the firebase realtime database
url = 'https://rasp-weather.firebaseio.com/'
#Creating firebase applicaiton
firebase = firebase.FirebaseApplication(url, None)

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    date_time = datetime.datetime.now()
    data = {'Temperature': temperature, 'Humidity' : humidity, 'Date - Time' : date_time}
    if temperature != None and humidity != None:
        print('Temperature: {}'.format(temperature))
        print('Humidity: {}\n'.format(humidity))
        firebase.post('/dht11', data)
    else:
        print('Reading error!')
    sleep(5)
