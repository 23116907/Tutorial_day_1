letter = 'A'
spam = [['cat', 'bat', 'rat'], [letter]]
print(spam[0][1])
print(spam[0][-1])
print('The ' +spam[0][-1] + ' is afraid of the ' +spam[0][0]+'.')

list1 = [1, 2, 3]
list1[0] = 'Hi'
print(list1)

list1[1:3] = ['I', 'am', 'here']
print(list1)
print(list1[1:])

del spam[1]
print(spam)

print(range(4))
print(list(range(5)))
print(list(range(4, 41, 4)))

items = ['computers', 'pens', 'books']
for i in range(len(items)):
    print('Item ' + str(i) + ' in items is ' + items[i])

print(items.index('computers'))
items.insert(1, 'rulers')
print(items)

index = ['rat', 'mouse', 'cat', 'Dog', 'mouse']
index.sort()
print(index)
index.remove('mouse')
print(index)
index.remove('mouse')
print(index)

group = [2, 5, 6, 7, 8, 2, 4, 2]
group.sort()
print(group)

print(list('Hello'))

name = 'Shravan the coder'
newname = name[0:11] + ' hardworking ' + name[12:17]
print(newname)

def eggs(cheese):
    cheese.append('Hello')
spam = [1, 2, 3]
eggs(spam)
print(spam)

import copy
span = ['A', 'B', 'C', 'D']
cheese = copy.deepcopy(span)
print(cheese)

fruits = ['apples',
          'orange',
          'bananas',
          'lemons']
print('Four score and seven' +\
      ' years ago')