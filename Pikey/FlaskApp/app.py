import l293d
from flask import Flask, render_template, request, copy_current_request_context
global xspeed
xspeed = int
app = Flask(__name__)

motorR = l293d.DC(18,16,12)
motorL = l293d.DC(13,11,7)

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/Pikey")
def pikey():
    return render_template('Pikey.html')

@app.route("/Monitoren")
def monitoren():
    return render_template('Monitoring.html')

@app.route("/FastenYourSeatbelts")
def fastenyourseatbelts():
    return render_template('FastenYourSeatbelts.html')

@app.route("/MyRealMusic")
def myrealmusic():
    return render_template('MyRealMusic.html')

@app.route("/Handleiding")
def handleiding():
    return render_template('Handleiding.html')

@app.route("/Motoren")
def motoren():
    return render_template('web-control.html')

@app.route("/set_speed")
def set_speed():
    xspeed = request.args.get("speed")
    xspeed = float(xspeed)
    pwm= l293d.PWM(xspeed,20)
    if xspeed ==1:
        motorL.clockwise(speed=25)
        motorR.clockwise(speed=25)
    elif xspeed ==0:
	motorL.stop()
	motorR.stop()

    return render_template('web-control.html', speed=xspeed)
def main():
    app.run(host='0.0.00',port=8000, debug=True)

if __name__ == '__main__':
    main()



