#!/usr/bin/env python
# -*- coding: utf-8 -*-

from xml.sax.handler import ContentHandler
from xml.sax import make_parser
import sys
import OSClassify
import CommonFunctions

CONST_BUFFER_OVERFLOW="BUFFER OVERFLOW"
CONST_XSS="Cross-site scripting (XSS)"
CONST_SQL_INJECTION="SQL INJECTION"
CONST_PATH_TRAVERSAL="PATH TRAVERSAL"
CONST_DOS="DoS VULNERABILITY"
CONST_INTEGER_OVERFLOW="INTEGER OVERFLOW"
CONST_HTTP_RESPONSE_SPLITTING="HTTP RESPONSE SPLITTING"
CONST_CSRF="CSRF"
CONST_FORMAT_STRING="FORMAT STRING VULNERABILITY"
CONST_USE_AFTER_FREE="USE AFTER FREE VULNERABILITY"
CONST_INTEGER_UNDERFLOW="INTEGER UNDERFLOW"
CONST_ARRAY_INDEX_ERROR="ARRAY INDEX ERROR"
CONST_UNRESTRICTED_FILE_UPLOAD="UNRESTRICTED FILE UPLOAD"
CONST_OPEN_REDIRECTION="OPEN REDIRECTION"

#XML labels
CONST_ENTRY="entry"
CONST_NVD="nvd"
CONST_CVE_ID="vuln:cve-id"
CONST_SUMMARY="vuln:summary"
CONST_PRODUCT="vuln:product"
CONST_CVSS="cvss:score"

#This class process and read the XML file
class VulnerabilitiesHandler(ContentHandler):
    #vulnerability identifier
    cve_id=""
    #vulnerability type
    cve_vulnerability=""
    #vulnerability cvss
    cve_cvss=""
    #vulnerability description
    summary=""
    content=""
    #product that is affected by the vulnerability
    product=""
    #List of Operating Systems affected by the vulnerability 
    #(Only considers these Operating Systems that are included in the OSTypes.py file)
    vulnerable_desktop_list=[]
    #List of Mobile Operating Systems affected by the vulnerability
    #(Only considers these Operating Systems that are included in the OSTypes.py file)
    vulnerable_mobile_list=[]
    #List of Operating Systems that do not match the two above categories
    vulnerable_nc_list=[]
    #Application tuples (Vendor, Product) affected by the vulnerability
    vulnerable_ap_list=[]
    #Raw description of HW affected by the vulnerability
    vulnerable_hw_list=[]
    processText=False
    fileManager = ""

    def startElement(self, name, attrs):
        if (name == CONST_ENTRY) :
            self.cve_id = ""
            self.cve_vulnerability=""
            self.cvss = ""
            self.summary = ""
            self.content = ""
            self.product = ""
            self.vulnerable_desktop_list=[]
            self.vulnerable_mobile_list=[]
            self.vulnerable_nc_list=[]
            self.vulnerable_ap_list=[]
            self.vulnerable_hw_list=[]
            self.processText=False
        if (name == CONST_CVE_ID or name == CONST_SUMMARY or name == CONST_PRODUCT or name == CONST_CVSS) :
            self.processText=True

    def endElement(self,name):
        if (name == CONST_NVD) :
            self.fileManager.closeOutputFiles()

        if (name == CONST_ENTRY) :
            if(not self.fileManager.isCandidate(self.cve_id)) :            
                self.fileManager.writeNoClassify(self.cve_id, self.cve_vulnerability, self.vulnerable_nc_list, self.cve_cvss)
                self.fileManager.writeApplication(self.cve_id, self.cve_vulnerability, self.vulnerable_ap_list, self.cve_cvss)
                self.fileManager.writeDesktop(self.cve_id, self.cve_vulnerability, self.vulnerable_desktop_list, self.cve_cvss)
                self.fileManager.writeMobile(self.cve_id, self.cve_vulnerability, self.vulnerable_mobile_list, self.cve_cvss)
                if (len(self.vulnerable_nc_list) == 0 and len(self.vulnerable_ap_list) == 0 and
                    len(self.vulnerable_desktop_list) == 0 and len(self.vulnerable_mobile_list) == 0 and
                    len(self.vulnerable_hw_list) == 0) :
                    self.fileManager.writeDesktopDefault(self.cve_id, self.cve_vulnerability, self.cve_cvss)

        if (name == CONST_CVE_ID) :
            #save the value of the vulnerability
            self.cve_id = self.content;

        if(name == CONST_CVSS) :
            self.cve_cvss = self.content;

        if (name == CONST_PRODUCT) :
            #save the product information
            self.product = self.content
            #classify product
            isOS,isAP,isHW,infoProduct = CommonFunctions.classifyProduct(self.product)
            if (isAP) :
               #product is an application
               tuplaAplication = CommonFunctions.processApplication(infoProduct)
               self.vulnerable_ap_list = CommonFunctions.addToVulnerableList(self.vulnerable_ap_list,tuplaAplication)
            if (isHW) :
               #product is a piece of hardware
               self.vulnerable_hw_list = CommonFunctions.addToVulnerableList(self.vulnerable_hw_list,infoProduct)
            if (isOS) :
               #product is an Operating System
               infoProduct = OSClassify.getOSInformation(infoProduct)
               isOSDesktop, isOSMobile, infoProduct = OSClassify.transformOSInformation(infoProduct)
               if (isOSDesktop) :
                  self.vulnerable_desktop_list = CommonFunctions.addToVulnerableList(self.vulnerable_desktop_list,infoProduct)
               else :
                  if (isOSMobile) :
                     self.vulnerable_mobile_list = CommonFunctions.addToVulnerableList(self.vulnerable_mobile_list,infoProduct)
                  else :
                     self.vulnerable_nc_list = CommonFunctions.addToVulnerableList(self.vulnerable_nc_list,infoProduct)

        if (name == CONST_SUMMARY) :
            #save the vulnerability description
            self.summary = self.content;

            #find the type of vulnerability
            if (CONST_BUFFER_OVERFLOW.lower() in self.summary.lower()) :
               self.cve_vulnerability=CONST_BUFFER_OVERFLOW
            elif (self.isXSS(self.summary.lower())) :
               self.cve_vulnerability=CONST_XSS
            elif (CONST_SQL_INJECTION.lower() in self.summary.lower()) :
               self.cve_vulnerability=CONST_SQL_INJECTION
            elif (self.isDotDotAttack(self.summary.lower())) :
               self.cve_vulnerability=CONST_PATH_TRAVERSAL
            elif (self.isDirectoryTraversal(self.summary.lower())) :
               self.cve_vulnerability=CONST_PATH_TRAVERSAL
            elif (self.isIntegerOverflow(self.summary.lower())) :
               self.cve_vulnerability=CONST_INTEGER_OVERFLOW
            elif (self.isHttpResponseSplitting(self.summary.lower())) :
               self.cve_vulnerability=CONST_HTTP_RESPONSE_SPLITTING
            elif (self.isCSRF(self.summary.lower())) :
               self.cve_vulnerability=CONST_CSRF
            elif (self.isFormatString(self.summary.lower())) :
               self.cve_vulnerability=CONST_FORMAT_STRING
            elif (self.isUseAfterFree(self.summary.lower())) :
               self.cve_vulnerability=CONST_USE_AFTER_FREE
            elif (self.isIntegerUnderflow(self.summary.lower())) :
               self.cve_vulnerability=CONST_INTEGER_UNDERFLOW
            elif (self.isArrayIndexError(self.summary.lower())) :
               self.cve_vulnerability=CONST_ARRAY_INDEX_ERROR
            elif (self.isOpenRedirection(self.summary.lower())) :
               self.cve_vulnerability=CONST_OPEN_REDIRECTION
            elif (self.isUnrestrictedFileUpload(self.summary.lower())) :
               self.cve_vulnerability=CONST_UNRESTRICTED_FILE_UPLOAD
            elif (self.isDoS(self.summary.lower())) :
               self.cve_vulnerability=CONST_DOS

        self.content = ""
        self.processText=False

    def characters(self, ch) :
        if self.processText :
            self.content += ch

    def setFileManager(self, fileManagerParam) :
        self.fileManager = fileManagerParam

    def isArrayIndexError(self, vuln):
        return "array index vulnerability" in vuln.lower()

    def isCSRF(self, vuln):
        return "cross-site request forgery (csrf)" in vuln.lower()

    def isDirectoryTraversal(self, vuln):
        return "directory traversal vulnerability" in vuln.lower() or "multiple directory traversal vulnerabilities" in vuln.lower() or "path traversal vulnerability" in vuln.lower()

    def isDoS(self, vuln):
        return ("allows remote attackers to cause a denial of service" in vuln.lower() or 
                "allow remote attackers to cause a denial of service" in vuln.lower() or 
                "allows attackers to cause a denial of service" in vuln.lower() or 
                "allows local users to cause a denial of service" in vuln.lower() or 
                "allows remote authenticated users to cause a denial of service" in vuln.lower())

    def isDotDotAttack(self, vuln):
        return "directory traversal vulnerability" in vuln.lower()

    def isFormatString(self, vuln):
        return "format string vulnerability" in vuln.lower()

    def isHttpResponseSplitting(self, vuln):
        return "http response splitting vulnerability" in vuln.lower()

    def isIntegerOverflow(self, vuln):
        return "multiple integer overflows" in vuln.lower() or "integer overflow" in vuln.lower()

    def isIntegerUnderflow(self, vuln):
        return "integer underflow" in vuln.lower()

    def isOpenRedirection(self, vuln):
        return "open redirect vulnerability" in vuln.lower()

    def isUnrestrictedFileUpload(self, vuln):
        return "unrestricted file upload vulnerability" in vuln.lower() or "multiple unrestricted file upload vulnerabilities" in vuln.lower()

    def isUseAfterFree(self, vuln):
        return "use-after-free vulnerability" in vuln.lower()

    def isXSS(self, vuln):
        return "cross-site scripting (xss)" in vuln.lower() or "cross-site scripting (css)" in vuln.lower()

