#python test.py -c conf/office.json -i datasets/labelimages-1600/images/csi_1600x1600_20180124_130211.jpg

import cv2
from libDP.vision import imgPyramid
from libDP.utils import Conf
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-c", "--conf", required=True, help="path to the configuration file")
ap.add_argument("-i", "--image", required=True, help="image filename")
args = vars(ap.parse_args())

conf = Conf(args["conf"])

for (i, layer) in enumerate(imgPyramid(cv2.imread(args["image"]), scale=conf["PyramidScale"], minSize=conf["minImageSize"])):
    cv2.imshow("Layer {}".format(i + 1), layer)
    cv2.waitKey(0)
