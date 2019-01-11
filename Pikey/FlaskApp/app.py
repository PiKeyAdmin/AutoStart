from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
import os


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('knop.html')

#Home
@app.route("/home")
def home():
    os.popen("sudo python3 /pi/home/Desktop/Pikey/motor.py")
    return 'Hallo'

if __name__ == '__main__':
    app.run(host="127.0.0.1",port=8000, debug=True)

