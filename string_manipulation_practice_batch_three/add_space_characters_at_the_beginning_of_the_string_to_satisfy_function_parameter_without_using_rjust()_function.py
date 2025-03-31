#Ask user to input sentence
sentence= input("Enter sentence:")
#Ask user ot input parameter
while True:
    parameter= int(input("Enter parameter:"))
    try:
        fill=input("Input symbol/letter you want to fill the space with (Optional):") #Ask user for fill(optional)
        if fill=="":
            fill=" "
        else:
            break
        
    except:
        ("!!INVALID INPUT. SHOULD BE A NUMBER!!")

character_count=len(sentence) #Determine number of characters of sentence
num_of_filler=parameter-character_count#Subtract number of characters of sentence to parameter
filler=num_of_filler*fill#Multipy space to the difference of character and parameter
rjust=sentence+filler#Add sentence and space

if fill==" ":
    print("'",rjust,"'")#Print the output
else:
    print(rjust)


