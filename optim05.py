import  cv2
import numpy

#提供了两个函数 傻瓜式的
# intel amd cpu
# ssm2 avx 指令集
# intel上面默认打开opencv的优化开关的
# amd

cv2.setUseOptimized(False)
def optim():
#     检查优化开关的开启和关闭？
    flag = cv2.useOptimized()

    print("优化开关的状态为{}".format(flag))
    flag2= cv2.setUseOptimized(False)
    print("此时已经关闭优化开关")
    flag3 = cv2.useOptimized()
    print("优化开关的状态为{}".format(flag3))

def optim1():
    flag =cv2.useOptimized()
    if flag ==1:
        print("当前我的优化开关状态为{}".format(flag))
    else:
        flag2 = cv2.setUseOptimized(True)
        flag3 = cv2.useOptimized()
        print("开启状态为{}".format(flag3))
# 9.6422998
# 8.9205604
cv2.setUseOptimized(True)
e1=cv2.getTickCount()
src =cv2.imread("demo.jpg")

for i in range(5,201,2):
    src=cv2.medianBlur(src,i)

# 渝西图像练习生


e2=cv2.getTickCount()
t=(e2-e1)/cv2.getTickFrequency()
print(t) #1.6472803 2.2667666 2.2430748

# 1.这个图像很小
# 2.电脑性能足够强
# 3. 机器视觉 工业相机 50m

