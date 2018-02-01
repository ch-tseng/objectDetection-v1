#python test-slidingwindow.py -c conf/office.json -i datasets/labelimages-1600/images/csi_1600x1600_20180124_130411.jpg

import time
import cv2
from libDP.vision import imgPyramid
from libDP.vision import sliding_window
from libDP.utils import Conf
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-c", "--conf", required=True, help="path to the configuration file")
ap.add_argument("-i", "--image", required=True, help="image filename")
args = vars(ap.parse_args())

conf = Conf(args["conf"])

# load the input image and unpack the command line arguments
image = cv2.imread(args["image"])
(winW, winH) = (conf["windowSize"][0], conf["windowSize"][1])

# loop over the image pyramid
for layer in imgPyramid(image, scale=conf["PyramidScale"], minSize=conf["minImageSize"]):
    print(layer.shape)
    # loop over the sliding window for each layer of the pyramid
    for (x, y, window) in sliding_window(layer, stepSize=conf["stepSize"], windowSize=(winW, winH)):
        # if the current window does not meet our desired window size, ignore it
        if window.shape[0] != winH or window.shape[1] != winW:
            continue
 
        # THIS IS WHERE WE WOULD PROCESS THE WINDOW, EXTRACT HOG FEATURES, AND
        # APPLY A MACHINE LEARNING CLASSIFIER TO PERFORM OBJECT DETECTION
 
        # since we do not have a classifier yet, let's just draw the window
        clone = layer.copy()
        cv2.rectangle(clone, (x, y), (x + winW, y + winH), (0, 255, 0), 2)
        cv2.imshow("Window", clone)
 
        # normally we would leave out this line, but let's pause execution
        # of our script so we can visualize the window
        cv2.waitKey(1)
        time.sleep(0.025)
