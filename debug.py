#Run:       $ python3 debug.py
#Debugger:  $ python3 -m pdb debug.py
#Debugger Commands: https://docs.python.org/3/library/pdb.html#debugger-commands
#Debugger Tutorial: https://pymotw.com/2/pdb/
#Debugger Examples: https://docs.python.org/2/library/pdb.html
#############################

## == Run PDB in CLI:
# $ python3
# >>> import debug
# >>> import pdb
# >>> pdb.run('debug.Person')
#############################

## == Run PDB from Script:
import pdb  # Allows debugging for larger projects.
# pdb.set_trace() # trace / break point for pdb
#############################

## == Commands:
## list         l     # See greater detail of area.
## where        w     # Current line.
## pretty print pp    # Pretty Print complicated variables, ex pp(name).
## print        p     # Print variable, ex p(name).
## args         a     # Get variables.
## step         s     # Step through every line starting at break point.
## next         n     # Steps all the way through the function call to the next statement
## up
## return             # View return value before it is returned.
## break line_num     # Break at specific line number after set_trace point.
#############################


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
        # pdb.set_trace() # trace / break point for pdb
        for hobby in hobbies:
            print(f'I like to {hobby}.')
            # pdb.set_trace() # trace / break point for pdb

    def say_car(self):
        car_details = f"{self.car['year']} {self.car['brand']} {self.car['model']}"
        car_msg = f'I drive a {car_details}'
        pdb.set_trace() # trace / break point for pdb
        print(car_msg)

#############################

## == Runner Code:
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
