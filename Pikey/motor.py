import l293d.driver as l293d
import time



motorR = l293d.DC(18,16,12)
motorL = l293d.DC(13,11,7)


def startMotor():
    while True:
	 motorR.clockwise(speed=30)
	 motorL.clockwise(speed=30)

def main():
    startMotor()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        motorR.clockwise(speed=0)
        motorL.clockwise(speed=0)
