# -*- coding: utf-8 -*-
import numpy as np
import cv2


img = cv2.imread("/Users/miyagawatakuya/.spyder-py3/OpenCV_Test/img/staba.JPEG")
# 油絵エフェクトパラメータ
# size, dynRatio
prms = [(10,1), (5, 1), (5,4), (3,10), (2,5)]

for (size, dynRatio) in prms:
    # 油絵エフェクト
    dst = cv2.xphoto.oilPainting(img, size, dynRatio, cv2.COLOR_BGR2Lab)
    # 結果を出力
    cv2.imshow("oil painting effect" % (size,dynRatio) , dst)
    cv2.imwrite("/Users/miyagawatakuya/.spyder-py3/OpenCV_Test/output/staba.jpg", dst)
    cv2.waitKey()
    cv2.destroyAllWindows()



#try:
  #capture = cv2.VideoCapture(0) #カメラ指定 1が内蔵インカメラの引数
  #while(True):
     #ret, frame = capture.read()
     #if ret == False:
     #    print('カメラから映像を取得できんかったよー')
     #    break
     
     #dst_resize = cv2.resize(gray,dsize=None, fx=0.7 , fy=0.7)     
     #cv2.imshow('My MacbookPro Camera',dst_resize)  #新しいウィンドウを開き画像を映し出す
     #if cv2.waitKey(1) & 0xFF == ord('q'):
     #    break 
  #capture.release()
  #cv2.destroyAllWindows()
 
#except:
#    import sys
#    print("ERROR:", sys.exc_info()[0])
#    print(sys.exc_info()[1])
#    import traceback
#    print(traceback.format_tb(sys.exc_info()[2]))