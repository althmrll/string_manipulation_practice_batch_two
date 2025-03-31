upper_count=0
character_count=0

#Ask user ot input sentence
sentence= input("Enter sentence:")

#Determine if letter is in lowercase without using islower()
for letter in sentence:
    if letter.isupper()==True:
        upper_count+=1
        character_count+=1
    elif letter.isalpha()==True:
        character_count+=1
        continue
    else:
        continue

#print
if upper_count!=0:
    print("The sentence IS NOT lower")

elif character_count==0:
    print("The sentence IS NOT lower")

else:
    print("The sentence IS lower")