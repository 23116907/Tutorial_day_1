#615-234-1324
import re


phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneNumRegex.findall('Call me 415-555-1011 tomorrow or 415-551-2043 tomorrow.'))

phonenumregex1 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phonenumregex1.search('My number is 415-555-4242')
print(mo.group())
print(mo.group(1))
print(mo.group(2))
phonenumregex1 = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
print(mo.group())

batRegex = re.compile(r'Bat(man|mobile|coptor|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())