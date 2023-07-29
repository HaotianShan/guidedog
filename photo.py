from SenseTime.utils.ImageShow import *
from SenseTime.utils.Sensor import *
from SenseTime.sdk.FaceDetector import *
import time
cnt=0

while True:
    frame=take_photo()
    imshow_platform(frame)
    name="Straight"
    if is_pressed(7):
        cnt+=1
        t=time.time()
        img_name="/device/public/SignPic/Straight/{}.jpg".format(t)
        imwrite(frame,img_name)
        print("cnt=",cnt,)