import re

txt = input()

pat = '(" ")|(".")|(",")'


print(re.split(pat, txt))
