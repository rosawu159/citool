#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import time

# your project path 
workspaceName="/Users/switchvmiworld/Programs/appium/Brahma_iOS_Client/Brahma.xcworkspace"
# input project scheme
# e.g. workspce 
# xcodebuild -list -workspace Brahma_iOS_Client/Brahma.xcworkspace/
# e.g. project
# xcodebuild -list -project Brahma_iOS_Client/Brahma.xcodeproj/
schemeName="Brahma"

# get Date 
dateTime=time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())

# get your path 
workspaceDirPath=os.getcwd()

#output folder
#get your desktop path  or  
desktopPath=os.path.join(os.path.expanduser("~"), 'Desktop')
desktopPath2=os.path.expanduser("~/Desktop")

#make folder
basePath=desktopPath+"/App"+dateTime

#build archive in folder
archivePath=basePath+"/archive"
if os.path.exists(archivePath)==False:
    os.makedirs(archivePath)

#input your ios sdk
#if you don't know, you can check your phone or xocde 
sdkName="iphoneos11.4" 
#can use [Debug|Release]
configurationName="Debug" 

#BaseCommand
baseCommand=" -workspace "+workspaceName+" -scheme "+schemeName+" -configuration "+configurationName+" -sdk "+sdkName

#clean
xcodebuild_clean="xcodebuild clean"+baseCommand

#check all targets，schemes和configurations
xcodebuild_list="xcodebuild -list"

#compiler
xcodebuild_build="xcodebuild build"+baseCommand

#check your sdk
xcodebuild_showsdks="xcodebuild -showsdks"

#archivePath parames
archivePathOption=" -archivePath "+archivePath+"/"+schemeName

#make archive 
xcodebuild_archive="xcodebuild archive"+archivePathOption+baseCommand

os.system(xcodebuild_clean)
os.system(xcodebuild_archive)


print "folder: "
print archivePath +"/"+ schemeName + ".xcarchive/"+"Products/Applications/AppRTC.app"



