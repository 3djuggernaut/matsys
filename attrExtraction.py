from typing_extensions import ParamSpec
import chemdataextractor as cde
import jconfig
import os
import re
txt_path=jconfig.load_attr('FILTED')
attr_path=jconfig.load_attr('ATTR')

# 根据匹配结果match_result高亮匹配成功的部分
def highlight_para(line,match_result):
    start=match_result.span()[0]
    end=match_result.span()[1]
    result=f'{line[:start]}`{line[start:end]}`{line[end:]}'
    return result

# 匹配过程 former用于记录匹配结果的前一句
def para_match(para,pattern):
    t=para.split('.')
    result=[]
    former=''
    for i,item in enumerate(t):
        match_result=re.search(pattern,item)
        if match_result!=None:
            hp=highlight_para(item,match_result)
            if hp.endswith('\n'):
                hp=hp[:-1]
            txt=f'...{former}.{hp}.'
            result.append(txt)
        former=item
    return result

class AttrExtract:
    attribute_pat=r'dielectric constant|ε|ε?r'
    attribute2_pat=r'Qf|Qxf'
    attribute3_pat=r't?f|τ?f'
    # attribute3_pat=
    unit3_pat=r'ppm/° ?C|° ?C'
    unit2_pat=r'GHz'
    unit1_pat=r'ε|ε ?r'
  
    def attrExtract(filename):
        attr1_result=[]
        attr2_result=[]
        attr3_result=[]
        fdr=open(os.path.join(txt_path,filename),'r',encoding='utf-8')
        fdw=open(os.path.join(attr_path,filename),'w',encoding='utf-8')
        for line in fdr:
            attr1_result+=para_match(line,AttrExtract.unit1_pat)
            attr2_result+=para_match(line,AttrExtract.unit2_pat)
            attr3_result+=para_match(line,AttrExtract.unit3_pat)
        print(f'result:{len(attr1_result)}:{len(attr2_result)}:{len(attr3_result)}')
        fdw.writelines(f'{len(attr1_result)}\n')
        for item in attr1_result:
            fdw.writelines(f'{item}\n')
        fdw.writelines(f'{len(attr2_result)}\n')
        for item in attr2_result:
            fdw.writelines(f'{item}\n')
        fdw.writelines(f'{len(attr3_result)}\n')
        for item in attr3_result:
            fdw.writelines(f'{item}\n')
        fdw.close()
        fdr.close()
def attrExtract_process():
    count=0
    total=len(os.listdir(txt_path))
    for item in os.listdir(txt_path):
        count+=1
        print(f'{count}/{total}:FINISH ATTR EXTRACT:{item}')
        AttrExtract.attrExtract(item)
if __name__=='__main__':
    attrExtract_process()
