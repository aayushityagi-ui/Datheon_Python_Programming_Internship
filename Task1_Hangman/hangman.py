
import random

# List of words
words = ["python", "developer", "computer", "programming", "keyboard"]

# Hangman drawings
hangman_stages = [
    """
     -----
     |   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
    =========
    """
]


def play_hangman():
    word = random.choice(words)
    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = 6

    print("\nWelcome to the Hangman Game!")
    print("Guess the word one letter at a time.")
    print("You have 6 incorrect attempts.\n")

    while incorrect_guesses < max_attempts:
        # Display the current word
        display_word = ""

        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("Word:", display_word)
        print("Guessed letters:", guessed_letters)
        print("Attempts remaining:", max_attempts - incorrect_guesses)

        # Check if the player has won
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word:", word)
            break

        guess = input("Guess a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one alphabet letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try another!\n")
            continue

        guessed_letters.append(guess)

        # Check the guessed letter
        if guess in word:
            print("Correct guess!\n")
        else:
            incorrect_guesses += 1
            print("Wrong guess!\n")

        # Display Hangman
        print(hangman_stages[incorrect_guesses])

    else:
        print("\nGame Over! You ran out of attempts.")
        print("The correct word was:", word)


# Start the game
play_hangman()
