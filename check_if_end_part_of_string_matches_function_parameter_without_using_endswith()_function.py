#Ask user to input sentence
sentence= input("Input sentence:")
#Ask user for parameter
parameter=input("Input parameter:")

#prints it
if sentence.startswith(parameter)==True: #determine if sentence ends with parameter without using endswith function
    print("The sentence DOES NOT end with '", parameter, "'")

else:
    print("The sentence DOES end with", parameter)