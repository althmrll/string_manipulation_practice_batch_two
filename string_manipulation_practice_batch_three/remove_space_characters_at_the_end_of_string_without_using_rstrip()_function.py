#Ask user to input sentence
sentence= input("Input sentence and add big spaace after:")

#strip space at the end without using rstrip
reversed_sentence=sentence[::-1]#reverse sentence
strip=reversed_sentence.lstrip()    #lstrip sentence
rstrip=strip[::-1]#reverse sentence again

#print output
print(rstrip)