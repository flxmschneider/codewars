def high(string):
    offset = ord('a')-1
    highest_count = 0
    highest_word = ''
    words = string.split(' ')
    print(words)
    for word in words:
        count = sum([ord(a)-offset for a in word])
        print('word: ',word,' count: ',count)
        if count > highest_count:
            highest_count = count
            highest_word = word
    return highest_word
