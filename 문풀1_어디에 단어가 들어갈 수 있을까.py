import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    # 행과 열에 0을 추가해 범위 설정 따로 하지 않음
    arr = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (N + 1)]

    ans = 0
    for _ in range(2):                  # 행, 열 한번씩
        for i in range(N + 1):
            cnts = 0
            for j in range(N + 1):
                if arr[i][j] == 1:      # 1이면 카운트 1씩 증가
                    cnts += 1
                else:
                    if cnts == K:       # 0을 만났을 때 카운트 값이 K랑 같으면
                        ans += 1        # 들어갈 수 있는 자리수 1 증가
                    cnts = 0            # K랑 다르면 카운트 초기화
        arr = list(zip(*arr))           # 전치 행렬

    print(f'#{test_case} {ans}')