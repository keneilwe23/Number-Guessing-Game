num = 7
user_input = int(input("Guess a number between 1 to 10: "))

while user_input != num:
    print("Try again!")
    user_input = int(input("Guess a number between 1 to 10: "))
print("You guessed it right!")
    