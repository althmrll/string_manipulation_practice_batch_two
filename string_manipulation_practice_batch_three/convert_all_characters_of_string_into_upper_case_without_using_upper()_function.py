upper=""

#Ask user to input sentence
sentence= input("Input sentence:")

#format sentence to uppercase
for letter in sentence:
    if letter.islower():
        upper+=letter.swapcase()
        
    else:
        upper+=letter

#print formatted sentence
print(upper)