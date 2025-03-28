#Ask user to input sentence
sentence=input("Input sentence:")

#Ask user to input parameter
while True:
    try:
        parameter=int(input("Input parameter:"))
        break
        continue
    except:
        print("!!PARAMETER SHOULD BE A NUMBER!!")


#Ask user to input separator
separator=input("Input separator(optional, space will be added if none is typed in):")
if separator=="":
    separator=" "

if parameter<=5:
    while len(sentence)!=parameter:
        sentence= separator+sentence
        if len(sentence)!=parameter:
            sentence+= separator

elif parameter>=6:
    while len(sentence)!=parameter:
        sentence+= separator
        if len(sentence)!=parameter:
            sentence= separator+sentence
            
if separator==" ":
    print("'"+sentence+"'")
else:
    print(sentence)