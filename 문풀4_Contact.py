import sys
sys.stdin = open("input.txt", "r")

def bfs(s):
    q = []                      # q, visited, 기타 초기화
    v = [0] * 101
    ans = s

    q.append(s)
    v[s] = 1

    while q:
        c = q.pop(0)
        #  장딥 처리: 더 늦게 방문 or 같은 거리인데 더 큰 번호인 경우
        if v[ans] < v[c] or v[ans] == v[c] and ans < c:
            ans = c

        for e in adjL[c]:
            if not v[e]:
                q.append(e)
                v[e] = v[c] + 1
    return ans

T = 10
for test_case in range(1, T + 1):
    N, S = map(int, input().split())
    lst = list(map(int, input().split()))

    # [1] 연결을 인접리스트에 저장
    adjL = [[] for _ in range(101)]
    for i in range(0, len(lst), 2):
        p, c = lst[i], lst[i + 1]
        adjL[p].append(c)

    ans = bfs(S)

    print(f'#{test_case} {ans}')