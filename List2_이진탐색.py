import sys
sys.stdin = open("input.txt", "r")

def binarySearch(S, E, Key):
    cnt = 0
    while S <= E:
        cnt += 1                        # 값을 찾을때 마다 cnt 1씩 증가
        middle = int((S + E) // 2)
        if middle == Key:
            return cnt
        elif middle > Key:
            E = middle
        else:
            S = middle
    return False


T = int(input())
for test_case in range(1, T + 1):
    P, Pa, Pb = map(int, input().split())
    lst = list(range(P))
    result = 0

    A = binarySearch(1, P, Pa)
    B = binarySearch(1, P, Pb)

    if A > B:
        result = 'B'
    if A < B:
        result = 'A'
    if A == B:
        result = 0

    print(f'#{test_case} {result}')
