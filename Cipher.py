import random
#sets the caesar cipher key
key = random.randint (1, 25)
print (key)
letters = 'abcdefghijklmnopqrstuvwxyz'
caps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
phrase = input('Type a phrase to be encoded: ')
encoded = ''
for place in range(0, len(phrase)):
    inCaps = caps.find(phrase[place])
    if inCaps < 26 and inCaps > -1: #should only be true if there was a capital letter
            phrase2 = ''#this variable handles some temporary stuff
            for i in range (0, len(phrase)): #goes through the user input, ready to replace the capital letter with a lowercase
                if i == place: #am I at the capital letter? if so add it to code 2 from the lowercase letter list
                    phrase2 += letters[inCaps]
                else: #otherwise, do nothing different
                    phrase2 += phrase[i]
            phrase = phrase2 
    placeInLetters = letters.find(phrase[place])
    if not(placeInLetters < 25 and placeInLetters > -1):
        encoded = encoded + phrase[place]
    else:
        encoded = encoded + letters[(placeInLetters+key) % 26]
print (encoded)    
