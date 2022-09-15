import sys
sys.stdin = open("input.txt", "r")

T = 10
for test_case in range(1, T + 1):
    N = int(input())
    magnetic = [list(map(int, input().split())) for _ in range(N)]

    # 1 = N극(붉은)성질 (아래로) , 2 = S극(푸른)성질 (위로)

    magnetic = list(zip(*magnetic))     # 전치행렬 (더 편함)
    cnts = 0                            # 교착상태 개수 변수

    for i in range(N):
        stack = 0                       # False
        for j in range(N):
            if magnetic[i][j] == 1:     # 1이면
                stack += 1              # True로 변경
            elif magnetic[i][j] == 2:   # 2일때
                if stack:               # True이면
                    stack = 0           # 초기화
                    cnts += 1           # 교착상태 개수 1 증가

    print(f'#{test_case} {cnts}')