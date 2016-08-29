#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os.path
import shutil
import OSClassify
import OSTypes

CONST_IS_OS="cpe:/o:"
CONST_IS_AP="cpe:/a:"
CONST_IS_HW="cpe:/h:"

def addToVulnerableList(vulnerable_list, info) :
    if (info not in vulnerable_list) :
       vulnerable_list += [info]
    return vulnerable_list

def classifyProduct(productAux) :
    isOS = False
    isAP = False
    isHW = False
    part1 = productAux[:7]
    info = productAux[7:]
    if (part1 == CONST_IS_OS) :
       isOS = True

    if (part1 == CONST_IS_AP) :
       isAP = True

    if (part1 == CONST_IS_HW) :
       isHW = True

    return isOS,isAP,isHW,info

def processApplication(infoProduct) :
    partition = infoProduct.split(":")
    tuplaResultado = ("","")
    if(len(partition) < 2) :
       if len(partition) == 1 :
          tuplaResultado[0] = partition[0].replace("_"," ")
    else :
       tuplaResultado = (partition[0].replace("_"," "),partition[1].replace("_"," "))
    return tuplaResultado
