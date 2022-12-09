import random

stages = ['''
     ______
    |      |
    |      
    |     
    |      
    |     
    |________

'''

,'''
     ______
    |      |
    |      O
    |     
    |      
    |     
    |________

'''

, '''
     ______
    |      |
    |      O
    |      |
    |      
    |     
    |________

'''

, '''
     ______
    |      |
    |      O
    |     \|
    |
    |     
    |________

'''

, '''
     ______
    |      |
    |      O
    |     \|/
    |
    |     
    |________

'''

,'''
     ______
    |      |
    |      O
    |     \|/
    |      |
    |     
    |________

'''

,'''
     ______
    |      |
    |      O
    |     \|/
    |      |
    |     L 
    |________

'''

, '''
     ______
    |      |
    |      O      YOU HAVE BEEN
    |     \|/
    |      |        KILLED!!!
    |     L L
    |________

''']

word_list = ["bird", "donkey", "bamboo", "turtle"]
chosen_word = random.choice(word_list)
display = []


lives = 0

word_length = len(chosen_word)

print("\nWelcome to HANGMAN\n")

for _ in range(word_length):
    display += '_'
    
print(display)

end_of_game = False

while not end_of_game:

    guess = input("\nEnter your guess: ")
    print("----------------------------------")


    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            print(display)

    if guess not in chosen_word:
        lives +=1
        print(display)
        if lives ==7:
            end_of_game = True

        

    if "_" not in display:
        end_of_game = True
        print("You WON!")

    print(stages[lives])

    