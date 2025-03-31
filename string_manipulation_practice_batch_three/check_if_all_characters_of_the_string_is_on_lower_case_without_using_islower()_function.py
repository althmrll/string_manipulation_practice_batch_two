lower_count=0

#Ask user ot input sentence
sentence= input("Enter sentence:")
sentence_count= sentence.count()
#Determine if letter is in lowercase without using islower()
for letter in sentence:
    if letter.isupper()==False:
        lower_count+=1
    
    elif letter.isupper()==True:
        continue

    else: 
        lower_count+=1
        continue

#print
if lower_count==sentence.count():
    print("sentence IS in lowercase")
else:
    print("sentence IS NOT in lowercase")