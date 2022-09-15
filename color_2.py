import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    C = int(input())
    N = 10
    arr = [[0] * N for _ in range(N)]
    ans = 0

    for _ in range(C):
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                arr[i][j] += color

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 3:
                ans += 1

    print(f'#{test_case} {ans}')