from animal import Animal

class Penguin(Animal):
    def __init__(self, name, age, health_level, happiness_level, unique_attr):
        super().__init__(name, age, health_level, happiness_level)
        self.unique_attr = unique_attr

    def feed(self):
        self.health_level += 25
        self.happiness_level += 20
        return ("PRRRTTTPRRTT!!! {} is happy! Health level increased by 25 and Happiness level increased by 20!").format(self.name)