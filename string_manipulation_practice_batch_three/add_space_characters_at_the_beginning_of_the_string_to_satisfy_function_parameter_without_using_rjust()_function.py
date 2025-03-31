#Ask user to input sentence
sentence= input("Enter sentence:")

#Ask user ot input parameter
while True:
    try:
        parameter= int(input("Enter parameter:"))
        break

    except:
        print("!!INVALID INPUT. SHOULD BE A NUMBER!!")

fill=input("Input symbol/letter you want to fill the space with (Optional):") #Ask user for fill(optional)
if fill=="":
    fill=" "

character_count=len(sentence) #Determine number of characters of sentence
num_of_filler=parameter-character_count#Subtract number of characters of sentence to parameter
filler=num_of_filler*fill#Multipy space to the difference of character and parameter
rjust=filler+sentence#Add sentence and filler

print(rjust)#Print the output