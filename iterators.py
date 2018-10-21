## W3 Schools TUTORIAL: https://www.w3schools.com/python/python_iterators.asp
####################################

## 1. == About Iterators:
## An iterator is an object which implements the iterator protocol, which consist of the methods
__iter__()
__next__()
iter()
####################################


## 2. == iter():

## Return a iterator from a tuple, and print each value:
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

## Strings are also iterable objects, containing a sequence of characters:
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
####################################


## 3. == Looping Through an Iterator:

## Iterate the values of a tuple:
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)

## Iterate the characters of a string:
mystr = "banana"

for x in mystr:
  print(x)
####################################


## 4. == Create an Iterator:

## Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.):
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
####################################


## 5. == StopIteration:
## Stop after 20 iterations:
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)
####################################
