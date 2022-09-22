import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    arr.sort(key=lambda x: x[1])
    last = ans = 0

    for (s, e) in arr:
        if last <= s:
            ans += 1
            last = e

    print(f'#{test_case} {ans}')




