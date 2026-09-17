print('Welcome to Rock, Paper and Scissors')
import random

choices = ('rock', 'paper', 'scissors')

player_score = 0
computer_score = 0

print('First to 3 points wins!')
print('Type rock, paper or scissors')

while player_score < 3 and computer_score < 3:

    player = input('Your choice: ').lower()

    if player not in choices:
        print('Invalid choice! Please choose rock, paper or scissors.')
        continue

    computer = random.choice(choices)

    print('You chose:', player)
    print('Computer chose:', computer)

    if player == computer:
        print("It's a draw!")

    elif (
        (player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock") or
        (player == "scissors" and computer == "paper")
    ):
        print("You win this round!")
        player_score += 1

    else:
        print("Computer wins this round!")
        computer_score += 1

    print('Score:', player_score, '-', computer_score)

if player_score == 3:
    print('YOU WON THE GAME!')
else:
    print('COMPUTER WON THE GAME!')
