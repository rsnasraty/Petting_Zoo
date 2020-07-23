

class PettingZoo:

    def __init__(self, attraction_name, description):
        self.attraction_name = attraction_name
        self.description = description
        self.animals = []

    def add_animals(self, animal):
        self.animals.append(animal)

    @property
    def last_critter_added(self):
        return f'{self.animals[-1].name} the {self.animals[-1].species}'


class SnakePit:

    def __init__(self, attraction_name, description):
        self.attraction_name = attraction_name
        self.description = description
        self.animals = []

    def add_animals(self, animal):
        self.animals.append(animal)

    @property
    def last_critter_added(self):
        return f'{self.animals[-1].name} the {self.animals[-1].species}'

class Wetlands:

    def __init__(self, attraction_name, description):
        self.attraction_name = attraction_name
        self.description = description
        self.animals = []
    
    def add_animals(self, animal):
        self.animals.append(animal)

    @property
    def last_critter_added(self):
        return f'{self.animals[-1].name} the {self.animals[-1].species}'