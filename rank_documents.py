import pyterrier as pt
import pandas as pd
from pyterrier.measures import RR, nDCG, MAP

# Path where the index is stored
index_path = "./msmarco_index"

# # Load the index from the given path
# index = pt.IndexFactory.of(index_path)

# # Create BM25 retrieval model
# bm25 = pt.terrier.Retriever(index, wmodel="BM25")

# load just inverted and lexicon into memory
inmem_inverted_index = pt.IndexFactory.of("./msmarco_index/data.properties", memory=['inverted', 'lexicon'])
bm25_fast = pt.terrier.Retriever(inmem_inverted_index, wmodel="BM25")

# Load queries
dataset = pt.get_dataset("msmarco_passage")

queries = pd.read_parquet("modified_queries.parquet")

pt.Experiment(
    [bm25_fast],
    queries,
    dataset.get_qrels("dev.small"),
    eval_metrics=[RR @ 10, nDCG @ 20, MAP],
)