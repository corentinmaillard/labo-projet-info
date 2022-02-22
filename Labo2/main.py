
import re

#ex 1.a
pattern = r'\+\d{2} \d{3} \d{2} \d{2} \d{2}'
p = re.compile(pattern)

print(p.match('+32 496 44 36 18'))


#ex 1.b
pattern = r'-?\+?\d+'
p = re.compile(pattern)

print(p.match('-12'))
print(p.match('123'))
print(p.match('+123'))

#ex 1.c
pattern = r'\d\d{3}[A-Z]{3}|\d[A-Z]{3}\d{3}'
p = re.compile(pattern)

print(p.match('1234AFD'))
print(p.match('1GHT534'))

#ex 1.d
pattern = r'C:\\'
p = re.compile(pattern)

print(p.match('C:\\'))