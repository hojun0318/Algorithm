import sys
sys.stdin = open("input.txt", "r")

def dfs(n, sm, s):
    global ans
    # 가지치기
    if ans <= sm:
        return

    if n == N - 1:
        # 여태까지의 배터리량 + 1번으로 돌아가기 위한 필요량
        ans = min(ans, sm + arr[s][1])
        return

    for j in range(2, N + 1):
        if not visited[j]:
            visited[j] = 1
            dfs(n + 1, sm + arr[s][j], j)
            visited[j] = 0

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

    visited = [0] * (N + 1)
    ans = 100 * N
    visited[1] = 1 # 1번에서 시작하니, 1번은 방문
    # 방문한 도시 수: 0, 배터리량: 0, 시작구역 번호: 1
    dfs(0, 0, 1)

    print(f'#{test_case} {ans}')