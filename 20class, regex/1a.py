import re

txt = input()

pat = '\d'


print(re.sub(pat, ' ', txt))
