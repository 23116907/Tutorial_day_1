print('"That is Alice\'s cat"')
print("Hello there!\n'How are you?'\nI am good")

spam = 'Hello World!'
print(spam.upper())
print(spam.lower())

print('Hello'.upper())
print('hello'.isalpha())
print('hello world'.isalpha())
print('Hello world'.startswith('H'))

print(','.join(['Cats', 'Rats', 'Bats']))

print('Hello'.center(20, ':'))

import pyperclip
pyperclip.copy('Hello Everyone!!!')
print(pyperclip.paste())

name = 'John'
place = 'my house'
time = '6:00'
food = 'cake'

print('Hello ' + name + ', you are invited to a party in ' + place + ' at ' + time+'. Please bring ' + food)

print('Do you want to play again?')

answer = input()
if answer.lower() == 'yes':
    print('All right')
elif answer.lower() == 'no':
    print('See you later')

