import random

# Difficulty presets: (min, max, max_attempts, multiplier)
DIFFICULTIES = {
    'easy': (1, 10, 6, 1),
    'medium': (1, 50, 8, 2),
    'hard': (1, 100, 10, 3),
}


def get_difficulty_settings(level):
    level = (level or '').lower()
    return DIFFICULTIES.get(level, DIFFICULTIES['easy'])


def compute_score(attempts_used, max_attempts, multiplier=1):
    remaining = max(0, max_attempts - attempts_used + 1)
    return remaining * 10 * multiplier


def check_guess(guess, target):
    if guess == target:
        return 0
    return -1 if guess < target else 1


def save_highscore(score, file_path='highscore.txt'):
    if not file_path:
        return False
    try:
        with open(file_path, 'r') as f:
            content = f.read().strip()
            current = int(content) if content else -1
    except Exception:
        current = -1
    if score > current:
        with open(file_path, 'w') as f:
            f.write(str(score))
        return True
    return False


def play_round(input_func=input, print_func=print, highscore_path=None):
    print_func('Choose difficulty: easy, medium, hard (default: easy)')
    level = input_func().strip().lower()
    lo, hi, max_attempts, mult = get_difficulty_settings(level)
    target = random.randint(lo, hi)

    attempts = 0
    while attempts < max_attempts:
        try:
            guess = int(input_func().strip())
        except Exception:
            print_func('Please enter a valid integer.')
            continue
        attempts += 1
        res = check_guess(guess, target)
        if res == 0:
            print_func('You guessed it right!')
            score = compute_score(attempts, max_attempts, mult)
            saved = save_highscore(score, highscore_path)
            if saved:
                print_func('New high score!', score)
            else:
                print_func('Score:', score)
            return score
        elif res < 0:
            print_func('Too low. Try again!')
        else:
            print_func('Too high. Try again!')

    print_func('Out of attempts. The number was {}'.format(target))
    return 0


if __name__ == '__main__':
    play_round()
    