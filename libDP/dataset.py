#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import cv2
from xml.dom import minidom

class dsPrepare:
    def __init__(self, xmlFolder, imgFolder, debug=False):
        self.labels = []
        self.trainData = []
        self.xmlFolder = xmlFolder
        self.imgFolder = imgFolder
        self.debug=debug

    def getLabel(self, xmlFilename, assignName=""):
        labelXML = minidom.parse(self.xmlFolder + '/' + xmlFilename)
        labelName = []
        labelXmin = []
        labelYmin = []
        labelXmax = []
        labelYmax = []

        tmpArrays = labelXML.getElementsByTagName("name")
        for elem in tmpArrays:
            labelName.append(str(elem.firstChild.data))

        tmpArrays = labelXML.getElementsByTagName("xmin")
        for elem in tmpArrays:
            labelXmin.append(int(elem.firstChild.data))

        tmpArrays = labelXML.getElementsByTagName("ymin")
        for elem in tmpArrays:
            labelYmin.append(int(elem.firstChild.data))

        tmpArrays = labelXML.getElementsByTagName("xmax")
        for elem in tmpArrays:
            labelXmax.append(int(elem.firstChild.data))

        tmpArrays = labelXML.getElementsByTagName("ymax")
        for elem in tmpArrays:
            labelYmax.append(int(elem.firstChild.data))

        for i in range(0, len(labelName)):
            if(assignName=="" or assignName==labelName[i]):
                yield (labelName[i], labelXmin[i], labelYmin[i], labelXmax[i], labelYmax[i]) 

    def getLabelImg(self, xmlFilename, assignName=""):
        filename, file_extension = os.path.splitext(xmlFilename)
        print(self.xmlFolder, filename, file_extension)
        print("IMG:", self.imgFolder + "/" + filename + ".jpg" )
        image = cv2.imread(self.imgFolder + "/" + filename + ".jpg")
        print("XML:", self.xmlFolder + '/' + xmlFilename )
        labelXML = minidom.parse(self.xmlFolder + '/' + xmlFilename )
        labelName = []
        labelXmin = []
        labelYmin = []
        labelXmax = []
        labelYmax = []
        #imgPart = []

        tmpArrays = labelXML.getElementsByTagName("name")
        for elem in tmpArrays:
            labelName.append(str(elem.firstChild.data))

        tmpArrays = labelXML.getElementsByTagName("xmin")
        for elem in tmpArrays:
            labelXmin.append(int(elem.firstChild.data))

        tmpArrays = labelXML.getElementsByTagName("ymin")
        for elem in tmpArrays:
            labelYmin.append(int(elem.firstChild.data))

        tmpArrays = labelXML.getElementsByTagName("xmax")
        for elem in tmpArrays:
            labelXmax.append(int(elem.firstChild.data))

        tmpArrays = labelXML.getElementsByTagName("ymax")
        for elem in tmpArrays:
            labelYmax.append(int(elem.firstChild.data))

        for i in range(0, len(labelName)):
            if(assignName=="" or assignName==labelName[i]):

                roi = image[labelYmin[i]:labelYmax[i], labelXmin[i]:labelXmax[i]]
                print(roi.shape)
                #imgPart.append(roi)
                yield (labelName[i], labelXmin[i], labelYmin[i], labelXmax[i], labelYmax[i], roi)
