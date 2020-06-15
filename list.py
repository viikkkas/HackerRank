n = int(input())
list1 = []
for i in range(n):
    comm = input()
    comm = comm.split(' ')
    if comm[0] == 'insert':
        list1.insert(int(comm[1]),int(comm[2]))
    elif comm[0] == 'remove':
        list1.remove(int(comm[1]))
    elif comm[0] == 'append':
        list1.append(int(comm[1]))
    elif comm[0] == 'pop':
        list1.pop()
    elif comm[0] == 'reverse':
        list1.reverse()
    elif comm[0] == 'sort':
        list1.sort()
    elif comm[0] == 'print':
        print(list1)


        
