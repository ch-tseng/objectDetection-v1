#python test-slidingwindow.py -c conf/office.json -i datasets/labelimages-1600/images/csi_1600x1600_20180124_130411.jpg

import time, os
import cv2
import numpy as np
from libDP.vision import imgPyramid
from libDP.vision import sliding_window
#from libDP.utils import Conf
from keras.models import model_from_yaml
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-n", "--negative", required=True, help="Save error images to mining/negative folder?")
ap.add_argument("-f", "--folder", required=True, help="Path to the negative image folder waiting for analysis.")
args = vars(ap.parse_args())

#conf = Conf(args["conf"])

def preditROI(img):
    dict_labels = {"negative": 0,"positive": 1 }
    inv_dict_labels = {v: k for k, v in dict_labels.items()}

    #cv2.imshow("labeIMG", img)
    #cv2.waitKeys(0)
    #time.sleep(0.025)
    
    img=cv2.resize(img,(48,48) ,interpolation=cv2.INTER_CUBIC) 
    inputimgs = np.array([img])
    inputimgs = inputimgs.astype('float32') / 255.0
    prediction = loaded_model.predict(inputimgs)
    print("Prediction result:", prediction)
    predict_label_tmp = np.argmax(prediction,axis=1)
    score = np.max(prediction)
    predict_label = inv_dict_labels[predict_label_tmp[0]]
    print("---> {}, ({})".format(predict_label, score))

    if(score>0.85 and predict_label=="positive"):
    #if(predict_label=="positive"):
        return True
    else:
        return False

#load YAML and create model
yaml_file = open('misOffice-model.yaml', 'r')
loaded_model_yaml = yaml_file.read()
yaml_file.close()
loaded_model = model_from_yaml(loaded_model_yaml)
# load weights into new model
loaded_model.load_weights("misOffice-yaml-model.h5")
print("Loaded model from disk")

dict_labels = {"negative": 0,"positive": 1 }
inv_dict_labels = {v: k for k, v in dict_labels.items()}

# load the input image and unpack the command line arguments
#image = cv2.imread(args["image"])
#(winW, winH) = (conf["window_dim"][0], conf["window_dim"][1])
winW = 23
winH = 23

for filename in os.listdir(args["folder"]):
    image = cv2.imread(args["folder"]+"/"+filename)
    # loop over the image pyramid
    for layer in imgPyramid(image, scale=0.85, minSize=[60,60]):
        print(layer.shape)
        # loop over the sliding window for each layer of the pyramid
        for (x, y, window) in sliding_window(layer, stepSize=12, windowSize=(winW, winH)):
            # if the current window does not meet our desired window size, ignore it
            if window.shape[0] != winH or window.shape[1] != winW:
                continue
 
            clone = layer.copy()
            cv2.rectangle(clone, (x, y), (x + winW, y + winH), (0, 255, 0), 2)
            cv2.imshow("Window", clone)

            predict = preditROI(window) 

            if(predict==True):
                yn = cv2.waitKey(0)
                if(yn==1048686 and args["negative"]==True):  # n
                    cv2.imwrite("mining/negative/"+str(time.time())+".jpg", window)
            else:
                yn = cv2.waitKey(1)
                time.sleep(0.025)
