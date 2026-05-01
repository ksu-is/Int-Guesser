import random

print("Welcome to Int-Guesser! \nYou have 8 chances to guess the number. Let's begin by setting the range.")

low = int(input("Enter the Lower Range: "))
high = int(input("Enter the Upper Range: "))

print(f"\nYou have 8 chances to guess the number between {low} and {high}. Let's start!")

num = random.randint(low, high) 
ch = 8                        # Total number of allowed guesses. IF changed, adjust line 3 and 8 messages accordingly.
gc = 0                        # Current number of guesses.

while gc < ch:
    gc += 1
    guess = int(input('Enter your guess: '))

    if guess == num:
        print(f'Correct! The number is {num}. You guessed it in {gc} attempts.')
        break

    elif gc >= ch and guess != num:
        print(f'Sorry! The number was {num}. Better luck next time.')

    elif guess > num:
        print('Too high! Try a lower number.')

    elif guess < num:
        print('Too low! Try a higher number.')
