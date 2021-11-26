import chemdataextractor as cde
from chemdataextractor.doc.document import Document
from chemdataextractor.doc.text import Paragraph, Span
import recsanalyser as recs
import jconfig as j
import os


pdf_path=j.load_attr('PDF_path')

def getTitle(filename):
    jsonobj=recs.load_recs()
    tmp=[]
    for item in jsonobj:
        if item.__contains__("DI"):
            if item['DI'][8:]==filename:
                title=item['TI']
                print(f"find:{title}")
                para=Paragraph(title)
                for ce in para.cems:
                    tmp.append(ce.text)
                item['CE']=tmp
                print('*'*20)
                recs.save_recs(jsonobj)
                return
    print('not find')
    return 

def getTxt(filename):
    jsonobj=recs.load_recs()
    for item in jsonobj:
        if item.__contains__("DI"):
            if item['DI'][8:]==filename: 
                if item.__contains__("Txt_path"):
                    fd=open(item['Txt_path'],'r',encoding='utf-8')
                    ## test
                    i=0
                    for line in fd:
                        print(line)
                        doc=cde.Document(line)
                        print(doc.cems)
                        i+=1
                        if i>5:
                            print('*'*20)
                            return
    print('not find')
    return 

def getTitleprocess():      
    for item in os.listdir(pdf_path):
         getTitle(item[:-4])
    

if __name__=='__main__':
    getTitleprocess()
    