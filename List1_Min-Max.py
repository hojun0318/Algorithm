import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))

    min_n = 1000000
    max_n = 1
    for i in range(N):
        if lst[i] < min_n:
            min_n = lst[i]
        if lst[i] > max_n:
            max_n = lst[i]

    print(f'#{test_case} {max_n - min_n}')