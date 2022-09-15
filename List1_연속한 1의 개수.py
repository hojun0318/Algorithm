import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input())) + [0]
    max_V = 0
    cnt = 0

    for i in range(len(lst)):
        if lst[i] == 1:
            cnt += 1
        else:
            if max_V < cnt:
                max_V = cnt
            cnt = 0

    print(f'#{test_case} {max_V}')