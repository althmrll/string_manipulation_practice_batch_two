title=""

#Ask user to input sentence
sentence=input("Input sentence:")

#Capitalize first letter of each word wihout using title
sentence=sentence.split()

for elements in sentence:
    title+=elements.capitalize()

title.join(" ")#adds space for each word

#print it
print (str(title))