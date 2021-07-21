import random
print('Hello. What is your name?')
name = input()

print("Hello "+  name,'I am thinking of a number between 1 and 20, can you guess the number?')
secretNumber = random.randint(1, 20)


for guessesTaken in range(1, 7):
    print('Take a guess')
    guess = int(input())
if guess > secretNumber:
    print("Too high" + name)