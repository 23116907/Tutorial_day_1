print('Is it raining?')
answer = input()
if answer == 'no' or answer == 'No':
    print("Go Outside")


if answer == 'yes' or answer == 'Yes' or answer == 'Yeah' or answer == 'yeah':
    print('Do you have an umbrella?')
    answer2= input()
    if answer2 == 'yes':
        print("Take it and go outside")
    elif answer2 == 'no' or answer2 == 'No':
        print("wait")
        print('Is it still raining?')
        answer3=input()
        if answer3=='no':
            print("You can go out now")
        if answer3=='yes':
            print('keep waiting')
            






