import sys
sys.stdin = open("input.txt", "r")

def dfs(n, ci, cj, num):
    if n == 7:
        sset.add(num)       # 중복제거
        return

    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ni, nj = ci + di, cj + dj
        if 0 <= ni < N and 0 <= nj < N:
            dfs(n + 1, ni, nj, num * 10 + arr[ni][nj])

T = int(input())
for test_case in range(1, T + 1):
    N = 4
    arr = [list(map(int, input().split())) for _ in range(N)]

    sset = set()
    for si in range(N):
        for sj in range(N):
            dfs(1, si, sj, arr[si][sj])

    print(f'#{test_case} {len(sset)}')
