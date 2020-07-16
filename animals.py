# import the python datetime module to help us create a timestamp
from datetime import date

# 1


class Hognose_Snake:

    def __init__(self, name, species, food):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on   {date.today().strftime("%m/%d/%Y")}.')
    def __str__(self):
        return f"{self.name} is a {self.species}"

snakey = Hognose_Snake("Snakey","Hognose Snake", "Mice")
print(snakey)
print(snakey.feed())

# 2

class Cobra:

    def __init__(self, name, species, food):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}.')
    def __str__(self):
        return f"{self.name} is a {self.species}"

mister_cobra = Cobra("Mister Cobra", "Cobra", "Mice")
print(mister_cobra)
print(mister_cobra.feed())

# 3


class Python:

    def __init__(self, name, species, food):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}.')
    def __str__(self):
        return f"{self.name} is a {self.species}"

monty = Python("Monty", "Python", "Mice")
print(monty)
print(monty.feed())

# 4


class Boa_Constrictor:

    def __init__(self, name, species, food):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}.')
    def __str__(self):
        return f"{self.name} is a {self.species}"
b_sizzle = Boa_Constrictor("B-Sizzle", "Boa Constrictor", "Mice")
print(b_sizzle)
print(b_sizzle.feed())

# 5


class Corn_Snake:

    def __init__(self, name, species, food):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}.')
    def __str__(self):
        return f"{self.name} is a {self.species}"
chip = Corn_Snake("Chip", "Corn Snake", "Mice")
print(chip)
print(chip.feed())

# 6


class Emu:

    def __init__(self, name, species, shift, food):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}.')
    def __str__(self):
        return f"{self.name} is a {self.species}"
googles = Emu("Googles", "Emu", "morning", "Emu Chow")
print(f'{googles.name} the {googles.species} is available to pet during the {googles.shift} shift.')
print(googles)
print(googles.feed())
# 7


class Llama:

    def __init__(self, name, species, shift, food):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}.')
    def __str__(self):
        return f"{self.name} is a {self.species}"
kuzco = Llama("Kuzco", "Llama", "Afternoon", "Fruit")

print(f'{kuzco.name} the {kuzco.species} is available to pet during the {kuzco.shift} shift.')
print(kuzco)
print(kuzco.feed())


# 8


class Donkey:

    def __init__(self, name, species, shift, food):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
        self.food = food

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

    def __init__(self, name, species, shift, food):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
        self.food = food

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

    def __init__(self, name, species, shift, food):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
        self.food = food

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

    def __init__(self, name, species, food):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}.')
    def __str__(self):
        return f"{self.name} is a {self.species}"
quackers = Mallard("Quackers", "Duck", "Bread")
print(quackers)
print(quackers.feed())

#12
class Goldfish:

    def __init__(self, name, species, food):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}.')
    def __str__(self):
        return f"{self.name} is a {self.species}"

goldeen = Goldfish("Goldeen", "Goldfish", "Fish Food")
print(goldeen)
print(goldeen.feed())

# 13


class Swan:

    def __init__(self, name, species, food):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}.')
    def __str__(self):
        return f"{self.name} is a {self.species}"

odette = Swan("Odette", "Swan", "Swan Snacks")
print(odette)
print(odette.feed())

# 14


class Koi:

    def __init__(self, name, species, food):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}.')

    def __str__(self):
        return f"{self.name} is a {self.species}"

jinli = Koi("Jinli", "Koi", "Koi Krunchies")
print(jinli)
print(jinli.feed())
# 15


class Goose:

    def __init__(self, name, species, food):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}.')

    def __str__(self):
        return f"{self.name} is a {self.species}"

untitled = Goose("Untitled", "Goose", "Bread")
print(untitled)
print(untitled.feed())