# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import cv2

try:
 capture = cv2.VideoCapture(0)#カメラ指定
 width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
 height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)

 print('frame size =' + str(width) + ' x ' + str(height))
 
except:
    import sys
    print("ERROR:", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))