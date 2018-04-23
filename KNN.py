import cv2
import numpy as np
import matplotlib.pyplot as plt
# Feature set containing (x,y) values of 25 known/training data
# 10个特征数据，每个数据都是由一个坐标构成，每个数都是0~100之间的随机数
# 特征数据矩阵为10行，2列 ：[10,2]
trainData = np.random.randint(0,100,(10,2)).astype(np.float32)
# Labels each one either Red or Blue with numbers 0 and 1
# 给每个数据标定label
responses = np.random.randint(0,2,(10,1)).astype(np.float32)
# Take Red families and plot them
# 让label = 0的数据为red三角
red = trainData[responses.ravel()==0]
plt.scatter(red[:,0],red[:,1],80,'r','^')
# Take Blue families and plot them
# 让label = 1的数据为blue的方块
blue = trainData[responses.ravel()==1]
plt.scatter(blue[:,0],blue[:,1],80,'b','s')
# 新加入的绿色圆圈
newcomer = np.random.randint(0,100,(1,2)).astype(np.float32)
plt.scatter(newcomer[:,0],newcomer[:,1],80,'g','o')
knn = cv2.ml.KNearest_create()
knn.train(trainData, cv2.ml.ROW_SAMPLE, responses)
ret, results, neighbours ,dist = knn.findNearest(newcomer, 3)
# 打印结果，如果属于red ,result中属于0 label;如果是blue,就是result=1
print( "result:  {}\n".format(results) )
print( "neighbours:  {}\n".format(neighbours) )
print( "distance:  {}\n".format(dist) )
plt.show()