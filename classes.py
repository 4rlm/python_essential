## W3 Schools TUTORIAL: https://www.w3schools.com/python/python_classes.asp
####################################

## == Example ==
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        name_msg = f'Hello my name is {self.name}\n'
        age_msg = f'I am {self.age} years old.\n'
        print(name_msg + age_msg)

p1 = Person("Adam", 42)
p1.intro()
p1.age = 30
p1.intro()
####################################


## 1. == Create a Class:
## Create a class named MyClass, with a property named x:
class MyClass:
  x = 5
####################################


## 2. == Create Object:
## Create an object named p1, and print the value of x:
p1 = MyClass()
print(p1.x)
####################################


## 3. == The __init__() Function:
## Create a class named Person, use the __init__() function to assign values for name and age:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
####################################


## 4. == Object Methods:
## Insert a function that prints a greeting, and execute it on the p1 object:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
####################################


## 5. == Modify Object Properties:
## Set the age of p1 to 40:
p1.age = 40
####################################


## 6. == Delete Object Properties:
## Delete the age property from the p1 object:
del p1.age
####################################


## 7. == Delete Objects:
## Delete the p1 object:
del p1
####################################
