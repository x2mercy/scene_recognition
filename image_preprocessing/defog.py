import cv2  
import numpy as np  
   
def zmMinFilterGray(src, r=7):  
    if r <= 0:  
        return src  
    h, w = src.shape[:2]  
    I = src  
    res = np.minimum(I  , I[[0]+range(h-1)  , :])  
    res = np.minimum(res, I[range(1,h)+[h-1], :])  
    I = res  
    res = np.minimum(I  , I[:, [0]+range(w-1)])  
    res = np.minimum(res, I[:, range(1,w)+[w-1]])  
    return zmMinFilterGray(res, r-1)  
   
def guidedfilter(I, p, r, eps):  
    height, width = I.shape  
    m_I = cv2.boxFilter(I, -1, (r,r))  
    m_p = cv2.boxFilter(p, -1, (r,r))  
    m_Ip = cv2.boxFilter(I*p, -1, (r,r))  
    cov_Ip = m_Ip-m_I*m_p  
   
    m_II = cv2.boxFilter(I*I, -1, (r,r))  
    var_I = m_II-m_I*m_I  
   
    a = cov_Ip/(var_I+eps)  
    b = m_p-a*m_I  
   
    m_a = cv2.boxFilter(a, -1, (r,r))  
    m_b = cv2.boxFilter(b, -1, (r,r))  
    return m_a*I+m_b  
   
def getV1(m, r, eps, w, maxV1):  #input rgb image, the range of value [0,1] 
    V1 = np.min(m,2)                                         #get dark path image  
    V1 = guidedfilter(V1, zmMinFilterGray(V1,7), r, eps)     #guided filter 
    bins = 2000  
    ht = np.histogram(V1, bins)                              #calculate light of atmosphere:A  
    d = np.cumsum(ht[0])/float(V1.size)  
    for lmax in range(bins-1, 0, -1):  
        if d[lmax]<=0.999:  
            break  
    A  = np.mean(m,2)[V1>=ht[1][lmax]].max()  
           
    V1 = np.minimum(V1*w, maxV1)                   #limit the range  
       
    return V1,A  
   
def deHaze(m, r=81, eps=0.001, w=0.95, maxV1=0.80, bGamma=False):  
    Y = np.zeros(m.shape)  
    V1,A = getV1(m, r, eps, w, maxV1)               #get shaded image and light  
    for k in range(3):  
        Y[:,:,k] = (m[:,:,k]-V1)/(1-V1/A)           #correct color
    Y =  np.clip(Y, 0, 1)  
    if bGamma:  
        Y = Y**(np.log(0.5)/np.log(Y.mean()))       #correct gamma 
    return Y  
   
if __name__ == '__main__':  
    m = deHaze(cv2.imread('/Users/wangmengxi/Documents/mercy/ec601/pj1/image processing/boston-fog.jpg')/255.0)*255  
    cv2.imwrite('boston-defog.jpg', m)  