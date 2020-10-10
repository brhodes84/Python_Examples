#4-1 Pizzas
pizzas = ['cheese', 'sausage', 'pepperoni', 'vegan']
for pizza in pizzas:
    print(f'I love getting {pizza} pizza from Beggers\n')
print('I really love pizza!!\n')

#4-2 Animals
animals = ['cat', 'dog', 'snake', 'fish']
for pet in animals:
    print(f'I would love to have a {pet} as a pet!\n')
print('I would take any of these as a pet and love them.\n')

#4-3 Counting to Twenty
twenty = []
for value in range (1, 21):
    twenty.append(value)
print(twenty)

#4-4 One Million / 4-5 Summing a Million
million = []
for value in range (1, 1_000_001):
    million.append(value)
print(min(million))
print(max(million))
print(sum(million))

#4-6 Odd Numbers
odd_numbers = []
for value in range(1, 21, 2):
    odd_numbers.append(value)
print(odd_numbers)

#4-7 Threes
threes = []
for value in range(3, 31, 3):
    threes.append(value)
print(threes)

#4-8 Cubes
cubes = []
for value in range(1, 11):
    cubes.append(value**3)
print(cubes)

#4-9 Cube Comprehension
cube = [value **3 for value in range(1, 11)]
print(cube)