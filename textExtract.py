import os
import re
import argparse
import jconfig as j
from pdfminer.high_level import extract_text

def textExtractProcess():

    pdf_dir = j.load_attr('PDF')
    text_path = j.load_attr('TEXT')

    pdf_files = [x for x in os.listdir(pdf_dir) if x.endswith(".pdf") or x.endswith(".PDF")]

    pdf_files_num = len(pdf_files)

    for idx, pdf_name in enumerate(pdf_files):
        pdf_file_path = os.path.join(pdf_dir, pdf_name)
        text_file_path = os.path.join(text_path, pdf_name[0:-4] + ".txt")
        with open(text_file_path, "w", encoding='utf-8') as text_file:
            text_file.write(re.sub("[^\n]\n[^\n]", "" , extract_text(pdf_file_path)))
        print(f"{idx+1}/{pdf_files_num}:Finish Text Extract:{pdf_name}")


if __name__=='__main__':
    textExtractProcess()