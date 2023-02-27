import re

txt = input()

txt_digits = re.sub(r'\D', '', txt)

if len(txt_digits) == 10:
    answer = '+7 ({}) {}-{}-{}'.format(
        txt_digits[:3], txt_digits[3:6], txt_digits[6:8], txt_digits[8:])
    print(answer)
elif len(txt_digits) == 11:
    answer = '+7 ({}) {}-{}-{}'.format(
        txt_digits[1:4], txt_digits[4:7], txt_digits[7:9], txt_digits[9:])
    print(answer)
else:
    print('What is this?')