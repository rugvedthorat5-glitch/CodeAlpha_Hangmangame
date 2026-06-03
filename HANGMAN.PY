
import random

WORDS = ['python', 'robot', 'engineer', 'castle', 'planet']
MAX_WRONG = 6

def display_state(secret, guessed, wrong, used):
    # show current word with guessed letters and wrong guesses
    masked = ' '.join([c if c in guessed else '_' for c in secret])
    print('\n' + masked)
    print(f'Wrong guesses: {wrong} / {MAX_WRONG}')
    if used:
        print('Tried letters:', ' '.join(sorted(used)))

def play_game():
    # run one round of Hangman
    secret = random.choice(WORDS)
    guessed = []   # letters correctly guessed
    used = []      # letters already tried
    wrong = 0
    while wrong < MAX_WRONG and any(c not in guessed for c in secret):
        display_state(secret, guessed, wrong, used)
        guess = input('Guess a letter: ').strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print('Please enter a single letter.')
            continue
        if guess in used:
            print('You already tried that letter.')
            continue
        used.append(guess)
        if guess in secret:
            guessed.append(guess)
            print('Good guess!')
        else:
            wrong += 1
            print('Wrong guess.')
    # result
    if all(c in guessed for c in secret):
        print(f"\nYou won! The word was \"{secret}\".")
    else:
        print(f"\nYou lost. The word was \"{secret}\".")

if __name__ == '__main__':
    print('Simple Hangman - 6 wrong guesses allowed.')
    while True:
        play_game()
        again = input('Play again? (y/n): ').strip().lower()
        if again != 'y':
            print('Thanks for playing!')
            break
