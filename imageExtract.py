import fitz
import io
import os
from PIL import Image
from pdfminer.utils import FileOrName
import jconfig as j
import recsHandle as recs


pdf_path=j.load_attr('PDF')
pic_path=j.load_attr('IMAGE')
recs_path=j.load_attr('RECS')

# TODO:判断图片的大小是否合适
def isSizelegal(width,height):
    return width

def getImage(filename):

    pdfd=fitz.open(os.path.join(pdf_path,f'{filename}.pdf'))
    
    if not os.path.exists(os.path.join(pic_path,filename)):
        os.mkdir(os.path.join(pic_path,filename))

    for page_index in range(len(pdfd)):
        page=pdfd[page_index]
        image_list=page.get_images()
        for image_index, img in enumerate(page.get_images(), start=1):
            # print(img)
            # print(image_index)
            xref = img[0]
        # extract the image bytes
            base_image = pdfd.extract_image(xref)
            image_bytes = base_image["image"]

        # Test
            # print(f'{base_image["width"]} {base_image["height"]}')
        # get the image extension
            image_ext = base_image["ext"]
        # load it to PIL
            image = Image.open(io.BytesIO(image_bytes))
        # save it to local disk
            t=os.path.join(pic_path,filename)
            save_path=os.path.join(t,f"image{page_index+1}_{image_index}.{image_ext}")
            image.save(open(save_path, "wb"))
    



def getImageProcess():
    total=len(os.listdir(pdf_path))
    count=0
    for item in os.listdir(pdf_path):
        getImage(item[:-4])
        count+=1
        print(f'{count}/{total}:Finish Image Extract:{item[:-4]}')
    print("Finish Image Extract")
    
if __name__=='__main__':
    getImageProcess()  
