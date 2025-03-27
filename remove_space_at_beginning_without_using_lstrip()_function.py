#Prog 1: lstrip() remove the space characters at the beginning of the string. Create a program that do the same functionality without using lstrip() function.

#Ask user to input their name
name= input("add big space and enter your name:")

#Remove space before name
no_space=name.replace(" ","")

#Print the formatted name
print(no_space)