import cv2
import numpy as np
from numpy.lib.function_base import average
import os
def dHash(img):
    # 差值hash
    img=cv2.resize(img,(9,8))
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    hash=[]
    for i in range(8):
        for j in range(8):
            if gray[i,j]>gray[i,j+1]:
                hash.append(1)
            else:
                hash.append(0)
    return hash

def pHash(img):
    # 感知hash
    img=cv2.resize(img,(32,32))
    gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    dct_convert=cv2.dct(img,np.float32(gray_image))
    dct_roi=dct_convert[0:8,0:8]

    hash=[]
    avg=np.mean(dct_roi)
    for i in range(dct_roi.shape[0]):
        for j in range(dct_roi.shape[1]):
            if dct_roi[i,j]>avg:
                hash.append(1)
            else:
                hash.append(0)
    return hash

def cmpHash(hash1,hash2):
    result=0
    if len(hash1)!=len(hash2):
        print("false")
        return 

    for i in range(len(hash1)):
        if hash1[i]!=hash2[i]:
            result+=1
    return result

def cmpImage(image_path1,image_path2):
    img1=cv2.imread(image_path1)
    img2=cv2.imread(image_path2)
    return cmpHash(dHash(img1),dHash(img2))

def cmpareTest():
    path1='../PDFImageOutput/1.1814167'
    path2='../PDFImageOutput/1.1871337'
    for img1 in os.listdir(path1):
        for img2 in os.listdir(path2):
            print(f'Difference between {img1} and {img2} is {cmpImage(os.path.join(path1,img1),os.path.join(path2,img2))}')

if __name__=='__main__':
    cmpareTest()