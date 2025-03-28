while True:

    sentence=input("Input sentence in improper case:")

#swapcase
    for letter in sentence:
        if letter.isupper()==True:
            lower_case= letter.lower()
            sentence= sentence.replace(letter, lower_case)

        elif letter.islower()==True:
            upper_case= letter.upper()
            sentence=sentence.replace(letter, upper_case)

    print(sentence)#print