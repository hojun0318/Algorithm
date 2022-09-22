import sys
sys.stdin = open("input.txt", "r")

def dfs(ci, cj, sm):
    global ans
    # 가지치기
    if ans <= sm:
        return
    # 종료조건
    if ci == N and cj == N:
        ans = min(ans, sm)
        return
    # 중복 처리 작업 및 하부 조건
    if ci < N:
        dfs(ci + 1, cj, sm + arr[ci + 1][cj])
    if cj < N:
        dfs(ci, cj + 1, sm + arr[ci][cj + 1])

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    # 위, 왼쪽에 0을 한 겹 씌움
    arr = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
    ans = 10 * N * 2

    dfs(1, 1, arr[1][1])

    print(f'#{test_case} {ans}')