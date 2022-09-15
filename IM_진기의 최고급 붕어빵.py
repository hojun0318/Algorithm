import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    people = list(map(int, input().split()))
    people = sorted(people)
    ans = 'Possible'

    for i in range(N):
        items = (people[i] // M) * K
        if items - (i + 1) < 0:
            ans = 'Impossible'
            break

    print(f'#{test_case} {ans}')