

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