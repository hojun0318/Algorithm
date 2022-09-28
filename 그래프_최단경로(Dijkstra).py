import sys
sys.stdin = open("input.txt", "r")

INF = 50 * 10
def dijkstra(start):
    D = adjList[start][::]
    visited = [0] * N
    visited[start] = 1

    for _ in range(N - 1):       # N - 1개의 노드 처리
        # [1] 미방문 노드 중 최소거리 노드 번호 찾고, 방문 표시
        mn, i_min = INF, 0
        for i in range(0, N):
            if visited[i] == 0 and mn > D[i]:
                i_min, mn = i, D[i]
        visited[i_min] = 1       # 기준 노드 찾았고, 방문 표시

        # [2] 모든 노드 대상으로 최단거리 갱신
        for i in range(N):
            D[i] = min(D[i], D[i_min] + adjList[i_min][i])

    return D[N - 1]

T = int(input())
for test_case in range(1, T + 1):
    N, E = map(int, input().split())
    adjList = [[INF] * N for _ in range(N)]
    for _ in range(E):
        start, end, weight = map(int, input().split())
        adjList[start][end] = weight
    for i in range(N):
        adjList[i][i] = 0

    ans = dijkstra(0)

    print(f'#{test_case} {ans}')