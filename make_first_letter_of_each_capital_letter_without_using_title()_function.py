title=""

#Ask user to input sentence
sentence=input("Input sentence:")

#Capitalize first letter of each word wihout using title
sentence=sentence.split()

for elements in sentence:
    title+=elements.capitalize()
    
    if elements.isspace()==True:
        title+=elements

#print it
print (str(title))