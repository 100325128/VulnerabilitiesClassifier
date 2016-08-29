#!/usr/bin/env python
# -*- coding: utf-8 -*-
import OSTypes

############################################################################
#EXAMPLES
#microsoft:windows_95:fff
#sun:sunos:4.1.4
#debian:debian_linux:0.93
#sun:solaris:1.1
#apple:mac_os
#apple:mac_os_x:10.11.0 and previous versions
#google:android:6.0.1
#nokia:symbian:9.2
#apple:iphone_os:9.3.1 and previous versions
#microsoft:windows_phone:7
############################################################################

def getOSInformation(infoProduct) :
    OSresult = infoProduct
    if(":" in infoProduct) :
       indexAux = infoProduct.index(":", 0, len(infoProduct))
       OSresult = infoProduct[indexAux:]
       OSresult = OSresult.replace("_"," ")
       OSresult = OSresult.replace(":"," ")
    return OSresult

def transformOSInformation(infoProduct) :
    isOSMobile = False
    isOSDesktop, finalOS = verifyIsOSDesktop(infoProduct)
    if (not isOSDesktop) :
       isOSMobile, finalOS = verifyIsOSMobile(infoProduct)
    return isOSDesktop, isOSMobile, finalOS

def verifyIsOSDesktop(infoProduct) :
    isOSDesktop = True
    finalOS = infoProduct
    if(OSTypes.MS_DOS.lower() in infoProduct.lower()) :
        finalOS = OSTypes.MS_DOS
    elif(OSTypes.WINDOWS_NT.lower() in infoProduct.lower()) :
        finalOS = OSTypes.WINDOWS_NT
    elif(OSTypes.WINDOWS_95.lower() in infoProduct.lower()) :
        finalOS = OSTypes.WINDOWS_95
    elif(OSTypes.WINDOWS_98.lower() in infoProduct.lower()) :
        finalOS = OSTypes.WINDOWS_98
    elif(OSTypes.WINDOWS_2000.lower() in infoProduct.lower()) :
        finalOS = OSTypes.WINDOWS_2000
    elif(OSTypes.WINDOWS_XP.lower() in infoProduct.lower()) :
        finalOS = OSTypes.WINDOWS_XP
    elif(OSTypes.WINDOWS_VISTA.lower() in infoProduct.lower()) :
        finalOS = OSTypes.WINDOWS_VISTA
    elif(OSTypes.WINDOWS_7.lower() in infoProduct.lower()) :
        finalOS = OSTypes.WINDOWS_7
    elif(OSTypes.WINDOWS_8.lower() in infoProduct.lower()) :
        finalOS = OSTypes.WINDOWS_8
    elif(OSTypes.WINDOWS_10.lower() in infoProduct.lower()) :
        finalOS = OSTypes.WINDOWS_10
    elif(OSTypes.MAC_OS_X_10_0.lower() in infoProduct.lower()) :
        finalOS = OSTypes.MAC_OS_X_10_0
    elif(OSTypes.MAC_OS_X_10_1.lower() in infoProduct.lower()) :
        finalOS = OSTypes.MAC_OS_X_10_1
    elif(OSTypes.MAC_OS_X_10_2.lower() in infoProduct.lower()) :
        finalOS = OSTypes.MAC_OS_X_10_2
    elif(OSTypes.MAC_OS_X_10_3.lower() in infoProduct.lower()) :
        finalOS = OSTypes.MAC_OS_X_10_3
    elif(OSTypes.MAC_OS_X_10_4.lower() in infoProduct.lower()) :
        finalOS = OSTypes.MAC_OS_X_10_4
    elif(OSTypes.MAC_OS_X_10_5.lower() in infoProduct.lower()) :
        finalOS = OSTypes.MAC_OS_X_10_5
    elif(OSTypes.MAC_OS_X_10_6.lower() in infoProduct.lower()) :
        finalOS = OSTypes.MAC_OS_X_10_6
    elif(OSTypes.MAC_OS_X_10_7.lower() in infoProduct.lower()) :
        finalOS = OSTypes.MAC_OS_X_10_7
    elif(OSTypes.MAC_OS_X_10_8.lower() in infoProduct.lower()) :
        finalOS = OSTypes.MAC_OS_X_10_8
    elif(OSTypes.MAC_OS_X_10_9.lower() in infoProduct.lower()) :
        finalOS = OSTypes.MAC_OS_X_10_9
    elif(OSTypes.MAC_OS_X_10_10.lower() in infoProduct.lower()) :
        finalOS = OSTypes.MAC_OS_X_10_10
    elif(OSTypes.MAC_OS_X_10_11.lower() in infoProduct.lower()) :
        finalOS = OSTypes.MAC_OS_X_10_11
    elif(OSTypes.SOLARIS_2_0.lower() in infoProduct.lower()) :
        finalOS = OSTypes.SOLARIS_2_0
    elif(OSTypes.SOLARIS_2_1.lower() in infoProduct.lower()) :
        finalOS = OSTypes.SOLARIS_2_1
    elif(OSTypes.SOLARIS_2_2.lower() in infoProduct.lower()) :
        finalOS = OSTypes.SOLARIS_2_2
    elif(OSTypes.SOLARIS_2_3.lower() in infoProduct.lower()) :
        finalOS = OSTypes.SOLARIS_2_3
    elif(OSTypes.SOLARIS_2_4.lower() in infoProduct.lower()) :
        finalOS = OSTypes.SOLARIS_2_4
    elif(OSTypes.SOLARIS_2_5_1.lower() in infoProduct.lower()) :
        finalOS = OSTypes.SOLARIS_2_5_1
    elif(OSTypes.SOLARIS_2_5.lower() in infoProduct.lower()) :
        finalOS = OSTypes.SOLARIS_2_5
    elif(OSTypes.SOLARIS_2_6.lower() in infoProduct.lower()) :
        finalOS = OSTypes.SOLARIS_2_6
    elif(OSTypes.SOLARIS_7.lower() in infoProduct.lower()) :
        finalOS = OSTypes.SOLARIS_7
    elif(OSTypes.SOLARIS_8.lower() in infoProduct.lower()) :
        finalOS = OSTypes.SOLARIS_8
    elif(OSTypes.SOLARIS_9.lower() in infoProduct.lower()) :
        finalOS = OSTypes.SOLARIS_9
    elif(OSTypes.SOLARIS_10.lower() in infoProduct.lower()) :
        finalOS = OSTypes.SOLARIS_10
    elif(OSTypes.SOLARIS_11.lower() in infoProduct.lower()) :
        finalOS = OSTypes.SOLARIS_11
    elif(OSTypes.LINUX.lower() in infoProduct.lower()) :
        finalOS = OSTypes.LINUX
    else :
        if (OSTypes.GENERIC_SUN_OS.lower() in infoProduct.lower()) :
           try :
               finalOS = OSType.LIST_SUNOS[infoProduct.lower()]
           except KeyError :
               finalOS = infoProduct
               isOSDesktop = False
        else :
            finalOS = infoProduct
            isOSDesktop = False
    return isOSDesktop,finalOS

def verifyIsOSMobile(infoProduct) :
    finalOS = ""
    isOSMobile = True
    if(OSTypes.IPHONE_OS_1_0.lower() in infoProduct.lower()) :
        finalOS = OSTypes.IPHONE_OS_1_0
    elif(OSTypes.IPHONE_OS_1_1_1.lower() in infoProduct.lower()) :
        finalOS = OSTypes.IPHONE_OS_1_1_1
    elif(OSTypes.IPHONE_OS_1_1.lower() in infoProduct.lower()) :
        finalOS = OSTypes.IPHONE_OS_1_1
    elif(OSTypes.IPHONE_OS_2_0.lower() in infoProduct.lower()) :
        finalOS = OSTypes.IPHONE_OS_2_0
    elif(OSTypes.IPHONE_OS_2_1.lower() in infoProduct.lower()) :
        finalOS = OSTypes.IPHONE_OS_2_1
    elif(OSTypes.IPHONE_OS_2_2.lower() in infoProduct.lower()) :
        finalOS = OSTypes.IPHONE_OS_2_2
    elif(OSTypes.IPHONE_OS_3_0.lower() in infoProduct.lower()) :
        finalOS = OSTypes.IPHONE_OS_3_0
    elif(OSTypes.IPHONE_OS_3_1.lower() in infoProduct.lower()) :
        finalOS = OSTypes.IPHONE_OS_3_1
    elif(OSTypes.IPHONE_OS_3_2.lower() in infoProduct.lower()) :
        finalOS = OSTypes.IPHONE_OS_3_2
    elif(OSTypes.IPHONE_OS_4_1.lower() in infoProduct.lower()) :
        finalOS = OSTypes.IPHONE_OS_4_1
    elif(OSTypes.IPHONE_OS_4_2_10.lower() in infoProduct.lower()) :
        finalOS = OSTypes.IPHONE_OS_4_2_10
    elif(OSTypes.IPHONE_OS_4_2.lower() in infoProduct.lower()) :
        finalOS = OSTypes.IPHONE_OS_4_2
    elif(OSTypes.IPHONE_OS_4_3.lower() in infoProduct.lower()) :
        finalOS = OSTypes.IPHONE_OS_4_3
    elif(OSTypes.IPHONE_OS_4.lower() in infoProduct.lower()) :
        finalOS = OSTypes.IPHONE_OS_4
    elif(OSTypes.IPHONE_OS_5_0.lower() in infoProduct.lower()) :
        finalOS = OSTypes.IPHONE_OS_5_0
    elif(OSTypes.IPHONE_OS_5_1.lower() in infoProduct.lower()) :
        finalOS = OSTypes.IPHONE_OS_5_1
    elif(OSTypes.IPHONE_OS_6.lower() in infoProduct.lower()) :
        finalOS = OSTypes.IPHONE_OS_6
    elif(OSTypes.IPHONE_OS_7.lower() in infoProduct.lower()) :
        finalOS = OSTypes.IPHONE_OS_7
    elif(OSTypes.IPHONE_OS_8.lower() in infoProduct.lower()) :
        finalOS = OSTypes.IPHONE_OS_8
    elif(OSTypes.IPHONE_OS_9.lower() in infoProduct.lower()) :
        finalOS = OSTypes.IPHONE_OS_9
    elif(OSTypes.ANDROID_1_0.lower() in infoProduct.lower()) :
        finalOS = OSTypes.ANDROID_1_0
    elif(OSTypes.ANDROID_1_1.lower() in infoProduct.lower()) :
        finalOS = OSTypes.ANDROID_1_1
    elif(OSTypes.ANDROID_1_5.lower() in infoProduct.lower()) :
        finalOS = OSTypes.ANDROID_1_5
    elif(OSTypes.ANDROID_1_6.lower() in infoProduct.lower()) :
        finalOS = OSTypes.ANDROID_1_6
    elif(OSTypes.ANDROID_2_0.lower() in infoProduct.lower()) :
        finalOS = OSTypes.ANDROID_2_0
    elif(OSTypes.ANDROID_2_1.lower() in infoProduct.lower()) :
        finalOS = OSTypes.ANDROID_2_1
    elif(OSTypes.ANDROID_2_2.lower() in infoProduct.lower()) :
        finalOS = OSTypes.ANDROID_2_2
    elif(OSTypes.ANDROID_2_3.lower() in infoProduct.lower()) :
        finalOS = OSTypes.ANDROID_2_3
    elif(OSTypes.ANDROID_3.lower() in infoProduct.lower()) :
        finalOS = OSTypes.ANDROID_3
    elif(OSTypes.ANDROID_4_0.lower() in infoProduct.lower()) :
        finalOS = OSTypes.ANDROID_4_0
    elif(OSTypes.ANDROID_4_1.lower() in infoProduct.lower()) :
        finalOS = OSTypes.ANDROID_4_1
    elif(OSTypes.ANDROID_4_2.lower() in infoProduct.lower()) :
        finalOS = OSTypes.ANDROID_4_2
    elif(OSTypes.ANDROID_4_3.lower() in infoProduct.lower()) :
        finalOS = OSTypes.ANDROID_4_3
    elif(OSTypes.ANDROID_4_4.lower() in infoProduct.lower()) :
        finalOS = OSTypes.ANDROID_4_4
    elif(OSTypes.ANDROID_5_0.lower() in infoProduct.lower()) :
        finalOS = OSTypes.ANDROID_5_0
    elif(OSTypes.ANDROID_6_0.lower() in infoProduct.lower()) :
        finalOS = OSTypes.ANDROID_6_0
    elif(OSTypes.WINDOWS_PHONE_7.lower() in infoProduct.lower()) :
        finalOS = OSTypes.WINDOWS_PHONE_7
    elif(OSTypes.WINDOWS_PHONE_8_1.lower() in infoProduct.lower()) :
        finalOS = OSTypes.WINDOWS_PHONE_8_1
    elif(OSTypes.WINDOWS_PHONE_8.lower() in infoProduct.lower()) :
        finalOS = OSTypes.WINDOWS_PHONE_8
    elif(OSTypes.BLACKBERRY_OS_1_0.lower() in infoProduct.lower()) :
        finalOS = OSTypes.BLACKBERRY_OS_1_0
    elif(OSTypes.BLACKBERRY_OS_3_6.lower() in infoProduct.lower()) :
        finalOS = OSTypes.BLACKBERRY_OS_3_6
    elif(OSTypes.BLACKBERRY_OS_4_5.lower() in infoProduct.lower()) :
        finalOS = OSTypes.BLACKBERRY_OS_4_5
    elif(OSTypes.BLACKBERRY_OS_4_6.lower() in infoProduct.lower()) :
        finalOS = OSTypes.BLACKBERRY_OS_4_6
    elif(OSTypes.BLACKBERRY_OS_5_0.lower() in infoProduct.lower()) :
        finalOS = OSTypes.BLACKBERRY_OS_5_0
    elif(OSTypes.BLACKBERRY_OS_6_0.lower() in infoProduct.lower()) :
        finalOS = OSTypes.BLACKBERRY_OS_6_0
    elif(OSTypes.BLACKBERRY_OS_7_0.lower() in infoProduct.lower()) :
        finalOS = OSTypes.BLACKBERRY_OS_7_0
    elif(OSTypes.BLACKBERRY_OS_7_1.lower() in infoProduct.lower()) :
        finalOS = OSTypes.BLACKBERRY_OS_7_1
    elif(OSTypes.BLACKBERRY_OS_10_0.lower() in infoProduct.lower()) :
        finalOS = OSTypes.BLACKBERRY_OS_10_0
    elif(OSTypes.BLACKBERRY_OS_10_1.lower() in infoProduct.lower()) :
        finalOS = OSTypes.BLACKBERRY_OS_10_1
    elif(OSTypes.BLACKBERRY_OS_10_2.lower() in infoProduct.lower()) :
        finalOS = OSTypes.BLACKBERRY_OS_10_2
    elif(OSTypes.BLACKBERRY_OS_10_3.lower() in infoProduct.lower()) :
        finalOS = OSTypes.BLACKBERRY_OS_10_3
    elif(OSTypes.SYMBIAN_OS_6_0.lower() in infoProduct.lower()) :
        finalOS = OSTypes.SYMBIAN_OS_6_0
    elif(OSTypes.SYMBIAN_OS_6_1.lower() in infoProduct.lower()) :
        finalOS = OSTypes.SYMBIAN_OS_6_1
    elif(OSTypes.SYMBIAN_OS_7_0.lower() in infoProduct.lower()) :
        finalOS = OSTypes.SYMBIAN_OS_7_0
    elif(OSTypes.SYMBIAN_OS_8_0.lower() in infoProduct.lower()) :
        finalOS = OSTypes.SYMBIAN_OS_8_0
    elif(OSTypes.SYMBIAN_OS_8_1.lower() in infoProduct.lower()) :
        finalOS = OSTypes.SYMBIAN_OS_8_1
    elif(OSTypes.SYMBIAN_OS_9_1.lower() in infoProduct.lower()) :
        finalOS = OSTypes.SYMBIAN_OS_9_1
    elif(OSTypes.SYMBIAN_OS_9_2.lower() in infoProduct.lower()) :
        finalOS = OSTypes.SYMBIAN_OS_9_2
    elif(OSTypes.SYMBIAN_OS_9_3.lower() in infoProduct.lower()) :
        finalOS = OSTypes.SYMBIAN_OS_9_3
    elif(OSTypes.SYMBIAN_OS_9_4.lower() in infoProduct.lower()) :
        finalOS = OSTypes.SYMBIAN_OS_9_4
    elif(OSTypes.SYMBIAN_OS_9_5.lower() in infoProduct.lower()) :
        finalOS = OSTypes.SYMBIAN_OS_9_5
    elif(OSTypes.SYMBIAN_OS_10_1.lower() in infoProduct.lower()) :
        finalOS = OSTypes.SYMBIAN_OS_10_1
    else :
        finalOS = infoProduct
        isOSMobile = False
    return isOSMobile,finalOS
