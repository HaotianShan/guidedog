from SenseTime.sdk.ClassificationDetector import *
from SenseTime.utils.GeneralClassifier import *
from SenseTime.utils.AudioClassifier import *
from SenseTime.utils.PlantDetector import *
from SenseTime.utils.Motor import *
from SenseTime.utils.ImageShow import *
from SenseTime.utils.Sensor import *
from SenseTime.sdk.FaceAttributeDetector import *
from SenseTime.sdk.FaceDetector import *
from SenseTime.utils.Motor import *
from SenseTime.utils.AudioClassifier import *
import time

speed=50
port1 = 1
port2 = 2
port3 = 4
headport = 6
base = time.time()

def left(speed,t):
    #set_motor(port1,-speed)
    #set_motor(port2,speed)
    run_tank(port1, -speed, port2, speed, seconds=t)
def right(speed,t):
    #set_motor(port1,speed)
    #set_motor(port2,-speed)
    run_tank(port1, speed, port2, -speed, seconds=t)
def forward(speed):
    set_motor(port1,speed+2)
    set_motor(port2,speed)
    #run_tank(port1, speed+3, port2, speed, seconds=3)
def stop_forward():
    stop_motor(port1,port2)
def head(speed):
    set_motor(headport,speed)
def photo():
    frame=take_photo()
    imshow_platform(frame)
    imshow_sensestorm(frame)
def RunAI(modelname):
    frame=take_photo()
    imshow_platform(frame)
    if modelname=="AIdecision":
        model=load_model("AIdecision.clf")
    elif modelname=="TrafficLight":
        model=load_model("TrafficLightAI.clf")
    elif modelname=="Signs":
        model=load_model("SignsAI.clf")
    res=predict(model,frame);
    return res

#identify object and perform actions
def makemove():
    print("In Function makemove()")
    time.sleep(1)
    #notice: object <1000mm
    stop_forward()
    dicision=RunAI("AIdecision")
    print("runned ai: AIdecision")
    if dicision=="TrafficLights":
        print("decision: TrafficLightsAI")
        res=RunAI("TrafficLight")
        print("result: ",res)
        #stop_forward()
        if res=="GreenLight":
            forward(50)
        elif res=="YellowLight" or res=="RedLight":
            stop_forward()
    elif dicision=="Signs":
        print("decision: SignsAI")
        res=RunAI("Signs")
        print("result: ",res)
        #stop_forward()
        if res=="TurnLeft":
            left(50,1)
            forward(50)
        elif res=="TurnRight":
            right(50,1)
            forward(50)
        elif res=="StopSign":
            stop_forward()
            #time.sleep(5)
        elif res=="Straight":
            forward(50)

cnt=0
head(50)
ispositive=True
forward(50)

while True:
    #camera move
    cnt=cnt+1
    print(cnt,"\n")
    if cnt>=3:
        cnt=0
        if ispositive:
            ispositive=False
            head(-4.5)
            photo()
            dis = get_ultrasonic(6)
            print(dis)
        else:
            head(4.5)
            ispositive=True
            photo()
            dis = get_ultrasonic(6)
            print(dis)
      if dis is None or dis ==0:
        forward(50)
    elif dis >200:
        forward(50)
    else:
        makemove()