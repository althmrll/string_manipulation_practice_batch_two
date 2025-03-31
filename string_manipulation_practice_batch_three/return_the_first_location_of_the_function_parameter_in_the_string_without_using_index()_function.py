#Ask user to input sentence
sentence=input("Enter sentence:")

#Ask user to input parameter
while True:
    try:
        parameter=input("Enter parameter:")
        break
    except:
        print("!!INVALID INPUT. SHOULD BE NUMBER!!")

print(sentence.find(parameter))