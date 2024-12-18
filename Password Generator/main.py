import random

print("Welcome to Your Password Generator!")

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!?@#$%&"
num_passwords = int(input("How many Passwords would you like to Generate? "))
password_length = int(input("What should be the Length of Each Password? "))

print("\nHere are your Generated Passwords:")

for pwd in range(num_passwords):
    password = ""
    for char in range(password_length):
        password += random.choice(characters)
    
    print(password)
