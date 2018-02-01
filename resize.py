import os
import cv2

folder = "datasets/labelimages-224/neg-images"
toFolder = "datasets/labelimages-224/neg-images/resized"
for file in os.listdir(folder):
    if file.endswith(".jpg"):
        imgfile = os.path.join(folder, file)
        tofile = os.path.join(toFolder, file)
        img = cv2.imread(imgfile)
        resizedIMG = cv2.resize(img, (224, 224)) 
        cv2.imwrite(tofile, resizedIMG)

