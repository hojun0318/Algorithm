import sys
sys.stdin = open("input.txt", "r")

def is_promising(x):
    for i in range(x):
        if lst[x] == lst[i] or abs(lst[x] - lst[i]) == abs(x - i):  # 같은 열 또는 대각선에 존재하면 놓지 못함
            return False

    return True

def N_Queens(x):
    global ans
    if x == N:                      # 모든 퀸을 다 놓았다면
        ans += 1
        return
    else:
        for i in range(N):
            lst[x] = i              # 퀸 위치 설정 (i, j)
            if is_promising(x):     # 퀸을 놓을 수 있는지 검증
                N_Queens(x + 1)     # 퀸을 놓을 수 있으면 다음 퀸 놓을 곳 설정

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    ans = 0
    lst = [0] * N

    N_Queens(0)
    print(f'#{test_case} {ans}')