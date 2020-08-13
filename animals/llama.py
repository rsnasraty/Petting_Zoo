
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