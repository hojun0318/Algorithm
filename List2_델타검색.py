import sys
sys.stdin = open("input.txt", "r")

def absolute(arr_A, arr_B):
    if arr_A > arr_B:
        result = arr_A - arr_B
    else:
        result = -(arr_A - arr_B)
    return result

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 상하좌우
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    ans = 0

    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    ans += absolute(arr[i][j], arr[ni][nj])

    print(f'#{test_case} {ans}')