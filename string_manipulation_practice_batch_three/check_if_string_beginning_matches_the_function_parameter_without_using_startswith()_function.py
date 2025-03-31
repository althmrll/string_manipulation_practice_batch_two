#Ask user input sentence
sentence= input("Enter sentence:")

#Ask user to input parameter
parameter= input("Enter parameter:")

#Determine if sentence starts with parameter
if sentence.endswith(parameter)==False:
    print("sentence DOES NOT start with '", parameter, "'")

else:
    print("sentence DOES NOT start with '", parameter, "'") #print message