import sys
sys.stdin = open("input.txt", "r")

def palindrome_check(lst):
    for i in range(len(lst) // 2):
        if lst[i] != lst[-i - 1]:
            return 0
    return 1

for test_case in range(1, 11):
    tc = int(input())
    row_arr = [list(input()) for _ in range(100)]
    col_arr = list(zip(*row_arr))
    max_pal = 1

    for length in range(100, 1, -1):
        if max_pal >= length:
            break
        for idx in range(100 - length + 1):
            if max_pal == length:
                break
            for lst, lst2 in zip(row_arr, col_arr):
                if palindrome_check(lst[idx:idx+length]) or palindrome_check(lst2[idx:idx+length]):
                    max_pal = length
                    break
    print(f'#{test_case} {max_pal}')
