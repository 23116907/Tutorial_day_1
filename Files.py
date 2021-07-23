print('c:\\spam\\eggs.png')#on idle, this line printed with two slashes
print('\\')
print(r'c:\\spam\\eggs.png')
print('\\'.join(['folder1', 'folder2', 'folder3']))#on idle, two slashes printed but here, only one prints

import os
print(os.path.join('folder1', 'folder2', 'folder3', 'file.png'))#once again, idle printed it with two slashes

print(os.sep)

print(os.path.isabs('..\\..\\spam.png'))

print(os.path.relpath('c:\\folder1\\folder1\\spam.png', 'c:\\folder1'))

print(os.path.getsize('c:\\windows\\system32\\calc.exe'))


os.makedirs('c:\\delicious\\walnut\\waffles')


