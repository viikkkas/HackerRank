n,m = (int(i) for i in input().split())
arr = map(int, input().strip().split(' '))
A = set(map(int, input().strip().split(' ')))
B = set(map(int, input().strip().split(' ')))
happiness = 0
for i in arr:
    if i in A:
        happiness = happiness + 1
    elif i in B:
        happiness = happiness - 1

print(happiness)
