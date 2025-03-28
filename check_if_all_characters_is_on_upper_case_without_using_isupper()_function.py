#Ask user to input sentence
sentence=input("Input sentence:")

#Check if characters are upper case without using upper
if sentence.islower()==True:
    print("The sentence is NOT in upper case") #prints if sentence are NOT in upper case

else:
    print("The sentence is in upper case") #prints if sentence are in upper case