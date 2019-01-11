#!/usr/bin/env python3
from mysql.connector import MySQLConnection, Error
from datetime import date
from sensor import *
import psutil
import datetime
import os
import time
import mysql.connector

#--------------------------------------------------------------------------------------------------
def getDate():
    Date = str(date.today())
    return (Date)

def getTime():
    Time = datetime.datetime.now().time()
    return (Time)

def getCPUtemperature():
    t_cpu = os.popen('vcgencmd measure_temp').readline()
    t_cpu = str(t_cpu.replace("temp=","").replace("'C\n",""))
    return(t_cpu)

def getCPUusage():
    cpu_usage = str(psutil.cpu_percent(interval=1))
    return(cpu_usage)

def connect_to_db():
    try:
        connection = mysql.connector.connect(host='oege.ie.hva.nl',
                                             user='oosterr4',
                                             password='wAK1P#ygvQMnX$',
                                             db='zoosterr4')
        cursor = connection.cursor()
    except:
        print ("Geen verbinding met de database")
    

def insert_to_db_SENSOR():
    try:
        connection = mysql.connector.connect(host='oege.ie.hva.nl',
                                             user='oosterr4',
                                             password='wAK1P#ygvQMnX$',
                                             db='zoosterr4')
        cursor = connection.cursor()
    except:
        print ("Geen verbinding met de database")
    
    today = getDate()
    time = getTime()
    Volume = getVolume()
    Scherm = getReed_State()
    insert_query = "INSERT INTO TAB_SENSOR (Volume, Scherm, Time, Date) VALUES (%s, %s, %s, %s)"
    
    try:
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
    
    
    today = getDate()
    time = getTime()
    temperature = getCPUtemperature()
    usage = getCPUusage()
    insert_query = "INSERT INTO TAB_CPU (Temperature,Cpu_Load,Date,Time) VALUES (%s, %s, %s, %s)"
        
    try:
        cursor.execute(insert_query, (str(temperature), str(usage), str(today), str(time)))
                
        connection.commit()
        
    except Error as error:
        print(error)
        
    finally:
        cursor.close()
        connection.close()

def main():
    while True:
        insert_to_db_TABCPU()
        insert_to_db_SENSOR()
        time.sleep(1)

                        
if __name__ == '__main__':
    try:
        main()
        
    except KeyboardInterrupt:
        connection = mysql.connector.connect(host='oege.ie.hva.nl',
                                         user='oosterr4',
                                         password='wAK1P#ygvQMnX$',
                                         db='zoosterr4')
        connection.close()
        print ("Disconnecting...")
