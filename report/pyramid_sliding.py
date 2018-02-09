# -*- coding: utf-8 -*-
#python test-slidingwindow.py -c conf/office.json -i datasets/labelimages-1600/images/csi_1600x1600_20180124_130411.jpg

import time
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="目標圖片的path")
ap.add_argument("-m", "--minwidth", type=int, help="影像金字塔最小的圖片寬度.")
ap.add_argument("-n", "--minheight", type=int, help="影像金字塔最小的圖片高度")
ap.add_argument("-r", "--scaleRatio", type=float, default=0.5, help="每次的縮小比例")
ap.add_argument("-s", "--stepSize", type=int, required=True, help="Sliding window每次移動的距離pixels")
ap.add_argument("-w", "--width", type=int, required=True, help="Sliding window的寬度")
ap.add_argument("-t", "--height", type=int, required=True, help=" Sliding window的高度")
args = vars(ap.parse_args())

winW = args["width"]
winH = args["height"]


# load the input image and unpack the command line arguments
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
for layer in pyramid(image, scale=args["scaleRatio"], minSize=(args["minwidth"], args["minheight"])):
    print(layer.shape)
    # loop over the sliding window for each layer of the pyramid
    for (x, y, window) in sliding_window(layer, stepSize=args["stepSize"], windowSize=(winW, winH)):
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
