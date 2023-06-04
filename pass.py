#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_chars = []
for i in range(1, nr_letters+1): #needed for amount of letters user requested
    password_chars.append(letters[random.randint(0, len(letters)-1)]) #list of letters, then letters[i], and picking a random one. we don't know the length of how many we need so we use len-1

for i in range(1, nr_symbols+1):
    password_chars.append(symbols[random.randint(0, len(symbols)-1)])

for i in range(1, nr_numbers+1):
    password_chars.append(numbers[random.randint(0,len(numbers)-1)])

random.shuffle(password_chars)

password = ''
for char in password_chars:
    password += char
print(password)



