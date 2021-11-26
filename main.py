import recsHandle as recs
import imageExtract as im
import textExtract as te
# import paraFilter as pa
# import titleHandle as ti
# import markdownMaker as ma
# import findExperiment as fi
# import operationExtractTest as oe
if __name__=='__main__':
    recs.fromfile_process()
    recs.registerHandlePDF_process()
    im.getImage_process()
    te.textExtract_process()
    # pa.paraFilterProcess()
    # fi.findExperiment_process()
    # ti.getTitleprocess()
    # oe.operationExtract()
    # ma.makeMDProcess()
