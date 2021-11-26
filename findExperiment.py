import torch
import os
from synthesis_classifier import get_model, get_tokenizer, run_batch
import jconfig

def findExperiment_process():
    txt_path=jconfig.load_attr('PDF_text')
    exp_path=jconfig.load_attr('PDF_exp')
    model = get_model()
    tokenizer = get_tokenizer()

    for item in os.listdir(txt_path):
        with open(os.path.join(txt_path,item), 'r') as fdr:
            paragraphs = list(map(str.strip, fdr))

        fdw=open(os.path.join(exp_path,item),'w')

        tmp=""
        print(f'{item}:')

        batch_size = 2
        batches = [paragraphs[i:min(i + batch_size, len(paragraphs))]
                for i in range(0, len(paragraphs), batch_size)]

        for batch in batches:
            result = run_batch(batch, model, tokenizer)
            print('*'*40)
            # print(result)
            for item in result:
                if item.__contains__('text'):
                    tmp+=item['text']

        fdw.write(tmp)
        fdr.close()
        fdw.close()

    
