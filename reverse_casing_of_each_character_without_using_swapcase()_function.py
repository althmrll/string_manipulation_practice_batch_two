#Ask user to input in impproper case
sentence=input("Input sentence in improper case:")

#swapcase
for letter in sentence:
    if letter.islower()==True:
        sentence+= letter.upper()

    elif letter.isupper()==True:
        sentence+= letter.lower()

#print
print(sentence)