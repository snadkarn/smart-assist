# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 01:02:34 2019

@author: shrey
"""

import cv2

import numpy as np
import sys
import urllib.request
host = "100.87.31.85:8080"
if len(sys.argv)>1:
    host = sys.argv[1]

hoststr = 'http://' + host + '/video'
print( 'Streaming ' , hoststr)

stream=urllib.request.urlopen(hoststr)

bytes=''
while True:
    bytes+=stream.read(1024)
    a = bytes.find('\xff\xd8')
    b = bytes.find('\xff\xd9')
    if a!=-1 and b!=-1:
        jpg = bytes[a:b+2]
        bytes= bytes[b+2:]
        i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.CV_LOAD_IMAGE_COLOR)
        cv2.imshow(hoststr,i)
        if cv2.waitKey(1) ==27:
            exit(0)
