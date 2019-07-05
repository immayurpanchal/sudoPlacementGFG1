#Solution 1 
for _ in range(int(input())):
    [arraySize, rotations] = list(map(int, input().split()))
    array = list(map(int, input().split()))
    ans = array[rotations::]+array[:rotations:]
    for val in ans:
        print(val, end=' ')
    print()