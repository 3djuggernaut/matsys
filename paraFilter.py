from json import load
from posixpath import join
import jconfig
import os
import re
txt_path=jconfig.load_attr('TEXT')
filted_path=jconfig.load_attr("FILTED")
para_minlen=20

# 过滤段落用关键词
keyword=['Abstract','experimental','abstraction','Introduction']
alphaIslower=re.compile('[a-z]')
attributeKeyword=['dielectric','tf']

# 添加过滤规则用函数
def paraHandle(para):

    # 若含有关键词，则保留
    for item in keyword:
        if re.match(item,para):
            return True
    for item in attributeKeyword:
        if re.match(item,para):
            return True
    # 若长度过短，则舍弃
    if len(para)<para_minlen:
        return False
    return True

def paraFilter(filename):
    tmp=[]
    i=0
    fdr = open(os.path.join(txt_path,filename),'r',encoding='utf-8')
    fdw = open(os.path.join(filted_path,filename),'w',encoding='utf-8')
    # 还原段落
    for line in fdr:
        if re.match(alphaIslower,line[0])==None:
            if paraHandle(line):
                tmp.append(line)
                i+=1
        else:
            if i>=1:
                tmp[i-1]=tmp[i-1][:-1]+line
    
    for line in tmp:
        fdw.write(line)
    fdr.close()
    fdw.close()

def paraFilter_process():
    for item in os.listdir(txt_path):
        paraFilter(item)

if __name__=='__main__':
    paraFilter_process()

