alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

#we need to collect encrypt or decode

print("Welcome to the Cesaer Cipher!\n\n")

state = input("Do you want to encrypt of encode?\n\n")

shift = input("What is the amount of position move you want?\n\n")

if state == "encode":
    print("")


def encrypt(plain_text, shift_amount, text_length):
    
    for position in range(text_length):
        letter = plain_text[position]
        for alphabet_position in range(25):
            if letter != alphabet[alphabet_position]:
                continue
            if letter == alphabet[alphabet_position]:
                letter = alphabet[alphabet_position + int(shift_amount)]
                plain_text[position] = letter
                print(plain_text)


text = input("What is the message you want to encrypt?")
length = len(text)

if state == "encrypt":
    encrypt(text, shift, length)

    






#after that it take the users input

#once we collected that it begins to go through each letter and of the input and change the letter.

