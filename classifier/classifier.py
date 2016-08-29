#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- coding: 850 -*-

import sys
import time
import VulnerabilitiesHandler
import FileManager
from threading import Thread
from time import sleep

#This function gets the name of the XML file to be processed
def getFileName() :
    msjError = ""
    fileName = ""
    if (len(sys.argv) == 2) :
       fileName = sys.argv[1]
       if (not fileName.lower().endswith(".xml")) :
          msjError = "Incorrect file extension, it must be an XML file"
    else :
       msjError = "Usage ==> python classifier.py fileNameXML"
    return msjError, fileName

#main function
def process(fileName) :
    fileManager = FileManager.FileManager()
    msjError = fileManager.createOutputFiles()
    if (msjError == "") :
       vulnerabilities = VulnerabilitiesHandler.VulnerabilitiesHandler()
       vulnerabilities.setFileManager(fileManager)
       saxparser = VulnerabilitiesHandler.make_parser()
       saxparser.setContentHandler(vulnerabilities)
       datasource = open(fileName,"r")
       saxparser.parse(datasource)
       fileManager.closeOutputFiles()
    else :
       print (msjError)

msjError, fileName = getFileName()
if (msjError == "") :
    subprocess = Thread(target=process, args=(fileName,))
    subprocess.start()
    print "Please wait ",
    while(subprocess.isAlive()):
        print ".",
        sleep(1)
else :
    print (msjError)


