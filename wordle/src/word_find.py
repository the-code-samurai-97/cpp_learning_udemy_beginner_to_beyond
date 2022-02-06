from operator import length_hint

from numpy import int16, unsignedinteger


with open ("data.txt", "r") as myfile:
    data=myfile.readlines()
five_letter_words = list()

for x in data:
        if(len(x) == 6):
            five_letter_words.append(x)
number_of_tries = 1 # max 6
correct_string_position = list()
correct_string_position = [-1,-1,-1,-1,-1]
wrong_position_for_correct_letter = list()
wrong_position_for_correct_letter = [[0],[0],[0],[0],[0]]
correct_string = ""
removed_wrong_positon_letters = list()
print(wrong_position_for_correct_letter[0][0])
while(True):
    correct_string_input = input("Enter the Correct Letters ")
    correct_string = correct_string + correct_string_input
    print(len(correct_string))
    
    wrong_string = input("Enter the wrong letters ")
    
    n = 0
    for character in correct_string:
        if(correct_string_position[n] == -1):
            print("Position for ", character , " in the word")
            correct_string_position[n] = int(input("Enter the correct position, -1 for not available "))
        n = n + 1
    m = 0
    for character in correct_string:
        if(wrong_position_for_correct_letter[m][0] == 0):
            print("Wrong Position for ", character , " in the word")
            x = int(input("wrong postion for this letter default -1"))
            wrong_position_for_correct_letter[m].append(x)
        m = m + 1
    print(wrong_position_for_correct_letter)
    ### remove the unwanted words
    removed_wrong_letters = list()
    correct_words_found_from_input = list()
    
    for y in five_letter_words:
        for alphabet in wrong_string:
            if(alphabet not in y and "'" not in y):
                removed_wrong_letters.append(y)
    ### find the words which have the correct letters 
    for character in removed_wrong_letters:
        if(correct_string[0] in character and correct_string[1] in character):
            correct_words_found_from_input.append(character)
    # print(correct_words_found_from_input)
    for y in correct_words_found_from_input:
        if(y[4] == "t" and y[3] != "o" and y[4] != "o" and y[3] != "o" and y[1] != "i" and y[3] != "i" and y[1] == "o" and y[2] == "i" and y[3]=="s" and y[4]=="t"):
            print(y)
        # if(y.find(correct_string[0]) != wrong_position_for_correct_letter[0][1] and y.find(correct_string[1]) != wrong_position_for_correct_letter[1][1]):
        #     removed_wrong_positon_letters.append(y)
    # print(removed_wrong_positon_letters)
    five_letter_words = removed_wrong_positon_letters
    # for y in correct_words_found_from_input:
        
                                        