lower_case=""
sentence=input("Input sentence in improper case:")

#turn upper cases into lower cases
for letter in sentence:
    if letter.isupper()==True:
        lower_case+= letter.swapcase()

    elif letter.islower()==True:
        lower_case+= letter
    
    elif letter.isspace()==True:
        lower_case+= letter

print(lower_case)#print