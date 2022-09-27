import sys
sys.stdin = open("input.txt", "r")

def is_minimum(x):
    global j
    for i in range(x):
        if i == j or arr[x][i] >= sm:
            return False

    return True

def price(x):
    global ans, sm
    if x == N:
        return sm
    else:
        for j in range(N):          # 0, 1, 2
            ans += arr[x][j]
            if is_minimum(x):
                if sm >= ans:
                    sm = ans
                price(x + 1)

T = int(input())
for test_case in range(1, 2):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    sm = 99 * N
    ans = 0

    price(0)
    print(ans)