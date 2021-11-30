import recsHandle as recs
import imageExtract as im
import textExtract as te
import paraFilter as pa
import findExperiment as fi
import titleHandle as ti
import attrExtraction as ae
import markdownMaker as ma
import pickle 
import jconfig as j

index=0
pkl_path=j.load_attr("PKL")
processing=j.load_attr("PROCESSING")
processlist=[ recs.fromfile_process,
    recs.registerHandlePDF_process,
    im.getImage_process,
    te.textExtract_process,
    pa.paraFilter_process,
    fi.findExperiment_process,
    ti.getTitle_process,
    ae.attrExtract_process,
    ma.makeMD_process]
process_num=len(processlist)
process_finished=[]

def load_pkl() -> list:
    fd=open(pkl_path,'rb')
    obj=pickle.load(fd)
    fd.close()
    return obj

def save_pkl(obj):
    fd=open(pkl_path,'wb')
    pickle.dump(obj,fd)
    fd.close()
    return

def initProcess():
    '''初始化,所有步骤未执行'''
    if not processing:
        process_finished=[False for i in range(process_num)]
        save_pkl(process_finished)
    else:
        process_finished=load_pkl()
    index=0
    print(process_finished)
def isProcessDone(index):
    '''是否已执行'''
    return load_pkl()[index]

def finishProcess(index):
    '''将步骤设置为已执行,并且设置为程序正在运行中'''
    process_finished=load_pkl()
    process_finished[index]=True
    save_pkl(process_finished)
    j.save_attr("PROCESSING",True)
    return index+1

def finishAllProcess():
    '''所有步骤执行完,程序不需要再运行'''
    j.save_attr("PROCESSING",False)



if __name__=='__main__':
    initProcess()
    for item in processlist:
        if not isProcessDone(index):
            item()
        index=finishProcess(index)
    finishAllProcess()
