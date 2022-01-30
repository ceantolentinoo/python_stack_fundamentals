from animal import Animal

class Lion(Animal):
    def __init__(self, name, age, health_level, happiness_level, unique_attr):
        super().__init__(name, age, health_level, happiness_level)
        self.unique_attr = unique_attr

    def feed(self):
        self.health_level += 10
        self.happiness_level += 15
        return ("ROOOARR!! {} is happy! Health level increased by 10 and Happiness level increased by 15!").format(self.name)

