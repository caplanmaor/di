from pickletools import read_unicodestring1


import math

class Circle:
    def __init__(self, radius, diameter=None):
        self.radius = radius
        self.diameter = diameter

    # @classmethod
    def calc_area(self):
        return math.pi * self.radius * self.radius

    def __repr__(self):
        return f'radius {self.radius}'

    def __add__(self, num):
        return self.radius + num.radius

    def __gt__(self, num):
        if self.radius > num.radius:
            return True
        else:
            return False

    def __eq__(self, num):
        if self.radius == num.radius:
             return True
        else:
            return False

    def __lt__(self, num):
        return self.radius < num.radius


c1 = Circle(2)
c2 = Circle(3)
c3 = Circle(5)
c4 = Circle(1)


print(c1.calc_area())

print('''
         , - ~ ~ ~ - ,
     , '               ' ,
   ,                       ,
  ,                         ,
 ,                           ,
 ,                           ,
 ,                           ,
  ,                         ,
   ,                       ,
     ,                  , '
       ' - , _ _ _ ,  '
''')

print(c1 + c2)
print(c1<c2)
print(c1==c2)
list_circles = [c1, c2, c3, c4]
print(list_circles)
list_circles.sort()
print(list_circles)