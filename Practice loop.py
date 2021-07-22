print('Is it raining?')
answer = input()
if answer.startswith('N') or answer.startswith('n'):
    print("Go Outside")


if answer.lower() == 'yes':
    print('Do you have an umbrella?')
    answer2= input()
    if answer2.lower() == 'yes':
        print("Take it and go outside")
    elif answer2.lower() == 'no':
        print("wait")
        while True:
            print('Is it still raining?')
            answer3=input()
            if answer3.lower()=='no':
                print("You can go out now")
                break
            if answer3.lower()=='yes':
                print('keep waiting')

