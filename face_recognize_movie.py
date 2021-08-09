#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 23:40:05 2021

@author: miyagawatakuya
"""

import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('./data/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('./data/haarcascade_eye.xml')

cap = cv2.VideoCapture(1) 

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    cv2.imshow("face_recognize",frame)

    k =  cv2.waitKey(1) & 0xFF # キー操作取得。64ビットマシンの場合,& 0xFFが必要
    prop_val = cv2.getWindowProperty("frame", cv2.WND_PROP_ASPECT_RATIO) # ウィンドウが閉じられたかを検知する用

# qが押されるか、ウィンドウが閉じられたら終了
    if k == ord("q") or (prop_val < 0):
        break

cap.release()
cv2.destroyAllWindows()