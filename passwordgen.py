#Logan Borrero
#CSI 4480 Final Project
#Password Generator

import string
import random

print("Specify the desired length of your password: ")
length = int(input())

password = []
values = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

if length >= 12:
    for x in range(length):
        randomize = random.choice(values)
        password.append(randomize)
    print("Your new Password is:", "".join(password))
else:
    print("Invalid length. A strong password should be at least 12 digits long.")

