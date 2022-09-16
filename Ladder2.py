T = 10
# T = int(input())
for test_case in range(1, T + 1):
    _ = input()
    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]
    mx = 100 * 100

    # j==1부터 100까지 1을 만나면 탐색시작
    for sj in range(1, 101):
        if arr[0][sj] == 0:
            continue

        cj = sj
        ci = cnt = dj = 0
        while ci < 99:
            cnt += 1
            if dj == 0:  # 아래방향: 이동후 방향설정
                ci += 1  # [1] 이동
                if arr[ci][cj - 1] == 1:  # 좌측에 길있음
                    dj = -1
                elif arr[ci][cj + 1] == 1:  # 우측에 길
                    dj = 1
            else:  # 좌/우방향
                cj += dj  # [1] 이동
                if arr[ci][cj + dj] == 0:  # 막다른길->아래
                    dj = 0
        if mx >= cnt:  # 같은거리면 높은좌표값이 정답
            mx, ans = cnt, sj - 1

    print(f'#{test_case} {ans}')  # 정답은 -1한 좌표