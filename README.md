# 🎮 Number Guessing Game

A fun multi-player number guessing game built with Python and SQLite!

## 📋 Overview

Players compete in a 3-level guessing game to earn the highest score. The game features:
- **3 Game Levels** with increasing difficulty
- **Multiple Players** - up to 3 players can compete
- **Leaderboard** - scores are saved to a SQLite database
- **Point System** - earn points based on how quickly you guess

## 🎯 Game Levels

### Level 1: Guess from a List
- Guess a number from a list of 4 numbers (1-10)
- **Points:** 15 for 1st attempt, 10 for 2nd attempt

### Level 2: Guess from Smaller List
- Guess a number from a list of 2 numbers (1-10)
- **Points:** 15 for 1st attempt, 10 for 2nd attempt

### Level 3: Guess the Exact Number
- Guess the exact number (6)
- **Points:** 15 for 1st attempt, 10 for 2nd attempt

**Maximum Attempts:** 4 per level

## 📊 Leaderboard

All player scores are saved to `leaderBoard.db` (SQLite database). The final leaderboard displays all players ranked by their total points.

## 🚀 How to Run

1. Make sure you have Python 3.x installed
2. Navigate to the project directory
3. Run the game:
   ```
   python number_guess.py
   ```
4. Follow the prompts to enter player names and make your guesses

## 📁 Files

- `number_guess.py` - Main game script
- `leaderBoard.db` - SQLite database storing player scores
- `README.md` - This file

## 🗄️ Database

### View Leaderboard
To view all scores in the database, use SQLite:
```
sqlite3 leaderBoard.db
```

Then query the leaderboard:
```sql
SELECT * FROM leaderboard ORDER BY score DESC;
```

## 👥 Author

Created by Kenei

---

**Have fun and good luck guessing! 🍀**