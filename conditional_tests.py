first_name = 'brandon'
last_name = 'rhodes'
full_name = f'{first_name} {last_name}'
age = 36
race = 'black'

#True tests
print("Is first name == 'brandon'? I predit True.")
print(first_name == 'brandon')

print("\nIs last name == 'rhodes'? I predit True")
print(last_name == 'rhodes')

print("\nIs full name 'brandon rhodes'? I predit True")
print(full_name == 'brandon rhodes')

print("\nIs your age == 36? I predit True")
print(age == 36)

print("\nIs your race == 'black'? I predit True")
print(race == 'black')

#false tests
print("\nIs first name == 'rashad'? I predit False")
print(first_name == 'rashad')

print("\nIs last name == 'ladd'? I predit False")
print(last_name == 'ladd')

print("\nIs full name == 'rashad ladd'? I predit False")
print(full_name == 'rashad ladd')

print("\nIs your age == 20? I predit False")
print(age == 20)

print("\nIs your race == 'white'? I predit False")
print(race == 'white')

big_name = 'BRANDON'
lil_name = 'brandon'

if big_name == 'BRANDON':
    print("\nName is using all caps!")

if lil_name != big_name:
    print("Name isn't using caps")

print("\nIs lil name == big_name.lower()?")
print(lil_name == big_name.lower())

