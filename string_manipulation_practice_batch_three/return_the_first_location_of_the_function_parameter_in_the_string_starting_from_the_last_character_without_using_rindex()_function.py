#Ask user to input sentence
sentence=input("Enter sentence:")

#Ask user to input parameter
parameter=input("Enter parameter:")

#Determine first occurence of parametre starting from the last
reversed_sentence=sentence[::-1]
reversed_parameter=parameter[::-1]
rindex=reversed_sentence.index(parameter)

#print index
print(rindex)