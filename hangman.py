import random

# List of predefined words
words = ["python", "computer", "program", "hangman", "gaming"]

# Select a random word
word = random.choice(words)

# Create hidden word display
guessed_word = ["_"] * len(word)

# Variables
guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("=== Welcome to Hangman Game ===")

# Game loop
while wrong_guesses < max_wrong and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))
    print("Wrong guesses left:", max_wrong - wrong_guesses)
    print("Guessed letters:", guessed_letters)

    # Take input from user
    guess = input("Enter a letter: ").lower()

    # Check input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter.")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Add letter to guessed list
    guessed_letters.append(guess)

    # Check if letter is in word
    if guess in word:
        print("Correct guess!")

        # Reveal matching letters
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        print("Wrong guess!")
        wrong_guesses += 1

# Game result
if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over!")
    print("The correct word was:", word)