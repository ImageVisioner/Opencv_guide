import  cv2
import  numpy as np

src = cv2.imread("img113.jpg")

cv2.imshow('src', src)

k=cv2.waitKey(0)

#exit esc
if k ==27 :
    cv2.destroyAllWindows()
elif k ==ord('s'):
    cv2.imwrite('./korddemo1.png',src)
    cv2.destroyAllWindows()
