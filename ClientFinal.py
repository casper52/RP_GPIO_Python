# -*- coding: utf-8 -*-
from websocket import create_connection
import RPi.GPIO as GPIO
from gpiozero import Button
from time import sleep, time
from signal import pause


# 라즈베리파이 serial number 가져오기
def getserial():
    cpuserial = "00000000000"
    try:
        f = open('/proc/cpuinfo', 'r')
        for line in f:
            if line[0:6] == 'Serial':
                cpuserial = line[10:26]
        f.close()
    except:
        cpuserial = "ERROR000000"
    return cpuserial



# serial number를 메시지로 보내기
def sendSerialNum():
    userID = getserial()
    ws.send("{\"fromDevice\":\"" + userID + "\"}")
    print(userID)
    sleep(5)


# 실행
# connect
ws = create_connection("ws://10.10.10.95:8080/name")
print("connecting....")

button = Button(21)

while True:
    print(Button)
    button.wait_for_press()
    button.when_pressed = sendSerialNum()


