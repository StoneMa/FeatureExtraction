# -- coding: utf-8 --
# 定义不同的滤波器，并用不同的滤波器对图像进行卷积
import cv2
import numpy as np
from scipy import ndimage

#这个是滤波器使用的模板矩阵
kernel_3x3 = np.array([[-1, 0, -1],
                       [-1, 0, -1],
                       [-1, 0, -1]])

kernel_5x5 = np.array([[-1, -1, -1, -1, -1],
                       [-1, 1, 2, 1, -1],
                       [-1, 2, 4, 2, -1],
                       [-1, 1, 2, 1, -1],
                       [-1, -1, -1, -1, -1]])
#显示原始图像
cv2.imshow("org", cv2.imread("./lena.jpg"))

#以灰度的方式加载图片
img = cv2.imread("./lena.jpg", 0)
cv2.imshow("img", img)

#通过使用模板矩阵进行高通滤波
k3 = ndimage.convolve(img, kernel_3x3)
k5 = ndimage.convolve(img, kernel_5x5)

#使用OpenCV的高通滤波
blurred = cv2.GaussianBlur(img, (11, 11), 0)
g_hpf = img - blurred

cv2.imshow("3x3", k3)
cv2.imshow("5x5", k5)
cv2.imshow("blurred", blurred)
cv2.imshow("g_hpf", g_hpf)

cv2.waitKey()
cv2.destroyAllWindows()