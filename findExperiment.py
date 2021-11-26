import torch
import os
from synthesis_classifier import get_model, get_tokenizer, run_batch
import jconfig

def findExperiment_process():
    txt_path=jconfig.load_attr('FILTED')
    exp_path=jconfig.load_attr('EXP')
    model = get_model()
    tokenizer = get_tokenizer()

    total=len(os.listdir(txt_path))
    count=0
    for item in os.listdir(txt_path):
        with open(os.path.join(txt_path,item), 'r') as fdr:
            paragraphs = list(map(str.strip, fdr))

        fdw=open(os.path.join(exp_path,item),'w')

        tmp=""

        batch_size = 2
        batches = [paragraphs[i:min(i + batch_size, len(paragraphs))]
                for i in range(0, len(paragraphs), batch_size)]

        for batch in batches:
            result = run_batch(batch, model, tokenizer)
            for t in result:
                if t.__contains__('text'):
                    tmp+=t['text']

        fdw.write(tmp)
        count+=1
        print(f'{count}/{total}:FINISH EXP EXTRACT {item}:')
        fdr.close()
        fdw.close()

if __name__=='__main__':
    findExperiment_process()
