import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input()))
    temp = [0] * 10
    cnt = []

    # 카드 숫자 장수
    for i in lst:
        temp[i] += 1

    mx = temp[0]
    max_num = 0
    for j in range(1, len(temp)):
        if mx <= temp[j]:
            max_num, mx = j, temp[j]

    print(f'#{test_case} {max_num} {mx}')