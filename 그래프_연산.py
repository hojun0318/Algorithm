import sys
sys.stdin = open("input.txt", "r")

from collections import deque


def bfs(s, e):
    # q = []
    # q = deque()
    q = [0] * 1000000  # 선형큐를 만들어서 사용
    rd = wr = 0
    v = [0] * 1000001

    # q.append(s)
    q[wr] = s
    wr += 1
    v[s] = 1

    while q:
        # c = q.pop(0)  # 기본 q사용은 시간초과  4000ms
        # c = q.popleft() # deque사용              350ms
        c = q[rd]
        rd += 1
        if c == e:
            return v[c] - 1  # 초기값이 1이므로 -1 처리
        # 네방향(연산), 범위내, 미방문 시
        for n in ((c + 1), (c - 1), (c * 2), (c - 10)):
            if 0 < n <= 1000000 and v[n] == 0:
                # q.append(n)
                q[wr] = n
                wr += 1
                v[n] = v[c] + 1

    return -1  # 이코드를 실행하지는 않지만..


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    ans = bfs(N, M)

    print(f'#{test_case} {ans}')