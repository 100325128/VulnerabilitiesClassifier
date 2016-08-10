#!/usr/bin/env python
# -*- coding: utf-8 -*-

GENERIC_WINDOWS="Windows"
GENERIC_MAC_OS_X="Mac OS X"
GENERIC_SOLARIS="Solaris"
GENERIC_SUN_OS="sun os"

GENERIC_IPHONE_OS="iphone OS"
GENERIC_ANDROID="Android"
GENERIC_WINDOWS_PHONE="Windows Phone"
GENERIC_BLACKBERRY_OS="BlackBerry OS"
GENERIC_SYMBIAN_OS="Symbian OS"

MS_DOS="MS-DOS"
WINDOWS_NT="Windows NT"
WINDOWS_95="Windows 95"
WINDOWS_98="Windows 98"
WINDOWS_2000="Windows 2000"
WINDOWS_XP="Windows XP"
WINDOWS_VISTA="Windows Vista"
WINDOWS_7="Windows 7"
WINDOWS_8="Windows 8"
WINDOWS_10="Windows 10"
MAC_OS_X_10_0="Mac OS X 10.0"
MAC_OS_X_10_1="Mac OS X 10.1"
MAC_OS_X_10_2="Mac OS X 10.2"
MAC_OS_X_10_3="Mac OS X 10.3"
MAC_OS_X_10_4="Mac OS X 10.4"
MAC_OS_X_10_5="Mac OS X 10.5"
MAC_OS_X_10_6="Mac OS X 10.6"
MAC_OS_X_10_7="Mac OS X 10.7"
MAC_OS_X_10_8="Mac OS X 10.8"
MAC_OS_X_10_9="Mac OS X 10.9"
MAC_OS_X_10_10="Mac OS X 10.10"
MAC_OS_X_10_11="Mac OS X 10.11"
SOLARIS_2_0="Solaris 2.0"
SOLARIS_2_1="Solaris 2.1"
SOLARIS_2_2="Solaris 2.2"
SOLARIS_2_3="Solaris 2.3"
SOLARIS_2_4="Solaris 2.4"
SOLARIS_2_5="Solaris 2.5"
SOLARIS_2_5_1="Solaris 2.5.1"
SOLARIS_2_6="Solaris 2.6"
SOLARIS_7="Solaris 7"
SOLARIS_8="Solaris 8"
SOLARIS_9="Solaris 9"
SOLARIS_10="Solaris 10"
SOLARIS_11="Solaris 11"
LINUX="Linux"

#mobile
IPHONE_OS_1_0="iphone OS 1.0"
IPHONE_OS_1_1="iphone OS 1.1"
IPHONE_OS_1_1_1="iphone OS 1.1.1"
IPHONE_OS_2_0="iphone OS 2.0"
IPHONE_OS_2_1="iphone OS 2.1"
IPHONE_OS_2_2="iphone OS 2.2"
IPHONE_OS_3_0="iphone OS 3.0"
IPHONE_OS_3_1="iphone OS 3.1"
IPHONE_OS_3_2="iphone OS 3.2"
IPHONE_OS_4="iphone OS 4"
IPHONE_OS_4_1="iphone OS 4.1"
IPHONE_OS_4_2="iphone OS 4.2"
IPHONE_OS_4_2_10="iphone OS 4.2.10"
IPHONE_OS_4_3="iphone OS 4.3"
IPHONE_OS_5_0="iphone OS 5.0"
IPHONE_OS_5_1="iphone OS 5.1"
IPHONE_OS_6="iphone OS 6"
IPHONE_OS_7="iphone OS 7"
IPHONE_OS_8="iphone OS 8"
IPHONE_OS_9="iphone OS 9"
ANDROID_1_0="Android 1.0"
ANDROID_1_1="Android 1.1"
ANDROID_1_5="Android 1.5"
ANDROID_1_6="Android 1.6"
ANDROID_2_0="Android 2.0"
ANDROID_2_1="Android 2.1"
ANDROID_2_2="Android 2.2"
ANDROID_2_3="Android 2.3"
ANDROID_3="Android 3"
ANDROID_4_0="Android 4.0"
ANDROID_4_1="Android 4.1"
ANDROID_4_2="Android 4.2"
ANDROID_4_3="Android 4.3"
ANDROID_4_4="Android 4.4"
ANDROID_5_0="Android 5.0"
ANDROID_6_0="Android 6.0"
WINDOWS_PHONE_7="Windows Phone 7"
WINDOWS_PHONE_8="Windows Phone 8"
WINDOWS_PHONE_8_1="Windows Phone 8.1"
BLACKBERRY_OS_1_0="BlackBerry OS 1.0"
BLACKBERRY_OS_3_6="BlackBerry OS 3.6"
BLACKBERRY_OS_4_5="BlackBerry OS 4.5"
BLACKBERRY_OS_4_6="BlackBerry OS 4.6"
BLACKBERRY_OS_5_0="BlackBerry OS 5.0"
BLACKBERRY_OS_6_0="BlackBerry OS 6.0"
BLACKBERRY_OS_7_0="BlackBerry OS 7.0"
BLACKBERRY_OS_7_1="BlackBerry OS 7.1"
BLACKBERRY_OS_10_0="BlackBerry OS 10.0"
BLACKBERRY_OS_10_1="BlackBerry OS 10.1"
BLACKBERRY_OS_10_2="BlackBerry OS 10.2"
BLACKBERRY_OS_10_3="BlackBerry OS 10.3"
SYMBIAN_OS_6_0="Symbian OS 6.0"
SYMBIAN_OS_6_1="Symbian OS 6.1"
SYMBIAN_OS_7_0="Symbian OS 7.0"
SYMBIAN_OS_8_0="Symbian OS 8.0"
SYMBIAN_OS_8_1="Symbian OS 8.1"
SYMBIAN_OS_9_1="Symbian OS 9.1"
SYMBIAN_OS_9_2="Symbian OS 9.2"
SYMBIAN_OS_9_3="Symbian OS 9.3"
SYMBIAN_OS_9_4="Symbian OS 9.4"
SYMBIAN_OS_9_5="Symbian OS 9.5"
SYMBIAN_OS_10_1="Symbian OS 10.1"

#equivalence
LIST_SUNOS={"sunos 5.0":SOLARIS_2_0, "sunos 5.1":SOLARIS_2_1, "sunos 5.2":SOLARIS_2_2, "sunos 5.3":SOLARIS_2_3, "sunos 5.4":SOLARIS_2_4,
            "sunos 5.5":SOLARIS_2_5, "sunos 5.5.1":SOLARIS_2_5_1, "sunos 5.6":SOLARIS_2_6, "sunos 5.7":SOLARIS_7, "sunos 5.8":SOLARIS_8, "sunos 5.9":SOLARIS_9 ,
            "sunos 5.10":SOLARIS_10, "sunos 5.11":SOLARIS_11}

OS_DESKTOP_INDEXES = {MS_DOS:6, WINDOWS_NT:7, WINDOWS_95:8, WINDOWS_98:9, WINDOWS_2000:10,
                      WINDOWS_XP:11, WINDOWS_VISTA:12, WINDOWS_7:13, WINDOWS_8:14,WINDOWS_10:15,
                      MAC_OS_X_10_0:16, MAC_OS_X_10_1:17, MAC_OS_X_10_2:18, MAC_OS_X_10_3:19, MAC_OS_X_10_4:20,
                      MAC_OS_X_10_5:21, MAC_OS_X_10_6:22, MAC_OS_X_10_7:23, MAC_OS_X_10_8:24, MAC_OS_X_10_9:25,
                      MAC_OS_X_10_10:26, MAC_OS_X_10_11:27, SOLARIS_2_0:28, SOLARIS_2_1:29, SOLARIS_2_2:30,
                      SOLARIS_2_3:31, SOLARIS_2_4:32, SOLARIS_2_5:33, SOLARIS_2_5_1:34, SOLARIS_2_6:35,
                      SOLARIS_7:36, SOLARIS_8:37, SOLARIS_9:38, SOLARIS_10:39, SOLARIS_11:40,
                      LINUX:41}

OS_MOBILE_INDEXES = {IPHONE_OS_1_0:6, IPHONE_OS_1_1:7, IPHONE_OS_1_1_1:8, IPHONE_OS_2_0:9, IPHONE_OS_2_1:10,
                      IPHONE_OS_2_2:11, IPHONE_OS_3_0:12, IPHONE_OS_3_1:13, IPHONE_OS_3_2:14, IPHONE_OS_4:15,
                      IPHONE_OS_4_1:16, IPHONE_OS_4_2:17, IPHONE_OS_4_2_10:18, IPHONE_OS_4_3:19, IPHONE_OS_5_0:20,
                      IPHONE_OS_5_1:21, IPHONE_OS_6:22, IPHONE_OS_7:23, IPHONE_OS_8:24, IPHONE_OS_9:25,
                      ANDROID_1_0:26, ANDROID_1_1:27, ANDROID_1_5:28, ANDROID_1_6:29, ANDROID_2_0:30, ANDROID_2_1:30,
                      ANDROID_2_2:31, ANDROID_2_3:32, ANDROID_3:33, ANDROID_4_0:34, ANDROID_4_1:35,
                      ANDROID_4_2:36, ANDROID_4_3:37, ANDROID_4_4:38, ANDROID_5_0:39, ANDROID_6_0:40,
                      WINDOWS_PHONE_7:41, WINDOWS_PHONE_8:42, WINDOWS_PHONE_8_1:43, BLACKBERRY_OS_1_0:44, BLACKBERRY_OS_3_6:45,
                      BLACKBERRY_OS_4_5:46, BLACKBERRY_OS_4_6:47, BLACKBERRY_OS_5_0:48, BLACKBERRY_OS_6_0:49, BLACKBERRY_OS_7_0:50,
                      BLACKBERRY_OS_7_1:51, BLACKBERRY_OS_10_0:52, BLACKBERRY_OS_10_1:53, BLACKBERRY_OS_10_2:54, BLACKBERRY_OS_10_3:55,
                      SYMBIAN_OS_6_0:56, SYMBIAN_OS_6_1:57, SYMBIAN_OS_7_0:58, SYMBIAN_OS_8_0:59, SYMBIAN_OS_8_1:60,
                      SYMBIAN_OS_9_1:61, SYMBIAN_OS_9_2:62, SYMBIAN_OS_9_3:63, SYMBIAN_OS_9_4:64, SYMBIAN_OS_9_5:65,
                      SYMBIAN_OS_10_1:66}
