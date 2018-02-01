#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob, os
import random
import cv2
import numpy as np

imageFolder = "datasets/neg-source/"  #待處理的相片資料夾路徑
areaSize = (48,48)   #要取得的圖片寸(w, h)
takePartNum = 8  #每張相片要隨機取幾張?
outputFolder = "datasets/neg/"  #輸出的相片路徑

locW = 0
locH = 0
takeparts = 0

for filename in os.listdir(imageFolder):
    print("FILE:", imageFolder + filename)
    image = cv2.imread(imageFolder + filename)
    print("SHAPE:", image.shape)
    width = image.shape[1]
    height = image.shape[0]
    #print("Process image: {}(size:{}x{}).....".format(filename,width,height))

    while takeparts<takePartNum:
        locH = random.randint(0, int(height / areaSize[1])-1)
        locW = random.randint(0, int(width / areaSize[0])-1)

        fromH = locH*areaSize[1]
        fromW = locW*areaSize[0]

        #print("locH:{}, locW:{} ,take the area: ({}:{},{}:{})".format(locH, locW, fromH, fromW, toH, toW))

        area = image[ fromH:fromH+areaSize[1], fromW:fromW+areaSize[0] ] 
        print("AREA.shape:{}, ({}:{}, {}:{})".format(area.shape, fromH, fromW, fromH+areaSize[1], fromW+areaSize[0]))        
        if not os.path.exists(outputFolder):
            os.mkdir(outputFolder)

        outputFile = outputFolder+"area_"+str(locW)+"_"+str(locH)+"_"+filename
        #print("locH:{}, locW:{} ,take the area: ({}:{},{}:{}) --> {}".format(locH, locW, fromH, fromW, toH, toW, outputFile))
        cv2.imwrite(outputFile, area)
        #print("write to {}", outputFile)
        #cv2.imshow("AREA ({},{})".format(locW, locH), area)
        #cv2.waitKey(0)

        takeparts += 1

    takeparts = 0
