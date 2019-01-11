import l293d.driver as l293d
import time


motorR = l293d.DC(18,16,12)
motorL = l293d.DC(13,11,7)

def xD():
    count = 0
    while count < 4:
        
        motorR.clockwise()
        motorL.clockwise()
        time.sleep(0.1)
        motorR.stop()
        motorL.stop()
        time.sleep(0.5)
        count = count +1

    
    


xD()

    



