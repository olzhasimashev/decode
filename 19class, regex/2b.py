import re

txt = input()

pat = 'a.+b$'


if re.findall(pat, txt):
    print(True)
else:
    print(False)