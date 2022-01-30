from lion import Lion
from elephant import Elephant
from penguin import Penguin

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    
    def add_animal(self, animal):
        self.animals.append(animal)
        return self
    
    def get_all_animals(self):
        for animal in self.animals:
            print(animal.display_info())

kazoo = Zoo("KaZoo")
kazoo.add_animal(Lion("Simba", 6, 80, 80, "Prince")).add_animal(Elephant("Dumbo", 25, 80, 75, "Big ears")).add_animal(Penguin("Brad", 18, 90, 70, "Happy feet"))
kazoo.get_all_animals()