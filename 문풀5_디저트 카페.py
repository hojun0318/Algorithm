import sys
sys.stdin = open("input.txt", "r")

directions = [(1, 1), (1, -1), (-1, -1), (-1, 1)]  # 우하->좌하->좌상->우상


def dfs(ci, cj, direction, cnt):
    global ans

    # 현재 방향 기준 방향 범위 설정용 temp 생성
    if direction < 3:
        temp = direction + 2
    else:
        temp = direction + 1

    # 종료 조건 (시작 좌표로 돌아왔을 때)
    if cnt > 0 and ci == start[0] and cj == start[1]:
        if ans < cnt:
            ans = cnt
        return

    # 현재 방향으로 직진하거나(dir), 방향 꺾거나(dir+1)
    # dir이 3이라면 (우상 방향) 계속 직진
    for nd in range(direction, temp):
        ni, nj = ci + directions[nd][0], cj + directions[nd][1]
        if 0 <= ni < N and 0 <= nj < N and visited[arr[ni][nj]] == 0:
            visited[arr[ni][nj]] = 1
            dfs(ni, nj, nd, cnt + 1)
            visited[arr[ni][nj]] = 0


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = -1
    visited = [0] * 101  # 디저트 중복 여부

    # 모든 좌표 출발점으로 탐색
    for i in range(N):
        for j in range(N):
            start = (i, j)
            dfs(i, j, 0, 0)

    print(f'#{test_case} {ans}')
