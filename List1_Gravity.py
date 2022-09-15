import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    max_block = 0

    for i in range(N):
        drop_block = 0
        for j in range(i + 1, N):
            if lst[i] > lst[j]:
                drop_block += 1

        if max_block < drop_block:
            max_block = drop_block
    print(f'#{test_case} {max_block}')