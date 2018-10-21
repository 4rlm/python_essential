## W3 Schools TUTORIAL: https://www.w3schools.com/python/python_while_loops.asp
####################################


## 1. == The while Loop:
## Print i as long as i is less than 6:
i = 1
while i < 6:
  print(i)
  i += 1
####################################


## 2. == The break Statement:
## Exit the loop when i is 3:
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
####################################


## 3. == The continue Statement:
## Continue to the next iteration if i is 3:
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
####################################
