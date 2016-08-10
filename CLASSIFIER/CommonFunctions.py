#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os.path
import shutil
import OSClassify
import OSTypes

#constante que identifica que el contenido del producto es una vulnerabilidad a nivel de SO
CONST_IS_OS="cpe:/o:"
#constante que identifica que el contenido del producto es una vulnerabilidad a nivel de aplicación
CONST_IS_AP="cpe:/a:"
#constante que identifica que el contenido del producto es una vulnerabilidad a nivel de HW
CONST_IS_HW="cpe:/h:"

#esta función agrega informacion de hw a la lista de hw vulnerable
def addToVulnerableList(vulnerable_list, info) :
    if (info not in vulnerable_list) :
       vulnerable_list += [info]
    return vulnerable_list

#isOS -> True si el parámetro productAux hace referencia a un Sistema Operativo y False eoc
#isAP -> True si el parámetro productAux hace referencia a una aplicacion y False eoc
#isHW -> True si el parámetro productAux hace referencia a hardware y False eoc
#info -> devuelve la información asociada al SO, a la aplicación o al hw
#ejemplo -> cpe:/o:microsoft:windows_95:fff -> microsoft:windows_95:fff
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

#tuplaResultado contiene como primer valor el nombre del fabricante y
#segundo valor el nombre de la aplicación
#ejemplo -> netscape:messaging_server:3.55 -> (netscape,messaging server)
def processApplication(infoProduct) :
    #dividimos la cadena separando por dos puntos
    partition = infoProduct.split(":")
    tuplaResultado = ("","")
    #comprobamos que se el texto contiene el fabricante y la aplicacion
    #en caso de no tener alguno de ellos se añade una nota para revisar
    #reemplazamos los _ por espacio
    if(len(partition) < 2) :
       if len(partition) == 1 :
          tuplaResultado[0] = partition[0].replace("_"," ")
    else :
       tuplaResultado = (partition[0].replace("_"," "),partition[1].replace("_"," "))
    return tuplaResultado
