import re

txt = input()

pat = '[\d]'


if re.findall(pat, txt):
    print(True)
else:
    print(False)