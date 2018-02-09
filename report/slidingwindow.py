# -*- coding: utf-8 -*-
#python slidingwindow.py -s 30 -i testImages/office-500.jpg -w 90 -t 60


import time
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-s", "--step", required=True, help="Sliding window每次移動的距離pixels")
ap.add_argument("-i", "--image", required=True, help="目標圖片的路徑")
ap.add_argument("-w", "--width", required=True, help="Sliding window的寬度")
ap.add_argument("-t", "--height", required=True, help=" Sliding window的高度")
args = vars(ap.parse_args())

winW = int(args["width"])
winH = int(args["height"])

def sliding_window(image, stepSize, windowSize):
    for y in range(0, image.shape[0], stepSize):
        for x in range(0, image.shape[1], stepSize):
            test = image[y:y + windowSize[1], x:x + windowSize[0]]
            yield (x, y, image[y:y + windowSize[1], x:x + windowSize[0]])


img = cv2.imread(args["image"])
for (x, y, window) in sliding_window(img, int(args["step"]), (winW, winH) ):
    # 如果傳回的圖片尺寸不符sliding window指定的尺寸，則予以忽略。
    if window.shape[0] != winH or window.shape[1] != winW:
        continue

    clone = img.copy()
    cv2.rectangle(clone, (x, y), (x + winW, y + winH), (0, 255, 0), 2)
    cv2.imshow("Window", clone)
    cv2.imshow("Part", window)

    cv2.waitKey(1)
    time.sleep(0.025)
