#Ask user input sentence
sentence= input("Enter sentence:")

#Ask user to input parameter
parameter= input("Enter parameter:")

reversed_sentence=sentence[::-1]
reversed_parameter= parameter[::-1]

#Determine if sentence starts with parameter
if reversed_sentence.endswith(reversed_sentence)==True:
    print("sentence DOES NOT start with '", parameter, "'")

else:
    print("sentence DOES NOT start with '", parameter, "'") #print message