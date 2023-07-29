from SenseTime.sdk.ClassificationDetector import *
from SenseTime.utils.GeneralClassifier import *
from SenseTime.utils.ImageShow import *
from SenseTime.utils.Sensor import *

while True:
    frame=take_photo()
    imshow_platform(frame)
    if is_pressed(7):
        frame=take_photo()
        imshow_platform(frame)
        model=load_model("SignsAI.clf")
        res=predict(model,frame)
        print(res)