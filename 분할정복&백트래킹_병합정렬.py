import sys
sys.stdin = open("input.txt", "r")


def merge_sort(lst):
    global cnt
    if len(lst) < 2:  # 정렬대상이 1개이면 종료
        return lst

    m = len(lst) // 2  # [1] 반을 나눠서 각각을 정렬
    left = merge_sort(lst[:m])
    right = merge_sort(lst[m:])

    # 정답 카운트 확인 (left[-1]>right[-1])
    if left[-1] > right[-1]:
        cnt += 1

    # [2] 좌우 더 작은값을 하나씩 추가
    ret = []
    l = r = 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            ret.append(left[l])
            l += 1
        else:
            ret.append(right[r])
            r += 1
    ret += left[l:] + right[r:]
    return ret


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    lst = merge_sort(lst)
    print(f'#{test_case} {lst[N // 2]} {cnt}')