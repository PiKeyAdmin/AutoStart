#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import sys
import subprocess

GPIO.setwarnings(False)

# Set Broadcom mode so we can addres GPIO pins by numer.
GPIO.setmode(GPIO.BOARD)

# GPIO pin number which is connected to  one of the Reed Sensor inputs.
# The other wire of the Reed Sensor goes to GOUND.
GPIO.setup(40, GPIO.IN)


# De waarde van het command vcgencmd display_power verandert op basis van
# de connectie van de Reed Sensor

def turn_on():
    subprocess.call(["/usr/bin/vcgencmd", "display_power", "1"])
    time.sleep(1)


def turn_off():
    subprocess.call(["/usr/bin/vcgencmd", "display_power", "0"])
    time.sleep(1)


while True:
    reedsensor_state = GPIO.input(40)
    if reedsensor_state == 1:

        print ("Screen on", reedsensor_state)
        turn_on()
    else:
        print("Screen off", reedsensor_state)
        turn_off()

    time.sleep(1)


