# import os

# cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in %r: %s" % (cwd, files))
def find_the_word(five_lett_words,correct_char,wrong_char,correct_pos,wrong_pos):
    words = list()
    for y in five_lett_words:
        # if(x[-1]!=n and x[-2]!=\):
        for character in y:
            if(character not in wrong_char and len(correct_char) != 0):
                if(character in correct_char):
                    if(correct_pos == -1):
                        for l in wrong_pos:
                            # print("wdaaaaaaaaaaa",l,correct_char[0],y[l-1])
                            if(y[l-1] != correct_char):
                                # print(y)
                                words.append(y)
                    else:
                        if(y[correct_pos - 1]== correct_char):
                            words.append(y)
            else:
                if(character not in wrong_char):
                    words.append(y)
    return words
    


with open ("data.txt", "r") as myfile:
    data=myfile.readlines()
five_letter_words = list()
# print(len(data))
# print(data[1][1])
for x in data:
    # if(x[-1]!=n and x[-2]!=\):
        
        if(len(x) == 6):
            five_letter_words.append(x)
# print(five_letter_words)
n = 1
correct_string  = ""
wrong_string = ""
wrong_postion_1 = [4]
wrong_postion_2 = [0]
wrong_postion_3 = [0]
wrong_postion_4 = [0]
wrong_postion_5 = [0]
correct_positon_1 = 2
correct_positon_2 = -1
correct_positon_3 = -1
correct_positon_4 = -1
correct_positon_5 = -1
removed_words = list()
while(n<6):
    correct_string_input = str(input("Enter the correct letters "))
    print(len(correct_string_input))
    wrong_string_input = str(input("Enter the wrong letters "))
    correct_string = correct_string_input
    wrong_string = wrong_string_input
    
    # removed_words  = find_the_word(five_letter_words,correct_char=correct_string,wrong_char=wrong_string,correct_pos=correct_positon_1,wrong_pos=wrong_postion_1)
    # print(removed_words)
    
    
    print(correct_string)
    print(wrong_string)
    first_letter_removed = list()
    for y in five_letter_words:
        # if(x[-1]!=n and x[-2]!=\):
        for character in y:
            if(character not in wrong_string and len(correct_string) != 0):
                if(character in correct_string):
                    if(correct_positon_1 == -1):
                        for l in wrong_postion_1:
                            print("wdaaaaaaaaaaa",l,correct_string[0],y[l-1])
                            if(y[l-1] != correct_string[0]):
                                first_letter_removed.append(y)
                                print(y)
                    else:
                        if(y[correct_positon_1 - 1]== correct_string[0]):
                                first letter_removed.append(y)
                                print(y)
            else:
                if(character not in wrong_string):
                    first_letter_removed.append(y)
                    print(y)
                    
    for y in first_letter_removed:
        # if(x[-1]!=n and x[-2]!=\):
        for character in y:
            if(character not in wrong_string and len(correct_string) != 0):
                if(character in correct_string):
                    if(correct_positon_1 == -1):
                        for l in wrong_postion_1:
                            print("wdaaaaaaaaaaa",l,correct_string[0],y[l-1])
                            if(y[l-1] != correct_string[0]):
                                first letter_removed.append(y)
                                print(y)
                    else:
                        if(y[correct_positon_1 - 1]== correct_string[0]):
                                first letter_removed.append(y)
                                print(y)
            else:
                if(character not in wrong_string):
                    first letter_removed.append(y)
                    print(y)
            # if ("c" not in y and "w" not in y and "'" not in y and "a" not in y and "u"  not in y and "d" not in y and "o"  not in y and "i" in y and y[1]== "i" and "r" not in y and y[3]== "h" and y[2]== "g" and y[4]== "t"):
                # print(y) 
        # for character in y:
        #     if "i" in y and y[3]!= "i":
        #         print(y)   
            
            # if(y[1] == "r" and y[2] == "u" and y[3] == "n"):
                
            #     print(y)
    n = n + 1