import random

secret = random.randint(1, 20)
tries = 0

while True:
    guess = int(input("Enter the number: "))
    tries += 1
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print(f"🎉 Correct! You guessed it in {tries} tries.")
        break
