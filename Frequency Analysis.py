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
key = letters.find(freq)-4#4 is the index of the letter e
print (key)#prints what the program thinks the key is
holder = ''
for char in code:
        #****
        #this part of the code handles capital letters.
        inCaps = caps.find(char) #if there is a capital letter, this line finds its position in the alphabet
        if inCaps < 26 and inCaps > -1: #should only be true if there was a capital letter
            char = letters[inCaps]
        #****
        placeInLetters = letters.find(char)#if the current character is a letter, find its position in the letters variable. Then the next part of the code will change the letter using the position and the key
        if not(placeInLetters < 26 and placeInLetters > -1):
            holder = holder + char
        else:
            holder = holder + letters[(placeInLetters-key) % 26]
print (holder)
