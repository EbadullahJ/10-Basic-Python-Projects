import random
import string
from words import words  

def get_valid_word(words):
    random_word = random.choice(words)
    while "-" in random_word or " " in random_word:
        random_word = random.choice(words)
    return random_word.upper()

def hangman():
    random_word = get_valid_word(words)
    word_letters = set(random_word)
    used_letters = set()  
    alphabet = set(string.ascii_uppercase)  
    lives = 7

    print("\nWelcome to Hangman! Try to guess the word one letter at a time.")

    while len(word_letters) > 0 and lives > 0:
        print(f"\nYou have {lives} lives left.")
        print("Used letters:", " ".join(sorted(used_letters)))

        word_list = [letter if letter in used_letters else "_" for letter in random_word]
        print("Current word: ", " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)

            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print(f"Good job! The letter '{user_letter}' is in the word.")
            else:
                lives -= 1
                print(f"Oops! The letter '{user_letter}' is not in the word.")
        elif user_letter in used_letters:
            print("\nYou already guessed that letter. Try a new one.")
        else:
            print("\nInvalid input. Please enter a valid letter.")


    if lives == 0:
        print(f"\nSorry, you lost! The word was '{random_word}'. Better luck next time!")
    else:
        print(f"\nCongratulations! You guessed the word '{random_word}' correctly!")


if __name__ == "__main__":
    hangman()

