# import the python datetime module to help us create a timestamp
from datetime import date

# 1


class Hognose_Snake:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True


snakey = Hognose_Snake("Snakey","Hognose Snake")

# 2


class Cobra:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True


mister_cobra = Cobra("Mister Cobra", "Cobra")

# 3


class Python:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True


monty = Python("Monty", "Python")

# 4


class Boa_Constrictor:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True


b_sizzle = Boa_Constrictor("B-Sizzle", "Boa Constrictor")

# 5


class Corn_Snake:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True


chip = Corn_Snake("Chip", "Corn Snake")

# 6


class Emu:

    def __init__(self, name, species, shift):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

        self.shift = shift

googles = Emu("Googles", "Emu", "morning")
print(f'{googles.name} the {googles.species} is available to pet during the {googles.shift} shift.')
# 7


class Llama:

    def __init__(self, name, species, shift):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift


kuzco = Llama("Kuzco", "Llama", "Afternoon")

print(f'{kuzco.name} the {kuzco.species} is available to pet during the {kuzco.shift} shift.')



# 8


class Donkey:

    def __init__(self, name, species, shift):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift

shrek = Donkey("Shrek", "Donkey", "morning")
print(f'{shrek.name} the {shrek.species} is available to pet during the {shrek.shift} shift.')

# 9


class Goat:

    def __init__(self, name, species, shift):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift


billy = Goat("Billy", "Goat", "Afternoon")
print(f'{billy.name} the {billy.species} is available to pet during the {billy.shift} shift.')

# 10


class Zebra:

    def __init__(self, name, species, shift):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift

z_man = Zebra("Z-Man", "Zebra", "afternoon")
print(f'{z_man.name} the {z_man.species} is available to pet during the {z_man.shift} shift.')

# 11


class Mallard:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True


quackers = Mallard("Quackers", "Duck")
# 12


class Goldfish:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True


goldeen = Goldfish("Goldeen", "Goldfish")

# 13


class Swan:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True


odette = Swan("Odette", "Swan")

# 14


class Koi:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True


jinli = Koi("Jinli", "Koi")
# 15


class Goose:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True


untitled = Goose("Untitled", "Goose")
