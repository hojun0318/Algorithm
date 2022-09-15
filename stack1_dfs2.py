import sys
sys.stdin = open("input.txt", "r")

def dfs(v):
    print(v)                    # 방문
    visited[v] = 1
    for w in adjList[v]:
        if visited[w] == 0:     # 방문하지 않은 곳이면
            dfs(w)

V, E = map(int, input().split())
N = V + 1
adjList = [[] for _ in range(N)]
for _ in range(E):
    a, b = map(int, input().split())
    adjList[a].append(b)
    adjList[b].append(a)

visited = [0] * N                # visited 생성,   N : 정점의 개수는 7개라는 걸 알고 주는 걸로
dfs(0)