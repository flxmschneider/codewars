def duplicate_encode(word):
    letter_dic = dict()
    keys = letter_dic.keys()
    for letter in word:
        if letter in keys:
            letter_dic[letter]+=1
        else:
            letter_dic[letter]=1
    result = ''
    for el in word:
        print(el, letter_dic)
        if letter_dic[el] > 1:
            result += ')'
        else:
            result += '('
    return result 
