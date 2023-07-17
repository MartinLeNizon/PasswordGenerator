import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-l', '--length', type=int, default=random.randint(8, 15), help='The number of character of the password')
parser.add_argument('--no-special-characters', action='store_true', help='Create the password without any special characters (only letters and numbers)');
args = parser.parse_args()

password = ""
password_length = args.length

if args.no_special_characters:
    ascii_range = list(range(48, 58)) + list(range(65, 91)) + list(range(97, 123))
else:
    ascii_range = list(range(33, 126))



for i in range(password_length):
		password += chr(random.choice(ascii_range))

print(password)