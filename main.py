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
    if not processing:
        for item in processlist:
            j.save_attr(item,False)
    index=0
        
def isDoProcess(index):
    return not j.load_attr(processlist[index])

def finishProcess(index):
    j.save_attr(processlist[index],True)
    j.save_attr("PROCESSING",True)
    return index+1

def finishAllProcess():
    j.save_attr("PROCESSING",False)

if __name__=='__main__':
    initProcess()
    if isDoProcess(index):
        recs.fromfile_process()
    index=finishProcess(index)
    if isDoProcess(index):
        recs.registerHandlePDF_process()
    index=finishProcess(index)
    if isDoProcess(index):
        im.getImage_process()
    index=finishProcess(index)
    if isDoProcess(index):
        te.textExtract_process()
    index=finishProcess(index)
    if isDoProcess(index):
        pa.paraFilter_process()
    index=finishProcess(index)
    if isDoProcess(index):
        fi.findExperiment_process()
    index=finishProcess(index)
    if isDoProcess(index):
        ti.getTitle_process()
    index=finishProcess(index)
    if isDoProcess(index):
        ae.attrExtract_process()
    index=finishProcess(index)
    if isDoProcess(index):
        ma.makeMD_process()
    index=finishProcess(index)
    finishAllProcess()
