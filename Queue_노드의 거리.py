import sys
sys.stdin = open("input.txt", "r")


def bfs(S, G):
    visited = [0] * (V + 1)
    q = []

    # q에 시작노드번호, 시작점으로부터의 거리
    q.append((S, 0))
    visited[S] = 1

    while q:
        c, d = q.pop(0)  # 현재 노드번호(cur)
        if c == G:  # 목적지인 경우 거리(d) 리턴
            return d

        for e in adjL[c]:  # c와 연결된 노드 순서대로 체크
            if not visited[e]:
                q.append((e, d + 1))  # 현재노드까지의 거리 + 1
                visited[e] = 1

    # G가 연결된 노드가 아님
    return 0


# T = 10
T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    adjL = [[] for _ in range(V + 1)]
    for _ in range(E):
        s, e = map(int, input().split())
        adjL[s].append(e)
        adjL[e].append(s)
    S, G = map(int, input().split())

    ans = bfs(S, G)

    print(f'#{test_case} {ans}')