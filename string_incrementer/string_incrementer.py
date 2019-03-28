import re

def increment_string(string):
    number = ''
    numbers = re.findall(r'\d+', string)
    try:
        number += str(numbers[-1])
    except:
        
        return string +'1'
    else:
        sub_string = string[0:-len(number)]
        len_number = len(number)
        number = int(number)+ 1
        string_number = str(number)
        number = '0'*(len_number-len(string_number))+string_number 
        sub_string += number
        string = sub_string
    return string
