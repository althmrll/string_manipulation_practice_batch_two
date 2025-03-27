#removeprefix() remove the characters at the beginning of the string that matches the function parameter. Create a program that do the same functionality without using removeprefix() function.

#ask to input
name=input("Enter sentence:")
parameter= input("Input prefix you want to remove:")

#remove prefix
name=name.replace(parameter,"")

#print function
print(name)