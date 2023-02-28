import re

txt = input()
txt_digits = re.sub(r'\D', '', txt)

pat="^[+]?(7|8)?(\s?)[(]?([0-9]{3})[)]?(\s?)([0-9]{3})(\s?)([0-9]{2})[-]?([0-9]{2})$"
pat_check=re.findall(pat,txt)

print(txt_digits)
if pat_check:
    if len(txt_digits)==10 and txt_digits[0]=="7":
        answer = '+7 ({}) {}-{}-{}'.format(txt_digits[:3], txt_digits[3:6], txt_digits[6:8], txt_digits[8:])
        print(answer)
    elif len(txt_digits)==11 and txt_digits[1]=="7":
        answer = '+7 ({}) {}-{}-{}'.format(txt_digits[1:4], txt_digits[4:7], txt_digits[7:9], txt_digits[9:])
        print(answer)
    else:
        print("What is this?")
else:
    print("What is this?")