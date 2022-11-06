import  cv2
import  numpy as np
#数学中  把图像当做一个矩阵  numpy
#include <string>

#如何显示一张图
#有一张图？
#图的位置：相对路径和绝对路径

def demo():
    # 0 1 flag
    src=cv2.imread("img113.jpg",0)
    #打印一下
    # print(src)
    '''
    显示图像 mat是opencv中图像特有的一个格式
    matlab素所有格式都可以保存为mat格式
    '''
    cv2.imshow('src',src)
    #保持显示操作
    #waitkey 是一个键盘绑定函数 毫秒级 ascii
    #作用：检测特定建是否被按下
    cv2.waitKey(0)
    # cv2.destroyWindow('src')
    cv2.destroyAllWindows()
    #保存
    # cv2.imwrite("./TEST.jpg",src)

if __name__ == '__main__':
    demo()