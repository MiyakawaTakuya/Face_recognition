# -*- coding: utf-8 -*-
# OpenCVのインポート
import cv2
import numpy as np
from PIL import Image

# カメラの解像度設定
WIDTH = 1920
HEIGHT = 1080

# 読み込みする画像の指定
img = "img/sekimaru.jpg"
cv2_img = cv2.imread(img, cv2.IMREAD_UNCHANGED)

#顔認識モデルの指定
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')

# 引数でカメラを選べれる。
cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)

def overlayImage(src, overlay, location, size):
    overlay_height, overlay_width = overlay.shape[:2]

    # webカメラの画像をPIL形式に変換
    src = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
    pil_src = Image.fromarray(src)
    pil_src = pil_src.convert('RGBA')

    # 合成したい画像をPIL形式に変換
    overlay = cv2.cvtColor(overlay, cv2.COLOR_BGRA2RGBA)
    pil_overlay = Image.fromarray(overlay)
    pil_overlay = pil_overlay.convert('RGBA')
    #顏の大きさに合わせてリサイズ
    pil_overlay = pil_overlay.resize(size)

    # 画像を合成
    pil_tmp = Image.new('RGBA', pil_src.size, (255, 255, 255, 0))
    pil_tmp.paste(pil_overlay, location, pil_overlay)
    result_image = Image.alpha_composite(pil_src, pil_tmp)

    # OpenCV形式に変換
    return cv2.cvtColor(np.asarray(result_image), cv2.COLOR_RGBA2BGRA)


def main():
    # 顔認識の左上角の座標を格納する変数
    x = 0
    y = 0

    # 顔の幅と高さを格納する変数
    w = 0
    h = 0
    while True:
        # VideoCaptureから1フレーム読み込む
        ret, frame = cap.read()

        #フレームをグレー形式に変換し、顔認識
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face = face_cascade.detectMultiScale(gray, 1.3, 5)

        # 顔が認識されていればx, y, w, hを更新
        if face != ():
            (x, y, w, h) = face[0]

        # 変数が初期値以外ならフレームに画像を合成
        if w != 0:
            frame = overlayImage(frame, cv2_img, (x, y), (w, h))


        # 加工したフレームを表示する
        cv2.imshow('Frame', frame)

        # キー入力を1ms待って、ESCを押されたらBreakする
        k = cv2.waitKey(1)
        if k == 27:
            break

    # キャプチャをリリースして、ウィンドウを閉じる
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()