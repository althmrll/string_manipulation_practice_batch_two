#Ask user to input sentence
sentence= input("Input sentence:")
#Ask user for parameter
parameter=input("Input parameter:")

endswith= sentence.find(parameter)

#prints it
if sentence.find(parameter)==-1: #determine if sentence ends with parameter without using endswith function
    print("False")
else:
    print("True")