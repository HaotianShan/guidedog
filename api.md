# SenseStorm Python接口目录
  -- 摄像头及渲染
  -- 人工智能相关接口
    --人脸检测
    --手势及人体检测
    -- 通用图像分类器
    -- 通用语音分类器
    -- 车道线检测接口
    -- 物体检测接口
  -- 电机
    -- 运动速度时间控制
    -- 运动时间角度控制
    -- 编码器读取和重置
  -- 传感器
    --光电传感器
    --触碰传感器
    --颜色传感器
    --彩灯
    --超声传感器
    --温湿度传感器
    
    
# SenseStorm Python接口说明
## 一、摄像头及渲染
### 功能
实时捕获图像信息，可用于后续的图像智能识别、智能分类。
### 函数接口
#### take_photo()
说明：获取一张摄像头的实时拍摄图像。
导入库: from SenseTime.utils.ImageShow import *
输入参数：无
返回值：
- image
  - 含义：实时拍摄的图像
  - 类型：numpy数组，大小为480\*640\*3
错误类型：当未能成功读取时返回None


####  imread(image_path)
说明：默认读取/device/image/下的图片。
导入库: from SenseTime.utils.ImageShow import *
输入参数：
- image_path 
  - 含义：待读取的图像名称
  - 类型：string
  - 默认：无
返回值：
- frame
  - 含义：读取的图片数据
  - 类型：numpy数组，大小为480\*640\*3
#### ---------------使用样例如下-----------------
* 若/device/image路径下存在图片sample.jpg,使用下面方式读取 *
frame = imread("sample.jpg")
print(frame)


#### 3. imwrite(frame,img_path)
说明：将图片数据存在/device/image/路径下。
导入库: from SenseTime.utils.ImageShow import *
输入参数：
- frame 
  - 含义：待保存的图像
  - 类型：numpy数组
  - 默认：无
- image_path 
  - 含义：待保存的图片名称
  - 类型：string
  - 默认："output.jpg"
返回值：无
错误类型：无
#### ---------------使用样例如下-----------------
* 将摄像头实时采集的图片frame保存在/device/image路径下，保存图片的文件名为sample.jpg *
frame = take_photo()
imwrite(frame,"sample.jpg")


#### imshow_platform(frame,window_index=0)
说明：将图像可视化在innolab平台
导入库: from SenseTime.utils.ImageShow import *
输入参数：
- frame 
  - 含义：待展示的图像
  - 类型：numpy数组，大小为480\*640\*3
- window_index
  - 使用场景：当需要同时显示多张图片（而不是一个窗口的视频流）时，才需要指定该参数（可选）
  - 含义：在innolab上待展示的窗口序号
  - 类型：整型
  - 默认：0
返回值：无
错误类型：无
#### ---------------使用样例如下-----------------
场景一：需要在innolab显示视频流
while True:
  frame = take_photo()
  imshow_platform(frame)
场景二：需要在innolab显示两张不同图片，且希望同时存在
f1 = imread(img1_path)
f2 = imread(img2_path)
imshow_platform(f1,window_index=1)
imshow_platform(f2,window_index=2)


#### 5. imshow_sensestorm(frame)
说明：将图像可视化在SenseStorm上
导入库: from SenseTime.utils.ImageShow import *
输入参数：
- frame 
  - 含义：待展示的图像
  - 类型：numpy数组，大小为480\*640\*3
返回值：无
错误类型：无
#### ---------------使用样例如下-----------------
需要在sensestorm显示视频流
while True:
  frame = take_photo()
  imshow_sensestorm(frame)


#### 6. render_rects(frame,rects)
说明：给选定的frame画出rect对应的框
导入库: from SenseTime.utils.ImageShow import *
输入参数：
- frame 
  - 含义：待展示的图像
  - 类型：numpy数组，大小为480\*640\*3
  - 默认：无
- rect
  - 含义：需要画框的位置
  - 类型：一维或者多维列表表征[[left,top,right,bottom],[left,top,right,bottom]]
  - 默认：无
返回值：渲染后的图片
错误类型：无
#### ---------------使用样例如下-----------------
在摄像头实时采集的图像frame上绘制矩形框[10,10,100,100]
frame = take_photo()
render_rects(frame,[10,10,100,100])


#### 7. crop_rect(frame,rect)
说明：提取选定的frame的rect区域的图片（得到裁剪图片）
导入库: from SenseTime.utils.ImageShow import *
输入参数：
- frame 
  - 含义：待处理的图像
  - 类型：numpy数组
  - 默认：无
- rect
  - 含义：需要提取的图片位置(left,top,right,bottom)
  - 类型：元组或者列表
  - 默认：无
返回值：提取后的图片
错误类型：无
#### ---------------使用样例如下-----------------
frame = take_photo()
roi = crop_rect(frame,[10,10,100,100])


#### 8. render_points(image,points)
说明：给选定的frame画出对应的points
导入库: from SenseTime.utils.ImageShow import *
输入参数：
- image 
  - 含义：待展示的图像
  - 类型：numpy数组，大小为480\*640\*3
  - 默认：无
- points
  - 含义：需要画点的位置
  - 类型：一维或者多维列表
  - 默认：无
返回值：渲染后的图片
错误类型：无
#### ---------------使用样例如下-----------------
frame = take_photo()
render_frame = render_points(frame,[[10,10],[100,100]])


#### 9. render_circle(frame,circle)
说明：给选定的frame画出对应的圆
导入库: from SenseTime.utils.ImageShow import *
输入参数：
- frame 
  - 含义：待展示的图像
  - 类型：numpy数组，大小为480\*640\*3
  - 默认：无
- circle
  - 含义：需要画圆的位置
  - 类型：列表，圆通过圆心位置和半径来描述，可用[center_x,center_y,radis]和[[center_x,center_y],radis]两种形式
  - 默认：无
返回值：渲染后的图片
错误类型：无
#### ---------------使用样例如下-----------------
frame = take_photo()
render_frame = render_circle(frame,[[100,100],20])


#### 10. render_skeleton(image,points)
说明：给选定的frame画出对应的人体关键点线条（仅适用于人体关键点检测后的渲染）
导入库: from SenseTime.utils.ImageShow import *
输入参数：
- image 
  - 含义：待展示的图像
  - 类型：numpy数组，大小为480\*640\*3
  - 默认：无
- points
  - 含义：人体的关键点位置
  - 类型：一维或者多维列表
  - 默认：无
返回值：渲染后的图片
错误类型：无
#### ---------------使用样例如下-----------------
frame = take_photo()
body_points = detect_body_points(frame)
if body_points is not None:
  render_frame = render_skeleton(frame,body_points)


#### 11. render_text(image,text,font_size=40,location=None)
说明：给图片上写上文字
导入库: from SenseTime.utils.ImageShow import *
输入参数：
- image 
  - 含义：输入图像数据
  - 类型：numpy数组，大小为480\*640\*3
  - 默认：无
- text
  - 含义：待渲染的文字内容
  - 类型：string
  - 默认：无
- font_size
  - 含义：待渲染的文字大小
  - 类型：整型
  - 默认：40
- location
  - 含义：待渲染的文字位置
  - 类型：tuple或者list
  - 默认：(width/2,50)
返回值：渲染文字后的图片
错误类型：无
#### ---------------使用样例如下-----------------
frame = take_photo()
render_frame = render_text(frame,"Hello")


####  get_image_width(frame)
说明：获取的图片的宽度
导入库: from SenseTime.utils.ImageShow import *
输入参数：
- frame 
  - 含义：输入图像数据
  - 类型：numpy数组，大小为480\*640\*3
  - 默认：无
返回值：
- width 
  - 含义：图片的宽度
  - 类型：int
错误类型：无
#### ---------------使用样例如下-----------------
frame = take_photo()
width = get_image_width(frame)
print(width)


#### 13. get_image_height(frame)
说明：获取的图片的高度
导入库: from SenseTime.utils.ImageShow import *
输入参数：
- frame 
  - 含义：输入图像数据
  - 类型：numpy数组，大小为480\*640\*3
  - 默认：无
返回值：
- width 
  - 含义：图片的高度
  - 类型：int
错误类型：无
#### ---------------使用样例如下-----------------
frame = take_photo()
height = get_image_height(frame)
print(height)



## 二、人脸检测相关程序接口
### 功能
人脸识别相关的功能。
### 函数接口
#### detect_face(frame)
说明：返回图片中的一张或者多张人脸框位置
     道具包中的人脸卡片，具体图片“男35岁.png、女5岁.png、女20岁.png、女60岁.png、sad.png、happy.png、sad.png、scard.png”
导入库: from SenseTime.sdk.FaceDetector import *
输入参数：
- frame 
  - 含义：图像数据
  - 类型：numpy数组，大小为480\*640\*3
  - 默认：无
- 返回值：检测到人脸矩形框坐标。  [[left1,top1,right1,bottom1],....[]]

错误类型：无

#### ---------------使用样例如下-----------------
frame = take_photo()
face_rects = detect_face(frame)
print(face_rects)


####  is_face_existed(frame)
说明：判断图片中是否包含人脸
     道具包中的人脸卡片，具体图片“男35岁.png、女5岁.png、女20岁.png、女60岁.png、sad.png、happy.png、sad.png、scard.png”
导入库: from SenseTime.sdk.FaceDetector import *
输入参数：
- frame 
  - 含义：图像数据
  - 类型：numpy数组，大小为480\*640\*3
  - 默认：无
返回值：
- flag 
  - 含义：是否存在人脸的标识，存在人脸时为True，不存在时为False
  - 类型：bool
#### ---------------使用样例如下-----------------
frame = take_photo()
flag = is_face_existed(frame)
print(flag)


#### get_face_attributes(frame)
说明：返回人脸属性信息
     道具包中的人脸卡片，具体图片“男35岁.png、女5岁.png、女20岁.png、女60岁.png、sad.png、happy.png、sad.png、scard.png”
导入库: from SenseTime.sdk.FaceAttributeDetector import *
输入参数：
- frame 
  - 含义：图像数据
  - 类型：numpy数组，大小为480\*640\*3
  - 默认：无
返回值：
- attributes 
  - 含义：人脸属性信息
  - 类型：二维list，里面包的是dict
        dict数据，表征人脸:
        性别：分为男女
        年龄：0-99岁
        颜值：0-99分
        表情：7种基本表情——生气，平静，厌恶，高兴，悲伤，害怕，吃惊
        眼镜：分为无眼镜，有眼镜以及墨镜
        口罩：有无
        种族：分为黑白黄三种
        张嘴：有无
        闭眼：有无
        胡子：有无
错误类型：当不存在人脸时返回[]
#### ---------------使用样例如下-----------------
frame1 = take_photo()
attributes = get_face_attributes(frame1)
print(attributes)


#### get_face_attribute(frame,select_info="age")
说明：返回指定属性的人脸信息
     道具包中的人脸卡片，具体图片“男35岁.png、女5岁.png、女20岁.png、女60岁.png、sad.png、happy.png、sad.png、scard.png”
导入库: from SenseTime.sdk.FaceAttributeDetector import *
输入参数：
- frame 
  - 含义：图像数据
  - 类型：numpy数组，大小为480\*640\*3
  - 默认：无
- select_info 
  - 含义：选定的属性
  - 类型：string
  - 取值：["age","gender","attractive","emotion","eye"]
  - 默认："age"
返回值：
- attribute
  - 含义：对应属性的人脸信息
  - 类型："age"-->float
        "gender"-->string
        "attractive"-->float
        "emotion"-->string
        "eye"-->string
  - 取值：当存在多个人脸时默认返回第1个人脸的对应的属性
错误类型：无
#### ---------------使用样例如下-----------------
frame1 = take_photo()
attribute = get_face_attribute(frame1，"age",gender","attractive", "emotion","eye)
print(attribute)


#### 5. is_face_smiled(frame)
说明：判断图片中人脸是否在笑
     道具包中的人脸卡片，具体图片“男35岁.png、女5岁.png、女20岁.png、女60岁.png、sad.png、happy.png、sad.png、scard.png”
导入库: from SenseTime.sdk.FaceAttributeDetector import *
输入参数：
- frame 
  - 含义：图像数据
  - 类型：numpy数组，大小为480\*640\*3
  - 默认：无
返回值：
- flag 
  - 含义：识别人脸是否在笑的标识，笑容为True，否则为False。当不存在人脸时，默认返回False
  - 类型：bool
#### ---------------使用样例如下-----------------
frame = take_photo()
flag = is_face_smiled(frame)
print(flag)


#### 6. get_face_pose(frame)
说明：返回图片中的人脸角度
导入库: from SenseTime.sdk.FaceAttributeDetector import *
输入参数：
- frame 
  - 含义：图像数据
  - 类型：numpy数组，大小为480\*640\*3
  - 默认：无
返回值：
（roll,pitch,yaw）
检测到人脸三个纬度的角度
错误类型：无
#### ---------------使用样例如下-----------------
frame = take_photo()
roll,pitch,yaw = get_face_pose(frame)
print(roll,pitch,yaw)


#### 7. extract_face_feature(frame)
说明：返回图片中的人脸特征
导入库: from SenseTime.sdk.FaceFeatureDetector import *
输入参数：
- frame 
  - 含义：图像数据
  - 类型：numpy数组
  - 默认：无
返回值：
  - features
    - 含义： 人脸特征
    - 类型：列表，二维
    - 大小：face_num * 128, [ [face1_feature1,face1_feature2,...,face1_feature128], [face2_feature1,face2_feature2,...,face2_feature128],...  ],即使是单个人脸是同样返回二维的人脸特征[ [face1_feature1,face1_feature2,...,face1_feature12] ]
错误类型：当不存在人脸时返回None
注意：如果一张图片只有一个人脸，在送入compare_feature_similarity是需要取出第零个元素，如features[0]
#### ---------------使用样例如下-----------------
frame = take_photo()
feature = extract_face_feature(frame)
print(feature)


#### 8. compare_feature_similarity(feature1,feature2)
说明：比对两个人脸特征是否是同一个人
导入库: from SenseTime.sdk.FaceFeatureDetector import *
输入参数：
- feature1
  - 含义：输入第一个特征数据
  - 类型：list, 1*128
  - 默认：无
- feature2
  - 含义：输入第二个特征数据
  - 类型：list, 1*128
  - 默认：无
返回值：
  两个特征的是否是同一个人标识
#### ---------------使用样例如下-----------------
frame1 = take_photo()
frame2 = take_photo()
feature1 = extract_face_feature(frame1)
feature2 = extract_face_feature(frame2)
flag = compare_feature_similarity(feature1[0],feature2[0])
print(flag)


#### 9. calculate_feature_similarity(feature1,feature2)
说明：返回图片中的人脸特征相似度
导入库: from SenseTime.sdk.FaceFeatureDetector import *
输入参数：
- feature1
  - 含义：输入第一个特征数据
  - 类型：list, 1*128
  - 默认：无
- feature2
  - 含义：输入第二个特征数据
  - 类型：list, 1*128
  - 默认：无
返回值：
  两个特征的相似度
错误类型：无
#### ---------------使用样例如下-----------------
frame1 = take_photo()
frame2 = take_photo()
feature1 = extract_face_feature(frame1)
feature2 = extract_face_feature(frame2)
similarity = calculate_feature_similarity(feature1[0],feature2[0])
print(similarity)


## 三、手势及人体检测相关程序接口
### 功能
包括手的检测、手势检测和人体检测相关功能。
### 函数接口
#### 1. detect_hand(frame))
说明：返回图片中的单个手势框的位置
导入库: from SenseTime.sdk.HandDetector import *
输入参数：
- frame 
  - 含义：图像数据
  - 类型：numpy数组，大小为480\*640\*3
  - 默认：无
返回值：检测到手势矩形框坐标
[left,top,right,bottom]
#### ---------------使用样例如下-----------------
frame = take_photo()
rect = detect_hand(frame)
print(rect)


#### 2. is_hand_existed(frame)
说明：判断图片中是否包含手势
导入库: from SenseTime.sdk.HandDetector import *
输入参数：
- frame 
  - 含义：图像数据
  - 类型：numpy数组，大小为480\*640\*3
  - 默认：无
返回值：
- flag 
  - 含义：是否存在手势的标识，存在时为True，不存在时为False
  - 类型：bool
#### ---------------使用样例如下-----------------
frame = take_photo()
flag = is_hand_existed(frame)
print(flag)


#### 3. detect_gesture(frame)
说明：返回图片中的单个手势种类
     道具包中的手势卡片，具体图片“OK.png、Fist.png、Six.png、Stop.png、ThumbUp.png、Tick.png、V.png”
导入库: from SenseTime.sdk.HandDetector import *
输入参数：
- frame 
  - 含义：图像数据
  - 类型：numpy数组，大小为480\*640\*3
  - 默认：无
返回值：检测到手势种类，不存在时返回None
#### ---------------使用样例如下-----------------
frame = take_photo()
gesture = detect_gesture(frame)
print(gesture)


#### 4. detect_hand_points(frame)
说明：返回图片中五个指尖关键点
导入库: from SenseTime.sdk.HandPointsDetector import *
输入参数：
- frame 
  - 含义：图像数据
  - 类型：numpy数组，大小为480\*640\*3
  - 默认：无
返回值：
  二维列表，(5*2)
  人手关键点坐标，大拇指、食指、中指、无名指、小指关键点位置
错误类型：无
#### ---------------使用样例如下-----------------
frame = take_photo()
points = detect_hand_points(frame)
print(points)


#### 5. detect_body(frame)
说明：返回图片中的一张或者多张人体框位置
导入库: from SenseTime.sdk.BodyDetector import *
输入参数：
- frame 
  - 含义：图像数据
  - 类型：numpy数组，大小为480\*640\*3
  - 默认：无
返回值：检测到人体矩形框坐标[[left1,top1,right1,bottom1],....[]]
错误类型：无
#### ---------------使用样例如下-----------------
frame = take_photo()
rect = detect_body(frame)
print(rect)


#### 6. is_body_existed(frame)
说明：判断图片中是否包含人体
导入库: from SenseTime.sdk.BodyDetector import *
输入参数：
- frame 
  - 含义：图像数据
  - 类型：numpy数组，大小为480\*640\*3
  - 默认：无
返回值：
- flag 
  - 含义：是否存在人的标识，存在时为True，不存在时为False
  - 类型：bool
#### ---------------使用样例如下-----------------
frame = take_photo()
flag = is_body_existed(frame)
print(flag)


#### 7. detect_body_points(frame)
说明：返回图片中人体关键点
导入库: from SenseTime.sdk.BodyAligner import *
输入参数：
- frame 
  - 含义：图像数据
  - 类型：numpy数组，大小为480\*640\*3
  - 默认：无
返回值：
  二维列表，(14*2)
  人体关键点坐标,依次为:头，颈，右肩，左肩，右手肘，左手肘，右手腕，左手腕，右腰，左腰，右膝，左膝，右脚，左脚
错误类型：无
#### ---------------使用样例如下-----------------
frame = take_photo()
points = detect_body_points(frame)
print(points)

## 四、机器学习——通用图像分类器相关接口
### 功能
集合SDK提取ImageNet特征，通过配合sklearn库函数实现通用分类器功能
### 函数接口
#### 1. classify_image(frame)
说明：返回图片分类结果
导入库: from SenseTime.sdk.ClassificationDetector import *
输入参数：
- frame 
  - 含义：图像数据
  - 类型：numpy数组，大小为480\*640\*3
  - 默认：无
返回值：
  0people，1baby，2food，3animal，4dog，\n
  5cat，6plant，7landscape，8mountain，9sea，\n
  10underwater，11sky，12sunrise&sunset，13snow，\n
  14desert，15nightscape，16fireworks，17building，18show，19transportation
错误类型：无
#### ---------------使用样例如下-----------------
frame = take_photo()
prediction = classify_image(frame)
print(prediction)


#### 2. extract_imageNet(frame)
说明：提取图片特征
导入库:from SenseTime.sdk.ImagetNetFeatureExtractor import *
输入参数：
- frame 
  - 含义：图像数据
  - 类型：numpy数组，大小为480\*640\*3
  - 默认：无
返回值：
  1*1024维的列表，表征图片特征
错误类型：无
#### ---------------使用样例如下-----------------
frame = take_photo()
imagenet_feature = extract_imageNet(frame)
print(imagenet_feature)


#### 3. train_classifier(data_path,classifier="SVM")
说明：基于给定的图片数据完成分类模型训练
导入库：from SenseTime.utils.GeneralClassifier import *
输入参数：
- data_path
  - 含义：图片存储绝对路径
  - 类型：string
  - 默认：无默认值
  - 样例如下：data_path = "/device/PicData/dataset"
  dataset/
        |-- dry
        |   |-- 3.jpg
        |   `-- 7.jpg
        `-- wet
            |-- 73.jpg
            `-- 76.jpg
- classifier
  - 含义：选择要使用的分类器模型
  - 类型：string
  - 默认：SVM,
  - 可选值: "KNN","SVM","GBDT","CNN"
返回值：
- model
  - 含义：训练好的模型
  - 类型：分类器对象
错误类型：无
#### ---------------使用样例如下-----------------
data = "/device/PicData/dataset"
model = train_classifier(data)
print(model)


#### 4. save_model(model,model_name)
说明：将训练好的模型保存下载,默认保存在"/device/model/classifier/"下
导入库：from SenseTime.utils.GeneralClassifier import *
输入参数：
- model
  - 含义：训练好的模型
  - 类型：分类器对象
  - 默认：无默认值
- model_name
  - 含义：要保存的模型名称
  - 类型：string
  - 默认：无默认值
返回值：无
错误类型：无
#### ---------------使用样例如下-----------------
data = "/device/PicData/dataset"
model = train_classifier(data)
save_model(model,"svm.clf") # 默认在"/device/model/classifier/"下生成svm.clf文件


#### load_model(model_name)
说明：加载训练好的模型用于预测，默认加载"/device/model/classifier/"下的对应名称的模型
导入库：from SenseTime.utils.GeneralClassifier import *
输入参数：
- model_name
  - 含义：要加载的模型名称
  - 类型：string
  - 默认：无默认值
返回值：加载过的分类器模型对象
错误类型：无
#### ---------------使用样例如下-----------------
model = load_model("svm.clf")
print(model)


#### predict(model,frame)
说明：用加载好的分类器对图片进行预测
导入库：from SenseTime.utils.GeneralClassifier import *
输入参数：
- model
  - 含义：加载过的分类器模型对象
  - 类型：分类器对象（经由load_model得到）
  - 默认：无默认值
- frame
  - 含义：图像数据
  - 类型：numpy数组，大小为480\*640\*3
  - 默认：无
返回值：预测的图片分类结果,注意返回结果是，训练数据集对应文件夹名称，比如"dry"
错误类型：无
#### ---------------使用样例如下-----------------
1. 训练后直接预测
data = "./dataset"
frame1 = cv2.imread("1.jpg")
model = train_classifier(data)
save_model(model,"svm.clf")
res = predict(model,frame1)
print(res)
2. 加载训练好的模型用于预测
frame1 = cv2.imread("72.jpg")
model = load_model("svm.clf")
res = predict(model,frame1)
print(res)


#### 7. predict_probability(model,frame)
说明：用加载好的分类器对图片进行预测，并输出对应种类的概率
导入库：from SenseTime.utils.GeneralClassifier import *
输入参数：
- model
  - 含义：加载过的分类器模型对象
  - 类型：分类器对象（经由load_model得到）
  - 默认：无默认值
- frame
  - 含义：图像数据
  - 类型：numpy数组，大小为480\*640\*3
  - 默认：无
返回值：预测的图片分类结果,注意返回结果是，训练数据集对应文件夹名称，比如"dry"
错误类型：无
#### ---------------使用样例如下-----------------
1. 训练后直接预测
data = "./dataset"
frame1 = cv2.imread("1.jpg")
model = train_classifier(data)
save_model(model,"svm.clf")
res = predict_probability(model,frame1)
print(res)
2. 加载训练好的模型用于预测
frame1 = cv2.imread("72.jpg")
model = load_model("svm.clf")
res = predict_probability(model,frame1)
print(res)

## 五、机器学习——通用语音分类器相关接口
### 功能
通用语音分类器功能
### 函数接口
#### 1. train_audio_classifier(audio_data_path)
说明：基于给定的语音数据完成分类模型训练，单音频数据录音时长尽量保持在2-5秒
导入库：from SenseTime.utils.AudioClassifier import *
输入参数：
- audio_data_path
  - 含义：音频存储路径，注意需要保证是绝对路径
  - 类型：string
  - 默认：无默认值
  - 样例如下：audio_data_path = "./audio_dataset"
  audio_dataset/
        |-- forward
        |   |-- forward3.wav
        |   `-- forward7.wav
        `-- backward
            |-- backward73.wav
            `-- backward76.wav
返回值：
- model
  - 含义：训练好的语音模型
  - 类型：分类器对象
错误类型：无
#### ---------------使用样例如下-----------------
data_path = "/device/VoiceData/multi_voice_data/"
model = train_audio_classifier(data_path)
print(model)


#### 2. save_audio_model(model,model_name)
说明：将训练好的语音模型保存下来，默认在"/device/model/classifier/"路径下保存对应名称文件
导入库：from SenseTime.utils.AudioClassifier import *
输入参数：
- model
  - 含义：训练好的模型
  - 类型：分类器对象
  - 默认：无默认值
- model_name
  - 含义：要保存的模型名称
  - 类型：string
  - 默认：无默认值
返回值：无
错误类型：无
#### ---------------使用样例如下-----------------
data_path = "/device/VoiceData/multi_voice_data/"
model = train_audio_classifier(data_path)
save_audio_model(model,"audio_model") # 默认在"/device/model/classifier/"路径下生成audio_model文件


#### 3. load_audio_model(model_name)
说明：加载训练好的模型用于预测，默认加载"/device/model/classifier/"路径下的模型文件
导入库：from SenseTime.utils.AudioClassifier import *
输入参数：
- model_name
  - 含义：要加载的模型名称
  - 类型：string
  - 默认：无默认值
返回值：加载过的分类器模型对象
错误类型：无
#### ---------------使用样例如下-----------------
new_model = load_audio_model("audio_model")
print(new_model)


#### 4. predict_audio(model,wav_file_path)
说明：用加载好的分类器对音频进行预测
导入库：from SenseTime.utils.AudioClassifier import *
输入参数：
- model
  - 含义：加载过的分类器模型对象
  - 类型：分类器对象（经由load_audio_model得到）
  - 默认：无默认值
- wav_file_path
  - 含义：默认加载，"/device/VoiceData/"路径下的音频文件
  - 类型：string
  - 默认：无
返回值：预测的语音分类结果
错误类型：无
#### ---------------使用样例如下-----------------

#### 5. SetFanSpeed(speed)
说明：设定风扇的转动速度(为了避免风扇声音对录音的影响，最好事先调小或者关闭风扇)
导入库：from SenseTime.utils.Motor import *
输入参数：
- speed
  - 含义：设定的风扇的转速
  - 类型：整型
  - 默认：无
  - 值：0-100
返回值: 无
错误类型：无
#### ---------------使用样例如下-----------------
SetFanSpeed(0)


#### record_audio(seconds,filename = "output.wav")
说明：调用麦克风进行录音(录音开始时有log提醒),并保存，默认保存路径"/device/VoiceData/"
导入库：from SenseTime.utils.AudioClassifier import *
输入参数：
- seconds
  - 含义：要录音的音频时长，单位秒
  - 类型：整型
  - 默认：无默认值
- file
  - 含义：待保存的音频的路径
  - 类型：string
  - 默认："output.wav"
返回值: 无
错误类型：无
#### ---------------使用样例如下-----------------
record_audio(10,"test.wav") # 在"/device/VoiceData/"下生成test.wav文件


#### 7. play_audio(wav_file)
说明：播放指定音频，暂定格式为wav，默认读取"/device/VoiceData/"路径下对应名称的音频文件
导入库：from SenseTime.utils.AudioClassifier import *
输入参数：
- wav_file
  - 含义：要播放的音频的路径，默认读取"/device/VoiceData/"路径下对应名称的音频文件
  - 类型：string
  - 默认：无
返回值：无
错误类型：无
#### ---------------使用样例如下-----------------
play_audio("test.wav") # 播放"/device/VoiceData/"下生成test.wav文件


#### 8. tone(frequency,seconds)
说明：播放指定时长、指定频率的的声音
导入库：from SenseTime.utils.AudioClassifier import *
输入参数：
- frequency
  - 含义：频率大小
  - 类型：int
  - 值：100-3000
  - 默认：无
返回值：无
错误类型：无
#### ---------------使用样例如下-----------------
tone(500,1)


#### 9. beep()
说明：播放警报声，默认1000Hz的0.1秒
导入库：from SenseTime.utils.AudioClassifier import *
输入参数：
- 无
返回值：无
错误类型：无
#### ---------------使用样例如下-----------------
beep()


#### 10. speak(content)
说明：控制发声指定内容，暂只支持英文
导入库：from SenseTime.utils.AudioClassifier import *
输入参数：
- content
  - 含义：要播放的声音内容
  - 类型：string
  - 默认：无
返回值：无
错误类型：无
#### ---------------使用样例如下-----------------
speak("Hello")


#### 11. play_preset_audio(wav_file)
说明：播放特定的音效视频
导入库：from SenseTime.utils.AudioClassifier import *
输入参数：
- wav_file
  - 含义：要播放的音频特效
  - 类型：string
  - 默认：无
  - 值: 从列表中选取一种，支持更多，不再一一列举
        [马.wav 猫.wav 笑声.wav 狼.wav]
返回值：无
错误类型：无
#### ---------------使用样例如下-----------------
play_preset_audio("马.wav")


#### classify_audio(audio_file)
说明：预置的分类器对音频文件进行分类，就分类器[起立、坐下、开始、结束、前进、后退、左转、右转、其他]
注意：保持环境的安静，音频文件最好来自盒子关闭风扇后的录音，录音时间大约3s
导入库：from SenseTime.utils.AudioClassifier import *
输入参数：
- audio_file
  - 含义：待分类的音频文件，默认路径"/device/VoiceData/"
  - 类型：string
  - 默认：无
返回值：预测的语音分类结果
错误类型：无
#### ---------------使用样例如下-----------------
record_audio(3,"output.wav") # 在录音过程中说出“起立”
cls = classify_audio("output.wav")
print(cls)

## 六、车道线检测接口
### 功能
车道线检测功能
### 函数接口
#### 1. detect_lane_line(image,row=None)
说明：返回图片中的双车道线位置
     白色背景环境下，贴上黄色、蓝色、或者黑色胶带
     具体赛道样式见"商小鸣地图_寻路.jpg"
导入库：from SenseTime.utils.YellowLaneLineDetector import *
输入参数：
- image 
  - 含义：图像数据
  - 类型：numpy数组，大小为480\*640\*3
  - 默认：无
- row 
  - 含义：要得到的图片中对应行数的车道线中心
  - 类型：整型
  - 默认：图片宽度1/3高度处的左右车道线位置，可指定如300，500等
返回值：
检测到的左右车道线位置，为固定距离下的左右车道线中心的坐标
[[left_lane_x,left_lane_y],[right_lane_x,right_lane_y]]
当不存在时返回None。
错误类型：无
#### ---------------使用样例如下-----------------
frame = cv2.imread("solidWhiteCurve.jpg")
location = detect_lane_line(frame)
print("lane location is: ", location)


#### 2. get_pid_speed(left, right, index="both")
说明：根据识别到左右车道线位置，返回左右轮控制速度，index用来指代左轮、右轮等
导入库：from SenseTime.utils.PID_Control import *
输入参数：
- left 
  - 含义：检测到左侧车道线中心点坐标，注意只含横坐标
  - 类型：int
  - 默认：无
- right
  - 含义：检测到右侧车道线中心点坐标，注意只含横坐标
  - 类型：int
  - 默认：无
- index
  - 含义：指定是选取左轮，右轮，还是左右轮速度
  - 类型：string
  - 取值：["left","right","both"]
  - 默认："both"
返回值：
- 当index为"both"，返回值为控制左右轮的速度
- 当index为"left"，返回值为控制左轮的速度
- 当index为"right"，返回值为控制右轮的速度
错误类型：无
#### ---------------使用样例如下-----------------
left_lane_location,right_lane_location = 200,600
left_speed,right_speed = get_pid_speed(left_lane_location,right_lane_location)
print(left_speed,right_speed )


## 七、物体检测接口
### 功能
目标物体检测，包括小球检测、矿石检测、植物检测等功能
### 函数接口
#### 1. detect_ball(frame)
说明：返回图片中的一个或者多个球体框位置
     道具包中的红色小球
导入库: from SenseTime.sdk.BallDetector import *
输入参数：
- frame 
  - 含义：图像数据
  - 类型：numpy数组，大小为480\*640\*3
  - 默认：无
返回值：检测到球体中心坐标和球体半径
(((center_x,center_y),radis),((center_x,center_y),radis))
错误类型：无
#### ---------------使用样例如下-----------------
from SenseTime.sdk.BallDetector import  *
import cv2
frame1 = cv2.imread("ball.jpg")
p = detect_ball(frame1)
print(p[0][0],p[0][1]) # 前者表示圆心(x,y),后者表示半径
frame = cv2.circle(frame1,p[0][0],p[0][1],(0,255,255),3)
cv2.imwrite("render_ball.jpg",frame)


#### 2. is_ball_existed(frame)
说明：判断图片中是否包含小球
导入库: from SenseTime.sdk.BallDetector import *
输入参数：
- frame 
  - 含义：图像数据
  - 类型：numpy数组，大小为480\*640\*3
  - 默认：无
返回值：
- flag 
  - 含义：是否存在小球的标识，存在时为True，不存在时为False
  - 类型：bool
#### ---------------使用样例如下-----------------
frame = take_photo()
flag = is_ball_existed(frame)
print(flag)


#### detect_mineral(frame)
导入库：from SenseTime.utils.MineralDetector import *
说明：返回图片中的矿石种类及位置
     道具包中的矿石卡片，具体图片样式“可识别的矿石1.png~可识别的矿石4.png”
输入参数：
- frame 
  - 含义：图像数据
  - 类型：numpy数组，大小为480\*640\*3
  - 默认：无

返回值：
检测到的一个及多个矿石的种类及位置。[[label1,[left,top,right,bottom]],[label2,[left,top,right,bootom]]]


#### ---------------使用样例如下-----------------
frame = take_photo()
detections = detect_mineral(frame)
print(detections)


#### 4. detect_plant(frame)
说明：返回图片中的植物种类及位置
     道具包中的植物卡片，具体图片样式“地被草.png、地被花.png、灌木.png、花灌木.png、乔木.png”
导入库：from SenseTime.utils.PlantDetector import *
输入参数：
- frame 
  - 含义：图像数据
  - 类型：numpy数组，大小为480\*640\*3
  - 默认：无
返回值：
检测到的一个及多个植物的种类及位置
[[label1,[left,top,right,bottom]],[label2,[left,top,right,bootom]]]
#### ---------------使用样例如下-----------------
frame = take_photo()
detections = detect_plant(frame)
print(detections)


#### 5. get_result_info(result,coordinate_type="x")
说明:基于通用的检测出的结果，对结果进行解析，返回得到的检测结果信息。适用于detect_ball,detect_mineral,detect_plant
导入库：from SenseTime.utils.PlantDetector import *
输入参数：
- result 
  - 含义：得到的检测结果信息
  - 类型：三维的复杂列表
  - 默认：无
- coordinate_type 
  - 含义：要从结果中解析得到的信息类型
  - 类型：string
  - 取值：x（中心点的横坐标），y（中心点的纵坐标），s（检测框的面积）
  - 默认：x
返回值：
检测到的一个及多个的目标位置信息，如[object1_x,object2_x,...,objectn_x]
#### ---------------使用样例如下-----------------
frame = take_photo()
detections = detect_plant(frame)
info = get_result_info(detections,"x")
print(info)


#### 6. get_result_label(result)
说明:基于通用的检测出的结果，对结果进行解析，返回得到的检测结果信息。适用于detect_ball,detect_mineral,detect_plant
导入库：from SenseTime.utils.PlantDetector import *
输入参数：
- result 
  - 含义：得到的检测结果信息
  - 类型：三维的复杂列表
  - 默认：无
- coordinate_type 
  - 含义：要从结果中解析得到的信息类型
  - 类型：string
  - 取值：x（中心点的横坐标），y（中心点的纵坐标），s（检测框的面积）
  - 默认：x
返回值：
检测到的一个及多个的目标label信息，如[label1,label2,...,labeln]
#### ---------------使用样例如下-----------------
frame = take_photo()
detections = detect_plant(frame)
info = get_result_label(detections)
print(info)


#### 7. get_result_location(result)
说明:基于通用的检测出的结果，对结果进行解析，返回所有检测框的位置信息。适用于detect_ball,detect_mineral,detect_plant
导入库：from SenseTime.utils.PlantDetector import *
输入参数：
- result 
  - 含义：得到的检测结果信息
  - 类型：三维的复杂列表
  - 默认：无
返回值：
result中所有检测框的位置信息，如[location1,location2,...,locationn]
#### ---------------使用样例如下-----------------
frame = take_photo()
detections = detect_plant(frame)
info = get_result_location(detections)
print(info)


#### 8. get_result_area(result)
说明:基于通用的检测出的结果，对结果进行解析，返回所有检测框的面积信息。适用于detect_ball,detect_mineral,detect_plant
导入库：from SenseTime.utils.PlantDetector import *
输入参数：
- result 
  - 含义：得到的检测结果信息
  - 类型：三维的复杂列表
  - 默认：无
返回值：
result中所有检测框的面积信息，如[area1,area2,...,arean]
#### ---------------使用样例如下-----------------
frame = take_photo()
detections = detect_plant(frame)
info = get_result_area(detections)
print(info)


#### 9. get_result_offset(result)
说明:基于通用的检测出的结果，对结果进行解析，返回所有检测框中心偏离图像中心的距离信息。适用于detect_ball,detect_mineral,detect_plant
导入库：from SenseTime.utils.PlantDetector import *
输入参数：
- result 
  - 含义：得到的检测结果信息
  - 类型：三维的复杂列表
  - 默认：无
返回值：
result中所有检测框中心偏离图像中心的距离信息，如[offset1,offset2,...,offsetn]
#### ---------------使用样例如下-----------------
frame = take_photo()
detections = detect_plant(frame)
info = get_result_offset(detections)
print(info)


#### 10. get_result_distance(result)
说明:基于通用的检测出的结果，对结果进行解析，返回所有检测物距离摄像头的距离信息。适用于detect_ball,detect_mineral,detect_plant
导入库：
输入参数：
- result 
  - 含义：得到的检测结果信息
  - 类型：三维的复杂列表
  - 默认：无
返回值：
result中所有检测物距离摄像头的距离信息，如[distance1,distance2,...,distancen]
#### ---------------使用样例如下-----------------
frame = take_photo()
detections = detect_plant(frame)
info = get_result_distance(detections)
print(info)


## 八、电机
### 功能
根据程序指令，输出可控速度和角度的扭力。
### 函数接口

#### run_time(port,speed,seconds) 
说明：设置某电机以指定速度转动指定时间,阻塞式
导入库：from SenseTime.utils.Motor import *
输入参数：
- port 
  - 含义：电机接口序号
  - 类型：数字
  - 值：M1～4
  - 默认：无默认值
- speed 
  - 含义：设定电机速度
  - 类型：数字
  - 值：-100～100
  - 默认：无默认值
- seconds
  - 含义：设定电机转动时间
  - 类型：数字，单位秒
  - 值：正数
  - 默认：无默认值
返回值：无
错误类型：无
#### ---------------使用样例如下-----------------
run_time(1,20,2)


#### run_angle(port,speed,angle) 
说明：设置某电机以指定速度转动指定角度,非阻塞式
导入库：from SenseTime.utils.Motor import *
输入参数：
- port 
  - 含义：电机接口序号
  - 类型：数字
  - 值：M1～4
  - 默认：无默认值
- speed 
  - 含义：设定电机速度
  - 类型：数字
  - 值：-100～100
  - 默认：无默认值
- angle
  - 含义：设定电机转动角度
  - 类型：数字，单位度
  - 值：-3600～3600,注意负值时会改变速度正负
  - 默认：无默认值
返回值：无
错误类型：无
#### ---------------使用样例如下-----------------
run_angle(1,20,180)


#### 3. run_rotations(port,speed=30,rotations=1) 
说明：设置某电机以指定速度转动指定角度,非阻塞式
导入库：from SenseTime.utils.Motor import *
输入参数：
- port 
  - 含义：电机接口序号
  - 类型：数字
  - 值：M1～4
  - 默认：无默认值
- speed 
  - 含义：设定电机速度
  - 类型：数字
  - 值：-100～100
  - 默认：30
- rotations
  - 含义：设定电机转动圈数
  - 类型：数字，单位圈
  - 值：-10～10,注意负值时会改变速度正负
  - 默认：无默认值
返回值：无
错误类型：无
#### ---------------使用样例如下-----------------
run_rotations(1,20,1)


#### run_tank(port1, speed1, port2, speed2, seconds=None)
说明：设置两个端口按照指定速度转动指定时间
导入库：from SenseTime.utils.Motor import *
 run_tank(port1, speed1, port2, speed2, seconds=None)
输入参数：
- port1&port2
  - 含义：电机接口序号
  - 类型：数字
  - 值：M1～4
  - 默认：无默认值
- speed1&speed2 
  - 含义：设定电机速度
  - 类型：数字
  - 值：-100～100
  - 默认：无
- seconds
  - 含义：设定电机转动时间
  - 类型：正数，单位秒
  - 默认：None，当seconds为None时，默认会一直转动
返回值：无
错误类型：无
#### ---------------使用样例如下-----------------
run_tank(1,30,2,40,3)


#### stop_motor(port)
说明：控制指定端口电机停止
导入库：from SenseTime.utils.Motor import *
输入参数：
- port
  - 含义：电机接口序号
  - 类型：变成序列
  - 值：M1～M4
  - 默认：无默认值
返回值：无
错误类型：无
#### ---------------使用样例如下-----------------
stop_motor(3)  # 停止单端口
stop_motor(3,2)  # 停止多端口


#### 6. get_motor_angle(port)
说明：获取电机编码值，默认以开机时刻角度为0，也可以借助reset_motor_angle函数中间重置0角度
导入库：from SenseTime.utils.Motor import *
输入参数：
- port 
  - 含义：电机接口序号
  - 类型：数字
  - 值：M1～4
  - 默认：无默认值
返回值：
- motor_code
  - 含义：电机编码值
  - 类型：数字
  - 值：-4294967296 ~ 4294967296
#### ---------------使用样例如下-----------------
current_angle = get_motor_angle(3)
print(current_angle)


#### 7. reset_motor_angle(port)
说明：重置电机编码值为0
导入库：from SenseTime.utils.Motor import *
输入参数：
- port 
  - 含义：电机接口序号
  - 类型：数字
  - 值：M1～4
  - 默认：无默认值
返回值：无
#### ---------------使用样例如下-----------------
reset_motor_angle(3)
current_angle = get_motor_angle(3)
print(current_angle) # 默认应该为0


#### set_motor(port, speed) 
说明：设置电机以指定速度转动，注意是一直转动，非阻塞式
导入库：from SenseTime.utils.Motor import *
输入参数：
- port 
  - 含义：电机接口序号
  - 类型：数字
  - 值：M1～M4
  - 默认：无默认值
- speed 
  - 含义：设定电机速度
  - 类型：数字
  - 值：-100～100
  - 默认：无默认值
返回值：无
错误类型：无
#### ---------------使用样例如下-----------------
set_motor(1, 30) 


#### set_servo(port, angle)
说明：设置舵机转动指定角度,角度0-270,且不支持速度控制
导入库：from SenseTime.utils.Motor import *
输入参数：
- port 
  - 含义：电机接口序号
  - 类型：数字
  - 值：[6,7,8],注意支持且仅支持P6、P7、P8三个端口
  - 默认：无默认值
- angle 
  - 含义：设定舵机转动角度
  - 类型：数字
  - 值：0～270
  - 单位：度
  - 默认：无默认值
返回值：无
错误类型：无
#### ---------------使用样例如下-----------------
set_servo(6,180) 


#### 10. set_motor_servo(port, speed, angle)
说明：设置电机以指定的速度转动指定角度，非阻塞式
导入库：from SenseTime.utils.Motor import *
输入参数：
- port 
  - 含义：电机接口序号
  - 类型：数字
  - 值：M1～4
  - 默认：无默认值
- speed 
  - 含义：设定电机速度
  - 类型：数字
  - 值：-100～100
  - 默认：无默认值
- angle 
  - 含义：设定电机转动角度
  - 类型：数字
  - 值：-3600～3600，当角度为负时会改变速度正负
  - 单位：度
  - 默认：无默认值
返回值：无
错误类型：无
#### ---------------使用样例如下-----------------
set_motor_servo(4,80,180) 


## 九、光电传感器
### 功能
可识别传感器前方对象的灰度值，并通过程序返回对应数值。
### 函数接口
#### 1. get_light(port) 
说明：读取光电传感器前方对象的灰度值
导入库：from SenseTime.utils.Sensor import *
输入参数：
- port 
  - 含义：接口序号
  - 类型：数字
  - 值：P1-8 
  - 默认：无默认值
返回值：
- light
  - 含义：灰度值
  - 类型：数字
  - 值：0～4095,0为全黑，4095最亮
错误类型：无
#### ---------------使用样例如下-----------------
light = get_light(4) 
print(light)

## 十、触碰传感器
### 功能
可识别触碰开关是否被按下，并通过程序返回对应的触碰状态。
### 函数接口
#### 1. get_touch(port) 
说明：读取触碰传感器状态
导入库：from SenseTime.utils.Sensor import *
输入参数：
- port 
  - 含义：接口序号
  - 类型：数字
  - 值：1-8 
  - 默认：无默认值
返回值：
- state
  - 含义：触碰开关的状态
  - 类型：数字
  - 值：0，触碰开关没有被按倒；1，触碰开关被按倒
错误类型：无
#### ---------------使用样例如下-----------------
state = get_touch(4) 
print(state)


#### is_pressed(port) 
说明：判断触碰传感器是否被按下
导入库：
from SenseTime.utils.Sensor import *
输入参数：
- port 
  - 含义：接口序号
  - 类型：数字
  - 值：1-8 
  - 默认：无默认值
返回值：
- flag
  - 含义：触碰开关的状态
  - 类型：bool
  - 值：False，触碰开关没有被按倒；True，触碰开关被按倒
错误类型：无
#### ---------------使用样例如下-----------------
state = is_pressed(4) 
print(state)


#### 3. wait_until_pressed(port) 
说明：等待直到触碰传感器被按下，阻塞式
导入库：from SenseTime.utils.Sensor import *
输入参数：
- port 
  - 含义：接口序号
  - 类型：数字
  - 值：1-8 
  - 默认：无默认值
返回值：无
错误类型：无
#### ---------------使用样例如下-----------------
wait_until_pressed(3) 
print("port 3 touch sensor has been pressed")


#### 4. wait_until_released(port) 
说明：等待直到触碰传感器被松开，阻塞式
导入库：from SenseTime.utils.Sensor import *
输入参数：
- port 
  - 含义：接口序号
  - 类型：数字
  - 值：1-8 
  - 默认：无默认值
返回值：无
错误类型：无
#### ---------------使用样例如下-----------------
wait_until_pressed(3) 
print("port 3 touch sensor has been released")


## 十一、颜色传感器
### 功能
可识别传感器前方对象的颜色，并通过程序返回对应的颜色数值。
### 函数接口
#### get_color(port)
说明：读取传感器前方对象的颜色
导入库：from SenseTime.utils.Sensor import *
输入参数：
- port 
  - 含义：接口序号
  - 类型：数字
  - 值：1-8 
  - 默认：无默认值
返回值：
- color
  - 含义：传感器前方对象的颜色
  - 类型：string
  - 值：None,"red","green","blue","yellow","black","white"
错误类型：无
#### ---------------使用样例如下-----------------
color = get_color(4) 
print(color)

#### 2. get_rgb(*port)
说明：读取传感器前方对象的RGB通道颜色强度
导入库：from SenseTime.utils.Sensor import *
输入参数：
- port 
  - 含义：接口序号
  - 类型：数字
  - 值：1-8 
  - 默认：无默认值
返回值：
- intensity
  - 含义：传感器前方对象的RGB通道颜色强度
  - 类型：数字
  - 值：(R,G,B)
错误类型：无
#### ---------------使用样例如下-----------------
intensity = get_rgb(4) 
print(intensity)


## 十二、彩灯
### 功能
内置彩色LED灯，可通过程序控制LED灯的工作状态和颜色。
### 函数接口
#### 1. set_led_color(port, color)
说明：设置彩灯模块颜色。
导入库：from SenseTime.utils.Sensor import *
输入参数：
- port 
  - 含义：接口序号
  - 类型：数字
  - 值：1-8 
  - 默认：无默认值
- color
  - 含义：彩灯的状态和颜色
  - 类型：数字
  - 值: "off","red","green","blue","yellow","purple","cyan","white"
  - 默认：无默认值
返回值：无
错误类型：无
#### ---------------使用样例如下-----------------
set_led_color(4,"green") 


## 十三、超声波传感器
### 功能
通过发射超声波信号，并接收被测距对象反射的超声波信号来判断距离。
### 函数接口
#### 1. get_ultrasonic(port)
说明：读取超声波传感器测量对象的距离。
导入库：from SenseTime.utils.Sensor import *
输入参数：
- port 
  - 含义：接口序号
  - 类型：数字
  - 值：1-8 
  - 默认：无默认值
返回值：
- distance
  - 含义：传感器前方对象的距离
  - 类型：数字
  - 值：5～180
  - 单位：厘米
错误类型：无
#### ---------------使用样例如下-----------------
from SenseTime.utils.Sensor import *
d = get_ultrasonic(4) 
print(d)


## 十四、温湿度传感器
### 功能
返回当前环境的温湿度值。
#### 1. get_temperature(port)
说明：读取温度值。
导入库：from SenseTime.utils.Sensor import *
输入参数：
- port 
  - 含义：接口序号
  - 类型：数字
  - 值：1-8 
  - 默认：无默认值
返回值：
- temperature
  - 含义：当前环境的温度值
  - 类型：数字
  - 单位：摄氏度
错误类型：无
#### ---------------使用样例如下-----------------
t = get_temperature(4) 
print(t)


#### 2. get_humidity(port)
说明：读取湿度值。
导入库：from SenseTime.utils.Sensor import *
输入参数：
- port 
  - 含义：接口序号
  - 类型：数字
  - 值：1-8 
  - 默认：无默认值
返回值：
- humidity
  - 含义：当前环境的湿度值
  - 类型：数字
错误类型：无
#### ---------------使用样例如下-----------------
h = get_humidity(4) 
print(h)


