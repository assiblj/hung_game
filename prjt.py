import random

def choose_word_from_file(prjt):
    with open(prjt, 'r') as file:
        words = file.readlines()
    return random.choice(words).strip()


def display_game_state(word, guessed_letters, attempts, message=""):
    gallows = [
        "  ____  ",
        " |    | ",
        " |      ",
        " |      ",
        " |      ",
        " |      ",
        " |______",
    ]
    if attempts < 6:
        gallows[2] = " |    O "
    if attempts < 5:
        gallows[3] = f" |   {'/' if attempts < 4 else ' '}{f'//' if attempts < 3 else ' '}"
    if attempts < 2:
        gallows[4] = " |    | "
    if attempts == 0:
        gallows[3] = " |   / \ "

    word_display = ''
    for letter in word:
        if letter in guessed_letters:
            word_display += letter + ' '
        else:
            word_display += '_ '

    game_state = [
        "\nWelcome to Hangman!",
        "",
        *gallows,
        "",
        "Guess the word:",
        word_display,
        "",
        message,
    ]
    return "\n".join(game_state)


def play_hangman():
    print("\033[1;32;40mWelcome to Hangman!\033[0m")
    name = input("\033[1;33;40mEnter your name: \033[0m")
    print("\033[1;34;40mHello,", name + "!\033[0m")

    prjt = r'C:\Users\buoya\Desktop\pythooon\py objet\Hangman\prjt.txt'
    guessed_letters = set()
    attempts = 6
    score = 0
    level = 1

    while True:
        print(f"\n--- Level {level} ---")
        word = choose_word_from_file(prjt)

        word_display = '_ ' * len(word)

        print(display_game_state(word, guessed_letters, attempts))

        while attempts > 0:
            guess = input("\033[1;37;40mGuess a letter: \033[0m").lower()

            if guess in guessed_letters:
                print("\033[1;31;40mYou already guessed that letter.\033[0m")
                continue

            guessed_letters.add(guess)

            word_display = ''
            for letter in word:
                if letter in guessed_letters:
                    word_display += letter + ' '
                else:
                    word_display += '_ '

            if guess in word:
                print("\033[1;32;40mCorrect!\033[0m")
                print(display_game_state(word, guessed_letters, attempts))
                if all(c in guessed_letters for c in word):
                    score += 1
                    print("\033[1;35;40mCongratulations! You guessed the word:", word, "\033[0m")
                    print("\033[1;36;40mYour score is:", score, "\033[0m")
            else:
                attempts -= 1
                print("\033[1;31;40mIncorrect! Try again.\033[0m")
                print(display_game_state(word, guessed_letters, attempts))

        if attempts == 0:
            print("\033[1;31;40mSorry, you ran out of attempts. The word was:", word, "\033[0m")  # Red bold text

        play_again = input("\033[1;33;40mDo you want to play again? (yes/no): \033[0m").lower()  # Yellow bold text
        if play_again != 'yes':
            print("\033[1;32;40mThanks for playing!\033[0m")  # Green bold text
            break
        else:
            level += 1
            guessed_letters.clear()
            attempts = 6


play_hangman()
