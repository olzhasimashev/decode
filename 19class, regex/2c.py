import re

txt = input()

pat = '^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'


if re.findall(pat, txt):
    print(True)
else:
    print(False)