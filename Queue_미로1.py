import sys
sys.stdin = open("input.txt", "r")

def bfs(si, sj, ei, ej):
    # 기본 구조
    q = []                                                      # 빈 q 생성
    visited = [[0] * N for _ in range(N)]                       # 방문 배열 생성
    # q에 시작 데이터 삽입 (초기화)
    q.append((si, sj))                                          # 시작점 q에 넣어 초기화
    visited[si][sj] = 1                                         # 시작점 1로 방문표시

    while q:
        ci, cj = q.pop(0)
        # 종료 조건
        if ci == ei and cj == ej:
            return 1
        # 상하좌우
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            # 이동할 좌표가 범위 안, 방문하지 않은 곳, 벽이 아닌 곳이면
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and arr[ni][nj] != 1:
                q.append((ni, nj))
                visited[ni][nj] = 1

    # 길이 없다면 0 리턴
    return 0

T= 10
for test_case in range(1, T + 1):
    _ = int(input())
    N = 16                                                      # 16 x 16 사이즈
    arr = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:                                  # 출발점 찾기
                si, sj = i, j
            elif arr[i][j] == 3:                                # 도착점 찾기
                ei, ej = i, j

    ans = bfs(si, sj, ei, ej)

    print(f'#{test_case} {ans}')