import recsHandle as recs
import imageExtract as im
import textExtract as te
import paraFilter as pa
import findExperiment as fi
import titleHandle as ti
import attrExtraction as ae
import markdownMaker as ma

import jconfig as j

index=0
processing=j.load_attr("PROCESSING")
processlist=[ recs.fromfile_process(),
    recs.registerHandlePDF_process(),
    im.getImage_process(),
    te.textExtract_process(),
    pa.paraFilter_process(),
    fi.findExperiment_process(),
    ti.getTitle_process(),
    ae.attrExtract_process(),
    ma.makeMDProcess()]

def initProcess():
    '''初始化,所有步骤未执行'''
    if not processing:
        for item in processlist:
            j.save_attr(item,False)
    index=0
        
def isProcessDone(index):
    '''是否已执行'''
    return j.load_attr(processlist[index])

def finishProcess(index):
    '''将步骤设置为已执行,并且设置为程序正在运行中'''
    j.save_attr(processlist[index],True)
    j.save_attr("PROCESSING",True)
    return index+1

def finishAllProcess():
    '''所有步骤执行完,程序不需要再运行'''
    j.save_attr("PROCESSING",False)



if __name__=='__main__':
    initProcess()
    for item in processlist:
        if not isProcessDone():
            item()
        index=finishProcess()
    finishAllProcess()
