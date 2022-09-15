import sys
sys.stdin = open("input.txt", "r")


def bfs(start_i, start_j):
    # [1] 초기화
    q = []                                                  # 큐 생성
    visited = [[0] * N for _ in range(N)]                   # 방문 기록 배열 생성

    # [2] q에 초기데이터(들) 삽입(단위작업)
    q.append((start_i, start_j))
    visited[start_i][start_j] = 1

    while q:
        # [3] 데이터 한 개 꺼냄
        ci, cj = q.pop(0)
        if ci == end_i and cj == end_j:  # 정답 확인 : 도착점(i, j)과 같다면
            return 1

        # 상하좌우
        for direct_i, direct_j in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            new_i, new_j = ci + direct_i, cj + direct_j

            # 이동할 좌표가 범위 내,                 방문 안했던 좌표,                      길이 아닌 곳
            if 0 <= new_i < N and 0 <= new_j < N and not visited[new_i][new_j] and arr[new_i][new_j] != '1':
                q.append((new_i, new_j))
                visited[new_i][new_j] = 1
    return 0


T = int(input())
# T = 10
for test_case in range(1, T + 1):
    N = int(input())
    arr = [input() for _ in range(N)]

    # 지도에서 si, sj
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':                # 시작점 찾기
                start_i, start_j = i, j
            elif arr[i][j] == '3':              # 도착점 찾기
                end_i, end_j = i, j

    ans = bfs(start_i, start_j)

    print(f'#{test_case} {ans}')