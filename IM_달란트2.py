import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, P = map(int, input().split())
    lst = [N // P] * P                  # 모두 같은 값으로 초기화(균등 배분)
    ans = 1


    # 나머지를 0 ~ 하나씩 증가
    for i in range(N % P):
        lst[i] += 1

    for n in lst:
        ans *= n

    # for i in range(P):
    #     ans *= N // (P - i)
    #     N = N - (N // (P - i))

    print(f'#{test_case} {ans}')