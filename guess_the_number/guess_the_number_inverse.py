import sys
import random


min_guess = 0
max_guess = 100
result = ""
intro = "=============================================\nThink of a number between 0-100\n=============================================\n\nl: if the number is lower than my guess\nh: if the number is high than my guess\nc: if I've guessed it right\n"
incorrect_input_count = 0

print(intro)
while True:
    guess = random.randint(min_guess, max_guess)
    
    result = input(f"Is {guess} the number you're thinking off?: ")

    match result:
        case "h":
            min_guess = guess
        case "l":
            max_guess = guess
        case "c":
            print(f"I'm the smartest. Thanks for playing with me!")
            if incorrect_input_count > 0:
                print(f"I'm glad it it only took you {incorrect_input_count + 1} times to understand how this works")
            sys.exit()
        case _:
            incorrect_input_count += 1
            print(f"\nI thought you were smart enough to understand the instruction in one go. Let me restate them for you\n")
            print(intro)
    
