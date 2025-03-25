import pandas as pd
import pyterrier as pt

# bm25 = pt.BatchRetrieve(pt.get_dataset("msmarco_passage").get_index(), wmodel="BM25")
df = pd.read_parquet("modified_queries.parquet")


dataset = pt.get_dataset("msmarco_passage")
# Path to MSMARCO passage collection
collection_path = dataset.get_corpus()[0]  # Gets "collection.tsv.gz"

# Load into DataFrame
docs = pd.read_csv(collection_path, sep="\t", names=["docno", "text"], compression="gzip")

# Show some samples
print(docs.head())