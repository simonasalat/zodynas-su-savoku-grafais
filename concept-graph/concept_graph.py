import pyvis.network
from classes import Triplet
from classes import Entity

pyvis_graph = pyvis.network.Network(notebook=True, width='100%', height='100%', cdn_resources='remote')

def create_new_node(entity, color, size):
    pyvis_graph.add_node(entity, label=entity, title="", color=color, size=size)

def create_new_relation(entity1, entity2, relation):
    pyvis_graph.add_edge(entity1, entity2, label=relation, color="black")
    
def make_triplet(word, related_entities):
    create_new_node(word, "red", 25)
    for related in related_entities:
        create_new_node(related.entity, "pink", 18)
        create_new_relation(word, related.entity, related.relation)
    return related_entities

def make_list_of_related_entities(triplets, word):
    related_entities = []
    for triplet in triplets:
        if triplet.entity1 == word:
            related_entities.append(Entity(triplet.entity2, triplet.relation))
        if triplet.entity2 == word:
            related_entities.append(Entity(triplet.entity1, triplet.relation))
    return related_entities


def add_first_and_second_level_entities(related_entities, triplets, color, size):
    for entity in related_entities:
        smaller_relations = make_list_of_related_entities(triplets, entity.entity)
        triplets = remove_triplets(triplets, entity.entity)
        for smaller in smaller_relations:
            create_new_node(smaller.entity, color, size)
            create_new_relation(entity.entity, smaller.entity, smaller.relation)
        add_second_level_entities(smaller_relations, triplets, "green", 7)

def add_only_first_level_entities(related_entities, triplets, color, size):
    for entity in related_entities:
        smaller_relations = make_list_of_related_entities(triplets, entity.entity)
        triplets = remove_triplets(triplets, entity.entity)
        for smaller in smaller_relations:
            create_new_node(smaller.entity, color, size)
            create_new_relation(entity.entity, smaller.entity, smaller.relation)

def add_second_level_entities(related_entities, triplets, color, size):
    for entity in related_entities:
        i = 0
        smaller_relations = make_list_of_related_entities(triplets, entity.entity)
        triplets = remove_triplets(triplets, entity.entity)
        for smaller in smaller_relations:
            create_new_node(smaller.entity, color, size)
            create_new_relation(entity.entity, smaller.entity, smaller.relation)
            i += 1
            if i > 2:
                break

def remove_triplets(triplets, word):
    new_list = []
    for triplet in triplets:
        if triplet.entity1 != word and triplet.entity2 != word:
            new_list.append(triplet)
    return new_list

def draw_graph(triplets, concept):
    word = concept.capitalize()
    related_entities = make_list_of_related_entities(triplets, word)
    triplets = remove_triplets(triplets, word)
    for triplet in triplets:
        print(triplet)
    related_entities2 = make_triplet(word, related_entities)
    for triplet in related_entities2:
        print(triplet)
    add_first_and_second_level_entities(related_entities2, triplets, "grey", 13)
    pyvis_graph.force_atlas_2based()
    ##pyvis_graph.show_buttons(filter_="physics")
    pyvis_graph.show("grafai_html/" + concept + ".html")

##t1 = Triplet("Vilnius", "Neris", "teka")
##t2 = Triplet("Neris", "upė", "yra")
##t3 = Triplet("upė", "jūra", "įteka")
##t4 = Triplet("Vilnius", "universitetas", "turi")
##t5 = Triplet("Nemunas", "Neris", "iteka")
##t6 = Triplet("Nemunas", "Kaunas", "teka")
##t7 = Triplet("Nemunas", "Baltijos jūra", "teka")
##t8 = Triplet("upė", "žuvis", "plaukia")
##t9 = Triplet("upė", "baidarė", "plaukia")
##t10 = Triplet("upė", "tiltas", "pastatytas virš")
##t11 = Triplet("Vilnius", "tiltas", "turi")
##t12 = Triplet("Kaunas", "marios", "turi")
##t13 = Triplet("jūra", "marios", "prie")
##t14 = Triplet("žvejys", "žuvis", "žvejoja")
##t15 = Triplet("Baltijos jūra", "jūra", "pavadinimas")

##triplets = [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15]
##triplets = [Triplet("Vilnius", "Neris", "teka"), Triplet("Neris", "upė", "yra"), Triplet("upė", "jūra", "įteka"), Triplet("Vilnius", "universitetas", "turi"), Triplet("Nemunas", "Neris", "iteka"),Triplet("Nemunas", "Kaunas", "teka")]



