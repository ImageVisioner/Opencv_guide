import  cv2
import  numpy as np

def demo( ):
    # 0 1 flag
    src=cv2.imread("img113.jpg")

    cv2.imshow('src',src)
    #长宽 维度
    #位数
    #图像的尺寸大小
    #图像的数据类型



    cv2.waitKey(0)
    # cv2.destroyWindow('src')
    cv2.destroyAllWindows()

def calImage(img):
    # 有参函数带返回值的
    # void ? calimage(*img)?calimage(&img)
    #return *

    #shape 形状 shape[0] shaoe[1] shape[2] shape of  you
    rows=img.shape[0] #行列 list matlab
    cols=img.shape[1]
    channel=img.shape[2] #通道

    #图像类型属性
    str1=str(img.dtype)

    #像素大小
    sizeImg=img.size

    return  rows, cols,channel,str1,sizeImg

if __name__ == '__main__':
    src = cv2.imread("img113.jpg")

    rows, cols, channel, str1, sizeImg=calImage(src);
    print(rows)
    print(cols)
    print(channel)
    print(str1)

    # note 我们保存的时候都用无符号整型八位
    print(sizeImg)

    #分离和合并通道。。




