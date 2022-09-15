import sys
sys.stdin = open("input.txt", "r")

def min_max(lst):
    mn = mx = 0
    for idx in range(1, len(lst)):
        if lst[mx] < lst[idx]:
            mx = idx
        if lst[mn] > lst[idx]:
            mn = idx
    return mx, mn

for test_case in range(1, 11):
    dump = int(input())
    lst = list(map(int, input().split()))

    for _ in range(dump):   # dump 횟수만큼 작업 반복
        block_max, block_min = min_max(lst)
        lst[block_max] -= 1                  # 최대 블록 갯수에 -1
        lst[block_min] += 1                  # 최소 블록 갯수에 + 1

    block_max, block_min = min_max(lst)
    print(f'#{test_case} {lst[block_max] - lst[block_min]}')