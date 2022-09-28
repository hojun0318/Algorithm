import sys
sys.stdin = open("input.txt", "r")

def dfs(n):
    for j in range(1, V + 1):
        # 연결되어 있고, 방문하지 않은 경우
        if adjList[n][j] == 1 and visited[j] == 0:
            ans.append(j)
            visited[j] = 1
            dfs(j)

T = int(input())
for test_case in range(1, T + 1):
    # 정점, 간선
    V, E = map(int, input().split())
    adjList = [[0] * (V + 1) for _ in range(V + 1)]        # 정점이 1부터 시작하니 V + 1로
    for _ in range(E):
        start, end = map(int, input().split())
        adjList[start][end] = adjList[end][start] = 1
    visited = [0] * (V + 1)
    ans = []

    ans.append(1)
    visited[1] = 1
    dfs(1)

    print(f'#{test_case}', *ans)