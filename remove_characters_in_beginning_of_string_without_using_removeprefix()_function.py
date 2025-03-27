#removeprefix() remove the characters at the beginning of the string that matches the function parameter. Create a program that do the same functionality without using removeprefix() function.

#ask to input
name=input("Enter sentence:")
parameter= input("input parameter:")
#remove prefix
name=name.split()

while True:
    try:
        if parameter == name[0]:
            no_suffix=name.remove(parameter)
            print(no_suffix)
            break
    except:
        print("!!THE PARAMETER YOU INPUTTED IS NOT A PREFIX!!")