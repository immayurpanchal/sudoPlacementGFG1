testCases = int(input())
#Solution 1
while testCases:
    n = int(input())
    array = list(map(int, input().split()))
    noOfRotation = int(input())
    i = noOfRotation
    while i < len(array):
        print(array[i], end=' ')
        i+=1
    for x in range(noOfRotation):
        print(array[x], end=' ')
    print('')
    testCases-=1

#Solution 2
for i in range(testCases):
    n=int(input())
    a=list(map(int,input().split()))
    d=int(input())
    l=[]
    for k in range(d,len(a)):
        l.append(a[k])
    for k in range(d):
        l.append(a[k])
    for i in l:
        print(i,end=' ')
    print('')

#Solution 3
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    rot = int(input())
    j = a[rot::]+a[:rot:]
    for i in j:
        print(i,end=" ")
    print()
    