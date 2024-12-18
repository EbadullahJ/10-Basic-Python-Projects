import random

def guess(e):
    unpredictable_number = random.randint(1, e)
    guess = 0
    while guess != unpredictable_number:
        guess = int(input(f"Guess a number between 1 and {e}: "))
        if guess > e:
            print("Invaild number. Try Again!")
            continue
        if guess > unpredictable_number:
            print("Sorry, Too High. Try Again!")
        elif guess < unpredictable_number:
            print("Sorry, Too Low. Try Again!")

    print(f"Congratulations, You have guessed the number {unpredictable_number} correctly!")

guess(10000)
