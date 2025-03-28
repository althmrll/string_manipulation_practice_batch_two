Capitalize=""

#Ask user to input sentence
sentence=input("Input sentence:")

#Capitalize first letter of each word wihout using title
sentence=sentence.split()

for elements in sentence:
    title+=elements.capitalize()+" "

#print it
print (title.strip())