import random

def computer_guess(e):
    low = 1
    high = e
    remarks = ""

    while remarks != "c":
        if low != high:
            user_guess = random.randint(low, high)
        else:
            user_guess = low

        remarks = input(f"Is {user_guess} High (H), Low (L), or Correct (C)? ").lower()
        
        if remarks not in ["h", "l", "c"]:
            print("That's not a Valid Option. Please enter 'H', 'L', or 'C'.")
            continue
        if remarks == "l":
            low = user_guess + 1
        elif remarks == "h":
            high = user_guess - 1

    print(f"I guessed your number {user_guess} correctly!")


computer_guess(10000)
