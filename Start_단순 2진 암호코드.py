import sys
sys.stdin = open("input.txt", "r")

pwd = {
    '0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
    '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

T = int(input())
for test_case in range(1, T  + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    # 끝위치 찾기
    row = end = 0
    for r in range(N):
        for i in range(M - 1, -1, -1):
            if arr[r][i] == '1':
                row = r
                end = i
                break
        if end:
            break

    start = end - 56 + 1    # end - 55

    # start부터 7 bit씩 잘라서 읽기
    # 패턴의 모든 시작 위치를 생성
    codes = []
    for i in range(start, end, 7):
        codes.append(pwd[arr[row][i : i + 7]])
        # print(pwd[arr[row]], pwd[arr[i : i + 7]])

    odd = codes[0]+ codes[2] + codes[4] + codes[6]
    even = codes[1] + codes[3] + codes[5] + codes[7]

    ans = 0
    if (odd * 3 + even) % 10 == 0:
        ans = odd + even
    print(f'#{test_case} {ans}')