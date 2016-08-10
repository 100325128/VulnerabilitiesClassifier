#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os.path
import shutil
import OSTypes

CONST_PATH_OUTPUT="output"
CONST_PATH_INPUT="input"
CONST_PATH_OS_DESKTOP=CONST_PATH_OUTPUT + "/desktop.csv"
CONST_PATH_OS_MOBILE=CONST_PATH_OUTPUT + "/mobile.csv"
CONST_PATH_APPLICATION=CONST_PATH_OUTPUT + "/application.csv"
CONST_PATH_OTHER=CONST_PATH_OUTPUT + "/noClassify.csv"
CONST_PATH_VULN_STATUS=CONST_PATH_INPUT + "/allitems.txt"

class FileManager() :
    fileDesktop = ""
    fileMobile = ""
    fileApp = ""
    fileNC = ""
    candidateList = []

    def createOutputFiles(self) :
        messageError = ""
        if (not os.path.exists(CONST_PATH_OUTPUT)) :
           os.mkdir(CONST_PATH_OUTPUT)
        messageError = self.setCandidateVulnerabilities()
        if (messageError == "") :
           try:
              self.fileDesktop = open(CONST_PATH_OS_DESKTOP,"w")
              self.fileDesktop.write(self.createHeaderDesktop())
              self.fileDesktop.close()
              self.fileDesktop = open(CONST_PATH_OS_DESKTOP,"a")
           except IOError :
              messageError = "Error al crear el fichero " + CONST_PATH_OS_DESKTOP
        if (messageError == "") :
           try:
               self.fileMobile = open(CONST_PATH_OS_MOBILE,"w")
               self.fileMobile.write(self.createHeaderMobile())
               self.fileMobile.close()
               self.fileMobile = open(CONST_PATH_OS_MOBILE,"a")
           except IOError :
               messageError = "Error al crear el fichero " + CONST_PATH_OS_MOBILE
        if (messageError == "") :
           try:
               self.fileApp = open(CONST_PATH_APPLICATION,"w")
               self.fileApp.write(self.createHeaderApplication())
               self.fileApp.close()
               self.fileApp = open(CONST_PATH_APPLICATION,"a")
           except IOError :
               messageError = "Error al crear el fichero " + CONST_PATH_APPLICATION
        if (messageError == "") :
           try:
               self.fileNC = open(CONST_PATH_OTHER,"w")
               self.fileNC.write(self.createHeaderNoClassify())
               self.fileNC.close()
               self.fileNC = open(CONST_PATH_OTHER,"a")
           except IOError :
               messageError = "Error al crear el fichero " + CONST_PATH_OTHER
        return messageError

    def closeOutputFiles(self) :
        self.fileDesktop.close()
        self.fileMobile.close()
        self.fileApp.close()
        self.fileNC.close()

    def createHeaderDesktop(self) :
        a = "Descripcion;TIPO VULNERABILIDAD;Revisar;Subcategoria;ESTADO;OTROS SO;"
        b = "MS-DOS;Windows NT;Windows 95;Windows 98;Windows 2000;"
        c = "Windows XP;Windows Vista;Windows 7;Windows 8;Windows 10;"
        d = "Mac OS X 10.0;Mac OS X 10.1;Mac OS X 10.2;Mac OS X 10.3;Mac OS X 10.4;"
        e = "Mac OS X 10.5;Mac OS X 10.6;Mac OS X 10.7;Mac OS X 10.8;Mac OS X 10.9;"
        f = "Mac OS X 10.10;Mac OS X 10.11;Solaris 2.0;Solaris 2.1;Solaris 2.2;"
        g = "Solaris 2.3;Solaris 2.4;Solaris 2.5;Solaris 2.5.1;Solaris 2.6;"
        h = "Solaris 7;Solaris 8;Solaris 9;Solaris 10;Solaris 11;"
        i = "Linux\n"
        return a + b + c + d + e + f + g + h + i

    def writeDesktop(self, cve_id, cve_vulnerability, vulnerable_desktop_list) :
        if (len(vulnerable_desktop_list) != 0) :
           maxColumns = 42
           auxList = [""] * maxColumns
           auxList[0:6] = [cve_id,cve_vulnerability,"","","",""]
           for OS in vulnerable_desktop_list :
               index = OSTypes.OS_DESKTOP_INDEXES[OS]
               #marcamos el SO afectado
               auxList[index] = "1"
           line = auxList[0]
           for i in range(1,maxColumns) :
               line = line + ";" + auxList[i]
           line = line + "\n"
           self.fileDesktop.write(line)

    def writeDesktopDefault(self, cve_id, cve_vulnerability) :
        maxColumns = 42
        auxList = [""] * maxColumns
        auxList[0:6] = [cve_id,cve_vulnerability,"NO HAY INFO SO","","",""]
        line = auxList[0]
        for i in range(1,maxColumns) :
            line = line + ";" + auxList[i]
        line = line + "\n"
        self.fileDesktop.write(line)


    def createHeaderMobile(self) :
        a = "Descripcion;TIPO VULNERABILIDAD;Revisar;Subcategoria;ESTADO;OTROS SO;"
        b = "iphone OS 1.0;iphone OS 1.1;iphone OS 1.1.1;iphone OS 2.0;iphone OS 2.1;"
        c = "iphone OS 2.2;iphone OS 3.0;iphone OS 3.1;iphone OS 3.2;iphone OS 4;"
        d = "iphone OS 4.1;iphone OS 4.2;iphone OS  4.2.10;iphone OS 4.3;iphone OS 5.0;"
        e = "iphone OS 5.1;iphone OS 6;iphone OS 7;iphone OS 8;iphone OS 9;"
        f = "Android 1.0;Android 1.1;Android 1.5;Android 1.6;Android 2.0/2.1;"
        g = "Android 2.2.x;Android 2.3.x;Android 3.x;Android 4.0.x;Android 4.1;"
        h = "Android 4.2;Android 4.3;Android 4.4;Android 5.0;Android 6.0;"
        i = "Windows Phone 7;Windows Phone 8;Windows Phone 8.1;BlackBerry 1.0;BlackBerry 3.6;"
        j = "BlackBerry 4.5;BlackBerry 4.6;BlackBerry 5.0;BlackBerry 6.0;BlackBerry 7.0;"
        k = "BlackBerry 7.1;BlackBerry 10.0;BlackBerry 10.1;BlackBerry 10.2;BlackBerry 10.3;"
        l = "Symbian 6.0;Symbian 6.1;Symbian 7.0;Symbian 8.0;Symbian 8.1;"
        m = "Symbian 9.1;Symbian 9.2;Symbian 9.3;Symbian 9.4;Symbian 9.5;"
        n = "Symbian 10.1\n"
        return a + b + c + d + e + f + g + h + i + j + k + l + m + n

    def writeMobile(self, cve_id, cve_vulnerability, vulnerable_mobile_list) :
        if (len(vulnerable_mobile_list) != 0) :
           maxColumns = 67
           auxList = [""] * maxColumns
           auxList[0:6] = [cve_id,cve_vulnerability,"","","",""]
           for OS in vulnerable_mobile_list :
               index = OSTypes.OS_MOBILE_INDEXES[OS]
               auxList[index] = "1"
           line = auxList[0]
           for i in range(1,maxColumns) :
               line = line + ";" + auxList[i]
           line = line + "\n"
           self.fileMobile.write(line)

    def createHeaderApplication(self) :
        return "Descripcion;TIPO VULNERABILIDAD;Revisar;Estado;Otros SO;Fabricante;Aplicación;Comentarios\n"

    def writeApplication(self, cve_id, cve_vulnerability, vulnerable_ap_list) :
        if (len(vulnerable_ap_list) != 0) :
           for vuln in vulnerable_ap_list :
               line = cve_id + ";" + cve_vulnerability + ";;;;" + vuln[0] + ";" + vuln[1] + "\n"
               self.fileApp.write(line)

    def createHeaderNoClassify(self) :
        return "Descripcion;TIPO VULNERABILIDAD;Operating System\n"

    def writeNoClassify(self, cve_id, cve_vulnerability, vulnerable_nc_list) :
        if (len(vulnerable_nc_list) != 0) :
           for vuln in vulnerable_nc_list :
               line = cve_id + ";" + cve_vulnerability + ";" + vuln + "\n"
               self.fileNC.write(line)

    def setCandidateVulnerabilities(self) :
        self.candidateList = []
        messageError = ""
        try:
           fileAllItems = open(CONST_PATH_VULN_STATUS,"r")
           nombre = ""
           note = False
           third = False
           party = False
           infor = False
           for line in fileAllItems:
               if("Name:" in line) :
                  nombre = line[6:len(line)-1]
                  note = False
                  third = False
                  party = False
                  infor = False
               if("Status: Candidate" in line) :
                  if("cve-1999" in nombre.lower() or "cve-2000" in nombre.lower() or "cve-2001" in nombre.lower() or "cve-2002" in nombre.lower()  or "cve-2003" in nombre.lower()  or "cve-2004" in nombre.lower()):
                     self.candidateList.append(nombre)
               if("** RESERVED **" in line or "** REJECT **" in line or "** DISPUTED **" in line) :
                  self.candidateList.append(nombre)
               if("NOTE:" in line) :
                  note = True
               if("third" in line) :
                  third = True
               if("party" in line) :
                  party = True
               if("information" in line):
                  infor = True
               if(note and third and party and infor) :
                  self.candidateList.append(nombre)
                  note = False
                  third = False
                  party = False
                  infor = False


           fileAllItems.close()
        except IOError :
           messageError = "Error al leer el fichero " + CONST_PATH_VULN_STATUS
        return messageError

    def isCandidate(self, cve) :
        return (cve in self.candidateList)