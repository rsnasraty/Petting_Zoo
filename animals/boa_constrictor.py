
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