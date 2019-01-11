#!/usr/bin/python
import RPi.GPIO as GPIO
import time
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
    return (reedsensor_state)
        
   
def main():
    while True:
        reedsensor_state= pass_input()
        if reedsensor_state ==1:
            turn_on()
        else:
            turn_off()
        time.sleep(1)
    
if __name__ == '__main__':
    main()
                                                                                            
    


