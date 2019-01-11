#!/usr/bin/env python3
from mysql.connector import MySQLConnection, Error
import psutil
import os
import time
import datetime
import mysql.connector

#--------------------------------------------------------------------------------------------------
def getCPUtemperature():
    t_cpu = os.popen('vcgencmd measure_temp').readline()
    t_cpu = str(t_cpu.replace("temp=","").replace("'C\n",""))
    return(t_cpu)

def getCPUusage():
    cpu_usage = str(psutil.cpu_percent(interval=1))
    return(cpu_usage)
   

def insert_to_db():
    
    try:
        connection = mysql.connector.connect(host='oege.ie.hva.nl',
                                         user='oosterr4',
                                         password='wAK1P#ygvQMnX$',
                                         db='zoosterr4')
        cursor = connection.cursor()
    except:
        print ("Geen verbinding met de database")
        
    temperature = (getCPUtemperature())
    usage = (getCPUusage())
    
    insert_query = "INSERT INTO TAB_CPU (Temperature,Cpu_Load,Date,Time) VALUES (%s, %s, %s, %s)"
        
    try:
        cursor.execute(insert_query, (str(temperature), str(usage), str(datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d")), str(datetime.datetime.fromtimestamp(time.time()).strftime("%H:%M:%S"))))
        
        if cursor.lastrowid:
            print ('laatste id: ', cursor.lastrowid)
        else:
            print ('laatste id niet gevonden')
            
        connection.commit()
        
    except Error as error:
        print(error)
        
    finally:
        cursor.close()
        connection.close()

def read_from_db():
    try:
        connection = mysql.connector.connect(host='oege.ie.hva.nl',
                                         user='oosterr4',
                                         password='wAK1P#ygvQMnX$',
                                         db='zoosterr4')
        cursor = connection.cursor()
    except:
        print ("Geen verbinding met de database")
        
    sql = "SELECT * FROM TAB_CPU ORDER BY ID DESC LIMIT 1"
    cursor.execute(sql)
    result = cursor.fetchall()
    if result is not None:
        print ('CPU temperature: ' , result[0][1], '°C | usage: ' , result[0][2], '% | time: ' , result[0][4], ' | datum: ' , result[0][3])
    
#-----------------------------------------------------------------------------------------------------------------------------------

def main():
    while True:
        read_from_db()   
        insert_to_db()
        time.sleep(1)

                        
if __name__ == '__main__':
    try:
        main()
        
    except KeyboardInterrupt:
        connection.close()
        print ("Disconnecting...")