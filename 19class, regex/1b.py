import re

txt = input()
pat = '[a-zA-Z0-9]'

if re.findall(pat, txt):
    print('Nashel sovpadenie')
else:
    print('Ne nashel sovpadenie')