from classes import Triplet

def remove_dublicates(triplets):
    for triplet in triplets:
        if triplet.entity1 == triplet.entity2:
            triplets.remove(triplet)
    return triplets

def lower_case(triplets):
    for triplet in triplets:
        triplet.entity1 = triplet.entity1.lower()
        triplet.entity2 = triplet.entity2.lower()
    return triplets

def first_capital(triplets):
    for triplet in triplets:
        triplet.entity1 = triplet.entity1.capitalize()
        triplet.entity2 = triplet.entity2.capitalize()
    return triplets