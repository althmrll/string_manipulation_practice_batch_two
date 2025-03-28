swapcase=""
sentence=input("Input sentence in improper case:")

#swapcase
for letter in sentence:
    if letter.isupper()==True:
        swapcase+= letter.lower()

    elif letter.islower()==True:
        swapcase+= letter.upper()

print(swapcase)#print