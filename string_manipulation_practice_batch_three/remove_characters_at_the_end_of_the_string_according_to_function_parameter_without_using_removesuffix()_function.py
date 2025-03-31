#Ask user to input sentence
sentence= input("Input sentence:")

#Ask user for parameter
parameter=input("Input parameter:")

if sentence.endswith(parameter)==True:
    remove_suffix=sentence.replace(parameter,"")

else:
    print("The parameter you entered is not a suffix.")

#print sentence with no suffix
print(remove_suffix)