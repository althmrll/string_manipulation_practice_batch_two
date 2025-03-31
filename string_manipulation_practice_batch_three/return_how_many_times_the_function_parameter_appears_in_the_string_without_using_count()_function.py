occurence_count=0

while True:
    sentence=input("Enter sentence:") #Ask user to input sentence
    if sentence=="":
        print("!!THERE IS NO SENTENCE TO BASE ON!!")
    
    else:
        while True:
            parameter=input("Enter parameter:") #Ask user to input parameter

#count occurence of parameter in sentence
            if parameter=="":
                print("!!A PARAMETER IS REQUIRED!!")
            else:
                if len(parameter)==1:
                    for letter in sentence:
                        if letter==parameter:
                            occurence_count+=1
                        else:
                            continue
                    print(occurence_count)
                    break

                elif len(parameter)>1:
                    word_list=sentence.split()
                    for item in word_list:
                        if item.find(parameter)==-1:
                            continue
                        else:
                            occurence_count+=1
                    print(occurence_count)
                    break
