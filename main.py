from random import randint

tries = 0
estimated = 0
secret_number = randint(1,100)

name = input("Tell me your name: ")

print(f"Hello {name}, i have thought in a number between 1 and 100\nYou have 8 tries to guess which number is")

while tries < 8:
    estimated = int(input("Which is the number?: "))
    tries += 1

    if estimated not in range(1,101):
        print("Your number is not in range between 1 and 100")
    elif estimated < secret_number:
        print("My number is higher")
    elif estimated > secret_number:
        print("My number is lower")
    else:
        print(f"Congratulations {name}! You guessed in {tries} tries")
        break

if estimated != secret_number:
    print(f"Sorry, attempts have been exhausted. The secret number was {secret_number}")