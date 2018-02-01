#python test.py -c conf/office.json -i csi_1600x1600_20180124_130411.jpg

import cv2
from libDP.dataset import dsPrepare
from libDP.utils import Conf
import argparse

output = "datasets/pos"

ap = argparse.ArgumentParser()
ap.add_argument("-c", "--conf", required=True, help="path to the configuration file")
ap.add_argument("-i", "--image", required=True, help="image filename")
args = vars(ap.parse_args())

conf = Conf(args["conf"])
ds = dsPrepare(xmlFolder=conf["dsLabelPath"], imgFolder=conf["dsImagePath"], debug=False)

for (labelname, xmin, ymin, xmax, ymax, img) in ds.getLabelImg(args["image"]):
    print(labelname, xmin, ymin, xmax, ymax)
    
    print(img.shape)
    cv2.imshow("test", img)
    cv2.waitKey(0)
