import pyterrier as pt
import random
import spacy
from deep_translator import GoogleTranslator
import pandas as pd

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

print(queries['query'].head())

# queries.to_parquet("modified_queries.parquet", index=False)

