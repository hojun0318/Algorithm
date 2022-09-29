import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, E = map(int, input().split())
    ans = [10000000] * (N + 1)
    arr = [[0]*(N+1) for _ in range(N+1)]
    ans[0] = 0                                        # 출발점은 항상 0

    for i in range(E):
        start, end, weight = map(int, input().split())
        arr[start][end] = weight

    for i in range(N + 1):
        for j in range(N + 1):
            if arr[i][j] != 0:                        # 경로가 있다면
                if ans[j] > arr[i][j] + ans[i]:       # 지금 경로가 다음 경로에 저장된 값보다 작다면
                    ans[j] = arr[i][j] + ans[i]       # 갱신

    print(f'#{test_case} {ans[N]}')