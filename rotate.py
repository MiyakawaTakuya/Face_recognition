# -*- coding: utf-8 -*-
import cv2
#import numpy as np

try:
  capture = cv2.VideoCapture(1) #カメラ指定 
  width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
  height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
  center = (width//2, height//2)
  degree = 0.0

  
  while(True):
     ret, frame = capture.read()
     if ret == False:
         print('カメラから映像を取得できんかったよー')
         break
     affin_trans = cv2.getRotationMatrix2D(center, degree, 1.0)
     dst = cv2.warpAffine(frame, affin_trans, (width, height))
     degree += 1.0
     
     cv2.imshow('MacbookPro Camera',dst)  #新しいウィンドウを開き画像を映し出す
     if cv2.waitKey(1) & 0xFF == ord('q'):
         break
     
  capture.release()
  cv2.destroyAllWindows()
except:
    import sys
    print("ERROR:", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))