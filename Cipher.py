import random
#sets the caesar cipher key
key = random.randint (1, 25)
print (key)#gives you the key, remove this for the key to be secret from the user
letters = 'abcdefghijklmnopqrstuvwxyz'
caps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
phrase = input('Type a phrase to be encoded: ')
encoded = ''
for char in phrase:
    inCaps = caps.find(char)
    if inCaps < 26 and inCaps > -1: #should only be true if there was a capital letter
        char = letters[inCaps]
    placeInLetters = letters.find(char)#if the current character is a letter, find its position in the letters variable. Then the next part of the code will change the letter using the position and the key
    if not(placeInLetters < 25 and placeInLetters > -1):
        encoded = encoded + char
    else:
        encoded = encoded + letters[(placeInLetters+key) % 26]
print(encoded)    
