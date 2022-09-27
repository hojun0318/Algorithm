import sys
sys.stdin = open("input.txt", "r")

def Quick_Sort(lst):
    if len(lst) <= 1:               # 원소가 1개인 경우
        return lst
    pivot = lst[len(lst) // 2]      # 중앙에 위치한 값을 피벗으로  설정
    lower_pivot, equal_pivot, upper_pivot = [], [], []
    for values in lst:
        if values < pivot:          # 피벗보다 작은 값 찾기
            lower_pivot.append(values)
        elif values > pivot:        # 피벗보다 큰 값 찾기
            upper_pivot.append(values)
        else:                       # 피벗과 같은 값 찾기
            equal_pivot.append(values)

    return Quick_Sort(lower_pivot) + equal_pivot + Quick_Sort(upper_pivot)

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))

    lst = Quick_Sort(lst)

    print(f'#{test_case} {lst[len(lst) // 2]}')