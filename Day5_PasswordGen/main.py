import random
counter = 0
randomness = 0
password = ""

number_count = 0
symbol_count = 0

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the password generator.")
user_length_choice = int(input("How long would you like the password to be?"))
user_number_choice = int(input("How many numbers would you like to include?"))
user_symbol_choice = int(input("How many symbols would you like to include?"))

while counter != user_length_choice:

    
        
print(password)