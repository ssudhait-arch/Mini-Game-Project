"""
Mini Game Project
1. Guess the Number
2. Word Scramble

Author : Your Name
"""

# Import random module
import random


# ---------------------------------------------------
# GAME 1 : GUESS THE NUMBER
# ---------------------------------------------------

def guess_the_number():
    """
    This function runs the Guess the Number game.
    """

    print("\n========== GUESS THE NUMBER ==========")

    # Random number between 1 and 100
    secret_number = random.randint(1, 100)

    # Variable to count attempts
    attempts = 0

    print("I have selected a number between 1 and 100.")
    print("Try to guess the number!")

    # Loop until user guesses correctly
    while True:

        # Get input from user
        guess = input("Enter your guess: ")

        # Check if input is numeric
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        # Convert string to integer
        guess = int(guess)

        # Increase attempt count
        attempts += 1

        # Conditions
        if guess < secret_number:
            print("Too Low!")

        elif guess > secret_number:
            print("Too High!")

        else:
            print("\nCongratulations!")
            print(f"You guessed the number in {attempts} attempts.")
            break

# ---------------------------------------------------
# GAME 2 : WORD SCRAMBLE
# ---------------------------------------------------

def scramble_word(word):
    """
    This function scrambles the letters of a word.
    """

    # Convert word into list
    word_list = list(word)

    # Shuffle letters
    random.shuffle(word_list)

    # Convert list back to string
    scrambled = "".join(word_list)

    return scrambled


def word_scramble_game():
    """
    This function runs the Word Scramble game.
    """

    print("\n========== WORD SCRAMBLE ==========")

    # Word list
    words = [
        "python",
        "javascript",
        "java",
        "automation",
        "pytest",
        "guvi",
        "selenium"
    ]

    # Randomly choose a word
    original_word = random.choice(words)

    # Scramble the word
    scrambled_word = scramble_word(original_word)

    print(f"Unscramble this word: {scrambled_word}")

    # Maximum attempts
    max_attempts = 3

    # Loop for attempts
    for attempt in range(1, max_attempts + 1):

        # User input
        user_guess = input(f"Attempt {attempt}: ").lower()

        # Check answer
        if user_guess == original_word:
            print("Correct! You guessed the word.")
            break

        else:
            print("Wrong guess!")

    else:
        print(f"\nGame Over! The correct word was '{original_word}'.")


# ---------------------------------------------------
# MAIN MENU
# ---------------------------------------------------

def main():
    """
    Main function for menu selection.
    """

    while True:

        print("\n========== MINI GAME MENU ==========")
        print("1. Guess the Number")
        print("2. Word Scramble")
        print("3. Exit")

        choice = input("Enter your choice: ")

        # Menu conditions
        if choice == "1":
            guess_the_number()

        elif choice == "2":
            word_scramble_game()

        elif choice == "3":
            print("Thank you for playing!")
            break

        else:
            print("Invalid choice. Please try again.")


# Program execution starts here
if __name__ == "__main__":
    main()
