import sys
sys.stdin = open("input.txt", "r")

p = [[0, 0, 0, 0], [1, 1, 1, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 0, 1], [0, 1, 0, 1], [0, 1, 1, 0], [1, 0, 1, 0]]
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
opp = [1, 0, 3, 2]


def bfs(si, sj):
    q = []
    v = [[0] * M for _ in range(N)]
    cnt = 0

    q.append((si, sj))
    v[si][sj] = 1
    cnt += 1

    while q:
        ci, cj = q.pop(0)
        if v[ci][cj] == L:
            return cnt

        for dr in range(4):  # 0~3방향
            ni, nj = ci + di[dr], cj + dj[dr]
            if 0 <= ni < N and 0 <= nj < M and not v[ni][nj] and p[arr[ci][cj]][dr] and p[arr[ni][nj]][opp[dr]]:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1
                cnt += 1

    # q를 모두 소진했는데 L을 못만난경우
    return cnt  # 이 코드가 실행될지는 알수없지만..


T = int(input())
for test_case in range(1, T + 1):
    N, M, SI, SJ, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = bfs(SI, SJ)
    print(f'#{test_case} {ans}')