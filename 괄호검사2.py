import sys
sys.stdin = open("input.txt", "r")

dct = {'{':'}', '(':')'}
tbl = '})'

T = int(input())
for test_case in range(1, T + 1):
    st = input()
    stack = []
    ans = 1
    for ch in st:
        if ch in dct : # ch가 괄호 열기 기호인 경우
            stack.append(dct[ch])
        elif ch in tbl: # ch가 괄호 닫기 기호인 경우
            if stack and ch == stack.pop():
                pass
            else:
                ans = 0
                break
    if stack: # 모든 괄호 비교 후 남은 괄호 체크(열린 괄호가 더 많은 경우)
        ans = 0

    print(f'#{test_case} {ans}')