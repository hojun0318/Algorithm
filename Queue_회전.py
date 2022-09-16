import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    queue = list(map(int, input().split()))
    cnt = 0

    while cnt < M:
        queue.append(queue.pop(0))
        cnt += 1
    print(f'#{test_case} {queue[0]}')