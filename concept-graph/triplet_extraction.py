import spacy
import lt_text_patterns
from spacy.matcher import Matcher
from classes import Triplet

nlp = spacy.load("lt_core_news_lg")
matcher = Matcher(nlp.vocab)
patterns = lt_text_patterns.get_lt_patterns()
matcher.add("Related_entities", patterns) 

def extract_entities_with_relation(sentence):
    doc = nlp(sentence)
    matches = matcher(doc)
    triplets = []
    for match_id, start, end in matches:
        verb_elem = ""
        for i in range(start, end):
            if doc[i].pos_ == "VERB":
             verb_elem = doc[i].text
             break
        triplets.append(Triplet(doc[start].lemma_, doc[end-1].lemma_, verb_elem))
    return triplets

def extract_entities_with_relation_as_text(sentence):
    doc = nlp(sentence)
    matches = matcher(doc)
    triplets = []
    for match_id, start, end in matches:
        verb_elem = ""
        for i in range(start, end):
            if doc[i].pos_ == "VERB":
             verb_elem = doc[i].text
             break
        triplets.append([doc[start].lemma_, doc[end-1].lemma_, verb_elem])
    return triplets

def sentence_segmentation(text):
    doc = nlp(text)
    sentences = [sent.text for sent in doc.sents]
    return sentences

def extract_entities(sentence):
    doc = nlp(sentence)
    matches = matcher(doc)
    entities = []
    for match_id, start, end in matches:
        entities.append((doc[start].lemma_, doc[end-1].lemma_))
    return entities

def extract_entities_from_text(text):
    sentences = sentence_segmentation(text)
    related_entities = []
    for sentence in sentences:
        related_entities.append(extract_entities(sentence))
    return related_entities



