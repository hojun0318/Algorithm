import sys
sys.stdin = open("input.txt", "r")

def BinarySearch(lst, E, Key):
    start = 0
    end = E - 1
    ans = 0
    while start <= end:
        middle = int((start + end) // 2)
        if lst[middle] == Key:
            return middle + 1
        elif lst[middle] > Key:
            end = middle - 1
        else:
            start = middle + 1
    return ans

T = int(input())
for test_case in range(1, T + 1):
    N, D = map(int, input().split())
    lst = list(map(int, input().split()))

    result = BinarySearch(lst, N, D)

    print(f'#{test_case} {result}')