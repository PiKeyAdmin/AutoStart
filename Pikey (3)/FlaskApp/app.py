from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
import os
import l293d.driver as l293d
import time

motorR = l293d.DC(18,16,12)
motorL = l293d.DC(13,11,7)

def startMotor():
    count = 0
    while count < 8:
        
        motorR.clockwise()
        motorL.clockwise()
        time.sleep(0.1)
        motorR.stop()
        motorL.stop()
        time.sleep(0.5)
        count = count +1
   

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('knop.html')

#Home
@app.route("/home")
def home():
    startMotor()
    return ('Moteren draaien')
    

if __name__ == '__main__':
    app.run(host="127.0.0.1",port=8000, debug=True)


