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
processlist=   [ "fromfile_process",
    "registerHandlePDF_process",
    "getImage_process",
    "textExtract_process",
    "paraFilter_process",
    "findExperiment_process",
    "getTitle_process",
    "attrExtract_process",
    "makeMDProcess" ]

def initProcess():
    for item in processlist:
        j.save_attr(item,False)
    index=0
    
def isDoProcess(index):
    return j.load_attr(processlist[index])

def finishProcess(index):
    j.save_attr(processlist[index],True)
    return index+1

if __name__=='__main__':
    initProcess()
    recs.fromfile_process()
    index=finishProcess(index)
    recs.registerHandlePDF_process()
    index=finishProcess(index)
    im.getImage_process()
    index=finishProcess(index)
    te.textExtract_process()
    index=finishProcess(index)
    pa.paraFilter_process()
    index=finishProcess(index)
    fi.findExperiment_process()
    index=finishProcess(index)
    ti.getTitle_process()
    index=finishProcess(index)
    ae.attrExtract_process()
    index=finishProcess(index)
    ma.makeMD_process()
