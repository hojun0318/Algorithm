import sys
sys.stdin = open("input.txt", "r")

def solve():
    global arr
    for si in range(0, N, M):
        for sj in range(0, N, M):
            chk = []
            for i in range(si, si + M):
                for j in range(sj, sj + M):
                    if arr[i][j] not in chk:
                        chk.append(arr[i][j])
                    else:
                        return 0
    for _ in range(2):
        for i in range(N):
            chk = []
            for j in range(N):
                if arr[i][j] not in chk:
                    chk.append(arr[i][j])
                else:
                    return 0
        arr = list(zip(*arr))
    return 1

T = int(input())
for test_case in range(1, T + 1):
    N = 9
    M = 3
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = solve()

    print(f'#{test_case} {ans}')
