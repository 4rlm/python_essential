##Note: Sample module to be imported to 'modules.py'
####################################


## Greetings Method ##
def greeting(name):
  print("Hello, " + name)


## Completed Dict ##
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}


## Make Dict Template ##
def make_person_dict():
    person_keys = ('name', 'age', 'city')
    person_vals = None
    return dict.fromkeys(person_keys, person_vals)


## Update Dict Template ##
def update_person_dict(dict, name, age, city):
    dict['name'] = name
    dict['age'] = age
    dict['city'] = city
    return dict
