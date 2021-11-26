import recsHandle as recs
import imageExtract as im
import textExtract as te
import paraFilter as pa
import titleHandle as ti
import markdownMaker as ma
import findExperiment as fi
import operationExtractTest as oe
if __name__=='__main__':
    recs.fromfile_process()
    im.getImageProcess()
    te.textExtractProcess()
    pa.paraFilterProcess()
    fi.findExperiment_process()
    ti.getTitleprocess()
    oe.operationExtract()
    ma.makeMDProcess()
