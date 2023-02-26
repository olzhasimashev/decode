import re

txt = input().lower()

pat = '^[the]'


if re.findall(pat, txt):
    print(True)
else:
    print(False)