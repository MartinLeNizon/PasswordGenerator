import random

password = ""
password_length = random.randint(8, 15)

for i in range(password_length):
		password += chr(random.randint(33, 125))

print(password)