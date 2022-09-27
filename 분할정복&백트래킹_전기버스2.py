import sys
sys.stdin = open("input.txt", "r")

def dfs(n, cnt, sm):
    global ans
    if ans <= cnt:
        return

    if n == N:
        ans = min(ans, cnt)
        return

    # 교체하지 않는 경우(가능한 지 체크 필요!!)
    if sm > 0:
        dfs(n + 1, cnt, sm - 1)

    # 교체하는 경우
    dfs(n + 1, cnt + 1, lst[n] - 1)



T = int(input())
for test_case in range(1, T + 1):
    lst = list(map(int, input().split()))
    N = lst[0]
    ans = N             # 최소값의 초기값 설정

    dfs(2, 0, lst[1] - 1)

    print(f'#{test_case} {ans}')