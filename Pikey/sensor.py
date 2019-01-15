#Het doel van dit bestand is om de waardes aan te maken die in de TAB_SENSOR table komen. Deze file wordt geimoprteerd in de database file en gebruikt de waardes die deze file aanmaakt.

from reedsensor import pass_input
from datetime import date
import datetime
import alsaaudio
import time


def getVolume():
    m = alsaaudio.Mixer('PCM')
    #volume variable met brackets: "[waarde]"
    volume = m.getvolume()
    #print(volume)
    volumeint = volume[0]
    #volume variable zonder brackets: "waarde"
    #print(volumeint)
    return (volume[0])

def getReed_State():
    #Reed state uit de reedsensor.py file uithalen en kopplen aan state
    state = pass_input()
    #print(state)
    return(state)

def getDate1():
    Date = str(date.today())
    #print (Date)
    return (Date)

def getTime1():
    Time = datetime.datetime.now().time()
    #print(Time)
    return (Time)

def main():
    while True:
        getDate1()
        getTime1()
        getReed_State()
        getVolume()
        time.sleep(1)

if __name__ == '__main__':
    while True:
        try:
            main()
        
        except KeyboardInterrupt:
            print ("Stop...")


