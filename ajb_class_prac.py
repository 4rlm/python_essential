#Run:       $ python3 ajb_class_prac.py
#Debugger:  $ python3 -m pdb ajb_class_prac.py
#Debugger Commands: https://docs.python.org/3/library/pdb.html#debugger-commands
#Debugger Tutorial: https://pymotw.com/2/pdb/
####################################

# $ python3
# >>> import ajb_class_prac
# >>> import pdb
# >>> pdb.run('ajb_class_prac.Person')
####################################

import pdb  # Allows debugging for larger projects.

class Person:
    def __init__(self, name, age, hobbies):
        self.name = name        # string
        self.age = age          # integer
        self.hobbies = hobbies  # list
        self.car = {}           # dict
        pdb.set_trace() # trace / break point for pdb

    def say_intro(self):
        name_msg = f'Hello my name is {self.name}\n'
        age_msg = f'I am {self.age} years old.\n'
        print(name_msg + age_msg)

    def say_hobbies(self):
        for hobby in hobbies:
            print(f'I like to {hobby}.')

    def say_car(self):
        car_details = f"{self.car['year']} {self.car['brand']} {self.car['model']}"
        car_msg = f'I drive a {car_details}'
        print(car_msg)


hobbies = ["play golf", "cook", "travel"]
p1 = Person("Adam", 42, hobbies)
p1.say_intro()
p1.age = 30
p1.say_hobbies()


car = {
    "brand": "Toyota",
    "model": "Prius",
    "year": 2014
}

p1.car = car
p1.car["brand"] = "Ford"
p1.car["model"] = "Mustang"
p1.car["year"] = 1964
p1.say_car()
