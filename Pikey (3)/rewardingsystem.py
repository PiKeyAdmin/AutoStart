import l293d.driver as l293d
import time
import test5

# De score wordt uit de game file opgehaald. Deze wordt dan de rewardsystem gezet, wat resulteerd in een expressie!

# bhscore =....
motorR = l293d.DC(18,16,12)
motorL = l293d.DC(13,11,7)

score1 = test5.getal


class Motor :
    def method_Motor (self):
        duur = (score1/100)*3.6
        
        motorR.clockwise()
        motorL.clockwise()
        time.sleep(duur)
        motorR.anticlockwise()
        motorL.anticlockwise()
        time.sleep(duur)

        motorR.stop()
        motorL.stop()
        
        l293d.cleanup()
    
def rewardsystem(score):
        if score >= 90:
            print ("Goed gedaan! Ga door naar het volgende niveau")
            class_ref = Motor()  
            class_ref.method_Motor()
            return "A"
            
        elif score >= 80:
            print("Goed gedaan! Ga jij voor de honderd procent?")
            class_ref = Motor()  
            class_ref.method_Motor()
            return "B"
            
            
        elif score >= 70:
            print("Oefening baart kunst, binnenkort speel je beter dan Bach!")
            class_ref = Motor()  
            class_ref.method_Motor()
            return "C"
            
            
        elif score >= 65:
           print("Goed begin, blijf zo door gaan!")
           class_ref = Motor()
           class_ref.method_Motor()
           return "D"
            
            
        else:
           print("Oeh, nog even oefenen")
           return "F"
    
print(rewardsystem(score1))
