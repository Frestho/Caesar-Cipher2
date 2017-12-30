letters = 'abcdefghijklmnopqrstuvwxyz'
caps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
code = input('Put your encoded Caesar Cipher here: ')
#loop that goes through every key, thus the brute force attck
for key in range (0, 25):
    holder = ''
    #this loop goes through every character in the encoded phrase and decodes it accordingly
    for place in range (0, len(code)):
        #****
        #this part of the code handles capital letters.
        inCaps = caps.find(code[place]) #if there is a capital letter, this line finds its position in the alphabet
        if inCaps < 26 and inCaps > -1: #should only be true if there was a capital letter
            code2 = ''#this variable handles some temporary stuff
            for i in range (0, len(code)): #goes through the user input, ready to replace the capital letter with a lowercase
                if i == place: #am I at the capital letter? if so add it to code 2 from the lowercase letter list
                    code2 += letters[inCaps]
                else: #otherwise, do nothing different
                    code2 += code[i]
            code = code2 
        #****
        placeInLetters = letters.find(code[place])
        if not(placeInLetters < 26 and placeInLetters > -1):
            holder = holder + code[place]
        else:
            holder = holder + letters[(placeInLetters+key) % 26]
    print (holder)
