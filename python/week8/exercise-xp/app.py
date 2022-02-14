# exercise 1
class Cat:
    ages = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.ages.update({name:age})

dubit = Cat("Dubit", 6)

shirly = Cat("Shirly", 10)

bobo = Cat("Bobo", 3)

pazit = Cat("Pazit", 1)

def find_oldest():
    oldest = max(Cat.ages.items(), key = lambda k : k[1])
    print(f"the oldest cat is {oldest[0]} and he is {oldest[1]} years old")
find_oldest()

# exercise 2
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height
    
    def bark(self):
        print(f"{self.name} goes woof")

    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high")

davids_dog = Dog("Rex", 50)
print(f"davids dog is called {davids_dog.name} and he is {davids_dog.height}cm tall")
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog("teacup", 20)
print(f"sarahs dog is called {sarahs_dog.name} and he is {sarahs_dog.height}cm tall")
sarahs_dog.bark()
sarahs_dog.jump()

print("who is bigger?")
if sarahs_dog.height > davids_dog.height:
    print(sarahs_dog.name)
else:
    print(davids_dog.name)

# exercise 3
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_song(self):
        for i in self.lyrics:
            print(i)

poem = Song(["the lady", "glitters", "shes buying a stairway"])

poem.sing_song()

# exercise 4
class Zoo:
    def __init__(self, zoo_name) -> None:
        self.animals = []
        self.name = zoo_name

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print(self.animals)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        self.animals.sort()
        groupAnimals = {}
        for i in self.animals:
            groupAnimals.setdefault(i[0],[]).append(i)
        sortedGroup = sorted(groupAnimals.values(), key=lambda s: s[0])
        return sortedGroup

    def get_groups(self):
        listOfAnimals = self.sort_animals()
        for i in listOfAnimals:
            for j in i:
                print(j)
    

ramat_gan_safari = Zoo("ramat_gan_safari")

ramat_gan_safari.add_animal("monkey")
ramat_gan_safari.add_animal("lemur")
ramat_gan_safari.add_animal("lion")
ramat_gan_safari.add_animal("crocodile")
ramat_gan_safari.add_animal("camel")

ramat_gan_safari.get_animals()
ramat_gan_safari.sell_animal("monkey")
ramat_gan_safari.get_animals()

print(ramat_gan_safari.sort_animals())
ramat_gan_safari.get_groups()