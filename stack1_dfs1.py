# A ~ G -> 0 ~ 6
adjList = [[1, 2],          # 0
           [0, 3, 4],       # 1
           [0, 4],          # 2
           [1, 5],          # 3
           [1, 2, 5],       # 4
           [3, 4, 6],       # 5
           [5]]             # 6

def dfs(v, N):     # visited 생성, stack 생성
    visited = [0] * N                # N : 정점의 개수는 7개라는 걸 알고 주는 걸로
    stack = [0] * N                  # stack에 정점이 한 번씩만 들어갔죠, append해도, append하면 간단하게 구현 가능
    top = -1
    print(v)                         # 방문한 정점들 출력해봐
    visited[v] = 1                   # 시작점 방문 표시

    while True:
        for w in adjList[v]:         # if (v의 인접 정점 중 방문 안 한 정점 w가 있으면)
            if visited[w] == 0:
                top += 1             # push(v)
                stack[top] = v
                v = w                # v <- w (w에 방문)
                print(v)             # 방문해서 할 일
                visited[w] = 1       # visited[w] <- True (w에 방문 했다는 표시 남기기)
                break
        else:                        # w가 없으면
            if top != -1:            # 1. stack이 비어있지 않은 경우
                v = stack[top]
                top -= 1             # 이 2개의 행이 pop()에 해당
            else:                    # 2. stack이 비어있는 경우
                break                # while 빠져나오게 만듬

dfs(0, 7)