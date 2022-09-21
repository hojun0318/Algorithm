import sys
sys.stdin = open("input.txt", "r")

def dfs(n, sm, cnt):
    global ans
    # 가지치기는 가장 위쪽에서: 더 이상 진행이 의미 없는 경우
    if sm > K:
        return

    # 종료조건: (n에 관련), 정답관련 처리
    if n == N:
        if sm == K and cnt == CNT:
            ans += 1
        return

    dfs(n + 1, sm + lst[n], cnt + 1)  # 사용하는 경우
    dfs(n + 1, sm, cnt)  # 사용하지 않는 경우


T = int(input())
# T = 10
for test_case in range(1, T + 1):
    CNT, K = map(int, input().split())
    lst = [n for n in range(1, 13)]
    N = 12

    ans = 0
    dfs(0, 0, 0)
    print(f'#{test_case} {ans}')