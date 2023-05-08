def get_lt_patterns():
    patterns = []
    patterns.append([{"POS": {"IN": ["NOUN", "PROPN", "ADJ"]}}, {"POS": {"IN": ["NOUN", "PROPN"]}}])
    patterns.append([{"POS": {"IN": ["NOUN", "PROPN"]}}, {"POS": {"IN": ["NOUN", "PROPN"]}}, {"POS": {"IN": ["NOUN", "PROPN"]}}])
    patterns.append([{"POS": {"IN": ["NOUN", "PROPN", "ADJ"]}}, {"POS": "VERB"}, {"POS": {"IN": ["NOUN", "PROPN", "ADJ"]}}])
    patterns.append([{"POS": {"IN": ["NOUN", "PROPN"]}}, {"POS": "VERB"}, {"POS": "ADP"}, {"POS": {"IN": ["NOUN", "PROPN"]}}])
    patterns.append([{"POS": {"IN": ["NOUN", "PROPN"]}}, {"POS": { "IN" : [ "VERB", "ADP"]}}, {"POS": {"IN": ["NOUN", "PROPN"]}},  {"POS": "CCONJ"}, {"POS": {"IN": ["NOUN", "PROPN"]}}])
    patterns.append([{"POS": {"IN": ["NOUN", "PROPN"]}}, {"POS": {"IN": ["VERB", "ADP", "CCONJ"]}}, {"POS": {"IN": ["NOUN", "PROPN"]}}])
    patterns.append([{"POS": {"IN": ["NOUN", "PROPN"]}}, {"POS": "AUX", "OP": "?"}, {"POS": "VERB"}, {"POS": "ADP"}, {"POS": {"IN": ["NOUN", "PROPN"]}}])
    patterns.append([{"POS": {"IN": ["NOUN", "PROPN"]}}, {"POS": {"IN": ["VERB", "ADP", "CCONJ"]}}, {"POS": "PRON", "OP" : "?"}, {"POS": {"IN": ["NOUN", "PROPN"]}}])
    patterns.append([{"POS": {"IN": ["NOUN", "PROPN"]}}, {"TEXT": "–"}, {"POS": {"IN": ["PRON", "ADV"]}, "OP" : "?"}, {"POS": {"IN": ["NOUN", "PROPN"]}}, {"POS": {"IN": ["NOUN", "PROPN"]}}])
    patterns.append([{"POS": {"IN": ["NOUN", "PROPN"]}}, {"TEXT": "–"}, {"POS": {"IN": ["PRON", "ADV"]}, "OP" : "?"}, {"POS": {"IN": ["NOUN", "PROPN", "ADJ"]}}])
    patterns.append([{"POS": {"IN": ["NOUN", "PROPN"]}}, {"TEXT": "–"}, {"POS": "ADJ"}, {"POS": "CCONJ"},  {"POS": "ADJ"}])
    patterns.append([{"POS": {"IN": ["NOUN", "PROPN"]}}, {"TEXT": "–"}, {"POS": "ADJ"}, {"TEXT": ","},  {"POS": "ADJ"}])
    patterns.append([{"POS": {"IN": ["NOUN", "PROPN"]}}, {"TEXT": ","}, {"POS": "DET", "OP": "?"}, {"POS": {"IN": ["CONJ", "SCONJ"]}}, {"TEXT": ":"}, {"POS": {"IN": ["NOUN", "PROPN"]}}])
    patterns.append([{"POS": {"IN": ["NOUN", "PROPN"]}}, {"TEXT": ","}, {"POS": "DET", "OP": "?"}, {"POS": {"IN": ["CONJ", "SCONJ"]}}, {"TEXT": ":"}, {"POS": {"IN": ["NOUN", "PROPN"]}}, {"TEXT": ","},  {"POS": {"IN": ["NOUN", "PROPN"]}}])
    patterns.append([{"POS": {"IN": ["NOUN", "PROPN"]}}, {"TEXT": ","}, {"POS": "DET", "OP": "?"}, {"POS": {"IN": ["CONJ", "SCONJ"]}}, {"TEXT": ":"}, {"POS": {"IN": ["NOUN", "PROPN"]}}, {"TEXT": ","},  {"POS": {"IN": ["NOUN", "PROPN"]}}, {"TEXT": ","},  {"POS": {"IN": ["NOUN", "PROPN"]}}])
    return patterns
