import os
import re
import jconfig as j
from pdfminer.high_level import extract_text


def analyseSinglePDF(filename):
    pdf_file_path = os.path.join(pdf_dir, f'{filename}.pdf')
    text_file_path = os.path.join(output_dir, f'{filename}.txt')
    with open(text_file_path, "w", encoding='utf-8') as text_file:
        text_file.write(re.sub("[^\n]\n[^\n]", "" , extract_text(pdf_file_path)))
    print(f"{filename} was converted!")


def analysePDF():

    pdf_dir = j.load_attr('PDF_path')
    output_dir = j.load_attr('test_encording')

    if not os.path.exists(output_dir):
        print("Path:{} doesn't exist. Now it's being created.".format(output_dir))
        os.mkdir(output_dir)

    pdf_files = [x for x in os.listdir(pdf_dir) if x.endswith(".pdf") or x.endswith(".PDF")]

    pdf_files_num = len(pdf_files)
    if pdf_files_num == 0:
        raise Exception("No pdf file was found in path:{}".format(pdf_dir))

    for idx, pdf_name in enumerate(pdf_files):
        pdf_file_path = os.path.join(pdf_dir, pdf_name)
        text_file_path = os.path.join(output_dir, pdf_name[0:-4] + ".txt")
        with open(text_file_path, "w", encoding='utf-16') as text_file:
            text_file.write(re.sub("[^\n]\n[^\n]", "" , extract_text(pdf_file_path,codec='utf-16')))
        print("{}/{}: {} was converted!".format(idx+1, pdf_files_num, pdf_name))


if __name__=='__main__':
    analysePDF()