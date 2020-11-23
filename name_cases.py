#Personal Message
name_you = "brandon rhodes"
message_1 = f"Hello, {name_you}! Let's change our future."
print(message_1)

#Name Cases
print(name_you.lower())
print(name_you.upper())
print(name_you.title())

#Famous Quote
print('Dave Chappelle once said, "WHITE POWER!"')

#Famous Quote 2
famous_person = "dave chappelle"
message_2 = f'{famous_person.title()} once said, "WHITE POWER"'
print(message_2)

#Stripping Names
name_son = " nehemiah 'nemo' rhodes"
print(name_son) # nehemiah 'nemo' rhodes
print(f"\t{name_son}") #    nehemiah 'nemo' rhodes
print(f"I think {name_son}\nlikes to eat boogers")
print(name_son)
print(name_son.rstrip()) # nehemiah 'nemo' rhodes
print(name_son.lstrip()) #nehemiah 'nemo' rhodes
print(name_son.strip()) #nehemiah 'nemo' rhodes