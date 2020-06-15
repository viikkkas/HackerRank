from collections import OrderedDict
dic = OrderedDict()
n = int(input())
for i in range(n):
    word = input()
    dic[word] = dic.get(word, 0) + 1


print(len(dic))
for i in dic:
    print(dic[i],end=" ")
