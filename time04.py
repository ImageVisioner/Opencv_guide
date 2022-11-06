import time
import cv2
import  numpy as np
import math
# ？？如何测试速度
# time
# 1.如何利用opencv库函数进行测试时间
# 2.如何提高代码性能 tips
# 单位是：s
# c++用的时钟频率和我们平时脚本语言用的不太一样

t1=time.time()
e1=cv2.getTickCount() #又返回值函数 时钟数
src=cv2.imread('img113.jpg')

 # intel 

cv2.imshow("src",src)
e2=cv2.getTickCount()
t2=time.time()
tall=t2-t1;
print("这是time时间{}".format(tall))
fre=cv2.getTickFrequency() #返回时钟的计数频率 就是每秒的时钟数
timeall=(e2-e1)/fre;

print("整个运行时间为{}".format(timeall))
cv2.waitKey()
cv2.destroyAllWindows()
e2=cv2.getTickCount()

fre=cv2.getTickFrequency() #返回时钟的计数频率 就是每秒的时钟数
timeall=(e2-e1)/fre;

print("整个运行时间为{}".format(timeall))