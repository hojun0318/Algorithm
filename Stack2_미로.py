import sys
sys.stdin = open("input.txt", "r")

def dfs(si, sj):
    stk = []
    visited[si][sj] = 1

    while True:
        # 상하좌우의 네 방향, 미방문지, 길이면(벽이 아니면)
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = si + di, sj + dj
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and arr[ni][nj] != 1:
                stk.append((si, sj))

                si, sj = ni, nj         # 탐색 기준점 변경
                visited[ni][nj] = 1
                break
        else:
            if stk:
                si, sj = stk.pop()
            else:
                break

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    # 출발점, 도착점 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                si, sj = i, j               # si, sj = 출발점 행과 열
            elif arr[i][j] == 3:
                ei, ej = i, j               # ei, sj = 도착점 행과 열

    # visited 배열 초기화 후 전체 방문 표시
    visited = [[0] * N for _ in range(N)]
    dfs(si, sj)             # 시작 좌표

    print(f'#{test_case} {visited[ei][ej]}')