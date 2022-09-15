import sys
sys.stdin = open("input.txt", "r")

def check():
    global sdoku
    for si in range(0, N, M):                           # 시작점 찾기 (3칸씩)
        for sj in range(0, N, M):                       # 시작점 찾기 (3칸씩)
            chk = []
            for i in range(si, si + M):
                for j in range(sj, sj + M):             # 3 x 3 확인
                    if sdoku[i][j] not in chk:
                        chk.append(sdoku[i][j])         # 중복이 없다면 1 ~ 9까지 들어감
                    else:
                        return 0                        # 중복이 있으면 0 반환

    for _ in range(2):                                  # 행, 열 2번 확인
        for i in range(N):
            chk = []
            for j in range(N):
                if sdoku[i][j] not in chk:
                    chk.append(sdoku[i][j])             # 중복이 없다면 1 ~ 9까지 들어감
                else:
                    return 0                            # 중복이 있으면 0 반환
        sdoku = list(zip(*sdoku))                       # 전치 행렬

    return 1                                            # 모두 만족하면 1 반환


T = int(input())
for test_case in range(1, T + 1):
    N = 9
    M = 3
    sdoku = [list(map(int, input().split())) for _ in range(N)]

    ans = check()

    print(f'#{test_case} {ans}')
