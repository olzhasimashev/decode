import re

txt = input().lower()

pat = 'decode'


index = re.search(pat, txt)
if index:
    print(index.start(), index.end())
else:
    print(False)