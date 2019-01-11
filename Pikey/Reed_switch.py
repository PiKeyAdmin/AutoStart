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
GPIO.setup (40, GPIO.IN)

# De waarde van het command vcgencmd display_power verandert op basis van
# de connectie van de Reed Sensor

def turn_on():
    subprocess.call(["/usr/bin/vcgencmd", "display_power", "1"])   
    
def turn_off():
    subprocess.call(["/usr/bin/vcgencmd", "display_power", "0"]) 
def pass_input():
    reedsensor_state= GPIO.input(40)
    if reedsensor_state==1:
        staat =1
        start_time = time.time()
    else:
        staat =0
        end_time = time.time
    passed_time = start_time - end_time
    return (passed_time)
    return (reedsensor_state)
    return (staat)
        
   
def main():
    while True:
        reedsensor_state= GPIO.input(40)
        if reedsensor_state ==1:
            turn_on()
        else:
            turn_off()
        time.sleep(1)
    
if __name__ == '__main__':
    main()
                                                                                            
    

