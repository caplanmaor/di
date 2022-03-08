# exercise 1
class Family:
    members = [
    {'name':'Michael','age':35,'gender':'Male','is_child':False},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False}
    ]

    def __init__(self, members, last_name):
        self.members = members
        self.last_name = last_name

    @classmethod
    def born(cls, **kwargs):
        member = {}
        for key,value in kwargs.items():
            member[key] = value
        cls.members.append(member)

    @staticmethod
    def is_18(name):  
        for member in Family.members:
            if member["name"] == name:
                if member["is_child"] == True:
                    return True
                else:
                    return False

    @staticmethod
    def show_members():
        for member in Family.members:
            print(f'''name: {member["name"]}
age: {member["age"]}
gender: {member["gender"]}
is child: {member["is_child"]}''')



Family.born(name="maor", age="26", gender="male", is_child=False)
print(Family.members)
print(Family.is_18("maor"))
Family.show_members()
print("------")

# exercise 2
class TheIncredibles(Family):
    members = [
    {'name':'Michael','age':35,'gender':'Male','is_child':False, 'power': "flying", 'incredible_name':'superman'},
    {'name':'Sarah','age':3,'gender':'Female','is_child':True, 'power': "strength", 'incredible_name':'hulk'}
    ]

    def __init__(self, members):
        self.members = members

    @staticmethod
    def use_power(name):
        for member in TheIncredibles.members:
            if member["name"] == name:
                if member["is_child"] == False:
                    print(f'the power of {member["name"]} is {member["power"]}')
                else:
                    raise Exception('under 18 cant show power')

    @staticmethod
    def indredible_presentation():
        for member in TheIncredibles.members:
            print(f'''name: {member["name"]}
age: {member["age"]}
gender: {member["gender"]}
is child: {member["is_child"]}
power: {member["power"]}
incredible name: {member["incredible_name"]}
''')

# TheIncredibles.use_power('Sarah')
TheIncredibles.use_power('Michael')

TheIncredibles.indredible_presentation()
TheIncredibles.born(name="Jack", age="2", gender="male", is_child=True, power="unkown", incredible_name="baby")
TheIncredibles.indredible_presentation()