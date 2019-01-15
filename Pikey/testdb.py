#!/usr/bin/env python3
from sensor import *
import psutil
import datetime
import os
import time
import mysql.connector

#--------------------------------------------------------------------------------------------------
# Functie voor variable Datum
def getDate():
    Date = str(date.today())
    return (Date)

#Fucntie voor variable Time
def getTime():
    Time = datetime.datetime.now().time()
    return (Time)

#Functie voor het maken variable CPU Temperature
def getCPUtemperature():
    t_cpu = os.popen('vcgencmd measure_temp').readline()
    #print(t_cpu) #Data met "temp" en Ç erbij
    t_cpu = str(t_cpu.replace("temp=","").replace("'C\n",""))
    #print(t_cpu) #Data met aleen de temperatuur waarde
    return(t_cpu)

#Functie voor variable CPU Usage
def getCPUusage():
    cpu_usage = str(psutil.cpu_percent(interval=1))
    return(cpu_usage)

def insert_to_db_SENSOR():
    try:
        connection = mysql.connector.connect(host='oege.ie.hva.nl',
                                             user='oosterr4',
                                             password='wAK1P#ygvQMnX$',
                                             db='zoosterr4')
        cursor = connection.cursor()
    except:
        print ("Geen verbinding met de database")
        
    # Variablen aanmaken en gelijkmaken aan de waardes die de uit sensor.py komen (zie import sensor *)
    today = getDate1()
    time = getTime1()
    Volume = getVolume()
    Scherm = getReed_State()
    
    #MySQL query zonder ID (Deze is AI en PK)
    insert_query = "INSERT INTO TAB_SENSOR (Volume, Scherm, Time, Date) VALUES (%s, %s, %s, %s)"
    
    try:
        #Query uitvoeren samen met de relevante data
        cursor.execute(insert_query, (str(Volume), str(Scherm), str(time), str(today)))
        connection.commit()
    except Error as error:
        print(error)
    finally:
        cursor.close()
        connection.close()
    
    
    

def insert_to_db_TABCPU():
    try:
        connection = mysql.connector.connect(host='oege.ie.hva.nl',
                                             user='oosterr4',
                                             password='wAK1P#ygvQMnX$',
                                             db='zoosterr4')
        cursor = connection.cursor()
    except:
        print ("Geen verbinding met de database")
    
    #Variabelen aanmaken en gelijkstellen aan de waardes die de funcites hierboven returnen
    today = getDate()
    time = getTime()
    temperature = getCPUtemperature()
    usage = getCPUusage()
    
    insert_query = "INSERT INTO TAB_CPU (Temperature,Cpu_Load,Date,Time) VALUES (%s, %s, %s, %s)"
        
    try:
        #insert query uitvoeren samen met de relevante waardes ingevuld in de query.
        cursor.execute(insert_query, (str(temperature), str(usage), str(today), str(time)))
                
        connection.commit()
        
    except Error as error:
        print(error)
        
    finally:
        cursor.close()
        connection.close()

def main():
    while True:
        #De methodes uivoeren met een interval van 1 seconde. Oftewel om de 1 seconde de database invullen.
        insert_to_db_TABCPU()
        insert_to_db_SENSOR()
 

                        
if __name__ == '__main__':
    try:
        #Op dit moment wordt de code pas uitgevoerd.
        main()
        
    except KeyboardInterrupt:
        connection = mysql.connector.connect(host='oege.ie.hva.nl',
                                         user='oosterr4',
                                         password='wAK1P#ygvQMnX$',
                                         db='zoosterr4')
        connection.close()
        print ("Disconnecting...")
