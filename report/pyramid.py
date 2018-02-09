# -*- coding: utf-8 -*-

import argparse
import cv2
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="目標圖片的path")
ap.add_argument("-m", "--minwidth", type=int, help="影像金字塔最小的圖片寬度.")
ap.add_argument("-n", "--minheight", type=int, help="影像金字塔最小的圖片高度")
ap.add_argument("-s", "--scale", type=float, default=1.5, help="每次的縮小比例")
args = vars(ap.parse_args())

def pyramid(image, scale=0.5, minSize=(30, 30)):
    yield image 
    while True:
        image = cv2.resize(image, (int(image.shape[1] * scale), int(image.shape[0] * scale)) )
        if image.shape[0] < minSize[1] or image.shape[1] < minSize[0]:
            break

        print("Image size: {}, {} ".format(image.shape[1], image.shape[0]))
        yield image

image = cv2.imread(args["image"])
for (i, layer) in enumerate(pyramid(image, scale=args["scale"], minSize=(args["minwidth"], args["minheight"]))):
    cv2.imshow("Layer {}".format(i + 1), layer)

cv2.waitKey(0)

