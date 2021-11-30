import jconfig
import recsHandle as recs
import os
md_path=jconfig.load_attr("MD")
pdf_path=jconfig.load_attr("PDF")
exp_path=jconfig.load_attr("EXP")
image_path=jconfig.load_attr("IMAGE")
attr_path=jconfig.load_attr("ATTR")
maxImageNumOfPDF=jconfig.load_attr("IMAGENUM")

class Mdfile:
    id=0
    title=''
    doi=''
    filename=''
    cem=[]
    attr1=''
    attr2=''
    attr3=''
    attr1_para=[]
    attr2_para=[]
    attr3_para=[]
    image_path=''
    experiment=''

    def __init__(self) -> None:
        self.id=0
        self.title=''
        self.doi=''
        self.cem=[]
        self.attr1=''
        self.attr2=''
        self.attr3=''
        self.attr1_para=[]
        self.attr2_para=[]
        self.attr3_para=[]
        self.image_path=''
        self.experiment=''
        return

    
    # image/experiment/
    # 设置DOI的同时关联好图片文件夹
    def add_doi(self,text):
        self.doi=text  
    
    def add_filename(self,text):
        self.filename=text

    def getImagePath(self):
        return f'{os.path.join(image_path,self.filename)}'
    def getAttrPath(self):
        return f'{os.path.join(attr_path,self.filename)}.txt'    
    def getExpPath(self):
        return f'{os.path.join(exp_path,self.filename)}.txt'
    

    def add_id(self,id):
        self.id=id
    def add_title(self,text):
        self.title=text

    def add_cem(self,text):
        self.cem.append(text)     
    def add_attr1(self,text):
        self.attr1=text
    def add_attr2(self,text):
        self.attr2=text
    def add_attr3(self,text):
        self.attr3=text
    def add_attr1_para(self,text):
        self.attr1_para.append(text)
    def add_attr2_para(self,text):
        self.attr2_para.append(text)
    def add_attr3_para(self,text):
        self.attr3_para.append(text)
    def add_experiment(self,text):
        self.experiment=text
    # 依据需要的信息生成MD，进而生成PDF
    def makemd(self):
        file_path=os.path.join(md_path,f'Paper{self.id}.md')
        fd=open(file_path,'w',encoding='utf-8')
        fd.write(f'# {self.title}\n')
        fd.write(f'## Basic Information\n')
        name=""
        for item in self.cem:
            name+=f'{item}'
        fd.write(f'**{name}**\n\n')
        fd.write(f'**DOI:{self.doi}**\n\n')
        fd.write(f'``εr:{self.attr1}``\n\n')
        for item in self.attr1_para:
            fd.write(f'> {item}\n\n')
        fd.write(f'``Qxf:{self.attr2}``\n\n')
        for item in self.attr2_para:
            fd.write(f'> {item}\n\n')
        fd.write(f'``τf:{self.attr3}``\n\n')
        for item in self.attr3_para:
            fd.write(f'> {item}\n\n')
        fd.write(f'## XRD and SEM Graph\n\n')

        # 显示图片，尺寸控制还需要再研究
        image_num=len(os.listdir(self.getImagePath()))
        if image_num < maxImageNumOfPDF:
            for item in os.listdir(self.getImagePath()):
                fd.write(f'![]({os.path.join(self.getImagePath(),item)})\n\n')
                # 用来调整图片尺寸的参数
                # {{:height="100px" width="400px"}}
        else:
            fd.write(f'> The image of this PDF is not properly extracted\n\n')

        fd.write(f'## Experiment Part\n\n')
        fd.write(f'{self.experiment}')
        ## 加入与实验有关的段落,还需要再研究
        fd.close()

    def clear(self):
        self.cem.clear()
        self.attr1_para.clear()
        self.attr2_para.clear()
        self.attr3_para.clear()

def makeMD_process():
    jsonobj=recs.load_recs()
    index=0
    for item in jsonobj:
        if item['ishandle']==True:
            m=Mdfile()
            m.add_id(index)
            index+=1
            m.add_doi(item['DI'])
            m.add_filename(item['filename'])
            m.add_title(item['TI'])
            # 添加属性
            attrfd=open(m.getAttrPath(),'r',encoding='utf-8')
            attrnum1=(int)(attrfd.readline())
            for count in range(attrnum1):
                m.add_attr1_para(attrfd.readline())
            attrnum2=(int)(attrfd.readline())
            for count in range(attrnum2):
                m.add_attr2_para(attrfd.readline())        
            attrnum3=(int)(attrfd.readline())
            for count in range(attrnum3):
                m.add_attr3_para(attrfd.readline())

            for t in item["CE"]:
                m.add_cem(t)

            fd=open(m.getExpPath(),'r',encoding='utf-8')
            tmptxt=''
            for line in fd:
                tmptxt+=line
            m.add_experiment(tmptxt)
            fd.close()
    
            m.makemd()
            m.clear()
            attrfd.close()


# m的生命周期怎么这么长
if __name__=='__main__':
    makeMD_process()
