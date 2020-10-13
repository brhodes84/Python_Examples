#4-10 Slices
pizzas = ['cheese', 'sausage', 'pepperoni', 'vegan']
print('The first three items in the list are:')
print(pizzas[0:3])

print('\nThree items from the middle of the list are:')
print(pizzas[1:])

print('\nThe last three items in the list are:')
print(pizzas[-3:])

#4-11 My Pizzas, Your Pizzas
friend_pizzas = pizzas[:]
pizzas.append('pineapple')
friend_pizzas.append('beef')
print('My favorite pizzas are:')
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

#4-12 More Loops
