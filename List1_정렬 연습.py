import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))

    for i in range(N - 1):
        i_min = i
        for j in range(i + 1, N):
            if lst[i_min] > lst[j]:
                i_min = j
        lst[i], lst[i_min] = lst[i_min], lst[i]

    print(f'{test_case}', *lst)