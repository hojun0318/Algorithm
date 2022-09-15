import sys
sys.stdin = open("input.txt", "r")


def bfs(s):
    # [1] q, visited, 필요한 flag 초기화
    q = []                                                              # 빈 q 생성
    visited = [0] * (V + 1)
    # [2] 초기데이터(들)를 q에 삽입(+단위작업: visit표시, sol처리 등)
    q.append(s)                                                         # 첫 위치를 q에 넣기
    visited[s] = 1                                                      # 방문 배열에 표시
    sols.append(s)                                                      # sol 배열에 첫 위치 넣기

    while q:                                                            # q에 데이터가 있는 동안 반복
        s = q.pop(0)                                                    # 제일 앞(FIFO)에서 데이터 꺼냄
        # 정답 처리가 필요한 경우 여기서

        # [3] 4, 8방향, 연결된 노드, ... 안가본, 조건에 맞는 곳이면..
        for e in range(1, V + 1):                                       # 1 ~ 7
            if e in adjList[s] and not visited[e]:
                q.append(e)
                visited[e] = 1
                sols.append(e)



T = int(input())
# T = 10
for test_case in range(1, T + 1):
    V, E = map(int, input().split())                                   # V : 정점의 갯수 E : 간선의 갯수
    # 인접리스트에 연결된 노드 추가(양방향)
    adjList = [[] * (V + 1) for _ in range(V + 1)]
    for _ in range(E):
        s, e = map(int, input().split())
        adjList[s].append(e)
        adjList[e].append(s)

    sols = []
    bfs(1)  # 시작지점 : 1, 방문 순서대로 sols에 추가

    print(f'#{test_case}', *sols)