# -*- coding: utf-8 -*-

import cv2
import numpy as np
import pafy

try:
  url = 'https://www.youtube.com/watch?v=WlzQuiqIIV4' #丸の内 東京駅前
  vPafy = pafy.new(url)
  play = vPafy.getbest(preftype="webm")

  #start the video
  capture = cv2.VideoCapture(1) #カメラ指定 1が内蔵インカメラの引数
  print(capture.get(cv2.CAP_PROP_FPS))
  print(capture.get(cv2.CAP_PROP_FRAME_COUNT))
  
  while(True):
     ret, frame = capture.read(play.url)
     if ret == False:
         print('カメラから映像を取得できんかったよー')
         break
     
     cv2.imshow('My MacbookPro Camera',frame)  #新しいウィンドウを開き画像を映し出す
        
     if cv2.waitKey(1) & 0xFF == ord('q'):
         break
     
  capture.release()
  cv2.destroyAllWindows()
  
        
 #width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
 #height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
 #print('frame size =' + str(width) + ' x ' + str(height))
 
except:
    import sys
    print("ERROR:", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))