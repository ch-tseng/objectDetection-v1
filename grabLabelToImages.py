#python grabLabelToImages.py -f datasets -d datasets/pos -l ""

import glob, os
import numpy as np
import argparse
from libDP.dataset import dsPrepare
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--folder", required=True, help="path to the folder with images and labels")
ap.add_argument("-d", "--distinct", required=True, help="path to the folder to save label images")
ap.add_argument("-l", "--label", required=False, help="label name for filterring")
args = vars(ap.parse_args())

ds = dsPrepare(xmlFolder=args["folder"]+"/labels", imgFolder=args["folder"]+"/images", debug=False)

i = 0
# loop over all annotations paths
for filename in os.listdir(args["folder"]+"/labels"):
    # load the bounding box associated with the path and update the width and height
    for (labelname, xmin, ymin, xmax, ymax, img) in ds.getLabelImg(filename, assignName=args["label"]):
        print(labelname, xmin, ymin, xmax, ymax)
        print("WRITE:", args["distinct"] + "/label-"+str(i)+".jpg")
        cv2.imwrite(args["distinct"] + "/label-"+str(i)+".jpg", img)
        i += 1

