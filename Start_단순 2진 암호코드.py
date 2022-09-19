import sys

sys.stdin = open("input.txt", "r")

pwd = {
    '0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
    '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    # 끝나는 점 찾기
    # 암호코드는 모두 1로 끝남
    row = end = 0                               # 2차 배열이므로
    for r in range(N):                          # row
        for i in range(M - 1, -1, -1):
            if arr[r][i] == '1':                # row
                row = r                         # row
                end = i                         # end = 59번째
                break
        # 0이 아니면 찾았다는 것이니 빠져나옴
        if end:
            break

    start = end - 56 + 1                        # 59 - 56 + 1 = 4번째

    # start부터 7 bit씩 잘라서 읽기 - 8자리 뽑기
    # 패턴의 모든 시작 위치를 생성
    codes = []
    for i in range(start, end, 7):
        codes.append(pwd[arr[row][i: i + 7]])  # row

    odd = codes[0] + codes[2] + codes[4] + codes[6]
    even = codes[1] + codes[3] + codes[5] + codes[7]

    # (홀수합*3 + 짝수합) % 10 == 0인 경우만 정상 암호 코드
    ans = 0
    if (odd * 3 + even) % 10 == 0:
        ans = odd + even

    print(f'#{test_case} {ans}')