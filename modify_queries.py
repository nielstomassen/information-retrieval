import pyterrier as pt
import random
import spacy
from deep_translator import GoogleTranslator
import re

dataset = pt.get_dataset("msmarco_passage")
queries = dataset.get_topics("dev.small")

nlp = spacy.load("en_core_web_sm")

def modify_query(query, degrees):
    doc = nlp(query)
    
    content_words = [token.text for token in doc if token.pos_ in ["NOUN", "VERB", "ADJ"]]
    
    if not content_words:
        return query 
    
    # Limit degrees to the number of available content words. 
    degrees = min(degrees, len(content_words))

    words_to_replace = random.sample(content_words, degrees)
    modified_query = query
    
    for word in words_to_replace:
        try:
            translated_word = GoogleTranslator(source='en', target="nl").translate(word)
        except Exception as e:
            print(f"Error translating '{word}': {e}")
            translated_word = word  # Fallback to original word if translation fails

        modified_query = modified_query.replace(word, translated_word, 1)

    return modified_query

# Clean the queries to remove or escape special characters
def clean_query(query):
    query = re.sub(r"[^\w\s]", "", query)  # Remove non-alphanumeric characters, keep accented ones
    return query

# Apply the translations, modify degrees for amount of words to change
queries['query'] = queries['query'].apply(lambda x: modify_query(x, degrees=3))
# Apply the cleaning function to all queries
queries['query'] = queries['query'].apply(clean_query)


queries.to_parquet("modified_queries_3.parquet", index=False)
print(queries.head())
