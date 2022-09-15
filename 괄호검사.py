import sys
sys.stdin = open("input.txt", "r")

# 우하좌상
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


T = int(input())
# T = 10
for test_case in range(1, T + 1):
    N = int(input())
    # [1] 초기값 설정
    arr = [[0] * N for _ in range(N)]
    i = j = dr = 0

    # [2] cnt 1 ~ N * N
    for cnt in range(1, N * N + 1):
        arr[i][j] = cnt

        ni, nj = i + di[dr], j + dj[dr]
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
            i, j = ni, nj
        else:       # 범위 밖 또는 그 자리에 이미 값이 존재
            dr = (dr + 1) % 4
            i, j = i + di[dr], j + dj[dr]

    print(f'{test_case}')
    for lst in arr:
        print(*lst)
