import math
import random

smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))

# calculate the minimum number of guesses needed
min_guesses = math.ceil(math.log(larger - smaller + 1, 2))

print("Alright, I will guess your number within", min_guesses, "tries.")

user_number = int(input("Enter your number for me to guess: "))

if user_number < smaller or user_number > larger:
    print("Your number must be between the smaller and larger numbers you've entered!")
else:
    count = 0
    while True:
        count += 1
        # guess the midpoint
        my_guess = (smaller + larger) // 2

        if my_guess < user_number:
            print(my_guess, "is too small!")
            smaller = my_guess + 1
        elif my_guess > user_number:
            print(my_guess, "is too large!")
            larger = my_guess - 1
        else:
            print("I've got it! Your number is", my_guess, "and I've guessed it in", count, "tries!")
            break

        if count > min_guesses:
            print("You cheated! I've guessed more than the minimum number of times.")
            break
