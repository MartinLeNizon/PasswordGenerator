import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--length', type=int, default=random.randint(8, 15), help='The number of character of the password')
args = parser.parse_args()

password = ""
password_length = args.length


for i in range(password_length):
		password += chr(random.randint(33, 125))

print(password)