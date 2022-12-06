import random
cc = 0

def computer_choice():
    cc = random.randint(0, 2)

def final_choices(choice):
    if choice == 0:
        print(rock)
    elif choice == 1:
        print(paper)
    elif choice == 2:
        print(scissors)
    else:
        print("FAIL")
    

paper =  '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.")
computer_choice()
user_choice = int(input())

final_choices(user_choice)

if user_choice == cc1:
    final_choices(user_choice)
    final_choices(cc)
    print("Draw")


