import sys
sys.stdin = open("input.txt", "r")

def bfs_drive(n):
    global sm, charge
    if n >= len(lst):        # 종점에 도착하면
        if sm >= charge:     # 충전 최소 횟수보다 작으면
            sm = charge      # 현재 값으로 대체
        return

    if sm <= charge:         # 현재 충전 횟수가 이전 충전 횟수보다 커지만 백트래킹
        return

    for i in range(n + lst[n], n, -1):
        charge += 1
        bfs_drive(i)
        charge -= 1



T = int(input())
for test_case in range(1, T + 1):
    lst = list(map(int, input().split()))           # len(lst) = 5
    N = lst[0]
    sm = 9999999            # 충전 최소 횟수
    charge = 0              # 현재 충전 횟수

    bfs_drive(1)                # idx 1부터 충전량 시작

    print(f'#{test_case} {sm - 1}')