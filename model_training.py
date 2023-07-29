from SenseTime.sdk.ClassificationDetector import *
from SenseTime.utils.GeneralClassifier import *
from SenseTime.utils.ImageShow import *
data_path="/device/public/SignPic"
model=train_classifier(data_path,classifier="CNN");
save_model(model,"SignsAI.clf");
print(model)