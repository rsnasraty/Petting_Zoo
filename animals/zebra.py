

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