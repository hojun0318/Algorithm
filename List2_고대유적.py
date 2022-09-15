import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_R = 0
    max_V = 0
    mx = 0

    for i in range(N):
        cnt = 0
        for j in range(M):
            if arr[i][j] == 1:
                cnt += 1
                if max_R < cnt:
                    max_R = cnt
            else:
                cnt = 0

    for j in range(M):
        cnt = 0
        for i in range(N):
            if arr[i][j] == 1:
                cnt += 1
                if max_V < cnt:
                    max_V = cnt
            else:
                cnt = 0

    if max_R >= max_V:
        mx = max_R
    else:
        mx = max_V

    print(f'#{test_case} {mx}')