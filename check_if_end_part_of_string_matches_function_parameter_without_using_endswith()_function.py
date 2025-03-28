#Ask user to input sentence
sentence= input("Input sentence:")

#Ask user for parameter
parameter=input("Input parameter:")

endswith= sentence[::-1] #reverses sentence
reversed_parameter=parameter[::-1] #reverses parameter

if endswith.startswith(reversed_parameter): #determines whether the start reverse of the sentence and parameter are equal
    print("The sentence DOES end with '", parameter, "'")

else:
    print("The sentence DOES NOT end with '", parameter, "'")
