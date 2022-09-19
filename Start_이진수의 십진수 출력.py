import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    lst = list(map(int, input()))
    ans = []
    values = lst[0]
    for i in range(1, len(lst)):
        values = values * 2 + lst[i]
        if i % 7 == 6:             # 7 bit씩 끊기
            ans.append(values)
            values = 0

    print(f'#{test_case}', *ans)