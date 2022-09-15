import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]
    cnts = 0

    center = N // 2                                         # 농장 크기 중앙값
    for i in range(N):
        if i <= center:                                     # i가 농장 중앙값보다 작을때의 j범위 설정
            for j in range(center - i, center + i + 1):
                cnts += farm[i][j]
        else:                                               # i가 농장 중앙값보다 클때의 j범위 설정
            for j in range(i - center, N - (i - center)):
                cnts += farm[i][j]

    print(f'#{test_case} {cnts}')