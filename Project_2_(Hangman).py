import random

def hangman():
    word_list = ['algorithm', 'function', 'variable', 'compile', 'iterate', 'recursion', 'binary', 'array', 'syntax', 'pointer']
    word = random.choice(word_list)
    guessed = ['_'] * len(word)
    guessed_letters = []
    tries = 7
    wrong_guesses = 0

    print("Welcome to Hangman!")
    print("Disclaimer: All the words are related to Computer Programming!")
    
    while tries >0:
        print(f"Word to guess: {' '.join(guessed)}")

        caret_position = " " * 2 * wrong_guesses + "^"
        print(f"    H A N G M A N")
        print(f"    {caret_position}")

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter!")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")

            for i in range(len(word)):
                if word[i] == guess:
                    guessed[i] = guess

        else:
            wrong_guesses +=1
            tries -=1
            print(f"Oops! '{guess}' is not in the word.")

        if "_" not in guessed:
            print(f"\nCongratulations! You have guessed the word: {''.join(guessed)}")
            print(f"Phew... you are saved")
            again = input("\nDo you want to play again: ")
            if(again.lower() == 'yes'):
                hangman()
            else:
                exit

    else:
        print(f"\nGame over! The word was: {word}")
        print("You are hanged")
        again = input("\nDo you want to play again: ")
        if(again.lower() == 'yes'):
            hangman()
        else:
            exit


hangman()