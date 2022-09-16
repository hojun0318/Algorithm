import sys
sys.stdin = open("input.txt", "r")

# T = 10
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    # [1] q생성 후 순서대로 피자 가득채움
    q = []
    for i in range(N):
        q.append((i + 1, lst[i]))
    print(q)

    i = N           # i == 3
    # [2] q가 not empty일 동안 루프
    while q:
        ans, piz = q.pop(0)  # 피자번호, 치즈량
        piz //= 2

        if piz == 0:  # 꺼내야하는 경우
            if i < M:  # 넣을 피자가 있는경우
                q.append((i + 1, lst[i]))
                i += 1
        else:  # 재투입
            q.append((ans, piz))

    print(f'#{test_case} {ans}')