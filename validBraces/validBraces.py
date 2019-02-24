import re

def validBraces(string):
    '''Checks if the string contains a valid bracket combination
    
    args: string(str): string which contains different bracket types
    return: bool: if this syntax combination is valid or not
    '''
    circle_left = [m.start() for m in re.finditer('\(', string)]
    circle_right = [m.start() for m in re.finditer('\)', string)]
    bracket_left = [m.start() for m in re.finditer('\[', string)]
    bracket_right = [m.start() for m in re.finditer('\]', string)]
    curly_left = [m.start() for m in re.finditer('{', string)]
    curly_right = [m.start() for m in re.finditer('}', string)]
    
    return ((circle_left < circle_right and len(circle_left) == len(circle_right)) or (circle_left==[] and circle_left==[])) \
            and ((bracket_left < bracket_right and len(bracket_left) == len(bracket_right)) or(bracket_left == [] and bracket_right==[]))\
            and ((curly_left < curly_right and len(curly_left) == len(curly_right)) or(curly_left==[] and curly_right==[]))
