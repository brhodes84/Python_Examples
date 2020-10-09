#Personal Message
name = "brandon"
message = f"Hello {name}, would you like to learn python today?"
print(message)

#Name Cases
name_cases = f"{name.lower()}\n{name.upper()}\n{name.title()} "
print(name_cases)

#Famous Quote
author = "Bruce Lee once said,"
quote = "Knowing is not enough, we must apply. Willing is not enough, we must do."
message = f'{author} "{quote}"'
print(message)

#Famous Quote 2
famous_person = author
quote = "Showing off is the fool's idea of glory"
message = f'{famous_person} "{quote}"'
print(message)

#Stripping Names
name = " brandon "
message = f"{name}\n{name.lstrip()}\n{name.rstrip()}\n{name.strip()}"
print(message)