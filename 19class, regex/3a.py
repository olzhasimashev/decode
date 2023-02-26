import re

txt = input()

pat = '^(7|8)(7{1})(\d{2})(\d{7})$'


if re.findall(pat, txt):
    print("Call me maybe")
else:
    print("Something else")