# information-retrieval code switching retrieval experiments
This is the GitHub repository for evaluating retrieval performance under various degrees of code switching.

## How to Run

The `modified_queries` folder contains query files with varying degrees of code-switching. The number in each filename indicates how many code-switched words are in that query. If you’d like to generate code-switched queries on a different dataset, you can use `modify_queries.py`. Adjust the `degrees` parameter to control the number of words to be code-switched.

The `create_index.py` script was used to build a custom MS MARCO index. This was necessary during a period when `data.terrier.org` was unavailable, preventing us from using PyTerrier’s built-in indexes. As a workaround, we indexed the MS MARCO document collection ourselves using the logic in this file. Once the PyTerrier index hosting service was restored, we switched back to using its built-in functionality and confirmed that the results matched our custom-built index.

To run the retrieval experiments, use `retrieve_documents.py`. This script tests all degrees of code-switching in a single execution, so ensure you have the appropriate modified query files in place. Results are saved in the `results` folder. We’ve included our results in this branch, so you can view them directly without re-running the experiments.
