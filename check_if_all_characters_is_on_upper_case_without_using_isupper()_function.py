lower=0

#Ask user to input sentence
sentence=input("Input sentence:")

#Check if characters are upper case without using upper
for letter in sentence: #Ensures that every letter is in upper case
    if letter.islower()==False:
        continue
    else:
        lower+=1

if lower==0:
    print("Sentence is in upper case.")
else:
    print("Sentence is NOT in upper case.")