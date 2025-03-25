import pyterrier as pt
import pandas as pd
import re
qid_to_lookup = '1051808'

queries = pd.read_parquet("modified_queries.parquet")


# Clean the queries to remove or escape special characters
def clean_query(query):

    query = re.sub(r"[^\w\s]", "", query) # Remove non-alphanumeric characters
    
    return query

# Apply the cleaning function to all queries
queries['query'] = queries['query'].apply(clean_query)

queries.to_parquet("modified_queries.parquet", index=False)