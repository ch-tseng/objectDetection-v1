#python test-slidingwindow.py -c conf/office.json -i datasets/labelimages-1600/images/csi_1600x1600_20180124_130411.jpg

import time, os
import cv2
import numpy as np
from libDP.vision import imgPyramid
from libDP.vision import sliding_window
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--folder", required=True, help="Path for negative images folder")
ap.add_argument("-o", "--output", required=True, help="Path for output folder")
args = vars(ap.parse_args())

winW = 48
winH = 48

for filename in os.listdir(args["folder"]):
    image = cv2.imread(args["folder"]+"/"+filename)
    # loop over the image pyramid
    for layer in imgPyramid(image, scale=0.5, minSize=[60,60]):
        print(layer.shape)
        # loop over the sliding window for each layer of the pyramid
        for (x, y, window) in sliding_window(layer, stepSize=24, windowSize=(winW, winH)):
            # if the current window does not meet our desired window size, ignore it
            if window.shape[0] != winH or window.shape[1] != winW:
                continue
 
            clone = layer.copy()
            cv2.rectangle(clone, (x, y), (x + winW, y + winH), (0, 255, 0), 2)
            cv2.imshow("Window", clone)

            cv2.imwrite(args["output"]+"/"+str(time.time())+".jpg", window)
            cv2.waitKey(1)
            time.sleep(0.025)
