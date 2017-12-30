words_file = open('google-10000-english.txt')#by default this reads the file
words = words_file.readlines()
for i in range(0, len(words)):
    words[i] = words[i].rstrip()
letters = 'abcdefghijklmnopqrstuvwxyz'
caps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
code = input('Put your encoded Caesar Cipher here: ')
all_codes = {}#this is the dictionary that will hold all possible phrases using a Caesar Cipher, each having a corresponding number that represents the amount of English words in the phrase
#loop that goes through every key, thus the brute force attack
for key in range (0, 25):
    holder = ''#defines a variable that will HOLD a decoded phrase temporarily
    #this loop goes through every character in the encoded phrase and decodes it accordingly
    for char in code:
        #****
        #this part of the code handles capital letters.
        inCaps = caps.find(char) #if there is a capital letter, this line finds its position in the alphabet
        if inCaps < 26 and inCaps > -1: #should only be true if there was a capital letter
            code2 = ''#this variable handles some temporary stuff
            for i in range (0, len(code)): #goes through the user input, ready to replace the capital letter with a lowercase
                if i == place: #am I at the capital letter? if so add it to code 2 from the lowercase letter list
                    code2 += letters[inCaps]
                else: #otherwise, do nothing different
                    code2 += code[i]
            code = code2 
        #****
        placeInLetters = letters.find(char)#if the current character is a letter, find its position in the letters variable. Then the next part of the code will change the letter using the position and the key
        if not(placeInLetters < 26 and placeInLetters > -1):
            holder = holder + char
        else:
            holder = holder + letters[(placeInLetters+key) % 26]
    all_codes.update({holder:0})#adds the decoded phrase to a dictionary for later use. see line 8 for more info
#goes through all brute forced strings and finds the one with most english words
for i in all_codes.keys():
    separated_words = i.split() #makes the decoded string into a list of words
    for j in separated_words: #goes through the word list and checks if each item on the list is in the real word list or not
        if j in words:#if it found one of the words in the real words file, the value associated with the key in the codes dictionary goes up by one.
            all_codes[i] += 1
#print(all_codes) #remove the '#' at the beginning of this line to have the program show the list of phrases with the amount of words found in them.
for i in range(0, len(all_codes)):
    high = max(zip(all_codes.values(), all_codes.keys()))[1] #finds the key (phrase) with the highest value (# of words) in the dictionary of all phrases
    print(high)#prints that phrase
    del all_codes[high]#deletes that phrase so the next time the loop runs, it will give the NEXT phrase with the most words. In case the first one wasn't the real phrase.
