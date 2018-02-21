#python explore_winsize.py -c conf/office.json -l "1"

import glob, os
import numpy as np
#from libDP.utils import Conf
import argparse
from libOB.dataset import dsPrepare

ap = argparse.ArgumentParser()
ap.add_argument("-l", "--labels", required=True, help="Folder of labels")
ap.add_argument("-i", "--images", required=True, help="Folder of images")
ap.add_argument("-n", "--labelname", required=True, help="Assign a label name to analysis")
args = vars(ap.parse_args())

# load the configuration file and initialize the list of widths and heights
ds = dsPrepare(xmlFolder=args["labels"], imgFolder=args["images"], debug=False)

widths = []
heights = []
 
# loop over all annotations paths
for filename in os.listdir(args["labels"]):
    # load the bounding box associated with the path and update the width and height
    for (labelname, xmin, ymin, xmax, ymax) in ds.getLabel(filename, assignName=args["labelname"]):
        print(labelname, xmin, ymin, xmax, ymax)
        widths.append(xmax-xmin)
        heights.append(ymax-ymin)
 
# compute the average of both the width and height lists
(avgWidth, avgHeight) = (np.mean(widths), np.mean(heights))
print("[INFO] avg. width: {:.2f}".format(avgWidth))
print("[INFO] avg. height: {:.2f}".format(avgHeight))
print("[INFO] aspect ratio: {:.2f}".format(avgWidth / avgHeight))
