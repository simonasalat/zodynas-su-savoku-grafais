# Creating Concept graph from Lithuanian text

## Files
classes.py - Entity and Triplet class

concept_graph.py - create concept graph

lt_text_patterns.py - text patterns used to find entities and relations

main.py - main program

print_sentence_pos.py - print POS of words

triplet_extraction.py - extract triplets - entities and relations from text

triplet_manager.py - remove dublicates, edit words

## Installation
```sh
virtualenv venv
source venv/bin/activate
pip install –U pip setuptools wheel
pip install –U spacy
python –m spacy download lt_core_news_lg
pip install pyvis
```

## Before running the code
in main.py 
- change the text file name, from which the triplets have to be extracted
- change the center word, based on it the graph is going to be created


## Run code
```sh
cd savoku_grafas
python3 main.py  
```
