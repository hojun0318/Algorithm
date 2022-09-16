import sys
sys.stdin = open("input.txt", "r")


def post(n):
    if lst[n]:  # 노드가 존재하는 경우
        # 연산자인 경우에는 좌/우 값을 연산
        if lst[n] == '+':
            return post(ch1[n]) + post(ch2[n])
        elif lst[n] == '-':
            return post(ch1[n]) - post(ch2[n])
        elif lst[n] == '*':
            return post(ch1[n]) * post(ch2[n])
        elif lst[n] == '/':
            return post(ch1[n]) / post(ch2[n])
        # 숫자인경우(문자로 저장)
        else:
            return int(lst[n])


T = 10
# T = int(input())
for test_case in range(1, 2):
    N = int(input())
    lst = [0] * (N + 1)
    ch1 = [0] * (N + 1)
    ch2 = [0] * (N + 1)
    # [1] 트리구조에 맞게 저장
    for _ in range(N):
        tlst = input().split()
        print(tlst)
        p = int(tlst[0])
        print(p)
        lst[p] = tlst[1]
        print(lst)
        if len(tlst) > 2:
            ch1[p] = int(tlst[2])
            ch2[p] = int(tlst[3])
            print(ch1)
            print(ch2)
    # [2] post order순회하면서 계산
    ans = int(post(1))
    print(f'#{test_case} {ans}')