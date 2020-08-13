# import the python datetime module to help us create a timestamp
from datetime import date
from attractions import SnakePit
from attractions import PettingZoo
from attractions import Wetlands

class Animal:
    def __init__(self, name, species, food, chip_num):
        self.name = name
        self.species = species
        self.food = food
        self.__chip_number = chip_num
        self.date_added = date.today()

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
    
    @property
    def chip_number(self):
        return self.__chip_number
    
    @chip_number.setter
    def chip_number(self, num):
        pass











critter_cove = Wetlands ("Wetlands", " Gatlinburg's only one-acre walk-through wetlands and wet bar, full of feathered friends and fantastic fish!")

critter_cove.add_animals(quackers)
critter_cove.add_animals(goldeen)
critter_cove.add_animals(odette)
critter_cove.add_animals(jinli)

slither_inn = SnakePit("Slither Inn", "more snakes than an Indiana Jones movie ")

slither_inn.add_animals(snakey)
slither_inn.add_animals(mister_cobra)
slither_inn.add_animals(monty)
slither_inn.add_animals(b_sizzle)
slither_inn.add_animals(chip)


varmint_village = PettingZoo("Varmint Village", "a petting zoo filled with your favorite animals")

varmint_village.add_animals(kuzco)
varmint_village.add_animals(shrek)
varmint_village.add_animals(googles)


print("last critter function", varmint_village.last_critter_added)

for animal in varmint_village.animals:
    print(f'You can find {animal.name} the {animal.species} in {varmint_village.attraction_name}')

for animal in slither_inn.animals:
    print(f'You can find {animal.name} the {animal.species} in {slither_inn.attraction_name}')

for animal in critter_cove.animals:
    print(f'You can find {animal.name} the {animal.species} in {critter_cove.attraction_name}')