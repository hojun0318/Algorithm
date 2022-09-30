import sys
sys.stdin = open("input.txt", "r")

INF = 100 * 100 * 10

def bfs(si, sj):
    q = []
    v = [[INF] * N for _ in range(N)]

    q.append((si, sj))
    v[si][sj] = 0

    while q:
        ci, cj = q.pop(0)
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            # 범위내 v[ni][nj]>v[ci][cj]+arr[ni][nj
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] > v[ci][cj] + arr[ni][nj]:
                v[ni][nj] = v[ci][cj] + arr[ni][nj]
                q.append((ni, nj))

    return v[N - 1][N - 1]


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    ans = bfs(0, 0)
    print(f'#{test_case} {ans}')