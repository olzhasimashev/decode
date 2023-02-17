def letters():
    s = set()
    for i in sentence:
        if i !=' ':
            s.add(i)
    print(s)

sentence = input()
letters()