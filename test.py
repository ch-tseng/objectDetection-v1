import cv2
from libDP.dataset import dsPrepare

ds = dsPrepare(xmlFolder="labelimages/labels", imgFolder="labelimages/images", debug=False)

(labelname, xmin, ymin, xmax, ymax, img) = ds.getLabel("csi_1600x1600_20180125_105958.jpg")

for i in range(0, len(labelname)):
    print(labelname[i], xmin[i], ymin[i], xmax[i], ymax[i])
    a = img[i]
    print(a.shape)
    cv2.imshow("test", img[i])
    cv2.waitKey(0)
