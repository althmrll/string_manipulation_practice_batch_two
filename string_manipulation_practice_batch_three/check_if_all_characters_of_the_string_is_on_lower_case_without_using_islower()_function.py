lower_count=0

#Ask user ot input sentence
sentence= input("Enter sentence:")
sentence_count= sentence.count()
#Determine if letter is in lowercase without using islower()
for letter in sentence:
    if letter.isupper()==True:
        lower_count+=1
    else: 
        continue

#print