import random

number=random.randint(1,9)
print(number)

chances=0
print("Enter your Guess: ")
while chances<5:
    guess = int(input("Guess a number from 1-9 "))
    if guess == number:
        print("Congratulations! You Win!")
        break
    elif guess<number:
        print("Your guess was too low. Try a number higher than ", guess)
    else:
        print("Your guess was too high. Try an number lower than ", guess)
    chances = chances+1
if not chances<5:
    print("Game Over! The number was ", number,".")