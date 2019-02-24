def first_non_repeating_letter(string):
    counter_dict = {}
    for letter in string:
        if letter in counter_dict.keys():
            counter_dict[letter] +=1
        else:
            counter_dict[letter] = 1

    
