##import esybiu_istraukimas_lt
import triplet_extraction
import concept_graph
import triplet_manager

file = open('Wikipedia_tekstai/vilniaus_universitetas.txt', 'r')
content = file.read()
file.close()

extracted_entities = triplet_extraction.extract_entities_with_relation(content)
triplets = triplet_manager.remove_dublicates(extracted_entities)
triplets = triplet_manager.first_capital(triplets)
concept_graph.draw_graph(triplets, "universitetas")

