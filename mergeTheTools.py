def remove_dup(word):
    new_word = ''
    for i in word:
        if i in new_word:
            continue
        else:
            new_word +=i
    return new_word


def merge_the_tools(string, k):
    length = len(string)
    divi = int(k)
    list1 = []
    for i in range(0, length, divi):
        temp = string[i:i + divi]
        list1.append(temp)

    for word in list1:
        temp = remove_dup(word)
        print(temp)
        
if __name__ == '__main__':
    string, k = raw_input(), int(raw_input())
    merge_the_tools(string, k)
