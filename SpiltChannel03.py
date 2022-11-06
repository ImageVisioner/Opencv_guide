import  cv2 #导入了整个opencv
import  numpy as np

#单个模块
from  cv2 import  dnn
from  cv2 import  flann

#include "opencv2/core/core_c.h"
#include "opencv2/core/core.hpp"

#include "opencv2"
# 降低速度

def demo( ):
    # 0 1 flag
    src=cv2.imread("img113.jpg")

    cv2.imshow('src',src)
    #长宽 维度
    #位数
    #图像的尺寸大小
    #图像的数据类型

#一张图像 我们默认是rgb色彩空间
#hsv hsi ycbcr cmrk
#but

def spliltImage(img):
    b,g,r=cv2.split(img)
    print("这是b通道 blue{}".format(b))
    # green

#     r red

# using namemspace std:
# using namespace cv:
# cv::

if __name__ == '__main__':

    src = cv2.imread("img113.jpg")
    b, g, r = cv2.split(src)
    # cv2.merge() #合并通道函数
    # newsrc=cv2.merge([b,g,r])
    newsrc = np.stack((b,g,r),axis=2) #快速
    # cv2.imshow('b', b)
    # cv2.imshow('g',g)
    # cv2.imshow('r',r)
    cv2.imshow('src',src)
    cv2.imshow('srcnew',newsrc)
    cv2.waitKey(0)
    cv2.destroyAllWindows();




