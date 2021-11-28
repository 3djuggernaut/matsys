import os
pdf_src="../../PDF"
pdf_des="../PDF"
max_num=100

count=0
for item in os.listdir(pdf_src):
    os.system(f'cp {pdf_src}/{item} {pdf_des}')
    count+=1
    if count > max_num:
        break