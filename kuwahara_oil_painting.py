# -*- coding: utf-8 -*-
import numpy as np
import cv2

class KuwaharaFilter:
    def __init__(self, kernelsize):
        # kernelsizeは5以上でかつ奇数であること。
        self.kernelsize = kernelsize

        # カーネル生成
        kimg = np.zeros((kernelsize, kernelsize), dtype=np.float32)
        length = (kernelsize-1)//2+1
        kimg[0:length, 0:length] = 1.0 / (length * length)
        self.kernel = np.empty((4,kernelsize,kernelsize), dtype=np.float32)
        self.kernel[0] = kimg                       # 左上 (a)
        self.kernel[1] = np.fliplr(kimg)            # 右上 (b) 上下反転
        self.kernel[2] = np.flipud(kimg)            # 左下 (c)
        self.kernel[3] = np.fliplr(self.kernel[2])  # 右下 (d) 上下反転


    # カラー画像のフィルタリング
    def filter(self, inimage):
        filtered_b = self.filterSingle(inimage[:,:,0])
        filtered_g = self.filterSingle(inimage[:,:,1])
        filtered_r = self.filterSingle(inimage[:,:,2])
        filtered = cv2.merge((filtered_b,filtered_g,filtered_r))
        return filtered

    # グレイスケール画像のフィルタリング
    def filterSingle(self, grayscale):
        fimage = grayscale.astype(np.float32)

        # ピクセル輝度二乗画像の生成
        squaredImg = fimage**2

        means = [None, None, None, None]
        sd = means.copy()

        # 計算
        for i in range(0,4):
            # カーネルの平均値画像
            means[i] = cv2.filter2D(fimage, -1, self.kernel[i]) 
            # カーネルのピクセル輝度二乗画像の平均画像
            sd[i] = cv2.filter2D(squaredImg, -1, self.kernel[i])    
            sd[i] = sd[i]-means[i]**2

        # 標準偏差の最小値インデックス配列を取得
        lo_sd_index = np.argmin(sd,0)

        # 結果画像を計算
        filtered = np.zeros(grayscale.shape, dtype=np.float32)
        height, width = grayscale.shape[:4]
        for y in range(0,height):
            for x in range(0,width):
                filtered[y,x] = means[lo_sd_index[y,x]][y,x]
        return filtered.astype(np.uint8)

#画像読込
#pic_image=cv2.imread('/Users/miyagawatakuya/.spyder-py3/OpenCV_Test/img/park.HEIC', cv2.IMREAD_COLOR)
#pic_image=cv2.imread('/Users/miyagawatakuya/.spyder-py3/OpenCV_Test/img/shibuya.PNG', cv2.IMREAD_COLOR)
pic_image=cv2.imread('/Users/miyagawatakuya/.spyder-py3/OpenCV_Test/img/staba.JPEG', cv2.IMREAD_COLOR)

# 桑原フィルタ  
kf = KuwaharaFilter(42)  #kfの値が60近くなってくると荒目すぎて油絵感を通り過ぎてしまう
filtered = kf.filter(pic_image)

cv2.imshow("Kuwahara filtered", filtered)
cv2.imwrite("/Users/miyagawatakuya/.spyder-py3/OpenCV_Test/output/staba5.jpg", filtered)
cv2.waitKey(0)
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