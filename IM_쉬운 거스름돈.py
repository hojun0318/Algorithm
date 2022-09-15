import sys
sys.stdin = open("input.txt", "r")

won = [50000, 10000, 5000, 1000, 500, 100, 50, 10]      # 거스름돈
lst = [0] * len(won)

T = int(input())
for test_case in range(1, T + 1):
    change = int(input())

    for i in range(len(won)):
        lst[i] = change // won[i]                       # 거스름돈 갯수
        change = change % won[i]                        # 잔액

    print(f'#{test_case}')
    print(*lst)