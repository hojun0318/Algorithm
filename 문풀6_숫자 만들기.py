import sys
sys.stdin = open("input.txt", "r")

def dfs(n, num, n1, n2, n3, n4):
    global mn, mx
    if n == N:
        mn = min(mn, num)
        mx = max(mx, num)
        return

    if n1:
        dfs(n + 1, num + lst[n], n1 - 1, n2, n3, n4)
    if n2:
        dfs(n + 1, num - lst[n], n1, n2 - 1, n3, n4)
    if n3:
        dfs(n + 1, num * lst[n], n1, n2, n3 - 1, n4)
    if n4:
        dfs(n + 1, int(num / lst[n]), n1, n2, n3, n4 - 1)


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    add, sub, mul, div = map(int, input().split())
    lst = list(map(int, input().split()))

    mn = int(1e8)
    mx = int(-1e8)
    dfs(1, lst[0], add, sub, mul, div)
    print(f'#{test_case} {mx - mn}')