import random

choices = ["rock", "paper", "scissors"]

while True:

    computer = random.choice(choices)

    player = input("Choose rock, paper or scissors: ")

    print("Computer chose:", computer)
    print("You chose:", player)

    if player == computer:
        print("It's a tie! Play again.")
    
    elif player == "rock" and computer == "scissors":
        print("You win!")
        break

    elif player == "paper" and computer == "rock":
        print("You win!")
        break

    elif player == "scissors" and computer == "paper":
        print("You win!")
        break

    else:
        print("Computer wins!")
        break