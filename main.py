# Import random module for generating random choices
import random

# Lists of characters to use in password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Get user input for password components
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Create password list and add random characters
password = []
for x in range(0, nr_letters):
    password.append(random.choice(letters))  # Add random letters
for x in range(0, nr_symbols):
    password.append(random.choice(symbols))  # Add random symbols
for x in range(0, nr_numbers):
    password.append(random.choice(numbers))  # Add random numbers

# Shuffle the password and convert to string
random.shuffle(password)
print("Your password is: " + "".join(password))
