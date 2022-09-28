import sys
sys.stdin = open("input.txt", "r")

def bfs(start):
    queue = []
    visited = [0] * (V + 1)

    queue.append(start)
    visited[start] = 1
    ans.append(start)

    while queue:
        current = queue.pop(0)
        for end in adjList[current]:
            if not visited[end]:
                queue.append(end)
                visited[end] = 1
                ans.append(end)

T = int(input())
for test_case in range(1, T + 1):
    # 정점, 간선
    V, E = map(int, input().split())
    adjList = [[] for _ in range(V + 1)]        # 정점이 1부터 시작하니 V + 1로

    # 양방향 연결
    for _ in range(E):
        start, end = map(int, input().split())
        adjList[start].append(end)
        adjList[end].append(start)

    # 낮은 번호 -> 높은 번호 방문: 필요시 정렬
    for i in range(1, V + 1):
        adjList[i].sort()

        ans = []
        bfs(1)

    print(f'#{test_case}', *ans)
