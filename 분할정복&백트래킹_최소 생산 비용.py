import sys
sys.stdin = open("input.txt", "r")

def dfs(n, sm):
    global ans
    if ans <= sm:
        return

    if n == N:
        ans = min(ans, sm)
        return

    for j in range(N):
        if visited[j] == 0:
            visited[j] = 1
            dfs(n + 1, sm + arr[n][j])
            visited[j] = 0

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    ans = 100 * N

    dfs(0, 0)

    print(f'#{test_case} {ans}')