import sys
sys.stdin = open("input.txt", "r")

def dfs(v, N):
    top = -1
    #print(v)
    lst.append(v)
    visited[v] = 1  # 시작점 방문 표시

    while True:
        for w in adjList[v]:  # if (v의 인접 정점 중 방문 안 한 정점 w가 있으면)
            if visited[w] == 0:
                top += 1  # push(v)
                stack[top] = v
                v = w  # v <- w (w에 방문)
                #print(v)  # 방문해서 할 일
                lst.append(v)
                visited[w] = 1  # visited[w] <- True (w에 방문 했다는 표시 남기기)
                break
        else:  # w가 없으면
            if top != -1:  # 1. stack이 비어있지 않은 경우
                v = stack[top]
                top -= 1   # 이 2개의 행이 pop()에 해당
            else:          # 2. stack이 비어있는 경우
                break      # while문 빠져나오게 만듬

T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    N = V + 1
    adjList = [[] for _ in range(N)]
    for _ in range(E):
        a, b = map(int, input().split())
        adjList[a].append(b)
    S, G = map(int, input().split())
    visited = [0] * N  # visited 생성,   N : 정점의 개수
    stack = [0] * N  # stack 생성,
    lst = []
    ans = 0
    dfs(S, G)
    if G in lst:
        ans = 1

    print(f'#{test_case} {ans}')