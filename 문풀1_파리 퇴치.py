import sys
sys.stdin = open("input.txt", "r")

def check():
    global arr
    mx = 0
    for si in range(N - M + 1):                 # 시작점 찾기
        for sj in range(N - M + 1):
            cnts = 0
            for i in range(si, si + M):         # M칸 만큼 파리 퇴치
                for j in range(sj, sj + M):
                    cnts += arr[i][j]
            if mx < cnts:
                mx = cnts                       # 최댓값 찾기
    return mx

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = check()

    print(f'#{test_case} {ans}')