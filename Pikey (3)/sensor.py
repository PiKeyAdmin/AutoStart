from reedsensor import pass_input
from datetime import date
import datetime
import alsaaudio
import time


def getVolume():
    m = alsaaudio.Mixer('PCM')
    volume = m.getvolume()
    return (volume[0])

def getReed_State():
    state = pass_input()
    #print(state)
    return(state)

def getDate():
    Date = str(date.today())
    #print (Date)
    return (Date)

def getTime():
    Time = datetime.datetime.now().time()
    #print(Time)
    return (Time)

def main():
    while True:
        getDate()
        getTime()
        getReed_State()
        getVolume()
        time.sleep(1)

if __name__ == '__main__':
    while True:
        try:
            main()
        
        except KeyboardInterrupt:
            print ("Stop...")


