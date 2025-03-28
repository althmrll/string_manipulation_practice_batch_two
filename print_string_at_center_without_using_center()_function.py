#Ask user to input sentence
sentence=input("Input sentence:")

#Ask user to input parameter
parameter=input("Input parameter:")

#Ask user to input separator
separator=input("Input separator(optional, space will be added if none is typed in):")
if separator=="":
    separator=" "
else:
    continue

#center based on parameter inputted by user
left=parameter//2
left_separator=separator*left
left_and_sentence=left_separator+sentence
right=parameter-len(left_and_sentence)
right_separator=separator*right
center=left_and_sentence+separator*right

#print it
print(center)