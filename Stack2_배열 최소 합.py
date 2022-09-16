import sys
sys.stdin = open("input.txt", "r")

def dfs(n, sm):
    global ans
    if ans <= sm:   # 현재 합이 이미 ans보다 큰 경우: 정답 갱신 가능성 없음
        return
    # 종료 조건
    if n == N:
        if ans > sm:
            ans = sm
        return
    # 열만큼 방문하기
    for j in range(N):
        if not visited[j]:
            visited[j] = 1
            dfs(n + 1, sm + arr[n][j])
            visited[j] = 0


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    ans = 10 * N
    dfs(0, 0)       # n == 0 (0행). sum = 0

    print(f'#{test_case} {ans}')