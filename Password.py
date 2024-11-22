import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z', ]
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
specialLetters = ['!', '@', '#', '$', '%', '^', '&', ' *', ' ( )', '-', '_', '=', '+']

print("Welcome to Password Generator:")
enter = int(input("How many letters would you like in your password:\n"))
enter1 = int(input("How many number would you like in your password:\n"))
enter2 = int(input("How many specialSymbols would you like in your password:\n"))

password = ""

for char in range(1, enter + 1):
    password += random.choice(letters)

for char in range(1, enter2 + 1):
    password += random.choice(numbers)
for char in range(1, enter2 + 1):
    password += random.choice(specialLetters)


print(password)
