import random

def hangman():
    # List of words to choose from
    word_list = ['python', 'java', 'react','JavaScript','PHP','Ruby','developer', 'algorithm', 'data', 'structure']
    
    # Select a random word
    word_to_guess = random.choice(word_list)
    guessed_word = ['_'] * len(word_to_guess)
    guessed_letters = set()
    max_attempts = 6
    attempts = 0

    print("Welcome to Hangman!")
    print("Coding")
    print("You have", max_attempts, "incorrect guesses allowed.")
    print("Word to guess:", ' '.join(guessed_word))

    while attempts < max_attempts:
        guess = input("\nGuess a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetic character.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try a different one.")
            continue

        guessed_letters.add(guess)

        if guess in word_to_guess:
            print("Good guess!")
            for i, letter in enumerate(word_to_guess):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            print("Incorrect guess.")
            attempts += 1

        print("Word to guess:", ' '.join(guessed_word))
        print("Attempts remaining:", max_attempts - attempts)

        if '_' not in guessed_word:
            print("\nCongratulations! You've guessed the word:", word_to_guess)
            break
    else:
        print("\nGame over! The word was:", word_to_guess)

# Run the game
if __name__ == "__main__":
    hangman()
