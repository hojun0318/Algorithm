for test_case in range(1, 11):
    N, M = input().split()
    stack = []
    for i in range(int(N)):
        if stack == [] or stack[-1] != M[i]:
            stack.append(M[i])
        elif stack[-1] == M[i]:
            stack.pop()
    print('#{} {}'.format(test_case, ''.join(stack)))