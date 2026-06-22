import random

choices = ["rock", "paper", "scissors"]

player_score = 0
computer_score = 0

while player_score < 3 and computer_score < 3:

    computer = random.choice(choices)

    player = input("Choose rock, paper or scissors: ")

    print("Computer chose:", computer)

    if player == computer:
        print("It's a tie!")

    elif player == "rock" and computer == "scissors":
        print("You win this round!")
        player_score += 1

    elif player == "paper" and computer == "rock":
        print("You win this round!")
        player_score += 1

    elif player == "scissors" and computer == "paper":
        print("You win this round!")
        player_score += 1

    else:
        print("Computer wins this round!")
        computer_score += 1

    print("Score:")
    print("You:", player_score)
    print("Computer:", computer_score)

print()

if player_score == 3:
    print("🏆 You won the match!")
else:
    print("💻 Computer won the match!")