from animal import Animal

class Elephant(Animal):
    def __init__(self, name, age, health_level, happiness_level, unique_attr):
        super().__init__(name, age, health_level, happiness_level)
        self.unique_attr = unique_attr

    def feed(self):
        self.health_level += 20
        self.happiness_level += 15
        return ("HURREERREERR!! {} is happy! Health level increased by 20 and Happiness level increased by 15!").format(self.name)