capitalize=""

#Ask user to input sentence
sentence=input("Input sentence:")

#Capitalize first letter of each word wihout using title
capitalize+=sentence[0].upper()
capitalize+=sentence[1:].lower()

#print it
print(capitalize)