from json import load
from posixpath import join
import jconfig
import os
import re
txt_path=jconfig.load_attr('PDF_text_output')
txt_after_filted=jconfig.load_attr("PDF_text")
para_minlen=jconfig.load_attr('Para_minlen')

keyword=['Abstract','experimental','abstraction','Introduction']
alphaIslower=re.compile('[a-z]')
attributeKeyword=['dielectric','tf']

# 添加过滤规则用函数
def paraFilter(para):

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

def paraFilterSingle(filename):
    tmp=[]
    i=0
    fdr = open(os.path.join(txt_path,filename),'r',encoding='utf-8')
    fdw = open(os.path.join(txt_after_filted,filename),'w',encoding='utf-8')
    for line in fdr:
        if paraFilter(line):
            if re.match(alphaIslower,line[0])==None:
                tmp.append(line)
                i+=1
            else:
                if i>=1:
                    tmp[i-1]=tmp[i-1][:-1]+line
    for line in tmp:
        fdw.write(line)
    fdr.close()
    fdw.close()

def paraFilterProcess():
    for item in os.listdir(txt_path):
        paraFilterSingle(item)

if __name__=='__main__':
    paraFilterProcess()

