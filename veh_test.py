import json
import os
import jav_trigger
import cv2
import tensorflow as tf
import SOS
import numplate_extrract
import time
import numpy

CATEGORIES = ["class0", "class1","class2"]
java_path = 'java_connect'

def prepare(file):
    IMG_SIZE = 50
    img_array = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)

def run(file):
    model = tf.keras.models.load_model("CNN2.model")
    image_ = "test/"+file#your image path
    # image_=r'E:\Hackerearth\Round 2\conda_tens\test_img\test11.jpeg'
    image=prepare(image_)
    prediction = model.predict([image])
    # print(prediction)
    # print(list(prediction[0]))
    prediction = list(prediction[0])
    # print(type(float(max(prediction))))

    file1=file.split('.')[0]+'_.'+file.split('.')[1]
    numplate=numplate_extrract.ocr("test/"+file1)
    # numplate='KL15A1365'
    print ("Numplate_value:",numplate)

    print("approach 1..")
    ans1 = CATEGORIES[prediction.index(max(prediction))]
    print("class:",ans1)
    # if (float(max(prediction))*100)<70:
    # f=cv2.imread(image_)
    # cv2.imwrite(java_path+"/"+file,f)
    # with open(java_path+"/request.txt",'w') as f:
    #     f.write(numplate)
    print("approach 2..")
    ans2=None
    while(True):
        ind,ans2=jav_trigger.jar_trigger(numplate)
        if ind is True:
            break
    # while (os.path.exists(java_path + '/class.json') is not True):
    #     continue
    # jf=open(java_path+'/class.json','r')
    # dic=json.load(jf)
    print("Type:",ans2)
    arr=["class0","class1","class2"]
    ind1=arr.index(ans1)
    if 'car' in ans2.lower():
        ans2="class0"
    if 'bus' in ans2.lower():
        ans2 = "class1"
    if 'carrier' in ans2.lower():
        ans2 = "class2"
    ind2=arr.index(ans2)

    final_ans=arr[max(ind1,ind2)]
    if final_ans==("class0"):
        SOS.sms(numplate,"ABC123","150")

    if final_ans==("class1"):
        SOS.sms(numplate,"ABC123","300")

    if final_ans==("class2"):
        SOS.sms(numplate,"ABC123","350")

if __name__ == '__main__':
    run("carTest11.jpeg")