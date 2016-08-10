
#VulnerabilitiesClassifier: Automated Classifier of Software Vulnerabilities

About VulnerabilitiesClassifier
============

Functional Description
----------------------

VulnerabilitiesClassifier is an opensource project for classifying software vulnerabilities. This project provides a set of various scripts that can be use to automatically classify vulnerabilities taking as an input source an XML file. The returned output is a file in csv format, semicolon separated.

Technical Description
---------------------

VulnerabilitiesClassifier is made of multiple scripts that work together:

1. **OSTypes**
2. **OSClassify**
3. **FileManager** is a python script that can be use to collect results stored in the elasticsearch database.
4. **CommonFunctions**
5. **VulnerabilitiesHandler** 
6. **classifier** 

More Information
----------------

* **Email:** [100325128@alumnos.uc3m.es](100325128@alumnos.uc3m.es)

Getting Started
===============

In order to use VulnerabilitiesClassifier you need a device on which you've installed:

* python 2.7 or later

Setup input files and directories
----------------------------------

In order to perform the classification, is necessary to download two files: 

1. **CVE entries** - [https://cve.mitre.org/data/downloads/index.html] (https://cve.mitre.org/data/downloads/index.html)
  Select and download "Text Format Raw". An allitems.txt file will be download.  
2. **NVD data feeds** - [https://nvd.nist.gov/download.cfm#CVE_FEED] (https://nvd.nist.gov/download.cfm#CVE_FEED)
  Choose the year for which you want to make the classification, download it and unzip it.
3. Create a new subdirectory named "input" in the directory in which all the scripts of this project have been cloned. Then put into "input" subdirectory, the allitems.txt file.

Run the classifier
----------------------------------

Python classifier script is in repository directory:

    > python classifier nvdcve-2.0-YYYY.xml

Expected results
----------------------------------

Contributing
============

I would be delighted if you could help me to improve this work.
Please use github features to provide your bugfixes and improvements.
