myCat = {'size': 'fat', 'color':'gray', 'disposition':'loud'}
print(myCat['size'])
print('My cat has ' + myCat['color'] + ' fur.')

print([1, 2, 3]==[3, 2, 1])
print({1, 2, 3, 4, 5} == {2, 4, 3, 1, 5}) #order does not matter

print(list(myCat.keys())) # prints the parts on the left of :
print(list(myCat.values())) # prints the description on right of :
print(list(myCat.items())) # prints all pairs in brackets


for k, v in myCat.items():
    print(k, v)

print('size' in myCat.keys())

print(myCat.get('size', 'none'))

print('I have a ' +str(myCat.get('color')) + ' and ' +str(myCat.get('size')) + ' cat.')

myCat.setdefault('speed', 'slow') # must change it the first time, won't change later
print(myCat)

message = 'It was a warm day in June, and people were enjoying themselves.'
count = {}

for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character] + 1

import pprint

text = pprint.pformat(count)
print(text)

