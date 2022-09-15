import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))
    n = len(arr)
    ans = 0

    for i in range(1, 1<<n):
        sm = 0
        for j in range(n):
            if i & (1<<j):
                sm += arr[j]
        if sm == 0:
            ans = 1
            break

    print(f'#{test_case} {ans}')
