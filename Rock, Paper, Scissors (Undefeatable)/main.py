import random

def game():
    while True:
        user = input("Choose one of these: 'R' for Rock, 'P' for Paper, 'S' for Scissors: ").lower()
        if user not in ['r', 'p', 's']:
            print("Invalid input! Please choose 'R', 'P', or 'S'.")
            continue
        break

    choices = {"r": "Rock", "p": "Paper", "s": "Scissors"}

    if user == "r":
        computer = "p" 
    elif user == "p":
        computer = "s"
    else:
        computer = "r"

    print(f"The Computer Chose: {choices[computer]}!")

    return "You Lost!"

print(game())