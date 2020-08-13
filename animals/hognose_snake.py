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