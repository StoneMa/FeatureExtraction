from skimage import data,filters,io,color
# #img=color.rgb2gray(data.coffee())
# # 若要读取自己的图片，可以采用以下代码：
# # 其中，path是图片所在的目录，尽量是完整的目录，灰度化处理同样，采用
# img=io.imread(".\img\yu1.png",1)
# color.rgb2gray(img)
# edge_img=filters.canny(img)
# io.imshow(edge_img)
# io.show()
from skimage.filters import gabor
from skimage.feature import canny
from skimage import data, io
from matplotlib import pyplot as plt
image = io.imread(".\lena.jpg",1)
# detecting edges in a coin image
filt_real, filt_imag = gabor(image, frequency=0.88)
edge_img= canny(image)
plt.figure()
io.imshow(edge_img)
io.show()