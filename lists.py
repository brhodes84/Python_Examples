#List of Names 3-1
names = ['keith', 'patrick', 'jasmine', 'kennard']
print(names[0])
print(names[1])
print(names[2])
print(names[3])

#Greetings 3-2
message = f'Happy Holidays! {names[0]}'
print(message)
message = f'Happy Holidays! {names[1]}'
print(message)
message = f'Happy Holidays! {names[2]}'
print(message)
message = f'Happy Holidays! {names[3]}'
print(message)

#Own list 3-3
import random
cars = ['model S','CX-5','model 3','350Z']
n = random.randint(0,4)
message = f'One day soon I will own {cars[n]}'
print(message)