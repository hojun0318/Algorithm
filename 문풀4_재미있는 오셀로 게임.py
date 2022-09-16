import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [[0] * (N + 1) for _ in range(N + 1)]

    mid = N // 2
    arr[mid][mid] = arr[mid + 1][mid + 1] = 2
    arr[mid][mid + 1] = arr[mid + 1][mid] = 1

    for _ in range(M):
        si, sj, d = map(int, input().split())
        arr[si][sj] = d

        # 8방향 뻗어나가면서 범위내(0: 끝, 같은돌: 후보를 뒤집고 끝, 다른돌: 후보에 추가), 범위외 종료
        for di, dj in ((-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1), (0, -1), (0, 1)):
            s = []
            for mul in range(1, N):
                ni, nj = si + di * mul, sj + dj * mul

                if 1 <= ni <= N and 1 <= nj <= N:
                    if arr[ni][nj] == 0:  # 빈 칸
                        break
                    elif arr[ni][nj] == arr[si][sj]:  # 같은돌
                        while s:
                            ti, tj = s.pop()
                            arr[ti][tj] = d
                        break
                    else:  # 다른돌
                        s.append((ni, nj))

                else:  # 범위 밖인 경우 끝 -> 다음방향으로
                    break

    bcnt = wcnt = 0
    for lst in arr:
        bcnt += lst.count(1)
        wcnt += lst.count(2)
    print(f'#{test_case} {bcnt} {wcnt}')