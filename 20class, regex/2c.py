import re

txt = input()

pat = r'\b[A-Z][a-z]+\b'

answer = re.findall(pat, txt)
print(answer)