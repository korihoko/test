# This is a guess the number game.
import random

nameInput = input("Hello. What is your name?\n")
nameInput.capitalize()
print('Well, {name}, I am thinking of a number between 1 and 20'.format(name=nameInput))

secretNumber = random.randint(1,20)
print('DEBUG: The secret number is ' + str(secretNumber) + '!')

try:
    for guessesTaken in range(1,7):
        print('Take a guess.')
        guess = int(input())

        if guess < secretNumber:
            print('Your guess was too low!')
        elif guess > secretNumber:
            print('Your guess was too high!')
        else:
            break #This is for the correct guess
except ValueError:
    print('You did not enter a number. Game shutting down.')

if guess == secretNumber:
    print('Good job, {name}! You took ' + str(guessesTaken) + ' guesses.'.format(name=nameInput))
else:
    print('You were not able to guess the number correctly. The number I was thinking of was ' + str(secretNumber) + '.\nPlease try again.')

