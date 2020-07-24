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




# 1


class Hognose_Snake(Animal):

    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True

    @property
    def chip_number(self):
        return self.__chip_number

    @chip_number.setter # The setter
    def chip_number(self, num):
        pass

    def feed(self):
        print(f'{self.name} was fed a light serving of {self.food} on   {date.today().strftime("%m/%d/%Y")}.')

    def __str__(self):
        return f"{self.name} is a {self.species}"

snakey = Hognose_Snake("Snakey","Hognose Snake", "Mice", 123789)
print(snakey)
snakey.feed()

# 2

class Cobra:

    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}.')
    def __str__(self):
        return f"{self.name} is a {self.species}"

mister_cobra = Cobra("Mister Cobra", "Cobra", "Mice")
print(mister_cobra)
mister_cobra.feed()

# 3


class Python:

    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}.')
    def __str__(self):
        return f"{self.name} is a {self.species}"

monty = Python("Monty", "Python", "Mice")
print(monty)
monty.feed()

# 4


class Boa_Constrictor:

    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}.')
    def __str__(self):
        return f"{self.name} is a {self.species}"
b_sizzle = Boa_Constrictor("B-Sizzle", "Boa Constrictor", "Mice")
print(b_sizzle)
b_sizzle.feed()

# 5


class Corn_Snake:

    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}.')
    def __str__(self):
        return f"{self.name} is a {self.species}"
chip = Corn_Snake("Chip", "Corn Snake", "Mice")
print(chip)
chip.feed()


# 6


class Emu:

    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift 
        self.walking = True


    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}.')
    def __str__(self):
        return f"{self.name} is a {self.species}"
googles = Emu("Googles", "Emu", "morning", "Emu Chow")
print(f'{googles.name} the {googles.species} is available to pet during the {googles.shift} shift.')
print(googles)
googles.feed()

# 7


class Llama:

    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift 
        self.walking = True

    def feed(self):
        print(f'on {date.today()}, {self.name} had "Rockytop" sung to it so it would eat its {self.food}')
    def __str__(self):
        return f"{self.name} is a {self.species}"
kuzco = Llama("Kuzco", "Llama", "Afternoon", "Fruit")

print(f'{kuzco.name} the {kuzco.species} is available to pet during the {kuzco.shift} shift.')
print(kuzco)
print(kuzco.feed())


# 8


class Donkey:

    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift 
        self.walking = True

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}.')
    def __str__(self):
        return f"{self.name} is a {self.species}"
shrek = Donkey("Shrek", "Donkey", "morning", "pasta")
print(f'{shrek.name} the {shrek.species} is available to pet during the {shrek.shift} shift.')
print(shrek)
print(shrek.feed())

# 9


class Goat:

    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift 
        self.walking = True

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}.')
    def __str__(self):
        return f"{self.name} is a {self.species}"
billy = Goat("Billy", "Goat", "Afternoon", "Grass")
print(f'{billy.name} the {billy.species} is available to pet during the {billy.shift} shift.')
print(billy)
print(billy.feed())

# 10


class Zebra:

    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift 
        self.walking = True

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}.')
    def __str__(self):
        return f"{self.name} is a {self.species}"

z_man = Zebra("Z-Man", "Zebra", "afternoon", "Berries")
print(f'{z_man.name} the {z_man.species} is available to pet during the {z_man.shift} shift.')
print(z_man)
print(z_man.feed())

# 11


class Mallard:

    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swimming = True

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}.')
    def __str__(self):
        return f"{self.name} is a {self.species}"
quackers = Mallard("Quackers", "Duck", "Bread")
print(quackers)
print(quackers.feed())

#12
class Goldfish:

    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swimming = True

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}.')
    def __str__(self):
        return f"{self.name} is a {self.species}"

goldeen = Goldfish("Goldeen", "Goldfish", "Fish Food")
print(goldeen)
print(goldeen.feed())

# 13


class Swan:

    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swimming = True

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}.')
    def __str__(self):
        return f"{self.name} is a {self.species}"

odette = Swan("Odette", "Swan", "Swan Snacks")
print(odette)
print(odette.feed())

# 14


class Koi:

    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swimming = True

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}.')

    def __str__(self):
        return f"{self.name} is a {self.species}"

jinli = Koi("Jinli", "Koi", "Koi Krunchies")
print(jinli)
print(jinli.feed())
# 15


class Goose:

    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swimming = True

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}.')

    def __str__(self):
        return f"{self.name} is a {self.species}"

untitled = Goose("Untitled", "Goose", "Bread")
print(untitled)
print(untitled.feed())



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