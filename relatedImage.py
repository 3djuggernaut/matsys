import cv2
import numpy as np
from numpy.lib.function_base import average
import os
import jconfig as j

repeat_path=j.load_attr('REPEAT')
image_path=j.load_attr('IMAGE')

def dHash(img):
    # 差值hash
    img=cv2.resize(img,(17,16))
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    hash=[]
    for i in range(16):
        for j in range(16):
            if gray[i,j]>gray[i,j+1]:
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



class ImageFolder:
    pdfname=''
    imagelist=[]
    imagehashlist=[]
    boollist=[]
    imageNum=0

    def __init__(self,pdfname) -> None:
        self.pdfname=pdfname
        self.imagelist=[]
        self.imagehashlist=[]
        self.boollist=[]
        self.imageNum=0
    
    def __repr__(self) -> None:
        print(self.imageNum)
        print(self.boollist)
        return f'{self.pdfname}'
    # 将所有的图片先求出hash

    def addImage(self):
        path=os.path.join(image_path,self.pdfname)
        for item in os.listdir(path):
            self.imagelist.append(item)
            img=cv2.imread(os.path.join(path,item))
            self.imagehashlist.append(dHash(img))
        self.imageNum=len(self.imagelist)
        self.boollist=[1 for v in range(len(self.imagelist))]
        

def cmpFolder(folder1,folder2):
    folder1_len=folder1.imageNum
    folder2_len=folder2.imageNum
    for i in range(folder1_len):
        if folder1.boollist[i]:
            for j in range(folder2_len):
                if folder2.boollist[j]:
                    result=cmpHash(folder1.imagehashlist[i],folder2.imagehashlist[j])
                    # 若两张图完全一样，则在两个集合中删除这两张图，并且退出当前循环
                    if result==0:
                        img1_path=f'{image_path}/{folder1.pdfname}/{folder1.imagelist[i]}'
                        img2_path=f'{image_path}/{folder2.pdfname}/{folder2.imagelist[j]}'
                        folder1.boollist[i]=0
                        folder2.boollist[j]=0
                        os.system(f'mv {img1_path} {repeat_path} ')
                        os.system(f'mv {img2_path} {repeat_path} ')

    
        



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


if __name__=='__main__':
    filelist=os.listdir(image_path)
    count=0
    total=len(filelist)
    folderlist=[]
    print("calculating hash...")
    for f in filelist:
        folderlist.append(ImageFolder(f))
    for folder in folderlist:
        folder.addImage()
        print(folder)
    print("begin compare")
    for i in range(total):
        for j in range(i+1,total):
            cmpFolder(folderlist[i],folderlist[j])
            count+=1
            print(f'{count}/{(int)(total-1)*(total)/2}:FINISH COMPARE: {folderlist[i].pdfname}:{folderlist[j].pdfname}')

    for folder in folderlist:
        print(folder)