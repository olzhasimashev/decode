student = {
    'name' : 'Aidana',
    'age' : 21,
    'gpa' : 3.88
}

def reverse(word):
    return word[::-1]

def sum_index(values):
    return max(values)+min(values)

def char_count(value):
    d = {}
    for i in value:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for i in d:
        print(i, ':', d[i])