## W3 Schools TUTORIAL: https://www.w3schools.com/python/python_while_loops.asp
####################################


## 1. == Looping Through a List:
## Print each fruit in a fruit list:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
####################################


## 2. == Looping Through a String:
## Loop through the letters in the word "banana":
for x in "banana":
  print(x)
####################################


## 3. == The break Statement:
## Exit the loop when x is "banana"
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
####################################


## 4. == The continue Statement:
## Do not print banana:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
####################################


## 5. == The range() Function:
## Parameters: range(start, end, increment)

## Prints numbers 0-5:
for x in range(6):
  print(x)

## Using the start parameter:
for x in range(2, 6):
  print(x)

## Increment the sequence with 3 (default is 1):
for x in range(2, 30, 3):
  print(x)
####################################


## 6. == Else in For Loop:
## Print all numbers from 0 to 5, and print a message when the loop has ended
for x in range(6):
  print(x)
else:
  print("Finally finished!")
####################################


## 7. == Nested Loops:
## Print each adjective for every fruit:
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
####################################


## 8. == Recursion:
def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
####################################
