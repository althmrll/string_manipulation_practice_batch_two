swapcase=""
sentence=input("Input sentence in improper case:")

#swapcase
for character in sentence:
    if character.isupper()==True:
        swapcase+= character.lower()

    elif character.islower()==True:
        swapcase+= character.upper()

    else:
        swapcase+=character

print(swapcase)#print