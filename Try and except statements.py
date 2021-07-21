def div42by(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: You tried to divide by zero')


print(div42by(2))
print(div42by(3))
print(div42by(6))
print(div42by(0))
print(div42by(7))

print('How many cats do you have?')
numCats = input()
try:
    if int(numCats) >= 4:
        print("That's a lot of cats")
    elif int(numCats) <0:
        print('Error')
    else:
        print('That is not as much')
except ValueError:
    print('You did not enter a number')



