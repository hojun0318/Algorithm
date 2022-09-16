import sys
sys.stdin = open("input.txt", "r")

def bfs(si, sj):
    queue = []
    ans = []

    queue.append((si, sj))
    visited[si][sj] = 1
    ans.append(arr[si][sj])

    while queue:
        ci, cj = queue.pop(0)
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            # 범위 내이고, 방문 안 한 곳이고, 나와 1차이만큼 나는 경우
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and abs(arr[ci][cj] - arr[ni][nj]) == 1:
                queue.append((ni, nj))
                visited[ni][nj] = 1
                ans.append(arr[ni][nj])

    return len(ans), min(ans)


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt, num = 0, N * N
    # 전체순회: 방문 안 한 노드라면 방문
    visited = [[0] * (N) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                tcnt, tnum = bfs(i, j)
                if cnt < tcnt or cnt == tcnt and num > tnum:
                    cnt, num = tcnt, tnum

    print(f'#{test_case} {num} {cnt}')  # 번호, 개수