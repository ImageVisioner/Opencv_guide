
import cv2
import numpy as np
# 渝西图像练习生

# 海康威视 或者大华 工业相机
# poe ethercat/net SDK

# 像素 ====>图像
# 图像 ===视频  27 30

cam = cv2.VideoCapture(0) #枚举号

while True:
    ret,frame=cam.read()
    frame=cv2.flip(frame,1) #1水平镜像  -1垂直图像
    frame=cv2.medianBlur(frame,3)

    cv2.imshow('videp',frame)

    if cv2.waitKey(1) &0xFF == ord('q'):
        break
cam.release() #析构函数
cv2.destroyAllWindows()


