#Ask user to input in impproper case
sentence=input("Input sentence in improper case:")

#swapcase
if sentence.lower([]):
    sentence= sentence.upper([])

else:
    sentence=sentence.lower([])

#print
print(sentence)