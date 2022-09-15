import sys
sys.stdin = open("input.txt", "r")

def rotate(arr):
    rota_arr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            rota_arr[j][N - 1 - i] = arr[i][j]

    return rota_arr

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    arr90 = rotate(arr)
    arr180 = rotate(arr90)
    arr270 = rotate(arr180)

    print(f'#{test_case}')
    for a, b, c in zip(arr90, arr180, arr270):
        print(f'{"".join(map(str, a))} {"".join(map(str, b))} {"".join(map(str, c))}')


