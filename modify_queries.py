import pyterrier as pt
import random
import spacy
from deep_translator import GoogleTranslator
import re

dataset = pt.get_dataset("msmarco_passage")
queries = dataset.get_topics("dev.small")

nlp = spacy.load("en_core_web_sm")

def modify_query(query):
    doc = nlp(query)
    
    content_words = [token.text for token in doc if token.pos_ in ["NOUN", "VERB", "ADJ"]]
    
    if not content_words:
        return query 

    word_to_replace = random.choice(content_words)
    
    try: 
        translated_word = GoogleTranslator(source='en', target='nl').translate(word_to_replace)
    except Exception as e:
        print(f"Error translating '{word_to_replace}': {e}")
        translated_word = word_to_replace
    
    modified_query = query.replace(word_to_replace, translated_word, 1)
    return modified_query

# Clean the queries to remove or escape special characters
def clean_query(query):
    query = re.sub(r"[^\w\s]", "", query)  # Remove non-alphanumeric characters, keep accented ones
    return query

# Apply the translations
queries['query'] = queries['query'].apply(modify_query)
# Apply the cleaning function to all queries
queries['query'] = queries['query'].apply(clean_query)

queries.to_parquet("modified_queries.parquet", index=False)

