import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    lst = sorted(lst)
    mx = 0
    ans = 0

    for i in range(N - K, N):
        ans += lst[i]
        if mx < ans:
            mx = ans

    print(f'#{test_case} {mx}')