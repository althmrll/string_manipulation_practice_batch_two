#Ask user to input in impproper case
sentence=input("Input sentence in improper case:")
swapcase=""

#swapcase
for letter in sentence:
    if letter.islower()==True:
        swapcase+= letter.upper()

    elif letter.isupper()==True:
        swapcase+= letter.lower()
    
    print(swapcase)#print