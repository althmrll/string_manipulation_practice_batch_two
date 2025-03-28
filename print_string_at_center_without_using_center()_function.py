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

#center based on parameter inputted by user
middle=parameter-len(sentence)
left=middle//2
left_separator=separator*left
left_and_sentence=left_separator+sentence
right=parameter-len(left_and_sentence)
right_separator=separator*right
center=left_and_sentence+separator*right

#print it
print(center)