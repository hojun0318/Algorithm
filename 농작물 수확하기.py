import sys
sys.stdin = open("input.txt", "r")

# 좌하, 우하, 우상, 좌상
di = [1, 1, -1, -1]
dj = [-1, 1, 1, -1]

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())                        # N = 5
    farm = [list(map(int, input())) for _ in range(N)]
    i = 0
    j = ((N - 1) // 2)      # j = 2 ( (5 - 1) // 2 )
    dr = 0
    sm = 0
    cnt = 2 

    while cnt < ((N * N) // 2) + 1:             # 1/2만 돌리기
        sm += farm[i][j]
        farm[i][j] = 6
        cnt += 1
        ni, nj = i + di[dr], j + dj[dr]         # 이동할 좌표 계산
        if 0 <= ni < N and 0 <= nj < N and farm[ni][nj] != 6:         # 좌표가 범위 내
            i, j = ni, nj # 현재 좌표로 이동
        else:
            dr = (dr + 1) % 4
        print(sm, end=' ')
    #print(f'#{test_case} {sm}')