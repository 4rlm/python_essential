## W3 Schools TUTORIAL: https://www.w3schools.com/python/python_modules.asp
####################################

## 1. == Create a Module:
## Save this code in a file named ajb_modules.py
def greeting(name):
  print("Hello, " + name)
####################################


## 2. == Use a Module:
## Import the module named ajb_modules, and call the greeting function:
import ajb_modules
ajb_modules.greeting("Jonathan")
####################################


## 3. == Variables in Module:

## Save this code in the file ajb_modules.py
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

## Import the module named ajb_modules, and access the person1 dictionary:
import ajb_modules
a = ajb_modules.person1["age"]
print(a)
####################################


## 4. == Re-naming a Module:
## You can create an alias when you import a module, by using the as keyword:
## Create an alias for ajb_modules called mx:
import ajb_modules as mx
a = mx.person1["age"]
print(a)
####################################


## 5. == Built-in Modules:
## Import and use the platform module:
import platform
x = platform.system()
print(x)
####################################


## 6. == Using the dir() Function:
## Lists all function names (or variable names) in a module
import platform
x = dir(platform)
print(x)
####################################


## 7. == Import From Module:
## The module named ajb_modules has one function and one dictionary:

## The module named ajb_modules has one function and one dictionary:
def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

## Import only the person1 dictionary from the module:
from ajb_modules import person1
print (person1["age"])

## Note: When importing using the from keyword, do not use the module name when referring to elements in the module. Example: person1["age"], not ajb_modules.person1["age"]
####################################
