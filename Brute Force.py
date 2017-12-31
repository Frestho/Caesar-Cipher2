letters = 'abcdefghijklmnopqrstuvwxyz'
caps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
code = input('Put your encoded Caesar Cipher here: ')
#loop that goes through every key, thus the brute force attck
for key in range (0, 25):
    holder = ''
    #this loop goes through every character in the encoded phrase and decodes it accordingly
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
            holder = holder + letters[(placeInLetters+key) % 26]
    print (holder)
