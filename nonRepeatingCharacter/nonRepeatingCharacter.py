from collections import OrderedDict

def first_non_repeating_letter(string):
    counter_dict = OrderedDict()
    for letter in string:
        if letter in counter_dict.keys():
            counter_dict[letter] +=1
        else:
            counter_dict[letter] = 1
    
    for key, value in counter_dict.items():
        if value == 1:
            return key
    return ''
