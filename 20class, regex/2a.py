import re

txt = input().lower()

pat = '(^(https://))|(^(http://))\w+[.]\w+[/]{0,1}'


index = re.findall(pat, txt)
if index:
    print(True)
else:
    print(False)