import re

batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The adventures of Batman')
print(mo.group())
print(mo == None)

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
re = phoneRegex.search('My phone number is 542-2006')
print(re.group())


batRegex1 = re.compile(r'Bat(wo)*man')#lines 13-15 strangely did not work here despite working on idle
print(batRegex1.search('The adventures of batman'))
print(batRegex1.search('The adventures of batwoman'))

