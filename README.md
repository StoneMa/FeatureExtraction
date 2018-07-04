# FeatureExtraction
feature extraction 特征提取，各类特征提取算法实现与三维特征提取

# env: Win10, Annaconda3， Python3.5, Opencv3
# Attention:
* 如果执行的时候会出现 ``import cv2`` 错误
  
* 解决办法:下载``python3.dll`` 下载地址: https://www.python.org/ftp/python/3.5.2/python-3.5.2-embed-amd64.zip, 解压这个文件夹，将其中的python3.dll 放入到Anaconda根目录

* 如果执行过程中发现 ``AttributeError: module 'cv2' has no attribute 'SIFT'``，要注意的是opencv3中SIFT，Surf 算法不在是免费的，它们默认放入到opencv_contrib库中，目前仅支持python3.5 和Python3.6, 所以要 
```shell
pip install opencv-contrib-python

```

同时它与opencv-python不能共存,需要卸载：

```shell
pip uninstall opencv-python
``` 

执行上述即可正常运行。
## Canny 边缘提取
通过Canny提取图像边缘
##FeatureDetection
这里使用的是SURF方法进行的特征提取
##Filter
图像滤波器的卷积操作
## Harris Corner
Harris 角点探测
## Hog 算法
主要与SVM结合使用来实现行人检测