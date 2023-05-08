class Triplet:
    def __init__(self, entity1, entity2, relation):
        self.entity1 = entity1
        self.entity2 = entity2
        self.relation = relation
    def __str__(self):
        return f"{self.entity1}, {self.entity2}, {self.relation}"

class Entity:
    def __init__(self, entity, relation):
        self.entity = entity
        self.relation = relation
    def __str__(self):
        return f"{self.entity}, {self.relation}"
    def add_id(self, id):
        self.id = id