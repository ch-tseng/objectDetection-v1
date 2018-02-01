import os
import cv2

def imgPyramid(image, scale=0.5, minSize=[120,120], debug=False):
    #image = cv2.imread(image)
    # yield the original image
    yield image

        # keep looping over the pyramid
    while True:
        w = int(image.shape[1] * scale)
        h = int(image.shape[0] * scale)
        image = cv2.resize(image, (w, h))
        if image.shape[0] < minSize[1] or image.shape[1] < minSize[0]:
            break

        # yield the next image in the pyramid
        yield image


file = "datasets/labelimages-1600/images/csi_1600x1600_20180126_084053.jpg"
image = cv2.imread(file)

for (i, img) in enumerate(imgPyramid(image , 0.5 , [120,120])):
    cv2.imshow("test", img)
    cv2.waitKey(0)
