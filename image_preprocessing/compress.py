#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 19:38:00 2017

@author: wangmengxi
"""

#coding:utf-8
from PIL import Image  
import os


def compressImage(srcPath,dstPath):  
    for filename in os.listdir(srcPath):  
        if not os.path.exists(dstPath):
                os.makedirs(dstPath)        

        srcFile=os.path.join(srcPath,filename)
        dstFile=os.path.join(dstPath,filename)
        print srcFile
        print dstFile

        if os.path.isfile(srcFile):     
            sImg=Image.open(srcFile)  
            w,h=sImg.size  
            print w,h
            dImg=sImg.resize((w/5,h/5),Image.ANTIALIAS) 
            dImg.save(dstFile) 
            print dstFile+" compressed succeeded"

        if os.path.isdir(srcFile):
            compressImage(srcFile,dstFile)

if __name__=='__main__':  
    compressImage("/Users/wangmengxi/Desktop/arthur","/Users/wangmengxi/Desktop/arthur-compressed")
