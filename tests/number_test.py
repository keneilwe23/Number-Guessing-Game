import number_guess


def test_get_difficulty_settings():
    lo, hi, attempts, mult = number_guess.get_difficulty_settings("medium")
    assert (lo, hi, attempts, mult) == (1, 50, 8, 2)


def test_compute_score():
    # with attempts_used=1, max_attempts=6, multiplier=1 -> remaining = 6
    assert number_guess.compute_score(1, 6, 1) == 60


def test_check_guess():
    assert number_guess.check_guess(5, 7) == -1
    assert number_guess.check_guess(9, 7) == 1
    assert number_guess.check_guess(7, 7) == 0


def test_play_round_win(monkeypatch):
    # force the random target to 7
    monkeypatch.setattr(number_guess.random, "randint", lambda a, b: 7)

    inputs = iter(["easy", "7"])  # choose difficulty then guess

    def fake_input(prompt=""):
        return next(inputs)

    printed = []

    def fake_print(*args, **kwargs):
        printed.append(" ".join(str(a) for a in args))

    score = number_guess.play_round(input_func=fake_input, print_func=fake_print, highscore_path=None)
    assert score > 0
    assert any("You guessed it right!" in p for p in printed)
