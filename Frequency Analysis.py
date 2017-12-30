letters = 'abcdefghijklmnopqrstuvwxyz'
caps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
code = input('Please enter text you want to decode: ')
#finds the character frequency on any string
def char_frequency(str):
    dict = {}
    for n in str:
        if letters.find(n) > -1 and letters.find(n) < 26:            
            keys = dict.keys()
            if n in keys:
                dict[n] += 1
            else:
                dict[n] = 1
    return dict
freq = max(zip(char_frequency(code).values(), char_frequency(code).keys()))[1]
print (freq)
key = letters.find(freq)-4
print (key)
holder = ''
for place in range(0, len(code)):    
    inCaps = caps.find(code[place])
    if inCaps < 26 and inCaps > -1:
        code2 = ''
        for i in range (0, len(code)):
            if i == place:
                code2+=letters[inCaps]
            else:
                code2+=code[i]
        code = code2
    placeInLetters = letters.find(code[place])
    if not(placeInLetters < 26 and placeInLetters > -1):
        holder = holder + code[place]
    else:
        holder = holder + letters[(placeInLetters-key) % 26]
print (holder)
