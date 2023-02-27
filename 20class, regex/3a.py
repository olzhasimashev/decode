import re

txt = input()

pat = '\b[a-z0-9_.]+[@]{1}[a-z]{2,6}[.]{1}[a-z]{2,4}\b'

answer = re.findall(pat, txt)
if answer:
    print("Send me meme")
else:
    print("Uh?")