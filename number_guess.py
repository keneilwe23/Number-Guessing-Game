import sqlite3

# Create database connection
connection = sqlite3.connect('leaderBoard.db')
cursor = connection.cursor()

# Create table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS leaderboard (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        player_name TEXT NOT NULL,
        score INTEGER NOT NULL
    )
''')
connection.commit()

for player in range(1, 4):
    print(f"PLAYER {player}")
    player_name = input("Enter your name: ")
    
    num_list = [3,9,2,7]
    number_of_guesses = 4
    points = 0
    attempts = 1

    user_input = int(input("Guess a number in a list of 4 numbers between(1 to 10): "))

    while user_input not in num_list and attempts < number_of_guesses:
        print("Try again!")
        attempts += 1
        user_input = int(input("Guess a number between 1 to 10: "))

    if user_input in num_list:
        if attempts == 1:
            points += 15
        elif attempts == 2:
            points += 10
        print("You guessed it right! let move to the next level.")
    else:
        print("Game over! No more guesses.")
        cursor.execute('INSERT INTO leaderboard (player_name, score) VALUES (?, ?)', (player_name, points))
        connection.commit()
        continue

    print("Level 2: Guess a number in a list of two numbers(between 1 to 10): ")
    num = [5,7]
    attempts = 1
    user_input = int(input("Guess a number between 1 to 10: "))

    while user_input not in num and attempts < number_of_guesses:
        print("Try again!")
        attempts += 1
        user_input = int(input("Guess a number between 1 to 10: "))

    if user_input in num:
        if attempts == 1:
            points += 15
        elif attempts == 2:
            points += 10
        print("You guessed it right! Congratulations!")
    else:
        print("Game over! No more guesses.")
        cursor.execute('INSERT INTO leaderboard (player_name, score) VALUES (?, ?)', (player_name, points))
        connection.commit()
        continue

    print("Level 3: Guess the correct number(between 1 to 10): ")
    num = 6
    attempts = 1
    user_input = int(input("Guess a number between 1 to 10: "))

    while user_input != num and attempts < number_of_guesses:
        print("Try again!")
        attempts += 1
        user_input = int(input("Guess a number between 1 to 10: "))

    if user_input == num:
        if attempts == 1:
            points += 15
        elif attempts == 2:
            points += 10
        print("You guessed it right! You are a number guessing master!")
    else:
        print("Game over! No more guesses.")

    print(f"Your total points: {points}")
    cursor.execute('INSERT INTO leaderboard (player_name, score) VALUES (?, ?)', (player_name, points))
    connection.commit()


print("\n=== FINAL LEADERBOARD ===")
# Fetch all scores from database
cursor.execute('SELECT player_name, score FROM leaderboard ORDER BY score DESC')
leaderboard_data = cursor.fetchall()

# Display the leaderboard
for name, score in leaderboard_data:
    print(f"{name}: {score} points")

connection.close()
