import sys
sys.stdin = open("input.txt", "r")

T = 10
for test_case in range(1, 11):
    tc = int(input())
    N = 100
    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(N)]

    # 초기값 설정
    i, j = N-1, 0
    # [1] 목적지(출발지)
    for tj in range(N + 2):
        if arr[i][tj] == 2:         # arr[99][0~99] == 2
            j = tj
            break

    while i > 0:                    # 기존 출발점이 i = 0이므로 음수가 될 경우 stop!
        if arr[i][j - 1] == 1:      # 왼쪽에 이동 가능한 길이 있다면
            arr[i][j] = 0           # 지나온 길은 0으로 만듬
            j -= 1
        elif arr[i][j + 1] == 1:    # 오른쪽에 이동 가능한 길이 있다면
            arr[i][j] = 0           # 지나온 길은 0으로 만듬
            j += 1
        else:
            i -= 1                  # 왼쪽, 오른쪽으로 가능한 길이 없다면 직진한다.

    print(f'#{test_case} {j-1}')    # 0을 넣어줬기 때문에 -1을 해줘야 원래 위치



