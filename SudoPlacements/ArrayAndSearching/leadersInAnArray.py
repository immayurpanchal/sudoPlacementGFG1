for _ in range(int(input())):
    size = int(input())
    array = list(map(int, input().split()))

    newArr = []
    maxVal = array[len(array)-1]
    i = len(array)-1
    while i >= 0:
        if array[i] >= maxVal:
            newArr.append(array[i])
            maxVal = array[i]
        i-=1
    newArr = newArr[::-1]
    [print(value, end=' ') for value in newArr]
    print()

#Solution 2
t=int(input())
for _ in range(t):
    n=int(input())
    ar=list(map(int,input().split()))
    maxx=ar[n-1]
    ans=[]
    for i in range(n-1,-1,-1):
        if maxx<=ar[i]:
            maxx=ar[i]
            ans.append(maxx)
    print(*ans[::-1])
            
        
