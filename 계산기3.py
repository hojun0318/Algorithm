import sys
sys.stdin = open('input.txt', 'r')

pri = {'*': 1, '+': 2, '(': 3, ')': 3}  # 연산자 우선순위 딕셔너리

def calulate(c1, c2, j):
    c1 = int(c1)
    c2 = int(c2)
    if j == '+':
        return c1 + c2
    elif j == '*':
        return c1 * c2
# T = 10
for test_case in range(1, 11):
    str = input()
    lst = list(input())
    stack_operator = []
    stack_result = []

    for i in lst:
        if '0' <= i <= '9':   # 숫자면 삽입
            stack_result.append(i)
        # 여는 괄호, empty stack, Stack top이 여는 괄호면
        elif not len(stack_operator) or i == '(' or stack_operator[-1] == '(':
            stack_operator.append(i)
        # 추가된 연산자가 stack top 연산자보다 우선순위가 높다면
        elif pri[i] < pri[stack_operator[-1]] and i != ')':
            stack_operator.append(i)
        else:
            # not empty stack, 추가된 연산자가 스택의 top보다 크거나 같을때까지
            while len(stack_operator) and pri[i] >= pri[stack_operator[-1]]:
                # 닫는 괄호면 괄호 pop -> break
                if stack_operator[-1] == '(':
                    stack_operator.pop()
                    break

                stack_result.append(stack_operator.pop())

            if i != ')':
                stack_operator.append(i)

    while len(stack_operator):
        temp = stack_operator.pop()
        if temp != '(':
            stack_result.append(temp)


    for j in stack_result:
        if '0' <= j <= '9':
            stack_operator.append(j)
        else:
            c2 = stack_operator.pop()
            c1 = stack_operator.pop()
            stack_operator.append(calulate(c1, c2, j))

    print(f'#{test_case} {stack_operator[0]}')