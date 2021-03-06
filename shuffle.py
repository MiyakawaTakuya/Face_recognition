# -*- coding: utf-8 -*-

import cv2
import numpy as np


try:
  capture = cv2.VideoCapture(0) #カメラ指定 1が内蔵インカメラの引数
  height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
  width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
  roi_target = [0,1,2,3]
  counter = 12
  
  while(True):
     ret, frame = capture.read()
     if ret == False:
         print('カメラから映像を取得できんかったよー')
         break
     

     dst = np.zeros((height,width,3), np.uint8)
     
     y1 = [0, height//2,height//2, 0]
     y2 = [height//2, height,height, height//2]
     x1 = [0, 0, width//2, width//2]
     x2 = [width//2, width//2, width, width]

     for i in range(0,4):
         dst[y1[i]:y2[i], x1[i]:x2[i]] = \
                 frame[y1[roi_target[i]]:y2[roi_target[i]],
                       x1[roi_target[i]]:x2[roi_target[i]]]
                 
     counter -= 1
     if counter <= 0:
         counter = 24
         for i in range(0,4):
             roi_target[i] += 1
             if roi_target[i] == 4:
                 roi_target[i] = 0


     dst_resize = cv2.resize(dst,dsize=None, fx=0.7 , fy=0.7)     
     cv2.imshow('My MacbookPro Camera',dst_resize)  #新しいウィンドウを開き画像を映し出す  
     dst2 = cv2.Canny(frame,40.0, 500.0) # エフェクト：エッジのみの抽出
     #cv2.imshow('My MacbookPro Camera2',dst2)  #新しいウィンドウを開き画像を映し出す  
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