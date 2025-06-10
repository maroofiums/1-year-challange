# # Guess the Number
# import random 

# number = random.randint(1,10)


# while True:
#     guess = int(input("Enter The Number(1-10):  "))
#     if guess == number:
#         print("Correct🎉")
#         break
#     else:
#         print("You are wrong❌")

# Check password
import random 
import string

while True:
    length = int(input("enter password length: "))
    chars = string.ascii_letters+string.ascii_lowercase+string.ascii_uppercase+string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))

    print(f"Generated password is {password}")