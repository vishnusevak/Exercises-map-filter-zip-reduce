my_pets = ['sisi', 'bibi', 'titi', 'carla']

def cap(item):
  return item.upper()

print(list(map(cap, my_pets)))

my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

print(list(zip(my_strings,sorted(my_numbers))))

scores = [73, 20, 65, 19, 76, 100, 88]

def approved(item):
  return item>50

print(list(filter(approved, scores)))

from functools import reduce
def accumulator(acc, item):
  return acc + item

print(reduce(accumulator, my_numbers+ scores, 0))