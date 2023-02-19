sampledict = {
    'physics': 82,
    'math': 65,
    'history': 75
}

for i in sampledict.keys():
    if sampledict.get(i) == min(sampledict.values()):
        print(i)