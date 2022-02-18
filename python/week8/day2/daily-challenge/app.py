class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = {}
    
    def add_animal(self, name, amount=1):
        for i in self.animals.items():
            if i[0] == name:
                self.animals[name] += amount
                return            
        self.animals[name] = amount
        
    def get_info(self):
        return self.animals

    def get_animal_types(self):
        types = list(self.animals.keys())
        types.sort()
        return types

    def get_short_info(self):
        types = self.get_animal_types()
        print(types)
        text = f"{self.name}'s farm has "
        for i,e in enumerate(types):
            if i < 2:
                text += f"{e}s "
            else:
                text += f"and {e}s "
        return text
            

        
macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())

print(macdonald.get_animal_types())
print(macdonald.get_short_info())