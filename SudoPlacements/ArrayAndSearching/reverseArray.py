for _ in range(int(input())):
    size = int(input())
    array = list(map(int, input().split()))
    index = len(array) - 1
    while index>=0:
        print(array[index],end=' ')
        index-=1
    print()