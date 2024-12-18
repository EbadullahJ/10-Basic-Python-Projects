import time

def countdown(t):
    while t > 0:
        minutes, seconds = divmod(t, 60)
        timer = "{:02d}:{:02d}".format(minutes, seconds)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print("00:00")
    print("The Timer has ended!")

while True:
    user_input = input("Enter the Countdown Time in Seconds: ").strip()

    if user_input.isdigit():
        t = int(user_input)
        if t < 0:
            print("Time cannot be negative. Please enter a Positive Number in Seconds.")
            continue

        countdown(t)
        break
    else:
        print("Invalid input! Please enter a valid number in Seconds.")
