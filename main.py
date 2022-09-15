import sys
sys.stdin = open("input.txt", "r")

def calculate(n):
    if len(lst[n]) == 1:                # 숫자면
        return lst[n][0]
    else:                               # 연산자면
        if lst[n][0] == '-':
            return calculate(lst[n][1]) - calculate(lst[n][2])
        if lst[n][0] == '+':
            return calculate(lst[n][1]) + calculate(lst[n][2])
        elif lst[n][0] == '/':
            return calculate(lst[n][1]) // calculate(lst[n][2])
        else:
            return calculate(lst[n][1]) * calculate(lst[n][2])


T = 10
for test_case in range(1, T + 1):
    N = int(input())
    lst = [0] * (N + 1)
    root = 1

    for i in range(N):
        tlst = input().split()
        if len(tlst) == 2:
            lst[int(tlst[0])] = [int(tlst[1])]
        else:
            lst[int(tlst[0])] = [tlst[1]]+list(map(int, tlst[2:]))

    ans = calculate(root)
    print(f'#{test_case} {ans}')