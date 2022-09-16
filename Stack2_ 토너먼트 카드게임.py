import sys
sys.stdin = open("input.txt", "r")

def solve(s, e):
    # [1] 종료 조건
    if s == e:
        return s
    # [2] 하부 호출, 최소 단위작업: 2등분해서 각각 승자를 구하고 최종 승자 구하기
    a = solve(s, (s + e) // 2)
    b = solve((s + e) // 2 + 1, e)

    if (lst[a] % 3) + 1 == lst[b]:       # b가 이긴 경우 b가 승자
        return b
    else:                                 # 비기거나 a가 이긴경우 a가 승자
        return a


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lst = [0] + list(map(int, input().split()))

    ans = solve(1, N)                     # 1부터 N 사이의 최종 승리자의 index를 Return


    print(f'#{test_case} {ans}')