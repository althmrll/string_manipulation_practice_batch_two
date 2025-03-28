#Ask user to input sentence
sentence= input("Input sentence:")

#Ask user for parameter
parameter=input("Input parameter:")

endswith= sentence[::-1]
reversed_parameter=parameter[::-1]

if endswith.startswith(reversed_parameter):
    print("The sentence DOES end with '", parameter, "'")

else:
    print("The sentence DOES NOT end with '", parameter, "'")
