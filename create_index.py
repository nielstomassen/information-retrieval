import pyterrier as pt
import pandas as pd
import shutil
import os

dataset = pt.get_dataset("msmarco_passage")
# Define where to store the index
index_path = "./msmarco_index"
# Remove the existing index if it exists
if os.path.exists(index_path):
    print("Removing existing index...")
    shutil.rmtree(index_path)

def msmarco_generate():
    n=100000
    count = 0
    with pt.io.autoopen(dataset.get_corpus()[0], 'rt') as corpusfile:
        for l in corpusfile:
            docno, passage = l.split("\t")
            yield {'docno' : docno, 'text' : passage}
            count+=1
            if(count % n == 0):
                print (f"processed {count} documents...")

iter_indexer = pt.IterDictIndexer(index_path, meta={'docno': 20, 'text': 4096})
indexref3 = iter_indexer.index(msmarco_generate())

print("Indexing complete! Index saved at:", index_path)
