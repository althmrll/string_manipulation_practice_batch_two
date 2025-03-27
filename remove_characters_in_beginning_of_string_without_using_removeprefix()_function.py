#removeprefix() remove the characters at the beginning of the string that matches the function parameter. Create a program that do the same functionality without using removeprefix() function.

name=input("Enter sentence:")#ask to input

while True:
        parameter=input("input parameter:")

#remove prefix
        if name.startswith(parameter)==True:
            no_suffix=name.replace(parameter,"")
            print(no_suffix)
            break
        else:
            print("!!THE PARAMETER YOU INPUTTED IS NOT A PREFIX!!")