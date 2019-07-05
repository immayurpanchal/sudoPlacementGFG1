# testCases = int(input())
# while testCases:
#     n = int(input())
#     values = [int(x) for x in input().split()]
#     i = 0 
#     while i != n-1:
#         if values[i] > values[i+1]:
#             print(values[i+1], end=' ')
#         else:
#             print('-1', end=' ')
#         i = i +1 
#     print('-1')
#     testCases = testCases - 1

#Better Solution
t = int(input())
while t>0:
    t-=1
    n=int(input())
    l=list(map(int,input().split()))
    for i in range(n-1):
        if l[i]>l[i+1]:
            print(l[i+1],end=" ")
        if(l[i]<=l[i+1]):
            print(-1,end=" ")
    print(-1)