import re

txt = input()

pat = 'cool$'


if re.findall(pat, txt):
    print(True)
else:
    print(False)