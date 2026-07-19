"""A console-based Hangman game for the CodeAlpha Python Internship."""

import random


WORDS = ["python", "apple", "planet", "computer", "guitar"]
MAX_INCORRECT_GUESSES = 6


def choose_word():
    """Return a random word from the predefined word list."""
    return random.choice(WORDS)


def display_word(word, guessed_letters):
    """Return the word with unguessed letters hidden by underscores."""
    return " ".join(letter.upper() if letter in guessed_letters else "_" for letter in word)


def get_guess(guessed_letters):
    """Read and validate one new alphabetic letter from the player."""
    while True:
        guess = input("\nGuess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter exactly one alphabetic letter.")
        elif guess in guessed_letters:
            print(f"You already guessed '{guess.upper()}'. Try another letter.")
        else:
            return guess


def check_guess(word, guess):
    """Return True when the guessed letter occurs in the word."""
    return guess in word


def play_game():
    """Run one complete round of Hangman."""
    word = choose_word()
    guessed_letters = set()
    attempts_left = MAX_INCORRECT_GUESSES

    print("\n" + "=" * 35)
    print("        WELCOME TO HANGMAN")
    print("=" * 35)

    while attempts_left > 0:
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Attempts Left: {attempts_left}")
        print("Guessed Letters:", " ".join(sorted(letter.upper() for letter in guessed_letters)) or "None")

        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)

        if check_guess(word, guess):
            print(f"Good job! '{guess.upper()}' is in the word.")
        else:
            attempts_left -= 1
            print(f"Sorry, '{guess.upper()}' is not in the word.")

        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations!")
            print(f"You guessed the word: {word.upper()}")
            return

    print("\nGame Over!")
    print(f"The word was {word.upper()}")


def play_again():
    """Ask whether the player wants another round."""
    while True:
        answer = input("\nPlay Again? (Y/N): ").strip().lower()
        if answer in {"y", "n"}:
            return answer == "y"
        print("Please enter Y for yes or N for no.")


def main():
    """Start the game and keep running while the player chooses to replay."""
    while True:
        play_game()
        if not play_again():
            print("\nThanks for playing Hangman!")
            break


if __name__ == "__main__":
    main()
