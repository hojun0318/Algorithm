import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    lst.append(N)                       
    i = ans = start = last = 0

    while i < M + 1:
        if lst[i] - start <= K:
            last = lst[i]
            i += 1
        else:
            if lst[i] - last > K:
                ans = 0
                break
            else:
                start = last
                ans += 1

    print(f'#{test_case} {ans}')