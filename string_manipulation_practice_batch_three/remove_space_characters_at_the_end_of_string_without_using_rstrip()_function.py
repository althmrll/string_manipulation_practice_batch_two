#Ask user to input sentence
sentence= input("Input sentence:")

#strip space at the end without using rstrip
    #reverse sentence
    reversed_sentence=sentence[::-1]
    #lstrip sentence
    strip=reversed_sentence.lstrip()
    #reverse sentence again
    rstrip=strip[::-1]

#print output
print(rstrip)