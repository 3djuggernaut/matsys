import jconfig
import recsHandle as recs
import os
md_path=jconfig.load_attr("MD_path")
pdf_path=jconfig.load_attr("PDF_path")
exp_path=jconfig.load_attr("PDF_exp")

class Mdfile:
    id=0
    title=''
    doi=''
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
        id=0
        title=''
        doi=''
        cem=[]
        attr1=''
        attr2=''
        attr3=''
        attr1_para=[]
        attr2_para=[]
        attr3_para=[]
        image_path=''
        experiment=''
        return

    
    # 设置DOI的同时关联好图片文件夹
    def add_doi(self,text):
        self.doi=text  
        jsonobj=recs.load_recs()
        for item in jsonobj:
            if item.__contains__('DI'):
                if item['DI']==self.doi:
                    if item.__contains__('Image_path'):
                        self.image_path=item['Image_path']

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

        num=len(os.listdir(self.image_path))
        # print(num)
        for item in os.listdir(self.image_path):
            fd.write(f'![]({os.path.join(self.image_path,item)})\n\n')
            # 用来调整图片尺寸的参数
            # {{:height="100px" width="400px"}}

        fd.write(f'## Experiment Part\n\n')
        fd.write(f'{self.experiment}')
        ## 加入与实验有关的段落,还需要再研究
        fd.close()

    def clear(self):
        self.cem.clear()
        self.attr1_para.clear()
        self.attr2_para.clear()
        self.attr3_para.clear()


def test():
    m=Mdfile()
    m.add_doi('10.1063/1.2200480')
    m.add_cem('cem')
    m.add_attr1('attr1')
    m.add_attr2('attr2')
    m.add_attr3('attr3')
    m.add_title('title')
    m.add_attr1_para('Some thing about 1')
    m.add_attr1_para('Another thing about 1')
    m.add_attr1_para('about 1')
    m.add_attr1_para('about attr1')
    m.add_attr2_para('Some thing about 2')
    m.add_attr2_para('Another thing about 2')
    m.add_attr2_para('Some thing about 3')
    m.add_attr3_para('Another about 3')
    m.makemd()

def makeMDProcess():
    jsonobj=recs.load_recs()
    index=0
    for item in jsonobj:
        if item.__contains__("CE"):
            m=Mdfile()
            m.add_id(index)
            index+=1
            m.add_doi(item['DI'])
            m.add_title(item['TI'])
            # 添加属性
            if(item.__contains__("PDF_Attr")):
                attrfd=open(item['PDF_Attr'],'r',encoding='utf-8')
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
            if item.__contains__('Exp_path'):
                fd=open(item['Exp_path'],'r',encoding='utf-8')
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
    makeMDProcess()
