import random
import string

length = int(input("Enter the length of password: "))
chars = string.ascii_letters+string.ascii_lowercase+string.punctuation+string.ascii_uppercase+string.digits
password = ''.join(random.choice(chars) for _ in range(length))
print(f"The passwoed is {password}")