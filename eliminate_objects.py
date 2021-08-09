# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import cv2

try:
    img = cv2.imread('./img/eliminate_base.png')
    msk = cv2.imread('./img/mask.png', cv2.IMREAD_GRAYSCALE)
    
    if img is None or msk is None:
        print('ファイルが読み込めまへん')
        import sys
        sys.exit()
        
    dst = cv2.inpaint(img, msk, 5, cv2.INPAINT_TELEA)

    cv2.imwrite("/Users/miyagawatakuya/.spyder-py3/OpenCV_Test/output/staba_eliminate.jpg", dst)
    cv2.imshow('img', dst)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except:
   import sys
   print("Error:", sys.exc_info()[0])    
   print(sys.exc_info()[1])
   import traceback
   print(traceback.format_tb(sys.exc_info()[2]))
