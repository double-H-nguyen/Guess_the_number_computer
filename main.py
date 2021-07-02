# Requirements
# * Computer will choose a random number
# * We (the user) will guess the number
import random


def main():
    # Generate a secret number for the computer
    secret_number = random.randint(1, 10)

    while True:
        # Ask the user to guess the number
        guessed_num = int(input('Guess the secret number between 1-10: '))

        # Determine if the guessed number is greater, lesser, or equal to the computer's number
        # If number is greater than computer's number, tell the user it's greater and try again
        if guessed_num > secret_number:
            print('Your guess was greater than the secret number.')
        # If number is lesser than computer's number, tell the user it's lesser and try again
        elif guessed_num < secret_number:
            print('Your guess was less than the secret number.')
        # If number is equal to the computer's number, end the game
        elif guessed_num == secret_number:
            print(f'You guessed the correct! The number was {secret_number}!')
            break


if __name__ == '__main__':
    main()
