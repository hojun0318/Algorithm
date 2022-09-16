T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (N + 1)]

    ans = 0
    for _ in range(2):
        for i in range(N + 1):
            cnt = 0
            for j in range(N + 1):
                if arr[i][j] == 1:
                    cnt += 1
                else:
                    if cnt == K:
                        ans += 1
                    cnt = 0
        arr = list(zip(*arr))

    print(f'#{test_case} {ans}')