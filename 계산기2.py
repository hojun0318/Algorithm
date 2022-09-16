import sys
sys.stdin = open("input.txt", "r")

for test_case in range(1, 11):
    N = int(input())
    str = input()
    equ = []
    stack = []
    for i in str:
        if i in '0123456789':
            equ.append(i)
        elif not stack:
            stack.append(i)
        else:
            if i == '*' and stack[-1] == '+':
                stack.append(i)
            else:
                x = equ.pop()
                y = equ.pop()
                z = stack.pop()
                if z == '+':
                    equ.append(int(x) + int(y))
                else:
                    equ.append(int(x) * int(y))
                stack.append(i)

    for i in range(len(stack)):
        x = equ.pop()
        y = equ.pop()
        z = stack.pop()
        if z == '+':
            equ.append(int(x) + int(y))
        else:
            equ.append(int(x) * int(y))

    print(f'#{test_case}', equ[0])