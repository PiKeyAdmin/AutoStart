import sys
import time
import traceback
import alsaaudio

from Phidget22.Devices.VoltageInput import *
from Phidget22.PhidgetException import *
from Phidget22.Phidget import *
from PhidgetHelperFunctions import *

x = float('inf')
##############################################################################
# Dit zijn de gegevens van de slidersensor die wij gebruiken
serialNumber = 438074
channel = 0


def onAttachHandler(self):
    
    ph = self
    ph.setDataInterval(1)
    ph.setVoltageChangeTrigger(0.4)
    ph.setSensorType(VoltageSensorType.PN_1112)


def onVoltageChangeHandler(self, voltage):
    MIN_VOLUME = 10
    MAX_VOLUME = 90
    #Doordat wij de slider verkeerd om in de doos hebben gezet (Thanks to Ruben) moesten wij
    #een formule bedenken die ervoor zorgt dat de volume nog steeds tussen 1 en 100 zit. 
    voltage1 = int(voltage * 20)
    volume = (100- voltage1)
    #link uitgerekende volume aan de volume van de PI
    m=alsaaudio.Mixer('PCM')
    m.setvolume(volume)
    print (m.getvolume())
    

def main():
    
    #Lees de waarde van de slider en voer die in de onVoltageChangeHandler.
    #Daar wordt de waarde omgezet in volume staat middels formule
    ch = VoltageInput()
    ch.setOnVoltageChangeHandler(onVoltageChangeHandler)

    
    try:
        #Wacht 5 seconden tot er een apparaat is aangesloten. 
        ch.openWaitForAttachment(5000)
    except PhidgetException as e:
        PrintOpenErrorMessage(e, ch)
        raise EndProgramSignal("Program Terminated: Open Failed")
        
#in line 11 wordt de variabele x oneindig gemaakt. Deze wordt hieronder gebruikt.
#Als we de time.sleep(x) invullen met getal y zetten, stopt het programma na y seconden.

    time.sleep(x)  

if __name__ == '__main__':
    try:
        main()
        
    except KeyboardInterrupt:
        ch = VoltageInput()
    
        # Schoon de gebeurtenissen in VoltageChangeHandler op
        ch.setOnVoltageChangeHandler(None)
        ch.close()
