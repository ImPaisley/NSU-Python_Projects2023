# Paisley Samuel
# BMME 8050 , Summer Semester
# Project 2 - RockPaperScissors_PS.py

import random  # import the module random in order to allow the computer to choose rps randomly
choices = ["rock", "paper", "scissors"]
computer_guesses = []  # start with empty list
user_guesses = []  # start with empty list
user_wins = 0
computer_wins = 0
draws = 0

import random # import the module random in order to allow the computer to choose rps randomly

print("Welcome to Rock, Paper, Scissors!\n")

# Choosing the number of rounds
while True:
    try:
        num_of_games = int(input("How many games would you like to play? \nChoose an odd number between 3 and 11:"))
        if num_of_games not in range(3,13,2):
            print('Sorry',f'{num_of_games} is not a valid number. Please try again.\n')
            continue
        break
    except ValueError:
        print("Invalid input! Please enter an odd integer between 3 and 11.\n")

print("\nLet's play!\n\n")

# Playing the actual game
for game_number in range(num_of_games):
    while True:
        print("Game",game_number + 1)
        user_choice = (input("Please choose rock, paper, or scissors: ").strip().lower())
        if user_choice in choices:
            break
        else:
            print("Invalid input! Please enter rock, paper, or scissors.")

    user_guesses.append(user_choice)
    computer_choice = random.choice(choices)
    computer_guesses.append(computer_choice)

    if user_choice == computer_choice:
        print("It's a tie!\n")
        draws = draws + 1
    elif user_choice == "rock":
        if computer_choice == "scissors":
            print("Rock beats scissors! You win!\n")
            user_wins = user_wins + 1
        else:
            print("Paper beats rock! Computer wins!\n")
            computer_wins = computer_wins + 1
    elif user_choice == "paper":
        if computer_choice == "rock":
            print("Paper beats rock! You win!\n")
            user_wins = user_wins + 1
        else:
            print("Scissors beats paper! Computer wins!\n")
            computer_wins = computer_wins + 1
    elif user_choice == "scissors":
        if computer_choice == "paper":
            print("Scissors beats paper! You win!\n")
            user_wins = user_wins + 1
        else:
            print("Rock beats scissors! Computer wins!\n")
            computer_wins = computer_wins + 1

# Printing game stats. table
print()
print('Game Statistics')
print('-'*40)
print('Games played: ', num_of_games)
print('-'*40)
print('{:<20s}{:<20s}'.format('Computer', 'Player'))
print('-'*40)
for i in range(num_of_games):
    print(f'{computer_guesses[i]:<20s}',f'{user_guesses[i]}\n', end='')
print('-'*40)
print(f'Player wins: {user_wins}')
print(f'Computer Wins: {computer_wins}')
print(f'Draws: {draws}\n')
print("Thanks for playing!\n")
