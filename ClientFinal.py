# -*- coding: utf-8 -*-
from websocket import create_connection
from gpiozero import Button
from time import sleep, time



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
    return True;


# 실행
# connect
ws = create_connection("ws://10.10.10.87:8080/name")
print("connecting....")

button = Button(21)

beforeSend = False
count = 0

def pressCheck():
    print("press check")
    global beforeSend, count

    while True:
        print("-----------------------" + str(count))

        button.wait_for_active(1)   #1초 간격으로 버튼 대기 활성화

        # 버튼 대기 상태임과 동시에 count가 0이상일 때 메시지를 보내고 count값을 -2로 변경
        if button.is_active and count >= 0:
            sendSerialNum()
            count = -2

        # count가 0보다 작을 때 값을 1씩 증가, count값을 0이상으로 변경 시킨다
        else:
            count = count + 1
            sleep(1)
            continue


        print(str(count)  + " :::: " + str(button))


pressCheck()
