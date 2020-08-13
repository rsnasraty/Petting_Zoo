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