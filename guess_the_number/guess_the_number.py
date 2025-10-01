import random
import sys

num = random.randint(0,10)

while True:
    guess = int(input("What's your guess: "))
    if num == guess:
        print("You got it!")
        sys.exit()
    else:
        print("Too Low..." if guess < num else "Too High...")