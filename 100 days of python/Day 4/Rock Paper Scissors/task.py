import random
from timeit import repeat
from zoneinfo import reset_tzpath

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

Options = [rock, paper, scissors]

user_choice = (input('''Choose "Rock", "Paper", "Scissors"''').lower())
computer_choice = random.choice(Options)


if user_choice == "rock":
    print ("You selected Rock", rock)

    if computer_choice == rock:
        print(rock,"Draw!")
    elif computer_choice == paper:
        print(paper,"You lose!")
    elif computer_choice == scissors:
        print(scissors,"You win!")

elif user_choice == "paper":
    print ("you selected paper",paper)

    if computer_choice == paper:
        print(paper,"Draw!")
    elif computer_choice == rock:
        print(rock,"You lose!")
    elif computer_choice == scissors:
        print(scissors,"You win!")

elif user_choice == "scissors":
    print (scissors)

    if computer_choice == paper:
        print(paper,"You Win!")
    elif computer_choice == scissors:
        print(scissors,"Draw!")
    elif computer_choice == rock:
        print(rock,"You lose!")

else:
    print("Select a valid option")





