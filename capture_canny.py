# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import cv2

try:
  capture = cv2.VideoCapture(1) #カメラ指定 1が内蔵インカメラの引数
  print(capture.get(cv2.CAP_PROP_FPS))
  print(capture.get(cv2.CAP_PROP_FRAME_COUNT))
  
  while(True):
     ret, frame = capture.read()
     if ret == False:
         print('カメラから映像を取得できんかったよー')
         break
     
     #cv2.imshow('My MacbookPro Camera',frame)  #新しいウィンドウを開き画像を映し出す   
     #cv2.imshow('My MacbookPro Camera',dst)  #新しいウィンドウを開き画像を映し出す
     dst = cv2.Canny(frame,10.0, 100.0) # エフェクト：エッジのみの抽出
     dst = cv2.bitwise_not(dst)

     #cv2.imshow('My MacbookPro Camera',dst)  #新しいウィンドウを開き画像を映し出す  
     #dst = cv2.resize(dst, (width, height),
                     # interpolation = cv2.INTER_NEAREST) #挙動しなかった

     cv2.imshow('My MacbookPro Camera',dst)  #新しいウィンドウを開き画像を映し出す  
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