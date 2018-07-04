# HOG(Histogram of Oriented Gradient) 特征
# 方向梯度直方图（Histogram of Oriented Gradient, HOG）特征是一种在计算机视觉和图像处理中用来进行物体检测的特征描述子。
# HOG特征通过计算和统计图像局部区域的梯度方向直方图来构成特征。
# HOG+SVM常用于行人检测
import cv2 as cv
from skimage import feature as ft
filename = './lena.jpg'
image = cv.imread(filename)
features = ft.hog(image,  # input image
                  orientations=9,  # number of bins
                  pixels_per_cell=(20,20), # pixel per cell
                  cells_per_block=(2,2), # cells per blcok
                  block_norm = 'L2', #  block norm : str {‘L1’, ‘L1-sqrt’, ‘L2’, ‘L2-Hys’}, optional
                  transform_sqrt = True, # power law compression (also known as gamma correction)
                  feature_vector=True, # flatten the final vectors
                  visualise=True) # return HOG map