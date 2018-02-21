# -*- coding: utf-8 -*-
#python pyramid_sliding.py -i testImages/office-500.jpg -m 120 -n 120 -r 0.75 -s 12 -w 75 -t 75

import time
import cv2
from libOB.conf import Conf
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="目標圖片的path")
ap.add_argument("-c", "--conf", required=True, help="path to the configuration file")
args = vars(ap.parse_args())

conf = Conf(args["conf"])
winW = conf["windowWidth"]
winH = conf["windowHeight"]

image = cv2.imread(args["image"])

def pyramid(image, scale=0.5, minSize=(30, 30)):
    yield image
    while True:
        print("Image resize:", (int(image.shape[1] * scale), int(image.shape[0] * scale)))
        image = cv2.resize(image, (int(image.shape[1] * scale), int(image.shape[0] * scale)) )
        if image.shape[0] < minSize[1] or image.shape[1] < minSize[0]:
            break

        print("Image size: {}, {} ".format(image.shape[1], image.shape[0]))
        yield image

def sliding_window(image, stepSize, windowSize):
    for y in range(0, image.shape[0], stepSize):
        for x in range(0, image.shape[1], stepSize):
            test = image[y:y + windowSize[1], x:x + windowSize[0]]
            yield (x, y, image[y:y + windowSize[1], x:x + windowSize[0]])


# loop over the image pyramid
for layer in pyramid(image, scale=conf["resizeScale"], minSize=(conf["minWidthStop"], conf["minHeightStop"])):
    print(layer.shape)
    # loop over the sliding window for each layer of the pyramid
    for (x, y, window) in sliding_window(layer, stepSize=conf["windowMovePixels"], windowSize=(winW, winH)):
        # if the current window does not meet our desired window size, ignore it
        if window.shape[0] != winH or window.shape[1] != winW:
            continue
 
        clone = layer.copy()
        cv2.rectangle(clone, (x, y), (x + winW, y + winH), (0, 255, 0), 2)
        cv2.imshow("Window", clone)
        cv2.imshow("Part", window)
 
        cv2.waitKey(1)
        time.sleep(0.025)
