
import re
pattern = r'\+\d{2} \d{3} \d{2} \d{2} \d{2}'
p = re.compile(pattern)

print(p.match('+32 496 44 36 18'))