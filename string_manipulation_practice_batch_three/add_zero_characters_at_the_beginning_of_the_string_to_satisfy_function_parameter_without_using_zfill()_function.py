#Ask user to input number
number=input("Enter number:")
#Ask user to input parameter
while True:
    try:
        parameter=int(input("Enter parameter:"))
        break
    except:
        print("!!INVALID INPUT. SHOULD BE A NUMBER!!")

#use rjust to satisfy parameter
print(number.rjust(parameter,"0"))#print out output
