import sys
import random
from enum import Enum


class RPS(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3


# Rock Paper Scissors GAME

title = "Rock Paper Scissors GAME".upper()
print(title.center(40, "="))
print("")

playerchoice = input(
    "Please enter:\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n"
)

try:
    player = int(playerchoice)

except ValueError:
    sys.exit("Enter a number!")

if player < 1 or player > 3:
    sys.exit("Enter 1, 2 or 3!")

computerchoice = random.choice("123")
computer = int(computerchoice)

print("")

print("You chose: " + str(RPS(player)).replace("RPS.", "") + ".")
print("Computer chose: " + str(RPS(computer)).replace("RPS.", "") + ".")

print("")

if player == 1 and computer == 3:
    print("You win!🥳")
elif player == 2 and computer == 1:
    print("You win!🥳")
elif player == 3 and computer == 2:
    print("You win!🥳")
elif player == computer:
    print("Tie!🤝")
else:
    print("Computer wins!🤖")
