# ============================================================
# Day 19 - Mini Project: Number Guessing Game
# File: day19_guessing_game.py
# ============================================================

import random
# 'import' brings in EXTRA functionality that isn't built into
# Python by default. 'random' is a module (a pre-written
# collection of code) that lets us generate random numbers.


# ── SECTION 1: Core Game Logic Functions ──────────────────────

def generate_secret_number(low, high):
    return random.randint(low, high)
    # random.randint(low, high) picks a random WHOLE number,
    # including BOTH low and high (unlike range(), which excludes the stop value!)


def get_valid_guess(low, high):
    """Keeps asking until the user enters a valid number within range."""
    while True:
        user_input = input(f"Enter your guess ({low}-{high}): ").strip()
        try:
            guess = int(user_input)
            if guess < low or guess > high:
                print(f"  Please enter a number between {low} and {high}.")
                continue
            return guess
        except ValueError:
            print("  Invalid input! Please enter a whole number.")


def give_hint(guess, secret):
    if guess < secret:
        return "Too Low! Try a higher number."
    elif guess > secret:
        return "Too High! Try a lower number."
    else:
        return "Correct!"


def calculate_score(attempts_used, max_attempts):
    # Fewer attempts used = higher score. Simple scoring formula.
    return max(0, (max_attempts - attempts_used + 1) * 10)


# ── SECTION 2: Difficulty Level Selector ──────────────────────

def choose_difficulty():
    print("\nSelect Difficulty Level:")
    print("  1. Easy   (1-50,  10 attempts)")
    print("  2. Medium (1-100, 7 attempts)")
    print("  3. Hard   (1-200, 5 attempts)")

    while True:
        choice = input("Enter choice (1-3): ").strip()
        if choice == "1":
            return 1, 50, 10
        elif choice == "2":
            return 1, 100, 7
        elif choice == "3":
            return 1, 200, 5
        else:
            print("  Invalid choice! Please select 1, 2, or 3.")


# ── SECTION 3: Single Round of the Game ───────────────────────

def play_round():
    low, high, max_attempts = choose_difficulty()
    secret_number = generate_secret_number(low, high)

    print(f"\nI'm thinking of a number between {low} and {high}.")
    print(f"You have {max_attempts} attempts. Good luck!\n")

    attempts_used = 0
    guess_history = []

    while attempts_used < max_attempts:
        attempts_used += 1
        print(f"--- Attempt {attempts_used}/{max_attempts} ---")

        guess = get_valid_guess(low, high)
        guess_history.append(guess)

        hint = give_hint(guess, secret_number)
        print(hint)

        if guess == secret_number:
            score = calculate_score(attempts_used, max_attempts)
            print(f"\n🎉 Congratulations! You guessed it in {attempts_used} attempt(s)!")
            print(f"Your score: {score} points")
            print(f"Your guesses: {guess_history}")
            return True, attempts_used, score

        remaining = max_attempts - attempts_used
        if remaining > 0:
            print(f"You have {remaining} attempt(s) left.\n")

    # If the loop finishes WITHOUT a correct guess (all attempts used up)
    print(f"\n😞 Game Over! You've used all {max_attempts} attempts.")
    print(f"The secret number was: {secret_number}")
    print(f"Your guesses: {guess_history}")
    return False, attempts_used, 0


# ── SECTION 4: Main Game Loop (Play Multiple Rounds) ──────────

def run_game():
    print("=" * 45)
    print("       NUMBER GUESSING GAME")
    print("=" * 45)

    total_wins = 0
    total_rounds = 0
    total_score = 0

    while True:
        total_rounds += 1
        won, attempts, score = play_round()

        if won:
            total_wins += 1
            total_score += score

        print("\n" + "-" * 45)
        print(f"Stats so far: {total_wins} win(s) out of {total_rounds} round(s)")
        print(f"Total score: {total_score}")
        print("-" * 45)

        play_again = input("\nPlay another round? (yes/no): ").strip().lower()
        if play_again != "yes":
            break

    print("\n" + "=" * 45)
    print("           FINAL STATISTICS")
    print("=" * 45)
    print(f"  Rounds Played : {total_rounds}")
    print(f"  Rounds Won    : {total_wins}")
    win_rate = (total_wins / total_rounds) * 100
    print(f"  Win Rate      : {win_rate:.1f}%")
    print(f"  Total Score   : {total_score}")
    print("=" * 45)
    print("\nThanks for playing! Goodbye!")


# ── SECTION 5: Program Entry Point ─────────────────────────────

if __name__ == "__main__":
    run_game()

# ============================================================
# END OF DAY 19
# ============================================================