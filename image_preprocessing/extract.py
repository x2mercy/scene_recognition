#%matplotlib inline
import numpy as np
from skimage.feature import corner_harris,corner_peaks
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
import skimage.io as io
from skimage.exposure import equalize_hist

def show_corners(corners,image):
    fig=plt.figure()
    plt.gray()
    plt.imshow(image)
    y_corner,x_corner=zip(*corners)
    plt.plot(x_corner,y_corner,'or')
    plt.xlim(0,image.shape[1])
    plt.ylim(image.shape[0],0)
    fig.set_size_inches(np.array(fig.get_size_inches())*1.5)
    plt.show()
if __name__ == '__main__':  
    mandrill=io.imread('/Users/wangmengxi/Documents/mercy/ec601/pj1/image processing/defog1.jpg')

    mandrill=equalize_hist(rgb2gray(mandrill))
    corners=corner_peaks(corner_harris(mandrill),min_distance=2)
    show_corners(corners,mandrill)
    