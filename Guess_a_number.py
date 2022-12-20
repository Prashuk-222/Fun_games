import random

Range = input("Type a number: ")

if Range.isdigit():
    Range = int(Range)

    if Range <= 0:
        print('Please type a number larger than zero')
        quit()

else:
    print('Please type a number....')
    quit()

random_num = random.randint(0,Range)

guesses = 0

while True:
    guesses += 1
    user_guess =input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.')
        continue

    if user_guess == random_num:
        print("You got it!")
        break
    elif user_guess > random_num:
        print("You were above the random number!")
    else:
        print("You were below the random number!")

print("You got it in ", guesses, "guesses")
