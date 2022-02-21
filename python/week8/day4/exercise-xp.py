 # exercise 1

from re import A
import random


class Pets():
     def __init__(self, animals):
         self.animals = animals

     def walk(self):
         for animal in self.animals:
             print(animal.walk())

class Cat():
    is_lazy = True
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def walk(self):
        return f'{self.name} is just walking around'
class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'
class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
class Panther(Cat):
    def sing(Self, sounds):
        return f'{sounds}'
pazit = Bengal("Pazit", 2)
bagira = Panther("Bagira", 4)
my_cats = [pazit, bagira]
my_pets = Pets(my_cats)
my_pets.walk()
# exercise 2 
class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    def bark(self):
        return f'{self.name} is barking'
    def run_speed(self):
        return self.weight / (self.age*10)
    def fight(self, dog):
        if self.run_speed()*self.weight > dog.run_speed()*dog.weight:
            return f'the winner is {self.name}'
        else:
            return f'the winner is {dog.name}'
rex = Dog("Rex", 3, 15)
dino = Dog("Dino", 1, 10)
lucky = Dog("Lucky", 5, 30)
print(lucky.fight(dino))
print(dino.fight(rex))

# exercise 3

class PetDog(Dog):
    def __init__(self, name, age, weight, trained = False):
        super().__init__(name,age,weight)
        self.trained = trained

    def train(self):
        self.trained = True
        return self.bark()

    def play(*args):
        sum = ""
        for i in args:
            sum = sum + f"{i} "
        print(f'{sum}all play together' )

    def do_a_trick(self):
        tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
        random_trick = random.choice(tricks)
        if self.trained:
            print(f'{self.name} {random_trick}')

luka = PetDog("Luka", 1, 10)
print(luka.train())
PetDog.play('rex','luka','snow')
luka.do_a_trick()