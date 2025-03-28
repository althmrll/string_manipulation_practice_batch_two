#Ask user to input in impproper case
sentence=input("Input sentence in improper case:")

#swapcase
if sentence.islower(sentence.index())==True:
    sentence= sentence.upper(sentence.index())

elif sentence.upper(sentence.index())==True:
    sentence= sentence.lower(sentence.index())


#print
print(sentence)