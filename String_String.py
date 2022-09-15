import sys
sys.stdin = open("input.txt", "r", encoding='UTF-8')


def cmp(st, N, p, M, i):                # (전체 문자열, 전체 문자열 길이, 찾을 문자열, 찾을 문자열 길이, 시작 지점)
    for j in range(M):
        if st[i + j] != p[j]:           # 찾을 문자열 한 문자씩 검사
            return 0
    return 1


T = 10
# T = int(input())
for test_case in range(1, T + 1):
    _ = input()
    p = input()                             # 찾을 문자열
    st = input()                            # 전체 문자열
    ans = 0
    N, M = len(st), len(p)

    for i in range(N - M + 1):              # 찾을 문자열 범위
        if cmp(st, N, p, M, i):
            ans += 1                        # 전체 문자열 안에 찾을 문자열이 있다면 1 증가

    print(f'#{test_case} {ans}')