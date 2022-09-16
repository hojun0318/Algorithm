import sys
sys.stdin = open("input.txt", "r")


def dfs(s):
    stk = []

    visited[s] = 1

    while True:
        for e in adjL[s]:
            if not visited[e]:
                stk.append(s)  # 되돌아올 위치 push

                s = e
                visited[s] = 1
                break
        else:
            if stk:
                s = stk.pop()
            else:
                break


for test_case in range(1, 11):
    tc, E = map(int, input().split())  # E : 길의 총 개수
    adjL = [[] for _ in range(100)]  # 인접리스트로 연결상태 저장
    lst = list(map(int, input().split()))

    for i in range(0, len(lst), 2):
        s = lst[i]
        e = lst[i + 1]
        adjL[s].append(e)

    s, g = 0, 99
    visited = [0 for _ in range(100)]
    dfs(s)

    print(f'#{tc} {visited[g]}')