import re

txt = input()

pat = '[.,\s]'


print(re.split(pat, txt))