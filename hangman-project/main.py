import random

words_list = ["apple", "banana", "ananas", "orange", "grapes", "pineapple", "peach", "tomato", "potato", "mushroom", "carrot"]

# Checks that all letter guessed
def check_win(secret_word, old_letters_guessed):
    for letter in secret_word:
        if letter not in old_letters_guessed:
            return False
    return True

# Displays guessed letters and hides non guessed letters
def show_hidden_word(secret_word, old_letters_guessed):
    display = ""
    for letter in secret_word:
        if letter in old_letters_guessed:
            display += letter + " "
        else:
            display += "_ "
    return display

# Checks valid letters
def check_valid_input(letter_guessed, old_letters_guessed):
    if not letter_guessed.isalpha() or len(letter_guessed) != 1:
        if not letter_guessed.isalpha() and len(letter_guessed) != 1:
            print("\nLetter must be alpha.\nLetter not must be longer than one character.") 
        elif not letter_guessed.isalpha():
            print("\nLetter must be alpha.")
        elif len(letter_guessed) != 1:
            print("\nLetter not must be longer than one character.")
        return False
    if letter_guessed in old_letters_guessed:
        print("\nYou guessed this letter!")
        return False
    return True

# Checks that letter exists in old_letter_guessed
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if not check_valid_input(letter_guessed, old_letters_guessed):
        print("\nGuessed letters: ")
        print(", ".join(sorted(old_letters_guessed)))
        return False
    letter_guessed = letter_guessed.lower()
    old_letters_guessed.append(letter_guessed)
    return True

# Choose random word from list
def choose_word(words_list):
    hidden_word = random.choice(words_list)
    return hidden_word

# Prints current attempt in the game
def print_hangman(num_of_tries):
    hangman_pics = [
    """
    """,
    """
    x
    |
    |
    |
    |
    |
    x
    """,
    """
    x--------x
    |
    |
    |
    |
    |
    x
    """,
    """
    x--------x
    |        |
    |
    |
    |
    |
    x
    """,
    """
    x--------x
    |        |
    |        0
    |
    |
    |
    x
    """,
    """
    x--------x
    |        |
    |        0
    |        |
    |
    |
    x
    """,
    """
    x--------x
    |        |
    |        0
    |       /|
    |
    |
    x
    """,
    """
    x--------x
    |        |
    |        0
    |       /|\\
    |
    |
    x
    """,
    """
    x--------x
    |        |
    |        0
    |       /|\\
    |       /
    |
    x
    """,
    """
    x--------x
    |        |
    |        0
    |       /|\\
    |       / \\
    |
    x
    """,
    """
    x--------x
    |        |
    |        0
    |       /|\\
    |       / \\
    |
    x______KAPUT!
    """
    ]
    print(hangman_pics[num_of_tries])

def main():
    print(f"Welcome to the game Hangman\n") 

    secret_word = choose_word(words_list)
    old_letters_guessed = []
    num_of_tries = 0
    max_tries = 10

    print("\nLet’s start!\n")
    print_hangman(num_of_tries)
    print(show_hidden_word(secret_word, old_letters_guessed))

    while num_of_tries < max_tries:
        letter_guessed = input("Guess a letter: ").strip().lower()

        if try_update_letter_guessed(letter_guessed, old_letters_guessed):
            if letter_guessed not in secret_word:
                num_of_tries += 1
                print(f"\nWrong letter! \nThe letter {letter_guessed.upper()} is not exist in secret word.")
                print_hangman(num_of_tries)
            print(show_hidden_word(secret_word, old_letters_guessed))
            if check_win(secret_word, old_letters_guessed):
                print("\nCongratulations! \nYou are won the game!")
                break
        else:
            print_hangman(num_of_tries)
            print(show_hidden_word(secret_word, old_letters_guessed))

    if num_of_tries == max_tries:
        print(f"\nGame over! \nThe word was {secret_word}.")

if __name__ == "__main__":
    main()