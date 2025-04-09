import pyterrier as pt
import pandas as pd
import re
qid_to_lookup = '1051808'

queries = pd.read_parquet("modified_queries_2.parquet")

print(queries.head(20))