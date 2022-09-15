import sys
sys.stdin = open("input.txt", "r")

for test_case in range(1, 11):
    tc = int(input())
    N = 100
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = s3 = s4 = 0
    for i in range(N):
        s1 = s2 = 0
        for j in range(N):
            s1 += arr[i][j]
            s2 += arr[j][i]
        if ans < s1: ans = s1
        if ans < s2: ans = s2

        s3 += arr[i][j]
        s4 += arr[i][N-1-i]
    if ans < s3: ans = s3
    if ans < s4: ans = s4

    print(f'#{test_case} {ans}')