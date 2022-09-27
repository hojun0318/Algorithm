import sys
sys.stdin = open("input.txt", "r")

def dfs(n, sm):
    global ans
    if ans >= sm:               # 가지치기
        return

    if n == N:                  # 끝까지 돌았으면
        ans = max(ans, sm)      # 최댓값 출력
        return

    for j in range(N):
        if visited[j] == 0:     # 방문 안했으면
            visited[j] = 1      # 방문 표시
            dfs(n + 1, sm * arr[n][j])      # 확률 곱하기
            visited[j] = 0      # 초기화

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    # 정수값을 소수값으로 변경해서 리스트로 받기
    arr = [list(map(lambda x : int(x) / 100, input().split())) for _ in range(N)]
    visited = [0] * N               # 방문 표시 초기화
    ans = 0                         # 현재값 초기화

    dfs(0, 1)
    values = ans * 100

    print(f'#{test_case} {values:.6f}')         # 소수점 6자리까지 출력