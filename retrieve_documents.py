import pyterrier as pt
import pandas as pd

# Run Experiments
# Make sure you have the relevant modified queries in the correct folder when running this.
dataset = pt.get_dataset("msmarco_passage")

bm25 = pt.BatchRetrieve.from_dataset('msmarco_passage', 'terrier_stemmed', wmodel='BM25')
pl2 = pt.BatchRetrieve.from_dataset('msmarco_passage', 'terrier_stemmed', wmodel='PL2')
tfidf = pt.BatchRetrieve.from_dataset('msmarco_passage', 'terrier_stemmed', wmodel='TF_IDF')
dph = pt.BatchRetrieve.from_dataset('msmarco_passage', 'terrier_stemmed', wmodel='DPH')
dirichletLM = pt.BatchRetrieve.from_dataset('msmarco_passage', 'terrier_stemmed', wmodel='DirichletLM')

code_switched_queries = pd.read_parquet("./modified_queries/modified_queries_1.parquet")
print("Regular queries: \n")
print(pt.Experiment(
    [bm25, pl2, tfidf, dph, dirichletLM],
    dataset.get_topics("dev.small"),
    dataset.get_qrels("dev.small"),
    eval_metrics=["map", "recip_rank", "num_ret", "num_rel", "num_rel_ret", "P_5", "P_10", "recall_5", "recall_10"],
    names=["BM25", "PL2", "TF-IDF", "DPH", "dirichletLM"],
    save_dir="./results/baseline",
    save_mode="overwrite"
))

print("One code switched word: \n")
print(pt.Experiment(
    [bm25, pl2, tfidf, dph, dirichletLM],
    code_switched_queries,
    dataset.get_qrels("dev.small"),
    eval_metrics=["map", "recip_rank", "num_ret", "num_rel", "num_rel_ret", "P_5", "P_10", "recall_5", "recall_10"],
    names=["BM25", "PL2", "TF-IDF", "DPH", "dirichletLM"],
    save_dir="./results/modified-1",
    save_mode="overwrite"
))

code_switched_queries = pd.read_parquet("./modified_queries/modified_queries_2.parquet")
print("Two code switched words: \n")
print(pt.Experiment(
    [bm25, pl2, tfidf, dph, dirichletLM],
    code_switched_queries,
    dataset.get_qrels("dev.small"),
    eval_metrics=["map", "recip_rank", "num_ret", "num_rel", "num_rel_ret", "P_5", "P_10", "recall_5", "recall_10"],
    names=["BM25", "PL2", "TF-IDF", "DPH", "dirichletLM"],
    save_dir="./results/modified-2",
    save_mode="overwrite"
))

code_switched_queries = pd.read_parquet("./modified_queries/modified_queries_3.parquet")
print("Three code switched words: \n")
print(pt.Experiment(
    [bm25, pl2, tfidf, dph, dirichletLM],
    code_switched_queries,
    dataset.get_qrels("dev.small"),
    eval_metrics=["map", "recip_rank", "num_ret", "num_rel", "num_rel_ret", "P_5", "P_10", "recall_5", "recall_10"],
    names=["BM25", "PL2", "TF-IDF", "DPH", "dirichletLM"],
    save_dir="./results/modified-3",
    save_mode="overwrite"
))