#3-4 Guest List
guest = ['brandon','dad','Uncle Kevin']
message = f'I would love to see and talk to you again. Please come to dinner {guest[0].title()}, {guest[1].title()}, and {guest[2]}'
print(message)

#3-5 Changing Guest
print(f"{guest[2]}, won't be able to make it tonight")
del guest[2]
guest.append('Jill')
message = f'I would love to see and talk to you again. Please come to dinner {guest[0].title()}, {guest[1].title()}, and {guest[2]}'
print(message)

#3-6 More Guest
print('Was able to get a bigger table so more people are able to come!')
guest.insert(0, 'nemo')
guest.insert(1, 'austin')
guest.append('jayden')
message = f"I would love to see and talk to you again. Please come to dinner {guest[0].title()}, {guest[1].title()}, {guest[2]}, {guest[3]}, {guest[4]} and {guest[5]}"
print(message)

#3-7 Shrinking Guest List
print('So sorry a change of plans I can only invite two people now.')
cancel_1 = guest.pop(1)
print(f'Sorry {cancel_1} you are not invited.')
cancel_2 = guest.pop(2)
print(f'Sorry {cancel_2} you are not invited.')
cancel_3 = guest.pop(2)
print(f'Sorry {cancel_3} you are not invited.')
cancel_4 = guest.pop(2)
print(f'Sorry {cancel_4} you are not invited.')
print(f"Hey {guest[0].upper()} and {guest[1].lower()} I still have room for you to come tonight!!")
del guest[0]
del guest[0]
print(guest)