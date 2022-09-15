import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    st = input()

    stack = []
    ans = 1

    for ch in st:
        if ch == '(':           # 여는 괄호면 스텍에 Push
            stack.append(ch)
        else:                   # 닫는 괄호면
            if stack:           # 스텍이 empty 상태가 아니면
                stack.pop()     # 여는 괄호 Pop
            else:               # 스텍이 empty면
                ans = 0         # 0 출력하고
                break           # break!!
    if stack:                   # 모든 괄호 처리하고도 스텍이 empty가 아니면
        ans = 0                 # 0 출력

    print(f'#{test_case} {ans}')
