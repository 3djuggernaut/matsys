import json
import jconfig as j
import os

recs_path=j.load_attr('RECS')
pdf_path=j.load_attr('PDF')

# 存取RECS文件（描述title和doi之间的关系）
def load_recs():
    fd=open('../Config/recs.json','r',encoding='utf-8-sig')
    jsonobj=json.load(fd)
    return jsonobj

def save_recs(jsonobj):
    fd=open('../Config/recs.json','w',encoding='utf-8-sig')
    fd.truncate(0)
    fd.seek(0)
    json.dump(jsonobj,fd)

def add_item(recs_list):
    jsonobj=load_recs()
    jsonobj+=recs_list
    save_recs(jsonobj)

# 从单个文件中逐条读取文献的标题和DOI信息
def fromfile(recsfile):
    fd=open(os.path.join(recs_path,recsfile),'r',encoding='utf-8')
    recs_list=[]
    tmp={}
    handleTitleFlag=False
    for line in fd:
        if line!='\n':
            if not handleTitleFlag:
                if line.startswith("DI"):
                    tmp['DI']=line[3:-1]
                if line.startswith("TI"):
                    tmp['TI']=line[3:-1]
                    handleTitleFlag=True
            else:
                ## 长标题判断中
                if not line.startswith("  "):
                    handleTitleFlag=False
                else:
                    tmp['TI']+=f' {line[3:-1]}'
        else:
            if tmp.__contains__('DI'):
                tmp['ishandle']=False
                recs_list.append(tmp)
            tmp={}
    add_item(recs_list)
    fd.close()

def fromfile_process():
    jsonobj=[]
    save_recs(jsonobj)
    for item in os.listdir(recs_path):
        fromfile(item)
# 记录已经处理的PDF的信息

def registerHandledPDF(filename):
    jsonobj=load_recs()
    for item in jsonobj:
        if item['DI'][8:]==filename:
            item['ishandle']=True
            print(f'{filename}:find')
            return True
    print(f'{filename}:not find')
    return False

def registerHandlePDFProcess():
    jsonobj=load_recs()
    count=0
    for filename in os.listdir(pdf_path):
        doi=filename[:-4]
        for item in jsonobj:
            if item['DI'][8:]==doi:
                item['ishandle']=True
                print(f'FIND:{doi}')
                count+=1
                break
    save_recs(jsonobj)
    print(f'Finish register {count}/{len(os.listdir(pdf_path))}')


if __name__=='__main__':
    # fromfile_process()
    registerHandlePDFProcess()