import recsHandle as recs
import imageExtract as im
import textExtract as te
import paraFilter as pa
import findExperiment as fi
import titleHandle as ti
import attrExtraction as ae
import markdownMaker as ma
if __name__=='__main__':
    recs.fromfile_process()
    recs.registerHandlePDF_process()
    im.getImage_process()
    te.textExtract_process()
    pa.paraFilter_process()
    fi.findExperiment_process()
    ti.getTitle_process()
    ae.attrExtract_process()
    ma.makeMDProcess()
