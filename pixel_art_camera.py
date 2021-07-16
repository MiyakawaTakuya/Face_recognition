# -*- coding: utf-8 -*-
import cv2
import numpy as np

# 減色処理
def sub_color(src, K):
    # 次元数を1落とす
    Z = src.reshape((-1,3))

    # float32型に変換
    Z = np.float32(Z)

    # 基準の定義
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

    # K-means法で減色
    ret, label, center = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    # UINT8に変換
    center = np.uint8(center)

    res = center[label.flatten()]

    # 配列の次元数と入力画像と同じに戻す
    return res.reshape((src.shape))


# モザイク処理
def mosaic(img, alpha):
    # 画像の高さ、幅、チャンネル数
    h, w, ch = img.shape

    # 縮小→拡大でモザイク加工
    img = cv2.resize(img,(int(w*alpha), int(h*alpha)))
    img = cv2.resize(img,(w, h), interpolation=cv2.INTER_NEAREST)

    return img


# ドット絵化
def pixel_art(img, alpha=2, K=9):
    # モザイク処理
    img = mosaic(img, alpha)

    # 減色処理
    return sub_color(img, K)


try:
  capture = cv2.VideoCapture(0) #カメラ指定 1が内蔵インカメラの引数  
  while(True):
     ret, frame = capture.read()
     if ret == False:
         print('カメラから映像を取得できんかったよー')
         break

     #ドット絵化 （img, alpha=小さいほど荒くなる, K=大きいほど色合いが落ちる）
     dst = pixel_art(frame, 0.1, 7)
     #cv2.imshow('pixel',dst)  #新しいウィンドウを開き画像を映し出す
     dst_resize = cv2.resize(dst,dsize=None, fx=0.7 , fy=0.7)
     cv2.imshow('pixel',dst_resize)  #新しいウィンドウを開き画像を映し出す
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