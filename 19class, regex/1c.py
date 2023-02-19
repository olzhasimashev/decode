import re

txt = input()
pat = '[A-Z][a-z]'

if re.findall(pat, txt):
    print(True)
else:
    print(False)