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