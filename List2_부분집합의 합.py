import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    L = len(arr)
    N, K = map(int, input().split())
    ans = 0

    for i in range(1<<L):               # 1<<n : 부분 집합의 개수
        sm = 0                          # 부분 집합 원소의 합
        cnt = 0                         # 부분 집합 원소의 개수
        for j in range(L):              # 원소의 수만큼 비트를 교환함
            if i & (1<<j):               # i의 j번 비트가 1인 경우
                sm += arr[j]
                cnt += 1
        if cnt == N and sm == K:        # 부분 집합 원소의 개수와 합이 동일할 경우
            ans += 1

    print(f'#{test_case} {ans}')