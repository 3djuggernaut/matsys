import chemdataextractor as cde
from chemdataextractor.doc.document import Document
from chemdataextractor.doc.text import Paragraph, Span
import recsHandle as recs
import jconfig as j
import os


pdf_path=j.load_attr('PDF')

def getTitle(filename):
    jsonobj=recs.load_recs()
    tmp=[]
    for item in jsonobj:
        if item['DI'][8:]==filename:
            title=item['TI']
            para=Paragraph(title)
            for ce in para.cems:
                tmp.append(ce.text)
            item['CE']=tmp
            recs.save_recs(jsonobj)
            return True
    return False

def getTitle_process():      
    count=0
    total=len(os.listdir(pdf_path))
    for item in os.listdir(pdf_path):
        getTitle(item[:-4])
        count+=1
        print(f'{count}/{total}:FINISH TITLE EXTRACT:{item}')
    

if __name__=='__main__':
    getTitle_process()
    