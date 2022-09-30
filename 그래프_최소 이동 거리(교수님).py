import sys
sys.stdin = open("input.txt", "r")

INF = 10 * 1000

def bfs(s):
    q = []
    v = [INF] * (N + 1)

    q.append(s)
    v[s] = 0

    while q:
        c = q.pop(0)
        for (e, w) in adjL[c]:  # 현재위치에서 이동가능한 (목적지,가중치)
            if v[e] > v[c] + w:  # 목적지의 현재비용 > 지금위치비용 + 현재->목적지 이동비용
                v[e] = v[c] + w
                q.append(e)

    return v[N]


T = int(input())
for test_case in range(1, T + 1):
    N, E = map(int, input().split())
    adjL = [[] for _ in range(N + 1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        adjL[s].append((e, w))
    ans = bfs(0)
    print(f'#{test_case} {ans}')