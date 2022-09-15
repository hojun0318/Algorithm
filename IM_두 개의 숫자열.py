import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    mx = 0

    if N < M:
        short = list(map(int, input().split()))
        long = list(map(int, input().split()))
    else:
        long = list(map(int, input().split()))
        short = list(map(int, input().split()))

    for i in range(len(long) - len(short) + 1):
        ans = 0
        for j in range(len(short)):
            ans += long[i + j] * short[j]

        if mx < ans:
            mx = ans

    print(f'#{test_case} {mx}')