import sys
sys.stdin = open("input.txt", "r")

def dfs(n, sm):
    global ans
    if ans < sm:
        return

    if n == N:
        if ans > sm:
            ans = sm
        return

    for j in range(N):
        if not visited[j]:
            visited[j] = 1
            dfs(n + 1, sm + arr[n][j])
            visited[j] = 0  # 반드시 해제!!


T = int(input())
# T = 10
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 10 * N  # 최소값
    visited = [0] * (N)
    dfs(0, 0)

    print(f'#{test_case} {ans}')