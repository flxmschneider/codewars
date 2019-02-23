def validBraces(string):
    return string.count('(') == string.count(')') and string.count('[') == string.count(']') and string.count('{') == string.count('}')
