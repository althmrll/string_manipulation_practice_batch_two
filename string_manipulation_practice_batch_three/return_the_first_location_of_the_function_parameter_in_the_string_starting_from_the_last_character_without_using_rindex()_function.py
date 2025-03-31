#Ask user to input sentence
sentence=input("Enter sentence:")

#Ask user to input parameter
while True:
    try:
        parameter=int(input("Enter parameter:"))
        break
    except:
        print("!!INVALID INPUT. SHOULD BE NUMBER!!")

#Determine first occurence of parametre starting from the last
reversed_sentence=sentence[::-1]
reversed_parameter=parameter[::-1]
index=reversed_sentence.index(parameter)
rindex=parameter-index


#print index
print(rindex)