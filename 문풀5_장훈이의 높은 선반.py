import sys
sys.stdin = open("input.txt", "r")

def dfs(n, sm):
    global ans

    if ans + B <= sm:
        return

    if n == N:
        if sm >= B and ans > sm - B:
            ans = sm - B
        return

    dfs(n + 1, sm + S[n])
    dfs(n + 1, sm)

T = int(input())
for test_case in range(1, T + 1):
    N, B = map(int, input().split())    # 점원의 수, 선반의 높이
    S = list(map(int, input().split()))

    ans = 10000 * N
    dfs(0, 0)    # n, sm

    print(f'#{test_case} {ans}')